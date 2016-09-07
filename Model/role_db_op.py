#!/usr/bin/env python
# coding:utf-8
import sys
from sqlalchemy.orm import sessionmaker
from operation_db import ENGINE

from Model.create_db import Role

Session = sessionmaker(bind=ENGINE)


reload(sys)
sys.setdefaultencoding('utf-8')


def get_role_by_user(user):
    session = Session()
    roles = session.query(Role).join(user).all()
    return roles


def role_is_admin(user):
    roles = user.roles
    if roles is None:
        return False
    for role in roles:
        if role.rolename == '1':
            return True
    return False



