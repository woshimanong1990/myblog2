#!/usr/bin/env python
# coding:utf-8
import sys
import time
import urlparse
import uuid
import base64
import re

import functools
from urllib import urlencode

from tornado.web import HTTPError

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
        pattern = re.compile(r'^(\w)+(\.\w+)*@(\w)+((\.\w{2,10}){1,3})$')
        if not pattern.match(user_email):
            raise ValueError('邮箱设置不正确')


def check_length(min_len, max_len, check_str, tag):
    if min_len <= len(check_str) <= max_len:
        return True
    else:
        raise ValueError('%s长度不合适' % tag)


def check_empty(check_str, tag):
    if not check_str:
        raise ValueError('%s 不能为空值' % tag)

def escape_replace_str(content):
    return content


def check_phone(phone):
    if phone:
        check_length(3, 20, phone, '电话')
        pattern = re.compile(r'\d{3,20}')
        if not pattern.match(phone):
            raise ValueError('电话设置有误')


def catch_exce(func):
    def wrapped(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            self.set_status(404, reason=e.message)

            self.write_error(404, **{'exc_info': e.message})
    return wrapped

def authenticated(method):
    """Decorate methods with this to require that the user be logged in.

    If the user is not logged in, they will be redirected to the configured
    `login url <RequestHandler.get_login_url>`.

    If you configure a login url with a query parameter, Tornado will
    assume you know what you're doing and use it as-is.  If not, it
    will add a `next` parameter so the login page knows where to send
    you once you're logged in.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.request.method in ("GET", "HEAD"):
                url = self.get_login_url()
                if "?" not in url:
                    if urlparse.urlsplit(url).scheme:
                        # if login url is absolute, make next absolute too
                        next_url = self.request.full_url()
                    else:
                        next_url = self.request.uri
                    url += "?" + urlencode(dict(next=next_url))
                self.redirect(url)
                return
            raise HTTPError(403)
        return method(self, *args, **kwargs)
    return wrapper

if __name__ == '__main__':
    print get_base_uuid()