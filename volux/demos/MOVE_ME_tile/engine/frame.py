from ..types import FrameRenderFunction, RenderingEngineSettings
from .base import RenderingEngine


class FrameEngine(RenderingEngine):
    """Generic interface for frame rendering methods.

    Context for producing visuals is limited to individual calls, frame engines are not intended for producing motion-like effects.
    """

    def __init__(
        self,
        render_func: FrameRenderFunction,
        settings: RenderingEngineSettings,
    ):
        super().__init__(render_func=render_func, settings=settings)
