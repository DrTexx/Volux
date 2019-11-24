import uuid
import time


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
        self.hz_delta = NoDelta()
        self.waittime = 1 / self.hz
        self.nickname = "{} -> {} @ {}hz".format(
            self.input._module_attr, self.output._module_attr, self.hz
        )

    def sync(self):

        t1 = time.process_time()

        self.output.set(self.input.get())

        # print("{} -> {}".format(self.input._module_name,self.output._module_name))

        t2 = time.process_time()

        while t2 - t1 < self.waittime:
            t2 = time.process_time()

        actual_Hz = 1 / (t2 - t1)
        self.hz_delta = int(actual_Hz - self.hz)

    def _stopped(self):

        self.hz_delta = NoDelta()

        # print(
        #     "{name:<40} ({target}Hz) ({delta:>{hz_chars}}Hz Δ)".format(
        #         name=self.nickname,
        #         target=self.hz,
        #         delta=self.hz_delta,
        #         hz_chars=self.hz_chars,
        #     )
        # )
