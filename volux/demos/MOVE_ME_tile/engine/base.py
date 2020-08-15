from ..types import FrameRenderFunction, LifxTileFrame, RenderingEngineSettings


class RenderingEngine:
    """Base class for all rendering engines.

    Provides a generic interface.
    """

    def __init__(
        self,
        render_func: FrameRenderFunction,
        settings: RenderingEngineSettings,
    ):
        self._render_func = render_func
        self.settings = settings

    def render(self, val) -> LifxTileFrame:
        return self._render_func(val, settings=self.settings)
