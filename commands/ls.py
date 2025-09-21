from .base import Command

class LsCommand(Command):
    """ls [path] - list files in the directory"""

    def execute(self, args, terminal):
        try:
            target = args[0] if args else "."
            path = terminal.resolve_path(target)
            if not path.exists():
                print(f"ls: {target}: No such file or directory")
                return
            if path.is_dir():
                for p in sorted(path.iterdir()):
                    suffix = "/" if p.is_dir() else ""
                    print(p.name + suffix)
            else:
                print(path.name)
        except Exception as e:
            print(f"ls error: {e}")
