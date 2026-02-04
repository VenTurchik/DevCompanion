import screeninfo

from src.dev_companion.utils.constants.config import( WINDOW_WIDTH,
                                                      WINDOW_HEIGHT,
                                                      DEFAULT_SCREEN_WIDTH,
                                                      DEFAULT_SCREEN_HEIGHT)


def _calc_offset(screen_w, screen_h):
    return (screen_w - WINDOW_WIDTH) // 4, (screen_h - WINDOW_HEIGHT) // 4

def get_offset():
    try:
        screen = screeninfo.get_monitors()[0]
        return _calc_offset(screen.width, screen.height)
    except Exception as e: # Сделать логирование
        return _calc_offset(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

# src/dev_companion/gui/utils/window_helpers.py
from pathlib import Path
import sys

def get_styles_dir() -> Path:
    """Возвращает путь к папке styles/ относительно корня gui"""
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent / "resources" / "styles"
    else:
        current_file = Path(__file__)
        gui_dir = current_file.parent.parent  # = src/dev_companion/gui
        return gui_dir / "resources" / "styles"

def load_stylesheet(file_name: str) -> str:
    """Загружает CSS-файл из styles/"""
    styles_dir = get_styles_dir()
    file_path = styles_dir / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"Стиль не найден: {file_path}")
    return file_path.read_text(encoding='utf-8')