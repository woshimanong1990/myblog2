#!/usr/bin/env python
# coding:utf-8
import sys
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from create_db import User, Base,Blog,Comment,Role,Permission

reload(sys)
sys.setdefaultencoding('utf-8')

ENGINE = create_engine("mysql+mysqldb://root:519966hao@localhost/sqlalchemy?charset=utf8", echo=False)


def log_test02():
    import logging
    import logging.config
    CONF_LOG = os.path.join(os.path.dirname(__file__), "log.conf")
    logging.config.fileConfig(CONF_LOG)  # 采用配置文件
    logger = logging.getLogger("xzs")
    return logger

def init_db():
    log = id(log_test02())
    logging.getLogger('sqlalchemy').setLevel(logging.INFO)
    Base.metadata.create_all(ENGINE)

