from enum import auto, Enum
from typing import Optional

from flet.core.control import Control

class WindowEffect(Enum):
    DISABLED = auto()
    SOLID = auto()
    TRANSPARENT = auto()
    AERO = auto()
    ACRYLIC = auto()
    MICA = auto()
    TABBED = auto()

class Blur(Control):
    """
    Blur Control.
    """

    def __init__(
        self,
        #
        # Control
        #
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
    ):
        Control.__init__(
            self,
            visible=visible,
            disabled=disabled,
        )

    def _get_control_name(self):
        return "blur"

    async def set_window_effect(self, effect: Optional[WindowEffect] = WindowEffect.DISABLED):
        arg = effect or WindowEffect.DISABLED
        await self.invoke_method_async("setWindowEffect", {"effect": arg.name})
