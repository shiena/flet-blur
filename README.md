# Flet Blur control
Blur control for [Flet](https://flet.dev/) integrating [flutter_acrylic](https://pub.dev/packages/flutter_acrylic)

## Installation

```bash
pip install flet-blur
```

Build the library before running the script.

for windows user:

```bash
flet build windows -v
```

for macOS user:

```bash
flet build macos -v
```

for linux user:

```bash
flet build linux -v
```

## Example

```py
import flet as ft

import flet_blur as ftb


def main(page: ft.Page):
    bgblur = ftb.Blur()

    def on_click(
        effect: ftb.WindowEffect,
        color: ft.Colors = ft.Colors.TRANSPARENT,
        dark: bool = True,
    ):
        async def f(e):
            await bgblur.set_window_effect(effect, color, dark)

        return f

    page.overlay.append(bgblur)
    page.bgcolor = ft.Colors.TRANSPARENT
    page.add(
        ft.Text("Acrylic!"),
        ft.ElevatedButton(
            "transparent",
            on_click=on_click(ftb.WindowEffect.TRANSPARENT, ft.Colors.BLACK, False),
        ),
        ft.ElevatedButton(
            "solid", on_click=on_click(ftb.WindowEffect.SOLID, ft.Colors.RED, True)
        ),
        ft.ElevatedButton(
            "aero", on_click=on_click(ftb.WindowEffect.AERO, ft.Colors.BLUE, False)
        ),
        ft.ElevatedButton(
            "acrylic",
            on_click=on_click(ftb.WindowEffect.ACRYLIC, ft.Colors.GREEN, True),
        ),
        ft.ElevatedButton(
            "mica",
            on_click=on_click(ftb.WindowEffect.MICA, ft.Colors.TRANSPARENT, False),
        ),
        ft.ElevatedButton(
            "tabbed", on_click=on_click(ftb.WindowEffect.TABBED, ft.Colors.BLACK, True)
        ),
        ft.ElevatedButton(
            "disabled",
            on_click=on_click(ftb.WindowEffect.DISABLED, ft.Colors.BLACK, False),
        ),
    )


ft.app(main)
```

## Known issues

Some effects do not work, see https://github.com/alexmercerind/flutter_acrylic/issues .

## Reference

- https://github.com/flet-dev/flet/pull/4441
