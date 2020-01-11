"""Defines the connection class and any related classes."""

# builtin
import uuid
import time
import threading
from typing import List, Union

# module
from .module import VoluxModule


class NoDelta:
    """Placeholder class for internal logic."""

    def __init__(self):
        """Create a new NoDelta instance."""
        pass

    def __str__(self):
        """Override default string to be N/A."""
        return "N/A"


class VoluxConnection:
    """Contains all the properties of a connection between two modules."""

    def __init__(
        self, input_module: VoluxModule, output_module: VoluxModule, hz: int
    ):
        """Instansiate a new connection."""
        self.input: VoluxModule = input_module
        self.output: VoluxModule = output_module
        self.UUID = uuid.uuid4()
        self.hz: int = hz
        self.hz_chars: int = len(str(self.hz))
        self.sync_times: List[float] = [0.0, 0.0, 0.0]
        self.waittime: float = 1 / self.hz
        self.nickname: str = "{} -> {} @ {}hz".format(
            self.input._module_attr, self.output._module_attr, self.hz
        )

    def sync(self) -> None:
        """Send the input modules output to the output module."""
        t_start = time.process_time()

        wait_thread = threading.Thread(target=self._wait)
        wait_thread.start()

        self.output.set(self.input.get())

        # print("{} -> {}".format(self.input._module_name,self.output._module_name))

        t_synced = time.process_time()
        wait_thread.join()
        t_finished = time.process_time()

        self.sync_times = [t_start, t_synced, t_finished]

    def _wait(self) -> None:
        time.sleep(self.waittime)

    def _get_delta(self) -> Union[int, NoDelta]:
        time_elapsed = self.sync_times[1] - self.sync_times[0]

        if time_elapsed > 0:
            time_needed = 1 / time_elapsed
            return int(time_needed - self.hz)
        else:
            return NoDelta()

    def _started(self) -> None:

        self.input._setup()
        self.output._setup()

    def _stopped(self) -> None:

        self.sync_times = [0, 0, 0]
        self.input._cleanup()
        self.output._cleanup()

        # print(
        #     "{name:<40} ({target}Hz) ({delta:>{hz_chars}}Hz Δ)".format(
        #         name=self.nickname,
        #         target=self.hz,
        #         delta=self.hz_delta,
        #         hz_chars=self.hz_chars,
        #     )
        # )
