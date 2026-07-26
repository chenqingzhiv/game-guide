#!/usr/bin/env python3
"""
Pipeline controller for game-guide.club.
Replaces LLM agent workflows with code-enforced pipeline.

Usage:
  python3 scripts/pipeline.py --site game --type database [--count 3]
  python3 scripts/pipeline.py --site game --type deep-guide [--topic "Factorio"]

Flow:
  1. Content strategy (rule-based rotation) → pick what to write
  2. Call LLM API (model only step) → generate .md content
  3. Validate generated content (frontmatter, word count, format)
  4. Run preflight checks (from preflight_check.run_all)
  5. mkdocs build --strict
  6. git commit + push
  7. Report

Model is ONLY used in step 2. All other steps are code-enforced.
"""
import argparse, json, os, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path


SITES = {
    "game": {
        "dir": "/home/hermes/game-guide",
        "git_remote": "origin",
        "git_branch": "main",
        "name": "Game Guide Club",
        "url": "https://game-guide.club",
        "games": {
            "satisfactory": "Satisfactory",
            "factorio": "Factorio",
            "dyson": "Dyson Sphere Program",
            "timberborn": "Timberborn",
            "shapez2": "Shapez 2",
            "valheim": "Valheim",
            "enshrouded": "Enshrouded",
            "vrising": "V Rising",
            "sons-forest": "Sons of the Forest",
            "grounded": "Grounded",
        },
        "llm_model": "deepseek-chat",
        "llm_temp": 0.4,
        "llm_max_tokens": 4000,
    },
}

DATABASE_PROMPT_TEMPLATE = """You are a game guide content writer for {site_name} ({site_url}).
Write a {content_type} page for {game_name}.

OUTPUT FORMAT (ABSOLUTELY REQUIRED):
The first line MUST be exactly three dashes: ---
Then frontmatter fields:
title: <Descriptive Title>
description: <Brief description>
date: 2026-06-26
Then another line with three dashes: ---
Then the markdown body.

Example start:
---
title: Satisfactory Alternate Recipes Database
description: Complete reference for all alternate recipes with efficiency data
date: 2026-06-26
---

# Title Here

Content here with tables and data.

Requirements:
- At least 500 words of useful information
- Use h2/h3 headers for structure
- Include data in markdown tables where applicable
- End with a "Quick Tips" section
- Output ONLY the file content, no explanations

Topic: {topic}
Target file: {target_path}
"""

DEEP_GUIDE_PROMPT_TEMPLATE = """You are a game guide content writer for {site_name} ({site_url}).
Write a comprehensive guide about {topic} for {game_name}.

OUTPUT FORMAT (ABSOLUTELY REQUIRED):
The first line MUST be exactly three dashes: ---
Then frontmatter fields:
title: <Descriptive Title>
description: <Brief description>
date: 2026-06-26
Then another line with three dashes: ---
Then the markdown body.

Requirements:
- At least 1500 words of in-depth coverage
- Include tables for stats/items/recipes
- Use h2/h3 headers for sections
- Include a "Beginner Tips" section
- Add strategy recommendations
- Output ONLY the file content, no explanations

Target file: {target_path}
"""


# ── API Key ──

def get_api_key():
    env_path = os.path.expanduser("~/.hermes/.env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("DEEPSEEK_API_KEY="):
                    return line.split("=", 1)[1].strip("\"'")
    return os.environ.get("DEEPSEEK_API_KEY", "")


# ── Step 1: Content Strategy ──

DATABASE_ROTATION = [
    {
        "game_key": "satisfactory",
        "target_path": "docs/satisfactory/alternate-recipes.md",
        "topic": "Satisfactory Alternate Recipes Database — All alternate recipes with input/output, savings, and priority ratings",
        "content_type": "database",
    },
    {
        "game_key": "factorio",
        "target_path": "docs/factorio/items.md",
        "topic": "Factorio Items Database — Complete item catalog with crafting costs, tech requirements, and usage",
        "content_type": "database",
    },
    {
        "game_key": "dyson",
        "target_path": "docs/dyson/resources.md",
        "topic": "Dyson Sphere Program Resources Database — All raw and refined resources with mining rates and production chains",
        "content_type": "database",
    },
    {
        "game_key": "timberborn",
        "target_path": "docs/timberborn/materials.md",
        "topic": "Timberborn Materials Database — All material types with production chains and storage requirements",
        "content_type": "database",
    },
    {
        "game_key": "shapez2",
        "target_path": "docs/shapez2/upgrades.md",
        "topic": "Shapez 2 Upgrades Database — Complete upgrade tree with costs, effects, and optimal path",
        "content_type": "database",
    },
    {
        "game_key": "valheim",
        "target_path": "docs/valheim/materials.md",
        "topic": "Valheim Materials Database — All crafting materials with sources, biomes, and usage",
        "content_type": "database",
    },
    {
        "game_key": "vrising",
        "target_path": "docs/vrising/castle.md",
        "topic": "V Rising Castle Building Database — All castle structures with costs, tier requirements, and bonuses",
        "content_type": "database",
    },
    {
        "game_key": "grounded",
        "target_path": "docs/grounded/resources.md",
        "topic": "Grounded Resources Database — All raw materials with locations, uses, and crafting recipes",
        "content_type": "database",
    },
]

DEEP_GUIDE_ROTATION = [
    {
        "game_key": "satisfactory",
        "target_path": "docs/satisfactory/early-game.md",
        "topic": "Satisfactory Early Game Guide — First 20 hours: tech tree order, base layout, power management, and efficient factory foundation",
        "content_type": "guide",
    },
    {
        "game_key": "factorio",
        "target_path": "docs/factorio/mega-base.md",
        "topic": "Factorio Mega Base Guide — Scaling from starter base to 1k+ SPM, train networks, city blocks, and UPS optimization",
        "content_type": "guide",
    },
    {
        "game_key": "timberborn",
        "target_path": "docs/timberborn/drought.md",
        "topic": "Timberborn Drought Survival Guide — Water management, food reserves, district planning, and Iron Teeth vs Folktails drought strategies",
        "content_type": "guide",
    },
    {
        "game_key": "valheim",
        "target_path": "docs/valheim/advancement.md",
        "topic": "Valheim Progression Guide — Complete advancement path from Meadows to Mistlands, boss order, gear tiers, and biome prep checklist",
        "content_type": "guide",
    },
    {
        "game_key": "enshrouded",
        "target_path": "docs/enshrouded/builds.md",
        "topic": "Enshrouded Build Guide — Best weapon/armor/skill combos for each playstyle, with progression tips",
        "content_type": "guide",
    },
    {
        "game_key": "sons-forest",
        "target_path": "docs/sons-forest/survival.md",
        "topic": "Sons of the Forest Survival Guide — Complete walkthrough from crash landing to endgame, with base defense, companion, and cave strategies",
        "content_type": "guide",
    },
]


def get_rotation_index(content_type):
    cfg_dir = Path(SITES["game"]["dir"]) / ".hermes"
    cfg_dir.mkdir(parents=True, exist_ok=True)
    marker = cfg_dir / "rotation_{}.idx".format(content_type)
    if marker.exists():
        return int(marker.read_text().strip())
    return 0


def advance_rotation(content_type):
    cfg_dir = Path(SITES["game"]["dir"]) / ".hermes"
    rotation = DATABASE_ROTATION if content_type == "database" else DEEP_GUIDE_ROTATION
    current = get_rotation_index(content_type)
    next_idx = (current + 1) % len(rotation)
    (cfg_dir / "rotation_{}.idx".format(content_type)).write_text(str(next_idx))
    return current


def select_content_brief(content_type):
    idx = advance_rotation(content_type)
    rot = DATABASE_ROTATION if content_type == "database" else DEEP_GUIDE_ROTATION
    return rot[idx]


# ── Step 2: LLM Content Generation ──

def call_llm(prompt, api_key, model="deepseek-chat", temp=0.4, max_tokens=4000):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temp,
        "max_tokens": max_tokens,
    })
    auth_header = "Authorization: Bearer " + api_key
    result = subprocess.run(
        ["curl", "-s", "-X", "POST", "https://api.deepseek.com/v1/chat/completions",
         "-H", auth_header,
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        print("  curl failed (exit {}): {}".format(result.returncode, result.stderr[:200]))
        return None
    try:
        data = json.loads(result.stdout)
        if "choices" not in data or not data["choices"]:
            print("  API returned no choices: " + json.dumps(data)[:300])
            return None
        return data["choices"][0]["message"]["content"]
    except (json.JSONDecodeError, KeyError) as e:
        print("  API response parse error: " + str(e))
        print("  Response preview: " + result.stdout[:300])
        return None


def generate_content(brief):
    site = SITES["game"]
    game_name = site["games"][brief["game_key"]]
    target_path = os.path.join(site["dir"], brief["target_path"])

    if brief["content_type"] in ("database",):
        prompt = DATABASE_PROMPT_TEMPLATE.format(
            site_name=site["name"], site_url=site["url"],
            game_name=game_name, content_type=brief["content_type"],
            topic=brief["topic"], target_path=brief["target_path"],
        )
    else:
        prompt = DEEP_GUIDE_PROMPT_TEMPLATE.format(
            site_name=site["name"], site_url=site["url"],
            game_name=game_name, topic=brief["topic"],
            target_path=brief["target_path"],
        )

    print("\nGenerating content for {}...".format(brief["target_path"]))
    api_key = get_api_key()
    if not api_key:
        print("  No API key found")
        return None

    content = None
    for attempt in range(2):
        content = call_llm(prompt, api_key, site["llm_model"], site["llm_temp"], site["llm_max_tokens"])
        if content:
            break
        print("  Retrying (attempt {})...".format(attempt + 2))
        time.sleep(3)

    if not content:
        print("  Failed after 2 attempts")
        return None

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w") as f:
        f.write(content.strip() + "\n")
    print("  Written to " + target_path)
    return target_path


# ── Step 3: Validation ──

def validate_content(filepath, content_type):
    errors = []
    print("\nValidating content at {}...".format(filepath))
    if not os.path.exists(filepath):
        errors.append("File not found: " + filepath)
        return False, errors

    with open(filepath) as f:
        content = f.read()

    if not content.startswith("---"):
        errors.append("Missing YAML frontmatter")
    else:
        fm_end = content.find("---", 3)
        if fm_end == -1:
            errors.append("Unclosed YAML frontmatter")
        else:
            fm = content[3:fm_end].strip()
            if "title:" not in fm:
                errors.append("Frontmatter missing 'title'")
            if "description:" not in fm:
                errors.append("Frontmatter missing 'description'")

    body = content
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            body = content[end + 3:]
    words = len(body.split())

    min_words = 400 if content_type == "database" else 1200
    if words < min_words:
        errors.append("Too short: {} words (min {})".format(words, min_words))
    else:
        print("  Word count: {}".format(words))

    if errors:
        print("  Validation failed:")
        for e in errors:
            print("    - " + e)
        return False, errors
    print("  Content OK")
    return True, errors


# ── Step 4-5-6 ──

def run_build(site_dir):
    print("\nBuilding site...")
    result = subprocess.run(
        ["mkdocs", "build", "--strict"],
        cwd=site_dir, capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        print("  Build failed:\n" + result.stderr[:500])
        return False
    print("  Build OK")
    return True


def preflight_check(site_dir, fast=True):
    try:
        sys.path.insert(0, site_dir)
        from scripts.preflight_check import run_all
        passed, errors, warnings = run_all(fast=fast)
        return passed
    except ImportError:
        print("  Running preflight as subprocess...")
        result = subprocess.run(
            [sys.executable, "scripts/preflight_check.py"],
            cwd=site_dir, timeout=120
        )
        return result.returncode == 0


def git_commit_push(site_dir, content_desc):
    print("\nGit commit & push...")
    status = subprocess.run(["git", "status", "--porcelain"], cwd=site_dir, capture_output=True, text=True, timeout=10)
    if not status.stdout.strip():
        print("  No changes")
        return False

    subprocess.run(["git", "add", "-A"], cwd=site_dir, capture_output=True, text=True, timeout=10)
    msg = "auto: " + content_desc
    commit = subprocess.run(["git", "commit", "-m", msg], cwd=site_dir, capture_output=True, text=True, timeout=10)
    if commit.returncode != 0:
        print("  Commit failed: " + commit.stderr[:200])
        return False
    print("  Committed: " + msg)

    push = subprocess.run(["git", "push"], cwd=site_dir, capture_output=True, text=True, timeout=30)
    if push.returncode != 0:
        print("  Push failed: " + push.stderr[:200])
        return False
    print("  Pushed")
    return True


def rollback_changes(site_dir):
    print("\nRolling back...")
    subprocess.run(["git", "checkout", "--", "."], cwd=site_dir, timeout=10)
    print("  Done")


def generate_report(content_type, brief, success, details):
    site = SITES["game"]
    status = "OK" if success else "FAIL"
    lines = [
        "{} Pipeline -- {}".format(status, site["name"]),
        "Type: {}".format(content_type),
        "Topic: {}...".format(brief["topic"][:60]),
        "Target: {}".format(brief["target_path"]),
    ]
    if details:
        lines.append("")
        lines.extend(details)
    return "\n".join(lines)


# ── Pipeline ──

def run_pipeline(content_type, count=1):
    site = SITES["game"]
    site_dir = site["dir"]
    all_ok = True
    report_details = []
    brief = None

    os.chdir(site_dir)
    print("Pipeline: {} -- {}".format(site["name"], content_type))

    for i in range(count):
        print("\n--- Iteration {}/{} ---".format(i + 1, count))

        # Step 1
        print("Step 1/6: Content strategy...")
        brief = select_content_brief(content_type)
        print("  Topic: {}...".format(brief["topic"][:80]))
        print("  Target: {}".format(brief["target_path"]))

        # Step 2 (model only)
        print("Step 2/6: LLM generation...")
        filepath = generate_content(brief)
        if not filepath:
            print("  Generation failed, aborting")
            report_details.append("FAIL Generation for " + brief["target_path"])
            all_ok = False
            break

        # Step 3
        validated, val_errors = validate_content(filepath, content_type)
        if not validated:
            print("  Validation failed, rollback")
            rollback_changes(site_dir)
            report_details.append("FAIL Validation: " + "; ".join(val_errors))
            all_ok = False
            break

        # Step 4
        print("Step 4/6: Preflight...")
        if not preflight_check(site_dir, fast=True):
            print("  Preflight failed, rollback")
            rollback_changes(site_dir)
            report_details.append("FAIL Preflight for " + brief["target_path"])
            all_ok = False
            break
        print("  Preflight OK")

        # Step 5
        print("Step 5/6: Build...")
        if not run_build(site_dir):
            print("  Build failed, rollback")
            rollback_changes(site_dir)
            report_details.append("FAIL Build for " + brief["target_path"])
            all_ok = False
            break
        print("  Build OK")

        # Step 6
        print("Step 6/6: Git push...")
        desc = "{}: {}".format(content_type, brief["topic"][:60])
        pushed = git_commit_push(site_dir, desc)
        if not pushed:
            report_details.append("WARN {} (local only)".format(brief["target_path"]))
        else:
            report_details.append("OK " + brief["target_path"])

        print("  Iteration {} done!".format(i + 1))

    print("\nPipeline: " + ("OK" if all_ok else "FAIL"))
    report = generate_report(content_type, brief, all_ok, report_details)
    return all_ok, report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game Guide pipeline")
    parser.add_argument("--type", required=True, choices=["database", "deep-guide"],
                        help="Content type")
    parser.add_argument("--count", type=int, default=1, help="Number of items")
    args = parser.parse_args()
    success, report = run_pipeline(args.type, count=args.count)
    print("\n\n---PIPELINE_REPORT---\n{}\n---END_PIPELINE_REPORT---".format(report))
    sys.exit(0 if success else 1)
