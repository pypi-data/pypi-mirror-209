import flet


def Widget_Browse_Frame(widget_name, widget_info_dict, on_click, page_name):
    def action(event):
        on_click(widget_name, page_name)

    def on_hover(event):
        event.control.bgcolor = "#474747" if event.data == "true" else "#5C5C5C"
        event.control.update()

    r = flet.Row(
        [
            flet.Text(" "),
            flet.Icon(widget_info_dict["icon"], size=18, color=flet.colors.WHITE),
            flet.Text(widget_name, size=13, color=flet.colors.WHITE)
        ],
        spacing=12
    )

    c = flet.Container(
        content=r,
        width=170,
        height=35,
        bgcolor="#5C5C5C",
        on_click=action,
        expand=True,
        on_hover=on_hover,
        border_radius=12
    )

    return flet.Row([c], alignment=flet.MainAxisAlignment.CENTER)
