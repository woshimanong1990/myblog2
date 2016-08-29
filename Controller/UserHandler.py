#!/usr/bin/env python
# coding:utf-8
import traceback
import sys
import json
from utils.tools import check_permission
from BaseHandler import BaseHandler
from tornado.web import authenticated

from Model.user_manager import UserManager
from Model.user_db_op import create_user

reload(sys)


class UserHandler(BaseHandler):
    @check_permission
    @authenticated
    def get(self, user_id):
        pass

    @check_permission
    @authenticated
    def put(self, user_id):
        pass

    @check_permission
    @authenticated
    def delete(self, user_id):
        pass


class UsersHandler(BaseHandler):

    @authenticated
    def get(self):
        pass



    def post(self):
        
        user_ip = self.request.headers.get('X-Real-Ip', None)
        body = json.loads(self.request.body)
        passwd = body.get('password', None)
        check_passwd = body.pop('check_passwd', None)
        if not passwd:
            raise ValueError('密码不能为空')
        if not check_passwd:
            raise ValueError('确认密码不能为空')
        if passwd != check_passwd:
            raise ValueError('两次密码不一致')
        code = self.get_secure_cookie('check_code')
        check_code = body.pop('check_code', None)
        if not check_code:
            raise ValueError('验证码不能为空')
        if code != check_code:
            raise ValueError('验证码不正确')

        body['login_ip'] = user_ip
        try:
            user = create_user(**body)
        except:
            s = traceback.format_exc()
            print s
        return user.id


class UsersLoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    @check_permission
    @authenticated
    def post(self):
        user_name = self.get_argument('username')
        user_passwd = self.get_argument('userpwd')
        UserManager.login(user_name, user_passwd)
        self.redirect('/v01/blogs')


class UsersLogoutHandler(BaseHandler):
    @check_permission
    @authenticated
    def get(self):
        pass


class SignOutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('signout.html')
user_handler = [
    (r'/v01/users', UsersHandler),
    (r'/v01/user/([0-9]+)', UserHandler),
    (r'/v01/login', UsersLoginHandler),
    (r'/v01/logout', UsersLogoutHandler),
    (r'/v01/signout', SignOutHandler),
]
