import flet as ft 

def main(page: ft.Page):
    # definindo o titulo do app
    # 
    page.title = "Calculadora"
    page.bgcolor = "#2d2d2d"
    page.window.width = 350
    page.window.height = 470

    todos_valores = ""

    resultado_texto = ft.Text(value="0", size=28, color="white", text_align="right" )

    def entrar_valores(e):
        nonlocal todos_valores
        todos_valores += str(e.control.text)
        resultado_texto.value = todos_valores
        page.update()

    def clear_display(e):
        nonlocal todos_valores
        todos_valores = ""
        resultado_texto.value = ""
        page.update()

    def calcular(e):
        nonlocal todos_valores
        try:
            resultado_texto.value = str(eval(todos_valores))
            todos_valores = resultado_texto.value
        except:
            resultado_texto.value = 'Error'
            todos_valores = ""
        page.update()

    display = ft.Container(
        content = resultado_texto,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right
    )

    # Estilização da grade de botões
    style_num = {
        "height": 60,
        "bgcolor": "#4d4d4d",
        "color": "white",
        "expand": 1,
    }

    style_oper = {
        "height": 60,
        "bgcolor": "#FF9500",
        "color": "white",
        "expand": 1,
    }

    style_clear = {
        "height": 60,
        "bgcolor": "#FF3B60",
        "color": "white",
        "expand": 1,
    }

    style_egual = {
        "height": 60,
        "bgcolor": "#34C759",
        "color": "white",
        "expand": 1,
    }



    grid_buttons = [
        [
            ('C',style_clear, clear_display),
            ('%',style_oper, entrar_valores),
            ('/',style_oper, entrar_valores),
            ('*',style_oper, entrar_valores)
        ],

        [
            ('7',style_num, entrar_valores),
            ('8',style_num, entrar_valores),
            ('9',style_num, entrar_valores),
            ('-',style_oper, entrar_valores)
        ],

        [
            ('4',style_num, entrar_valores),
            ('5',style_num, entrar_valores),
            ('6',style_num, entrar_valores),
            ('+',style_oper, entrar_valores)
        ],

        [
            ('1',style_num, entrar_valores),
            ('2',style_num, entrar_valores),
            ('3',style_num, entrar_valores),
            ('=',style_egual,calcular)
        ],

        [
            ('0', {**style_num, "expand":2}, entrar_valores),
            ('.',style_num, entrar_valores),
            ('Del',style_oper, lambda e: None)
        ],
    ]

    botoes = []
    
    for row in grid_buttons:
        row_control = []
        for text, style, handler in row:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0
                )
            )
            row_control.append(btn)
        botoes.append(ft.Row(row_control, spacing=5))

    page.add(
        ft.Column(
            [
                display, 
                ft.Column(botoes, spacing=5)
            ]
        )
    )

ft.app(target=main)