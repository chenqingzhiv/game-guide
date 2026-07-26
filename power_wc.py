#!/usr/bin/env python3
import re

with open('/home/hermes/game-guide/docs/satisfactory/power.md', 'r') as f:
    content = f.read()

all_tokens = content.split()
print(f"Total whitespace-separated tokens: {len(all_tokens)}")

# Estimate prose by removing markdown formatting
stripped = content
stripped = re.sub(r'```.*?```', '', stripped, flags=re.DOTALL)
stripped = re.sub(r'\|.*?\|', '', stripped)
stripped = re.sub(r'^---+$', '', stripped, flags=re.MULTILINE)
stripped = re.sub(r'^!!!.*$', '', stripped, flags=re.MULTILINE)
stripped = re.sub(r'\*+', '', stripped)
stripped = re.sub(r'^#+\s*', '', stripped, flags=re.MULTILINE)
stripped = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', stripped)
stripped = re.sub(r'\s+', ' ', stripped).strip()

prose_tokens = stripped.split()
print(f"Prose (no markdown): {len(prose_tokens)}")
