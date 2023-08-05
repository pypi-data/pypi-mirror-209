from __future__ import annotations

from pathlib import Path


BASE_PATH = Path(__file__).parent


CLI_EPILOG = 'Project Homepage: https://github.com/jedie/inverter-connect'


ERROR_STR_NO_DATA = 'no data'
AT_READ_FUNC_NUMBER = 0x03
AT_WRITE_FUNC_NUMBER = 0x10
TYPE_MAP = {
    'float': float,
    'int': int,
}

SETTINGS_DIR_NAME = 'inverter-connect'
SETTINGS_FILE_NAME = 'inverter-connect'
