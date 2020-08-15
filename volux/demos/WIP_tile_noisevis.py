#!/usr/bin/env python3


import time
import threading
from queue import Queue

import lifxlan

import voluxaudio


from volux.demos.MOVE_ME_tile.engines import (
    NoiseFrameEngine,
    SolidFrameEngine,
    NorthernMotionEngine,
)

vlxaudio = voluxaudio.VoluxAudio()
vlxaudio.setup()


def engage_x_pixels(x, _max=64):
    """Return a list of 64 HSVK tuples. Turn on x many pixels of tile."""
    HSVK_normal = (0, 0, (65535 / 100) * vlxaudio.get(), 3500)
    HSVK_it_off = (0, 65535, 10000, 3500)

    def _func(i):
        if i <= x:
            return HSVK_normal
        else:
            return HSVK_it_off

    return map(_func, range(_max))


# HACK: quick and dirty implementation
def mutate_pixel(n, new_color, all_colors):
    """Change only the color of pixel n of tile."""
    all_colors[n] = new_color
    return all_colors


nfe = NoiseFrameEngine()
sfe = SolidFrameEngine()
nme = NorthernMotionEngine()

lifx = lifxlan.LifxLAN()

tilechains = lifx.get_tilechain_lights()

min_pixels = 0
max_pixels = 64
n_pixels = min_pixels
tilechains_tiles_colors = [
    tile.get_tile_colors(idx) for idx, tile in enumerate(tilechains)
]
print(tilechains_tiles_colors)

print_lock = threading.Lock()


def timeit(func):
    def _func(*args, **kwargs):
        start_t = time.perf_counter()
        func(*args, **kwargs)
        with print_lock:
            print(f"effective Hz: {600 * (time.perf_counter() - start_t)}")

    return _func


try:

    lifx_packet_lock = threading.Lock()
    ready_for_next_packet = threading.Event()
    q = Queue()
    last_time = time.perf_counter()
    hz = 1 / 120

    def t_send_color(val, timeout):
        # when this exits, the lock is released
        with lifx_packet_lock:
            global last_time

            # ready_for_next_packet.wait(timeout=timeout)
            if time.perf_counter() - last_time < timeout:
                return

            for tc_idx, tilechain in enumerate(tilechains_tiles_colors):
                for t_idx, tile in enumerate(tilechains):
                    try:
                        tilechains_tiles_colors[tc_idx][t_idx] = nme.render(
                            min(val * 1, 100)
                        )
                    except Exception as e:
                        print(e)
                        tilechains_tiles_colors[tc_idx][t_idx] = sfe.render(
                            val
                        )

            for tc_idx, tilechain in enumerate(tilechains_tiles_colors):
                for t_idx, tile in enumerate(tilechains):
                    tile.set_tile_colors(
                        0, tilechains_tiles_colors[tc_idx][t_idx], rapid=True
                    )

            print(f"shifted [{'#' * int(val):100}]")

            time_now = time.perf_counter()
            delta = time_now - last_time
            # print(f"time between: {600*delta}ms")
            print(
                f"latency | {600*delta:.2f}: {'-' * int(((600*delta) - 19))}#"
            )
            last_time = time_now

    def t_timing_manager(timeout):
        ready_for_next_packet.clear()
        time.sleep(timeout)
        ready_for_next_packet.set()

    # define the worker which will run on each thread
    def worker(timeout):
        while True:
            t_send_color(val=q.get(), timeout=timeout)
            q.task_done()

    # create timing manager worker
    # t = threading.Thread(target=t_timing_manager, kwargs={"timeout": hz})
    # t.daemon = True
    # t.start()

    # create workers
    for x in range(5):
        t = threading.Thread(target=worker, kwargs={"timeout": hz})
        # this ensures the thread will die when the main thread dies
        # can set t.daemon to False if you want it to keep running
        t.daemon = True
        t.start()

    # populate the queue with values
    while True:
        val = vlxaudio.get()
        q.put(val)
        time.sleep(hz)


except KeyboardInterrupt:
    pass

vlxaudio.cleanup()
