from aiogram import Dispatcher

from Jobs.chat_server_aiogram.loader import dp
from .throttling import ThrottlingMiddleware
# from .my_middlewares import ban_member


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    # dp.middleware.setup(ban_member())
