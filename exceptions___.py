class Exit(Exception):
    def __init__(self, exitcode):
        self.exitcode = exitcode

    def __str__(self):
        return self.exitcode
