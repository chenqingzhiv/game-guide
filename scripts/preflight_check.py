#!/usr/bin/env python3
"""
Pre-deployment check for game-guide.club.
Dual-mode: run as script (CLI) OR import as module (run_all).

CLI Usage:
  python3 scripts/preflight_check.py          # full check
  python3 scripts/preflight_check.py --paths  # only path validation (fast)

Module Usage:
  from scripts.preflight_check import run_all
  passed, errors, warnings = run_all(fast=False)
"""
import os, re, sys, subprocess, threading, time, urllib.request, http.server

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(SITE_DIR, "docs")
BUILD_DIR = os.path.join(SITE_DIR, "site")
PORT = 9998


def log(errors, warnings, level, msg):
    icon = "🔴" if level == "ERROR" else "🟡"
    print(f"  {icon} {level}: {msg}")
    if level == "ERROR":
        errors.append(msg)
    else:
        warnings.append(msg)


def check_build(errors, warnings):
    print("\n📦 Step 1: mkdocs build --strict")
    result = subprocess.run(
        ["mkdocs", "build", "--strict"],
        cwd=SITE_DIR, capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        log(errors, warnings, "ERROR", f"Build failed:\n{result.stderr[:500]}")
        return False
    print(f"  ✅ Build OK ({len(os.listdir(BUILD_DIR))} dirs)")
    return True


def check_paths(errors, warnings):
    print("\n🔗 Step 2: Path validation")
    bad_refs = []
    total_refs = 0
    for root, dirs, files in os.walk(DOCS_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath) as f:
                content = f.read()
            refs = re.findall(r'<(?:script|img|link)\s+[^>]*(?:src|href)="([^"]+)"', content)
            total_refs += len(refs)
            for ref in refs:
                if ref.startswith("http") or ref.startswith("//"):
                    continue
                if "#" in ref:
                    ref = ref.split("#")[0]
                md_dir = os.path.dirname(fpath)
                ref_path = os.path.normpath(os.path.join(md_dir, ref))
                if not os.path.exists(ref_path):
                    rel = os.path.relpath(fpath, DOCS_DIR)
                    bad_refs.append((rel, ref, ref_path))
    if bad_refs:
        for file, ref, resolved in bad_refs:
            log(errors, warnings, "ERROR", f"{file}: broken reference '{ref}' -> {resolved}")
    else:
        print(f"  ✅ All in-page references resolve ({total_refs} checked)")
    return len(bad_refs) == 0


def check_content_depth(errors, warnings):
    print("\n📝 Step 3: Content depth check")
    thin_pages = []
    for root, dirs, files in os.walk(DOCS_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath) as f:
                text = f.read()
            words = len(text.split())
            rel = os.path.relpath(fpath, DOCS_DIR)
            if words < 400:
                thin_pages.append((rel, words))
    if thin_pages:
        for rel, wc in thin_pages:
            log(errors, warnings, "WARNING", f"Thin page: {rel} ({wc} words)")
        print(f"  🟡 {len(thin_pages)} page(s) under 400 words (may need expansion)")
    else:
        print("  ✅ All pages have sufficient content")
    return True


def check_http(errors, warnings):
    print(f"\n🌐 Step 4: HTTP smoke test (port {PORT})")
    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer(("", PORT), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    time.sleep(1)
    pages = [
        "/", "/satisfactory/", "/factorio/", "/dyson/",
        "/timberborn/", "/shapez2/", "/tools/", "/games/comparison/",
    ]
    old_dir = os.getcwd()
    os.chdir(BUILD_DIR)
    all_ok = True
    for page in pages:
        try:
            resp = urllib.request.urlopen(f"http://localhost:{PORT}{page}", timeout=5)
            if resp.status != 200:
                log(errors, warnings, "ERROR", f"HTTP {resp.status} for {page}")
                all_ok = False
        except Exception as e:
            log(errors, warnings, "ERROR", f"Failed to fetch {page}: {e}")
            all_ok = False
    os.chdir(old_dir)
    server.shutdown()
    if all_ok:
        print(f"  ✅ All {len(pages)} URLs returned 200")
    return all_ok


def check_og_image(errors, warnings):
    print("\n🖼️  Step 5: OG image check")
    og_path = os.path.join(DOCS_DIR, "assets", "img", "og-image.png")
    if os.path.exists(og_path):
        print(f"  ✅ OG image: {os.path.getsize(og_path) / 1024:.0f}KB")
        return True
    log(errors, warnings, "WARNING", "OG image missing at docs/assets/img/og-image.png")
    return True


def summarize(errors, warnings):
    print("\n" + "=" * 50)
    if errors:
        print(f"🔴 FAILED - {len(errors)} error(s):")
        for e in errors:
            print(f"   . {e}")
        print("\nFix errors before pushing!")
    else:
        print(f"✅ ALL CHECKS PASSED ({len(warnings)} warnings)")
        for w in warnings:
            print(f"   🟡 {w}")
    print("=" * 50)
    return len(errors) == 0


# ── Module entry point ──

def run_all(fast=False):
    """
    Run all preflight checks. Returns (passed: bool, errors: list, warnings: list).
    'fast=True' skips build and HTTP smoke test (for quick rounds).
    """
    errors = []
    warnings = []
    passes = True

    passes &= check_content_depth(errors, warnings)
    if not fast:
        passes &= check_build(errors, warnings)
    passes &= check_paths(errors, warnings)
    if not fast:
        passes &= check_http(errors, warnings)
    passes &= check_og_image(errors, warnings)

    passed = summarize(errors, warnings)
    return passed, errors, warnings


# ── CLI entry point ──

if __name__ == "__main__":
    fast = "--paths" in sys.argv
    passed, errors, warnings = run_all(fast=fast)
    sys.exit(0 if passed else 1)
