from pathlib import Path

def safe_resolve(root: Path, cwd: Path, target: str) -> Path:
    """
    Resolve target path relative to cwd (if not absolute).
    Ensure the resolved path is inside root.
    Raise ValueError if it escapes.
    """
    p = Path(target)
    if not p.is_absolute():
        p = cwd.joinpath(p)
    resolved = p.resolve()
    root_resolved = root.resolve()
    try:
        resolved.relative_to(root_resolved)
    except Exception:
        raise ValueError(f"Access denied: path escapes sandbox root ({root_resolved})")
    return resolved


def format_size(n: int) -> str:
    """Return human-readable file size (e.g., 1.23MB)."""
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    size = float(n)
    while size >= 1024 and i < len(suffixes) - 1:
        size /= 1024.0
        i += 1
    return f"{size:.2f}{suffixes[i]}"
