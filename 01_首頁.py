import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 吳承翰1105的網站

        這是一個顯示2D台北捷運圖以及3D台北建築圖的網站
        <br>
        (但我還沒讀交通地理)
        """

        solara.Markdown(markdown)