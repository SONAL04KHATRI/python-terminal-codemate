from .base import Command

class PwdCommand(Command):
    """pwd - print working directory"""

    def execute(self, args, terminal):
        try:
            rel = terminal.cwd.relative_to(terminal.root)
            print("/" if str(rel) == "." else f"/{rel}")
        except Exception:
            print(str(terminal.cwd))
