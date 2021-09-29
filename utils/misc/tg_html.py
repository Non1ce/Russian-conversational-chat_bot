# -*- coding: utf-8 -*-


from html import escape


async def mention_html(user_id, name):

    """

    The function is designed to output a link to a telegram.

    """

    return f'<a href="tg://user?id={user_id}">{escape(name)}</a>'
