#!/usr/bin/env python
# coding:utf-8
import sys
from create_db import UserLogin,User
from sqlalchemy.orm import sessionmaker
from operation_db import ENGINE
from utils.tools import check_length,check_empty,check_passwd,check_email,check_ip,check_user_name,check_phone
Session = sessionmaker(bind=ENGINE)

reload(sys)
sys.setdefaultencoding('utf-8')


def check_fields(**kwargs):
    check_user_name(kwargs.get('user_name', None))
    check_passwd(kwargs.get('password', None))
    check_email(kwargs.get('email', None))
    check_phone(kwargs.get('phone', None))
    check_ip(kwargs.get('login_ip'), None)


def create_user(**kwargs):
    session = Session()
    kwargs.pop('id', None)
    check_fields(**kwargs)
    user = UserLogin(**kwargs)
    session.add(user)
    session.commit()
    return user


def get_users():
    session = Session()
    users = session.query(UserLogin).all()
    return users


def get_user(user_name=None, user_email=None, user_phone=None,user_id=None):
    session = Session()
    user = None
    if user_name is not None:
        try:
            user = session.query(UserLogin).filter_by(user_name=user_name).first()
        except:
            raise Exception('用户不存在')
    elif user_email is not None:
        try:
            user = session.query(UserLogin).filter_by(email=user_email).first()
        except:
            raise Exception('用户不存在')
    elif user_id is not None:
        try:
            user = session.query(UserLogin).filter_by(id=user_id).first()
        except:
            raise Exception('用户不存在')
    elif user_phone is not None:
        try:
            user = session.query(UserLogin).filter_by(phone=user_phone).first()
        except:
            raise Exception('用户不存在')
    else:
        raise Exception('用户参数错误')
    if user is not None:
        return user
    else:
        raise Exception('用户不存在')


def delete_user(user):
    session = Session()
    try:
        session.delete(user)
        session.commit()
    except:
        raise Exception('删除用户失败')


def update_user(user, **kwargs):
    session = Session()
    kwargs.pop('id', None)
    kwargs.pop('check_passwd', None)
    check_fields(**kwargs)
    if kwargs:
        for k, v in kwargs.items():
            setattr(user, k, v)
        session.merge(user)
    session.commit()


def is_user_exist(user_name=None, user_email=None, user_phone=None,user_id=None):
    try:
        user = get_user(user_name=user_name, user_email=user_email, user_phone=user_phone,user_id=user_id)
    except:
        return False
    if user is not None:
        return True
    else:
        return False

