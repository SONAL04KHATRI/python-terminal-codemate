class Command:
    """Base class for all commands."""
    def execute(self, args, terminal):
        raise NotImplementedError("Each command must implement execute(args, terminal)")
