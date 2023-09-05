import flet as ft
from utils import call_api
from flet_core.constrained_control import ConstrainedControl
from flet_core.control_event import ControlEvent

def main(page: ft.Page):
    # Functions
    def horizontal_cernter(*some_objects: ConstrainedControl) -> ft.Container:
        return ft.Container(content=ft.Row(
            [some_object for some_object in some_objects],
            alignment=ft.MainAxisAlignment.CENTER,
        ))

    def image_box(image_file_name: str) -> ft.Image:
        return ft.Image(
            src=f".\\{image_file_name}",
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )

    def image_select_button() -> ft.ElevatedButton:
        def clicked(_: ControlEvent):
            pick_files_dialog.pick_files(allow_multiple=True)
            page.update()
        
        return ft.ElevatedButton(
            "選択する",
            icon=ft.icons.IMAGE,
            on_click = clicked
        )
    
    def image_dicision_button() -> ft.ElevatedButton:
        def clicked(_: ControlEvent):
            main_contents.content.controls.append(horizontal_cernter(ft.Text("こんな料理ができそうです！気になる料理はありますか？", size=16)))
            main_contents.content.controls.append(horizontal_cernter(ft.Text("Wait for the completion...")))
            main_contents.content.controls.append(horizontal_cernter(ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee")))
            page.update()
            main_contents.content.controls.append(horizontal_cernter(dish_select_buttons(image_box_field.src)))
            del main_contents.content.controls[-3:-1]
            page.update()
        
        return ft.ElevatedButton(
            "これで探す",
            icon=ft.icons.SEARCH,
            on_click = clicked,
        )

    def dish_select_buttons(image_file_name: str) -> ft.Column:
        def clicked(e: ControlEvent):
            main_contents.content.controls.append(horizontal_cernter(ft.Text(f"{e.control.text}を実際に作ってみましょう！", size=16)))
            main_contents.content.controls.append(horizontal_cernter(ft.ProgressRing(), ft.Text("Wait for the completion...")))
            page.update()
            main_contents.content.controls.append(horizontal_cernter(cooking_steps(e.control.text)))
            del main_contents.content.controls[-2]
            page.update()
        
        response = call_api(
            "api1",
            {"some_input": image_file_name}
        ).json()["some_list"]
        return_object = ft.Column()
        for index, dish in enumerate(response):
            if index % 3 == 0:
                return_object.controls.append(ft.Row())
                return_object.controls[index//3].controls.append(ft.ElevatedButton(
                    text=dish,
                    on_click=clicked
                ))
            else:
                return_object.controls[index//3].controls.append(ft.ElevatedButton(
                    text=dish,
                    on_click=clicked
                ))
        return return_object

    def pick_files_result(e: ft.FilePickerResultEvent):
        image_box_field.src = f".\\{e.files[0].name}"
        main_contents.content.controls.append(horizontal_cernter(ft.Text("この画像で料理を探しますか？", size=16), image_dicision_button()))
        page.update()

    def cooking_steps(selected_dish: str) -> ft.DataTable:
        response = call_api(
            "api1",
            {"some_input": selected_dish}
        ).json()["some_list"]
        return_object = ft.DataTable(
            width=400,
            columns=[ft.DataColumn(ft.Text(column)) for column in ["順番", "手順"]],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(index+1)), ft.DataCell(ft.Text(step))]) for index, step in enumerate(response)]
        )
        return return_object
        
    def reset(_: ControlEvent):
        print("ToDo")
    
    def debug(_: ControlEvent):
        print("Debug")
    
    # Base Objects
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    image_box_field = image_box("no_image.jp")
    page.overlay.append(pick_files_dialog)
    main_contents = ft.Container(ft.Column(
        controls = [
            horizontal_cernter(ft.Text("まず初めに、食材が写った画像を選択しましょう！", size=16)),
            horizontal_cernter(image_select_button(), image_box_field),
            # horizontal_cernter(ft.Text("この画像で料理を探しますか？", size=16), image_dicision_button()),
            # horizontal_cernter(ft.Text("こんな料理ができそうです！気になる料理はありますか？", size=16)),
            # horizontal_cernter(dish_select_buttons()),
            # horizontal_cernter(ft.Text("実際に作ってみましょう！", size=16)),
            # horizontal_cernter(cooking_steps()),
        ],
        height=800,
        scroll=ft.ScrollMode.ALWAYS,
    ))

    page.add(
        ft.AppBar(
            leading=ft.Icon(ft.icons.SPORTS_VOLLEYBALL_OUTLINED),
            title=ft.Text("Sample App"),
            center_title=False,
            bgcolor=ft.colors.LIGHT_BLUE_50,
        ),
        main_contents,
        ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.FOOD_BANK_OUTLINED, label="Dish"),
                ft.NavigationDestination(icon=ft.icons.RESTORE_FROM_TRASH, label="Trash"),
            ]
        ),
        ft.FloatingActionButton(
            icon=ft.icons.REFRESH,
            on_click=reset,
            bgcolor=ft.colors.LIGHT_BLUE_50,
        )
    )

# デスクトップの場合
ft.app(target=main)

# Webの場合
# ft.app(target=main, port=8900, view=ft.AppView.WEB_BROWSER)
