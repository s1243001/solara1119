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
        zoom=15,
    )

    # 調整地圖高度 (採用使用者設定的 450px)
    split_control.layout.height = "600px"

    return split_control

@solara.component
def Page():
    solara.Markdown("##馬太鞍溪堰塞湖位置")
    solara.Markdown("馬太鞍堰塞湖位置位於馬太鞍溪上游，形成原因為多年地震造成周圍土石鬆脫，受颱風薇帕影響堵塞於上游。在初次的評估中，並不認為這個堰塞湖會造成危險，在沒有發生大豪雨的情況下不用擔心。但是在颱風樺加紗來臨前的再次評估，此堰塞湖可能造成的破壞及影響範圍結果為非常嚴重，因此緊急撤離光復鄉、鳳林鎮、萬榮鄉等下游住戶，以致力將傷害降到最低")
    repo_url = "https://raw.githubusercontent.com/s1243001/solara1119/main/"
    solara.Image(
                image=f"{repo_url}loc.png",
                width="100%",
                # 移除 height 和 alt 參數以提高相容性
            )
    solara.Markdown("## 馬太鞍溪堰塞湖位置2D 捲簾比對 (Split Map)")

    # 使用 solara.use_memo 確保地圖只建立一次
    split_widget = solara.use_memo(create_split_map, dependencies=[])

    with solara.Column(style={"width": "100%", "height": "700px"}):
        solara.display(split_widget)
