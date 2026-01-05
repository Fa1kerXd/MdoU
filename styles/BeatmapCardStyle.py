""" Styles para BeatmapCard.py """

""" Variáveis de cores e estilos """

bg_color_beatmapcard = "#2a2a2a"
border_color_beatmapcard = "#444"
hover_bg_color_beatmapcard = "#333"
hover_border_color_beatmapcard = "#666"

bg_color_img_label = "#1a1a1a"
font_size_img_label = "40px"
border_radius_img_label = "5px"

open_btn_bg = "#ff66aa"
open_btn_hover_bg = "#ff88cc"
open_btn_color = "white"
open_btn_border_radius = "5px"

start_btn_bg = "#66aaff"
start_btn_hover_bg = "#88ccff"
start_btn_disabled_bg = "#555"
start_btn_disabled_color = "#888"
start_btn_color = "white"
start_btn_border_radius = "5px"

progress_bar_border_color = "#444"
progress_bar_bg = "#1a1a1a"
progress_bar_color = "#fff"
progress_bar_chunk_bg = "#66aaff"
progress_bar_chunk_radius = "4px"
progress_bar_border_radius = "5px"

reset_btn_bg = "#66ff66"
reset_btn_color = "white"
reset_btn_border_radius = "5px"

beatmapcard = f"""
    BeatmapCard {{
        background-color: {bg_color_beatmapcard};
        border: 1px solid {border_color_beatmapcard};
        border-radius: 8px;
        margin: 5px;
    }}
    BeatmapCard:hover {{
        background-color: {hover_bg_color_beatmapcard};
        border: 1px solid {hover_border_color_beatmapcard};
    }}
"""

beatmapcard_img_label = f"""
    QLabel {{
        background-color: {bg_color_img_label};
        border-radius: {border_radius_img_label};
        font-size: {font_size_img_label};
    }}
"""

open_btn_style = f"""
    QPushButton {{
        background-color: {open_btn_bg};
        color: {open_btn_color};
        border: none;
        border-radius: {open_btn_border_radius};
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {open_btn_hover_bg};
    }}
"""

start_download_btn_style = f"""
    QPushButton {{
        background-color: {start_btn_bg};
        color: {start_btn_color};
        border: none;
        border-radius: {start_btn_border_radius};
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {start_btn_hover_bg};
    }}
    QPushButton:disabled {{
        background-color: {start_btn_disabled_bg};
        color: {start_btn_disabled_color};
    }}
"""

progress_bar_style = f"""
    QProgressBar {{
        border: 1px solid {progress_bar_border_color};
        border-radius: {progress_bar_border_radius};
        text-align: center;
        background-color: {progress_bar_bg};
        color: {progress_bar_color};
    }}
    QProgressBar::chunk {{
        background-color: {progress_bar_chunk_bg};
        border-radius: {progress_bar_chunk_radius};
    }}
"""

reset_btn_style = f"""
    QPushButton {{
        background-color: {reset_btn_bg};
        color: {reset_btn_color};
        border: none;
        border-radius: {reset_btn_border_radius};
        font-weight: bold;
    }}
"""





