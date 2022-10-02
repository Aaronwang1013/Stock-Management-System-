
##build-in module
import sys

## Installed module
import pymysql
import sqlalchemy
from sqlalchemy import create_engine


from . import config


class Connect():
    def __init__(self , table) -> None:
        self.dbconfig = config.DBTable
        self.dbtable = config.DBTable.table[table]
    def connectdb(self):
        connection = pymysql.connect(self.dbconfig)
        cursor = connection.cursor()
        




if __name__ == '__main__':
    connect()