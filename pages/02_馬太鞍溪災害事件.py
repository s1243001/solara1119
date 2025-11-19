import solara
import leafmap.leafmap as leafmap

def create_split_map():
    # 建立 Leafmap 的 Split Map 控制項
    split_control = leafmap.split_map(
        left_layer="Esri.WorldImagery",  # 左邊：衛星圖 只能底圖圖層  不能是物件
        right_layer="OpenStreetMap",     # 右邊：街道圖 只能底圖圖層  不能是物件
        left_label="衛星影像",
        right_label="街道地圖",
        center=[23.696394945673422, 121.29008028277161], # 花蓮萬榮鄉 (近似值)
        zoom=12,
    )

    # 調整地圖高度 (採用使用者設定的 450px)
    split_control.layout.height = "450px"

    return split_control

@solara.component
def Page():

    
    solara.Markdown("## 馬太鞍溪堰塞湖位置2D 捲簾比對 (Split Map)")

    # 使用 solara.use_memo 確保地圖只建立一次
    split_widget = solara.use_memo(create_split_map, dependencies=[])

    with solara.Column(style={"width": "100%", "height": "700px"}):
        solara.display(split_widget)
