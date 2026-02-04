from PySide6.QtWidgets import QWidget, QVBoxLayout

from src.dev_companion.gui.widgets.BottomWidget import BottomWidget
from src.dev_companion.gui.widgets.TopBar import TopBar
from src.dev_companion.utils.constants.config import LAYOUT_SPACING, LAYOUT_EXTERNAL_FIELD


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_layout()
        self._init_widget()

    def __init_layout(self):
        self._layout = QVBoxLayout()
        self._layout.setSpacing(LAYOUT_SPACING)
        self._layout.setContentsMargins(*LAYOUT_EXTERNAL_FIELD)
        self.setLayout(self._layout)

    def _init_widget(self):
        self._add_widget(TopBar())
        self._add_widget(BottomWidget())

    def _add_widget(self, widget):
        self._layout.addWidget(widget)