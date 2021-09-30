# -*- coding: utf-8 -*-


from data import config
import mysql.connector
import logging


"""


    Created on 24.09.2021
    
    @author: Nikita


"""


db = mysql.connector.connect(host=config.host,
                             database=config.database,
                             user=config.user,
                             password=config.password)

cursor = db.cursor()

logging.info('The connection to the database is established!')
