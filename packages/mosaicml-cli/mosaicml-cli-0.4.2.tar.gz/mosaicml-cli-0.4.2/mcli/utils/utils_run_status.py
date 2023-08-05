"""Utilities for interpreting pod status"""
from __future__ import annotations

from enum import Enum, EnumMeta
from typing import List, Union

from mcli.utils.utils_string_functions import camel_case_to_snake_case, snake_case_to_camel_case

__all__ = ['RunStatus']


class StatusMeta(EnumMeta):
    """Metaclass for RunStatus that adds some useful class properties
    """

    @property
    def order(cls) -> List[RunStatus]:
        """Order of pod states, from latest to earliest
        """
        return [
            RunStatus.FAILED,
            RunStatus.FAILED_PULL,
            RunStatus.STOPPED,
            RunStatus.COMPLETED,
            RunStatus.STOPPING,
            RunStatus.TERMINATING,
            RunStatus.RUNNING,
            RunStatus.STARTING,
            RunStatus.SCHEDULED,
            RunStatus.QUEUED,
            RunStatus.PENDING,
            RunStatus.UNKNOWN,
        ]


class RunStatus(Enum, metaclass=StatusMeta):
    """Possible statuses of a run
    """

    #: The run has been dispatched and is waiting to be received
    PENDING = 'PENDING'

    #: The run has been scheduled and is waiting to be queued
    SCHEDULED = 'SCHEDULED'

    #: The run is queued and is awaiting execution
    QUEUED = 'QUEUED'

    #: The run is starting up and preparing to run
    STARTING = 'STARTING'

    #: The run is actively running
    RUNNING = 'RUNNING'

    #: The run is in the process of being terminated
    TERMINATING = 'TERMINATING'

    #: The run is in the process of being stopped
    STOPPING = 'STOPPING'

    #: The run has finished without any errors
    COMPLETED = 'COMPLETED'

    #: The run has stopped
    STOPPED = 'STOPPED'

    #: The run has failed due to a kubernetes error
    FAILED_PULL = 'FAILED_PULL'

    #: The run has failed due to an issue at runtime
    FAILED = 'FAILED'

    #: A valid run status cannot be found
    UNKNOWN = 'UNKNOWN'

    def __str__(self) -> str:
        return self.value

    def __lt__(self, other: RunStatus):
        if not isinstance(other, RunStatus):
            raise TypeError(f'Cannot compare order of ``RunStatus`` and {type(other)}')
        return RunStatus.order.index(self) > RunStatus.order.index(other)

    def __gt__(self, other: RunStatus):
        if not isinstance(other, RunStatus):
            raise TypeError(f'Cannot compare order of ``RunStatus`` and {type(other)}')
        return RunStatus.order.index(self) < RunStatus.order.index(other)

    def __le__(self, other: RunStatus):
        if not isinstance(other, RunStatus):
            raise TypeError(f'Cannot compare order of ``RunStatus`` and {type(other)}')
        return RunStatus.order.index(self) >= RunStatus.order.index(other)

    def __ge__(self, other: RunStatus):
        if not isinstance(other, RunStatus):
            raise TypeError(f'Cannot compare order of ``RunStatus`` and {type(other)}')
        return RunStatus.order.index(self) <= RunStatus.order.index(other)

    def before(self, other: RunStatus, inclusive: bool = False) -> bool:
        """Returns True if this state usually comes "before" the other

        Args:
            other: Another :class:`~mcli.utils.utils_run_status.RunStatus`
            inclusive: If True, equality evaluates to True. Default False.

        Returns:
            If this state is "before" the other

        Example:
            >>> RunStatus.RUNNING.before(RunStatus.COMPLETED)
            True
            >>> RunStatus.PENDING.before(RunStatus.RUNNING)
            True
        """
        return (self < other) or (inclusive and self == other)

    def after(self, other: RunStatus, inclusive: bool = False) -> bool:
        """Returns True if this state usually comes "after" the other

        Args:
            other: Another :class:`~mcli.utils.utils_run_status.RunStatus`
            inclusive: If True, equality evaluates to True. Default False.

        Returns:
            If this state is "after" the other

        Example:
            >>> RunStatus.RUNNING.before(RunStatus.COMPLETED)
            True
            >>> RunStatus.PENDING.before(RunStatus.RUNNING)
            True
        """
        return (self > other) or (inclusive and self == other)

    @classmethod
    def from_string(cls, run_status: Union[str, RunStatus]) -> RunStatus:
        """Convert a string to a valid RunStatus Enum

        If the run status string is not recognized, will return RunStatus.UNKNOWN
        instead of raising a KeyError
        """
        if isinstance(run_status, RunStatus):
            return run_status

        default = RunStatus.UNKNOWN
        try:
            key = camel_case_to_snake_case(run_status).upper()
            return cls[key]
        except TypeError:
            return default
        except KeyError:
            return default

    @property
    def display_name(self) -> str:
        return snake_case_to_camel_case(self.value, capitalize_first=True)


# pylint: disable-next=invalid-name
CLI_STATUS_OPTIONS = [state.display_name for state in RunStatus]
