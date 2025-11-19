import solara
import leafmap.leafmap as leafmap

def create_split_map():
    # 直接使用 split_map，傳入底圖名稱字串
    split_control = leafmap.split_map(
        left_layer="Esri.WorldImagery",  # 左邊：衛星圖 只能底圖圖層  不能是物件
        right_layer="OpenStreetMap",     # 右邊：街道圖 只能底圖圖層  不能是物件
        left_label="衛星影像",
        right_label="街道地圖",
        center=[23.696394945673422, 121.29008028277161], # 台北
        zoom=12,
        # ipyleaflet 的 split_map 本身就會回傳一個地圖物件，不需要額外設定 height
    )

    # (可選) 如果您想調整高度，可以在回傳的地圖物件上設定
    split_control.layout.height = "650px"

    return split_control

@solara.component
def Page():
    
    solara.Markdown("##簡介")
    solara.Markdown("花蓮馬太鞍溪堰塞湖災害，於2025年九月發生，肇因為薇帕颱風的雨勢引發山崩，在馬太鞍溪上游萬榮鄉處形成堰塞湖。其後因樺加沙颱風導致多次溢流，造成下游光復鄉多處遭洪水淹沒，導致多人傷亡與嚴重毀損")
    repo_url = "https://raw.githubusercontent.com/s1243001/11055solara-webmap-app/main/"
    #在這裡幫我新增圖片
    solara.Markdown("## 現場照片")
    with solara.Row(gap="16px", style={"flex-wrap": "wrap", "justify-content": "center"}):
        
        # 圖片 1: 馬太鞍溪堰塞湖災害圖 1
        solara.Image(
            image=f"{repo_url}pic_01.jpg",
            style={
                # 使用 flex 屬性使兩張圖片平均分佈並排，並在小螢幕時換行
                "flex": "1 1 48%",
                "min-width": "300px", # 確保在小螢幕上不會太小
                "max-height": "400px",
                "object-fit": "cover",
                "border-radius": "8px",
                "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.1)"
            },
            alt="馬太鞍溪堰塞湖"
        )
        
        # 圖片 2: 馬太鞍溪堰塞湖災害圖 2
        solara.Image(
            image=f"{repo_url}pic_02.jpg",
            style={
                "flex": "1 1 48%",
                "min-width": "300px",
                "max-height": "400px",
                "object-fit": "cover",
                "border-radius": "8px",
                "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.1)"
            },
            alt="馬太鞍溪堰塞湖災害"
        )
    solara.Markdown("## 馬太鞍溪堰塞湖位置2D 捲簾比對 (Split Map)")

    split_widget = solara.use_memo(create_split_map, dependencies=[])

    with solara.Column(style={"width": "100%", "height": "700px"}):
        solara.display(split_widget)
