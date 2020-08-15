from .base import RenderingEngine


class MotionEngine(RenderingEngine):
    """Generic interface for rendering engines which produce a motion-like effect.

    Engines based on this class can produce more complex visuals.
    """

    def __init__(self, render_func):
        super().__init__(render_func=render_func)
