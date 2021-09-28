# -*- coding: utf-8 -*-

from Jobs.chatbot.loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
