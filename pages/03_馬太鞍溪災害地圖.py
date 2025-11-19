import solara
import leafmap.maplibregl as leafmap
import os

# 1. 從 Hugging Face Secret 讀取 API Key
# 如果未設定，提供一個預設值，但地圖將無法正常載入
MAPTILER_KEY = os.environ.get("MAPTILER_API_KEY", "")

def create_3d_map():
    # 檢查 API Key 是否存在
    if not MAPTILER_KEY:
        # 如果沒有 Key，回傳一個基礎地圖，但不會有地形
        m = leafmap.Map(
            center=[120.9, 23.7],
            zoom=7,
            style="OpenStreetMap",
        )
        # 這是標準的 ipywidgets 語法，對 maplibregl.Map 物件有效
        m.layout.height = "700px"
        return m

    # MapTiler Outdoor-v2 Style 內建支援地形資料
    style_url = f"https://api.maptiler.com/maps/outdoor-v2/style.json?key={MAPTILER_KEY}"

    m = leafmap.Map(
        style=style_url,
        center=[121.42961489442239,23.68323270710366], # 台灣中心偏向山區，方便觀察地形
        zoom=12,
        pitch=45,  # 傾斜角度
        bearing=15, # 旋轉角度
        )
    m.layout.height = "700px"
    return m

@solara.component
def Page():
    # 3. 使用 solara.use_memo 快取地圖物件
    # 依賴於 MAPTILER_KEY，當 Key 改變時地圖會重新生成
    map_object = solara.use_memo(create_3d_map, dependencies=[MAPTILER_KEY])
    
    # 修正：使用 solara.Column 容器將所有 UI 元素包裝起來並回傳
    with solara.Column():
        # 2. 警示使用者如果金鑰未設定
        if not MAPTILER_KEY:
            solara.Warning(
                "MapTiler API Key 未設定。請在 Hugging Face Space Settings 中加入 'MAPTILER_API_KEY' Secret，否則 3D 地形無法載入。"
            )
        
        solara.Markdown("## 馬太鞍溪堰塞湖潰堤災害")
        solara.Markdown("在樺加沙颱風來臨後，馬太鞍溪堰塞湖潰堤，洪水挾帶泥沙沖向下游，馬太鞍溪橋被沖毀，同時下游南側的堤防受損，導致大量洪水沖入光復鄉。在當下，政府將民眾疏散至較高的光復糖廠，並將糖廠站設為指揮所。")
        solara.Markdown("## 3D 地形展示 (MapLibre GL)")

        # 4. 渲染地圖
        solara.display(map_object.to_solara()) # 使用 solara.display 渲染 map_object

    # 當使用 with 語法時，solara.Column() 會被隱式地作為 Page 元件的回傳值。