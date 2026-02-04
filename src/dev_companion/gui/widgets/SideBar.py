from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy

from src.dev_companion.utils.constants.config import SIDEBAR_MIN_WIGHT, SIDEBAR_MAX_WIGHT, LAYOUT_EXTERNAL_FIELD, \
    LAYOUT_SPACING


class SideBar(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()
        self._init_layout()
        self._init_widgets()

    def _init_ui(self):
        self.setStyleSheet("background-color: black;")
        self.setMinimumWidth(SIDEBAR_MIN_WIGHT)
        self.setMaximumWidth(SIDEBAR_MAX_WIGHT)

    def _init_layout(self):
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(*LAYOUT_EXTERNAL_FIELD)
        self._layout.setSpacing(LAYOUT_SPACING)
        self.setLayout(self._layout)

    def _init_widgets(self):
        for _ in range(10):
            self._add_widget(QLabel("For testing purposes only"))

    def _add_widget(self, widget):
        self._layout.addWidget(widget)