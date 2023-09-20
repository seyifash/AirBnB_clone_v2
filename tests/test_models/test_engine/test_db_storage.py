#!/usr/bin/python3
""" """
import unittest
from os import getenv
import MySQLdb
from models.engine.db_storage import DBStorage
from models.state import State


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'Not db storage')
class TestDBStorage(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(self):
        self.user = getenv('HBNB_MYSQL_USER')
        self.password = getenv('HBNB_MYSQL_PWD')
        self.database = getenv('HBNB_MYSQL_DB')
        self.host = getenv('HBNB_MYSQL_HOST')
        self.db = MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.database
        )

        self.cur = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def teardown(self):
        self.cur.close()
        self.db.close()

    def test_add(self):
        """ """
        self.cur.execute("SELECT * FROM states")
        states1 = self.cur.fetchall()
        obj = State(name="Texas")
        obj.save()
        self.cur.execute("SELECT * FROM states")
        states2 = self.cur.fetchall()
        self.assertEqual(len(states2), len(states1) + 1)
