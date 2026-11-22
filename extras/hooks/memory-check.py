"""PreToolUse hook: block a NEW auto-memory file unless it states where Claude checked first.
Keeps rules in the brains (CLAUDE.md, topics/, skills) instead of scattered memory copies.
Edits of existing files and MEMORY.md pass."""
import json, os, re, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
if d.get("tool_name") != "Write":
    sys.exit(0)
ti = d.get("tool_input") or {}
path = (ti.get("file_path") or "").replace("\\", "/")
if not re.search(r"/\.claude/projects/[^/]+/memory/[^/]+\.md$", path, re.I):
    sys.exit(0)
if path.lower().endswith("/memory.md") or os.path.exists(ti.get("file_path", "")):
    sys.exit(0)
if re.search(r"^\*{0,2}Checked:", ti.get("content", ""), re.M | re.I):
    sys.exit(0)
sys.stderr.write(
    "New memory file blocked. First grep ~/.claude/CLAUDE.md, the hub brains (CLAUDE.md, topics/, learnings/) "
    "and ~/.claude/skills/*/SKILL.md for this learning. If it exists, sharpen it there instead. If it belongs "
    "to one project or skill, write it there. Only if it has no home: add a line 'Checked: <paths searched>' "
    "to the memory body and write again."
)
sys.exit(2)
