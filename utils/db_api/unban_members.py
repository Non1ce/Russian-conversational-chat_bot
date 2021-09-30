# -*- coding: utf-8 -*-


from utils.db_api.creat_db import cursor


"""


    Created on 24.09.2021
    
    @author: Nikita


"""


async def unban_member(user_id, ban_time):

    """

    The function is designed to unban the chat user.

    """

    del_members = f"DELETE from banned_chat_members WHERE time_out < DATE_SUB(NOW(), INTERVAL {ban_time} SECOND)"

    add_members = f"""SELECT user_id FROM banned_chat_members WHERE user_id={user_id}"""

    cursor.execute(del_members)
    cursor.execute(add_members)

    result = cursor.fetchall()
    result = [row[0] for row in result]

    return result
