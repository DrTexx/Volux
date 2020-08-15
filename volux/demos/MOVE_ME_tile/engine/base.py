from ..types import FrameRenderFunction


class RenderingEngine:
    """Base class for all rendering engines.

    Provides a generic interface.
    """

    def __init__(self, render_func: FrameRenderFunction):
        self.render = render_func
