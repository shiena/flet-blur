from enum import auto, Enum
from typing import Optional

from flet.core.colors import Colors
from flet.core.control import Control
from flet.core.types import ColorEnums, ColorValue


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

    async def set_window_effect(
        self,
        effect: WindowEffect = WindowEffect.DISABLED,
        bgcolor: Optional[ColorValue] = Colors.TRANSPARENT,
        dark: Optional[bool] = True,
    ):
        arg2 = bgcolor or Colors.TRANSPARENT
        arg3 = dark or True
        self._set_enum_attr("blurBgcolor", arg2, ColorEnums)
        await self.invoke_method_async(
            "setWindowEffect", {"effect": effect.name, "dark": str(arg3).lower()}
        )
