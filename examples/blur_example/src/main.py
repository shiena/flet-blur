import flet as ft

import blur as ftb

def main(page: ft.Page):
    bgblur = ftb.Blur()

    def on_click(v: ftb.WindowEffect):
        async def f(e):
            await bgblur.set_window_effect(v)
        return f

    page.overlay.append(bgblur)
    page.bgcolor = ft.Colors.TRANSPARENT
    page.add(
        ft.Text("Acrylic!"),
        ft.ElevatedButton("transparent", on_click=on_click(ftb.WindowEffect.TRANSPARENT)),
        ft.ElevatedButton("solid", on_click=on_click(ftb.WindowEffect.SOLID)),
        ft.ElevatedButton("aero", on_click=on_click(ftb.WindowEffect.AERO)),
        ft.ElevatedButton("acrylic", on_click=on_click(ftb.WindowEffect.ACRYLIC)),
        ft.ElevatedButton("mica", on_click=on_click(ftb.WindowEffect.MICA)),
        ft.ElevatedButton("tabbed", on_click=on_click(ftb.WindowEffect.TABBED)),
        ft.ElevatedButton("disabled", on_click=on_click(ftb.WindowEffect.DISABLED)),
    )

ft.app(main)
