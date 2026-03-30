#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


BEGIN_MARKER = "<!-- design-buff:begin -->"
END_MARKER = "<!-- design-buff:end -->"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_portable_instructions(root: Path) -> str:
    path = root / "adapters" / "shared" / "portable-instructions.md"
    return path.read_text(encoding="utf-8").strip()


def wrap_managed_block(title: str, body: str) -> str:
    return f"{BEGIN_MARKER}\n## {title}\n\n{body.rstrip()}\n{END_MARKER}\n"


def upsert_markdown_block(path: Path, block: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        original = path.read_text(encoding="utf-8")
        if BEGIN_MARKER in original and END_MARKER in original:
            before, remainder = original.split(BEGIN_MARKER, 1)
            _, after = remainder.split(END_MARKER, 1)
            updated = before.rstrip() + "\n\n" + block.rstrip() + "\n" + after.lstrip("\n")
        else:
            updated = original.rstrip() + "\n\n" + block.rstrip() + "\n"
    else:
        updated = block
    path.write_text(updated, encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_claude_block(portable: str) -> str:
    intro = (
        "Use this installed Design Buff block when the user asks for design review, "
        "design self-check, flow diagnosis, Figma review, screenshot review, or product-minded UX critique.\n\n"
    )
    return wrap_managed_block("Design Buff", intro + portable)


def render_claude_command(root: Path) -> str:
    return (root / "adapters" / "claude-code" / "design-buff-review.md").read_text(encoding="utf-8").strip()


def render_cursor_rule(portable: str) -> str:
    return (
        "---\n"
        "description: Use Design Buff for product-minded design review from Figma, screenshots, or flow docs\n"
        "alwaysApply: false\n"
        "---\n\n"
        "Use this rule when the user asks for design review, self-check, flow diagnosis, or UX critique from Figma, screenshots, exports, or product documents.\n\n"
        f"{portable.rstrip()}\n"
    )


def render_agents_block(portable: str) -> str:
    intro = (
        "Use this installed Design Buff block when the user asks for design review, "
        "Figma review, screenshot critique, journey diagnosis, or product-minded UX feedback.\n\n"
    )
    return wrap_managed_block("Design Buff", intro + portable)


def install_claude(root: Path, scope: str, target: Path | None) -> list[Path]:
    portable = read_portable_instructions(root)
    if scope == "user":
        base = Path.home() / ".claude"
    else:
        if target is None:
            raise SystemExit("--target is required for project scope")
        base = target / ".claude"
    claude_md = base / "CLAUDE.md"
    command_md = base / "commands" / "design-buff-review.md"
    upsert_markdown_block(claude_md, render_claude_block(portable))
    write_text(command_md, render_claude_command(root))
    return [claude_md, command_md]


def install_cursor(root: Path, target: Path | None) -> list[Path]:
    if target is None:
        raise SystemExit("--target is required for cursor adapter")
    portable = read_portable_instructions(root)
    rule_path = target / ".cursor" / "rules" / "design-buff-review.mdc"
    write_text(rule_path, render_cursor_rule(portable))
    return [rule_path]


def install_generic(root: Path, target: Path | None) -> list[Path]:
    if target is None:
        raise SystemExit("--target is required for generic-agents adapter")
    portable = read_portable_instructions(root)
    agents_md = target / "AGENTS.md"
    upsert_markdown_block(agents_md, render_agents_block(portable))
    return [agents_md]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install Design Buff adapters into another project or user config.")
    parser.add_argument(
        "platform",
        choices=["claude-code", "cursor", "generic-agents"],
        help="Target runtime adapter to install.",
    )
    parser.add_argument(
        "--scope",
        choices=["project", "user"],
        default="project",
        help="Install scope. Only Claude Code supports user scope.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        help="Target project path. Required for project-scope installs.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = repo_root()

    if args.platform != "claude-code" and args.scope != "project":
        raise SystemExit("Only claude-code supports --scope user.")

    if args.platform == "claude-code":
        written = install_claude(root, args.scope, args.target.resolve() if args.target else None)
    elif args.platform == "cursor":
        written = install_cursor(root, args.target.resolve() if args.target else None)
    else:
        written = install_generic(root, args.target.resolve() if args.target else None)

    for path in written:
        print(path)


if __name__ == "__main__":
    main()
