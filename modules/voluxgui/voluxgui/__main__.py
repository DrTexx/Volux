# builtin
import threading
import logging
from time import sleep

# external
import tkinter as tk
from tkinter import ttk

# site
import volux
import colorama
import lifxlan

colorama.init()

log = logging.getLogger("volux script - GUI")
log.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d"
)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)


def main():

    from .launch import launch

    launch()


if __name__ == "__main__":

    main()
