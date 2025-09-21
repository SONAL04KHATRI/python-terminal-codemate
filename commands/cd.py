from .base import Command

class CdCommand(Command):
    """cd <path> - change directory"""

    def execute(self, args, terminal):
        target = args[0] if args else str(terminal.root)
        try:
            new_path = terminal.resolve_path(target)
            if not new_path.exists() or not new_path.is_dir():
                print(f"cd: {target}: No such directory")
                return
            terminal.cwd = new_path
        except Exception as e:
            print(f"cd error: {e}")
