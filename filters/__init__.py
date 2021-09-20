from aiogram import Dispatcher

from Jobs.chat_server_aiogram.loader import dp
# from .is_admin import AdminFilter
from .eng_symbols import eng_symbols


if __name__ == "filters":
    dp.filters_factory.bind(eng_symbols)

