from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton

from src.dev_companion.gui.utils.draggable import DraggableWindow
from src.dev_companion.utils.constants.config import (TOPBAR_HEIGHT,
                                                      WIDGET_EXTERNAL_FIELD,
                                                      LAYOUT_EXTERNAL_FIELD,
                                                      LAYOUT_SPACING)


class TopBar(DraggableWindow, QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()
        self._init_layout()
        self._init_widget()

    def _init_ui(self):
        self.setStyleSheet("background-color: blue;")
        self.setFixedHeight(TOPBAR_HEIGHT)
        self.setContentsMargins(*WIDGET_EXTERNAL_FIELD)

    def _init_layout(self):
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(*LAYOUT_EXTERNAL_FIELD)
        self._layout.setSpacing(LAYOUT_SPACING)
        self.setLayout(self._layout)

    def _init_widget(self):
        self._add_widget(QLabel("For testing purposes..."))


    def _add_widget(self, widget):
        self._layout.addWidget(widget)
