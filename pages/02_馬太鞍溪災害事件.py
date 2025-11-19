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

    # 調整地圖高度
    split_control.layout.height = "650px"

    return split_control

@solara.component
def Page():
    
    solara.Markdown("## 簡介")
    solara.Markdown("花蓮馬太鞍溪堰塞湖災害，於2025年九月發生，肇因為薇帕颱風的雨勢引發山崩，在馬太鞍溪上游萬榮鄉處形成堰塞湖。其後因樺加沙颱風導致多次溢流，造成下游光復鄉多處遭洪水淹沒，導致多人傷亡與嚴重毀損")
    
    # GitHub 圖片庫的基礎 URL
    repo_url = "https://raw.githubusercontent.com/s1243001/11055solara-webmap-app/main/"
    
    # 新增圖片並排顯示 (使用 solara.Row 實現並排)
    solara.Markdown("## 現場照片")
    solara.Image(
                image=f"{repo_url}pic_01.jpg",
                alt="馬太鞍溪堰塞湖",
                # 移除 style 參數，改用 width/height 確保圖片填充容器
                width="100%",
                height="100%",
            )
        
    solara.Image(
                image=f"{repo_url}pic_02.jpg",
                alt="馬太鞍溪堰塞湖災害",
                # 移除 style 參數，改用 width/height 確保圖片填充容器
                width="100%",
                height="100%",
            )
    
    solara.Markdown("## 馬太鞍溪堰塞湖位置2D 捲簾比對 (Split Map)")

    # 使用 solara.use_memo 確保地圖只建立一次
    split_widget = solara.use_memo(create_split_map, dependencies=[])

    with solara.Column(style={"width": "100%", "height": "700px"}):
        solara.display(split_widget)
