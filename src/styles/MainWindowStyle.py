"""Style para o MainWindow.py"""

""" Variáveis de cores e estilos"""

bg_mainwindow = "#1a1a1a"
label_color = "#fff"

lineedit_bg = "#2a2a2a"
lineedit_color = "#fff"
lineedit_border_color = "#444"
lineedit_border_radius = "5px"
lineedit_padding = "8px"
lineedit_font_size = "14px"

btn_bg = "#ff66aa"
btn_hover_bg = "#ff88cc"
btn_disabled_bg = "#555"
btn_disabled_color = "#888"
btn_color = "white"
btn_border_radius = "5px"
btn_padding = "8px 16px"
btn_font_weight = "bold"
btn_font_size = "14px"

combobox_bg = "#2a2a2a"
combobox_color = "#fff"
combobox_border_color = "#444"
combobox_border_radius = "5px"
combobox_padding = "5px"

scroll_area_border = "none"
scroll_area_bg = "transparent"




setup_ui_style = f"""
    QMainWindow {{
        background-color: {bg_mainwindow};
    }}
    QLabel {{
        color: {label_color};
    }}
    QLineEdit {{
        background-color: {lineedit_bg};
        color: {lineedit_color};
        border: 1px solid {lineedit_border_color};
        border-radius: {lineedit_border_radius};
        padding: {lineedit_padding};
        font-size: {lineedit_font_size};
    }}
    QPushButton {{
        background-color: {btn_bg};
        color: {btn_color};
        border: none;
        border-radius: {btn_border_radius};
        padding: {btn_padding};
        font-weight: {btn_font_weight};
        font-size: {btn_font_size};
    }}
    QPushButton:hover {{
        background-color: {btn_hover_bg};
    }}
    QPushButton:disabled {{
        background-color: {btn_disabled_bg};
        color: {btn_disabled_color};
    }}
    QComboBox {{
        background-color: {combobox_bg};
        color: {combobox_color};
        border: 1px solid {combobox_border_color};
        border-radius: {combobox_border_radius};
        padding: {combobox_padding};
    }}
"""

scroll_area_style = f"""
    QScrollArea {{
        border: {scroll_area_border};
        background-color: {scroll_area_bg};
    }}
"""
