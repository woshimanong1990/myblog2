#!/usr/bin/env python
# coding:utf-8
import sys
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from create_db import User, Base,Blog,Comment,Role

reload(sys)
sys.setdefaultencoding('utf-8')

ENGINE = create_engine("mysql+mysqldb://root:519966hao@localhost/sqlalchemy?charset=utf8", echo=True, logging_name='mylog.log')


def init_db(SERVER_LOG=None):
    Base.metadata.create_all(ENGINE)
    User()
    Blog()
    Comment()
    Role()


