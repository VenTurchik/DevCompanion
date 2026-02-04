from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter

from src.dev_companion.gui.widgets.ContentPanel import ContentPanel
from src.dev_companion.gui.widgets.SideBar import SideBar
from src.dev_companion.utils.constants.config import (WIDGET_EXTERNAL_FIELD,
                                                      LAYOUT_EXTERNAL_FIELD,
                                                      LAYOUT_SPACING,
                                                      SPLIT_SIZE,
                                                      SPLITTER_SIZES)


class BottomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()
        self._init_layout()
        self._init_splitter()
        self._init_widget()

    def _init_ui(self):
        self.setContentsMargins(*WIDGET_EXTERNAL_FIELD)
        self.setStyleSheet("background-color: green")

    def _init_layout(self):
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(*LAYOUT_EXTERNAL_FIELD)
        self._layout.setSpacing(LAYOUT_SPACING)
        self.setLayout(self._layout)

    def _init_widget(self):
        self.splitter.addWidget(SideBar())
        self.splitter.addWidget(ContentPanel())
        self._add_widget(self.splitter)

    def _init_splitter(self):
        self.splitter = QSplitter()
        self.splitter.setHandleWidth(SPLIT_SIZE)
        self.splitter.setSizes(SPLITTER_SIZES)

    def _add_widget(self, widget):
        self._layout.addWidget(widget)