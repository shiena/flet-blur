import flet as ft

from blur import Blur


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=Blur(
                    tooltip="My new Blur Control tooltip",
                    value = "My new Blur Flet Control", 
                ),),

    )


ft.app(main)
