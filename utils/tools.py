#!/usr/bin/env python
# coding:utf-8
import sys
import time
import uuid
import base64
import re

reload(sys)
sys.setdefaultencoding('utf-8')


def get_base_uuid():
    return base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)


def get_time():
    return int(time.time()*1000000)


def get_uuid():
    uuid_str = str(uuid.uuid1())
    return uuid_str.replace('-', '')


def check_permission(method):
    pass


def check_user_name(user_name):
    check_empty(user_name, '用户名')
    check_length(3, 50, user_name, '用户名')
    pattern = re.compile(r'^[A-Za-z0-9_]{3,50}$')
    if not pattern.match(user_name):
        raise Exception('用户名不正确')


def check_ip(user_ip):
    if user_ip:

        check_length(7, 15, user_ip, 'ip')
        pattern = re.compile(r'\d[1-3]\.\d[1-3]\.\d[1-3]\.\d[1-3]')
        if not pattern.match(user_ip):
            raise ValueError('ip设置不正确')


def check_passwd(user_passwd):
    check_empty(user_passwd, '密码')
    check_length(3, 50, user_passwd, '密码')


def check_email(user_email):
    if user_email:
        pattern = re.compile(r'^[A-Za-z0-9_][3,100]@\.[A-Za-z0-9][1-20]\.[A-Za-z0-9][1-20]\.[A-Za-z0-9][1-20]$')
        if not pattern.match(user_email):
            raise ValueError('邮箱设置正确')


def check_length(min_len, max_len, check_str, tag):
    if min_len <= len(check_str) <= max_len:
        return True
    else:
        raise ValueError('%s长度不合适' % tag)


def check_empty(check_str, tag):
    if not check_str:
        raise ValueError('%s 不能为空值' % tag)


def check_phone(phone):
    if phone:
        check_length(3, 20, phone, '电话')
        pattern = re.compile(r'\d[3,20]')
        if not pattern.match(phone):
            raise ValueError('电话设置有误')

if __name__ == '__main__':
    print get_base_uuid()