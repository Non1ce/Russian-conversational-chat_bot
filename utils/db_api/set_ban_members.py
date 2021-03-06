# -*- coding: utf-8 -*-


from utils.db_api.creat_db import db, cursor


"""


    Created on 24.09.2021
    
    @author: Nikita


"""


async def ban_members(user_id, time_out):

    """

    The function is designed to ban the chat user.

    """

    add_members = f"""
                    INSERT 
                    INTO banned_chat_members (user_id, time_out) 
                    VALUES ({user_id}, FROM_UNIXTIME({time_out})) 
                    ON DUPLICATE KEY UPDATE time_out = time_out
                    """

    cursor.execute(add_members)

    db.commit()
