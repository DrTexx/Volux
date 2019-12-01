# builtin
import uuid
import time
import threading


class NoDelta:
    def __init__(self):
        pass

    def __str__(self):
        return "N/A"


class VoluxConnection:
    """Contains all the properties of a connection between two modules"""

    def __init__(self, input_module, output_module, hz):

        self.input = input_module
        self.output = output_module
        self.UUID = uuid.uuid4()
        self.hz = hz
        self.hz_chars = len(str(self.hz))
        self.sync_times = [0, 0, 0]
        self.waittime = 1 / self.hz
        self.nickname = "{} -> {} @ {}hz".format(
            self.input._module_attr, self.output._module_attr, self.hz
        )

    def sync(self):

        t_start = time.process_time()

        wait_thread = threading.Thread(target=self._wait)
        wait_thread.start()

        self.output.set(self.input.get())

        # print("{} -> {}".format(self.input._module_name,self.output._module_name))

        t_synced = time.process_time()
        wait_thread.join()
        t_finished = time.process_time()

        self.sync_times = [t_start, t_synced, t_finished]

    def _wait(self):
        time.sleep(self.waittime)

    def _get_delta(self):
        time_elapsed = self.sync_times[1] - self.sync_times[0]

        if time_elapsed > 0:
            time_needed = 1 / time_elapsed
            return int(time_needed - self.hz)
        else:
            return NoDelta()

    def _started(self):

        self.input._setup()
        self.output._setup()

    def _stopped(self):

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
