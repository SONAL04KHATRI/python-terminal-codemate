import shutil
from .base import Command

class RmCommand(Command):
    """rm <file|dir> - remove file or directory"""

    def execute(self, args, terminal):
        if not args:
            print("rm: missing operand")
            return
        target = args[0]
        try:
            path = terminal.resolve_path(target)
            if not path.exists():
                print(f"rm: cannot remove '{target}': No such file or directory")
                return
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
        except Exception as e:
            print(f"rm error: {e}")
