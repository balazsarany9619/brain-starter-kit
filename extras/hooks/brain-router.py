"""UserPromptSubmit hook: point Claude to the right project brain, silent when nothing matches.

Fill ROUTES with your own projects: a display name, the path to that project's CLAUDE.md and a regex of
trigger words (lowercase). Keep it in sync with the router table in ~/.claude/CLAUDE.md.
Only fires when the session does NOT already run inside the matched project folder.
Test: echo '{"prompt":"how is my landing page going","cwd":"/home/me"}' | python brain-router.py
"""
import json
import re
import sys
from pathlib import Path

HUB = str(Path.home() / "Projects")  # your hub folder

ROUTES = [
    # (name, path to CLAUDE.md, trigger regex)
    ("Example Website", f"{HUB}/Example Website/CLAUDE.md", r"\b(website|landing ?page|homepage)\b"),
    ("Example App", f"{HUB}/Example App/CLAUDE.md", r"\b(my app|expo|supabase)\b"),
]


def main() -> None:
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace"))
    except Exception:
        return
    prompt = (data.get("prompt") or "").lower()
    cwd = (data.get("cwd") or "").replace("\\", "/").lower()
    if not prompt.strip():
        return
    hits = []
    for name, path, pattern in ROUTES:
        project_dir = path.replace("\\", "/").rsplit("/", 1)[0].lower()
        if cwd.startswith(project_dir):
            continue  # brain already loaded in this session
        if re.search(pattern, prompt):
            hits.append((name, path))
    if not hits:
        return
    sys.stdout.reconfigure(encoding="utf-8")
    lines = [f"- {name}: read {path} (and its @topics) before answering" for name, path in hits[:3]]
    print("Brain-Router match:\n" + "\n".join(lines) + "\nIgnore if the match is accidental.")


if __name__ == "__main__":
    main()
