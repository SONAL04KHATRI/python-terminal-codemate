import os
from .base import Command

class MkdirCommand(Command):
    """mkdir <dir> - make directory"""

    def execute(self, args, terminal):
        if not args:
            print("mkdir: missing operand")
            return
        target = args[0]
        try:
            path = terminal.resolve_path(target)
            os.makedirs(path, exist_ok=False)
        except FileExistsError:
            print(f"mkdir: cannot create directory '{target}': File exists")
        except Exception as e:
            print(f"mkdir error: {e}")
