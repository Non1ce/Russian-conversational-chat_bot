# -*- coding: utf-8 -*-

import mysql.connector
from Jobs.chatbot.data import config


"""


Created on 10.09.2021

@author: Nikita


"""

db = mysql.connector.connect(host=config.host,
                             database=config.database,
                             user=config.user,
                             password=config.password)

cursor = db.cursor()
