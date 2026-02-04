from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from src.dev_companion.utils.constants.config import (CONTENTPANEL_MIN_WIGHT,
                                                      CONTENTPANEL_MAX_WIGHT,
                                                      LAYOUT_EXTERNAL_FIELD,
                                                      LAYOUT_SPACING)


class ContentPanel(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()
        self._init_layout()
        self._init_widget()

    def _init_ui(self):
        self.setStyleSheet("background-color: white")
        self.setMinimumWidth(CONTENTPANEL_MIN_WIGHT)
        self.setMaximumWidth(CONTENTPANEL_MAX_WIGHT)

    def _init_layout(self):
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(*LAYOUT_EXTERNAL_FIELD)
        self._layout.setSpacing(LAYOUT_SPACING)
        self.setLayout(self._layout)

    def _init_widget(self):
        self._add_widget(QLabel("TODO"))

    def _add_widget(self, widget):
        self._layout.addWidget(widget)