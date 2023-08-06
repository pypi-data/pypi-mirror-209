import functools
import sys
from dataclasses import dataclass, field

# -----------------------------------------------------------------------------
slots_frozen = functools.partial(dataclass, slots=True, frozen=True)


@slots_frozen
class ShellError(Exception):
    """Shell error.
    """
    code: int | None = None
    mesg: str = ''


@slots_frozen
class ShellCommandError(ShellError):
    """Shell command error.
    """
    command: str
    stdout: type(sys.stdout)
    stderr: type(sys.stderr)


@slots_frozen
class ShellCommandNotFound(ShellCommandError):
    """Shell command not found error.
    """


@slots_frozen
class ShellCommandFailed(ShellCommandError):
    """Shell command failed error.
    """


@slots_frozen
class ShellCommandTimeout(ShellCommandError):
    """Shell command timeout error.
    """
    timeout: int


@slots_frozen
class ShellCommandSignal(ShellCommandError):
    """Shell command killed error.
    """
    signal: int
