import logging

from abc import ABCMeta, abstractmethod
from mysql.connector import pooling, Error
from ..tools import singleton
from ..properties import LOG_FORMAT, LOG_PATHES, POOL_NAME, POOL_SIZE, DB_CONFIG

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__],
                    filemode="a+", format=LOG_FORMAT)

class IDatabase(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        '''
        Should connect to DB using connectionpool
        '''

    @abstractmethod
    def close(self):
        '''
        Should close all connections from pool
        '''


class IConnection(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, db : IDatabase):
        '''
        Should take connectionfrom the pool
        '''

    @abstractmethod
    def __del__(self):
        '''
        Should put connectionback to the pool
        '''


@singleton
class MySQL_DB(IDatabase):
    def connect(self):
        try:
            self.cnx_pool = pooling.MySQLConnectionPool(pool_name = POOL_NAME,
                                                        pool_size = POOL_SIZE,
                                                        **DB_CONFIG)
        except Error:
            logging.exception()

    def close(self):
        self.cnx_pool._remove_connections()


class MySQL_CNX(IConnection):
    def __init__(self, db : MySQL_DB):
        self.db = db
        try:
            self.cnx = self.db.cnx_pool.get_connection()
        except AttributeError:
            logging.exception('Most likely forgot to connect to DB')
        except Error:
            logging.exception()

    def __del__(self):
        self.cnx.close()