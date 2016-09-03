#!/usr/bin/env python
# coding:utf-8
import sys

import user_db_op

reload(sys)
sys.setdefaultencoding('utf-8')


class UserManager(object):
    def __init__(self, user_name=None, user_id=None, user_email=None, user_phone=None, user_password=None):
        if user_name is not None:
            self.user_object = user_db_op.get_user(user_name=user_name)
        elif user_id is not None:
            self.user_object = user_db_op.get_user(user_id=user_id)
        elif user_email is not None:
            self.user_object = user_db_op.get_user(user_email=user_email)
        elif user_phone is not None:
            self.user_object = user_db_op.get_user(user_phone=user_phone)
        else:
            raise Exception('用户名或者密码错误')

    @classmethod
    def login(cls, user_name=None, user_email=None, user_phone=None, user_password=None, user_ip=None):

        if not user_db_op.is_user_exist(user_name=user_name, user_email=user_email, user_phone=user_phone):
            raise Exception('用户名或者密码错误')
        user = user_db_op.get_user(user_name=user_name, user_email=user_email, user_phone=user_phone)
        if not user.check_passwd(user_password):
            raise Exception('用户名或者密码错误')
        if not user.status:
            raise Exception('账号被禁，禁止登陆')

        kwgs = dict()
        if user_ip:
            kwgs['login_ip'] = user_ip
            user_db_op.update_user(user, **kwgs)



