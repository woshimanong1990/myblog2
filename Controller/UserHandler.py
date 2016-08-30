#!/usr/bin/env python
# coding:utf-8
import traceback
import sys
import json
from utils.tools import check_permission, catch_exce
from BaseHandler import BaseHandler
from tornado.web import authenticated

from Model.user_manager import UserManager
from Model.user_db_op import create_user,get_user

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

    @catch_exce
    def post(self):
        user_ip = self.request.headers.get('X-Real-Ip', None)
        body = json.loads(self.request.body)
        passwd = body.get('password', None)
        check_passwd = body.pop('check_passwd', None)
        message = None
        if not passwd:
            raise Exception('密码不能为空')
        if not check_passwd:
            message = '确认密码不能为空'
            self.write_error(404, **{'exc_info': message})
        if passwd != check_passwd:
            message = '两次密码不一致'
            self.write_error(404, **{'exc_info': message})
        code = self.get_secure_cookie('check_code')
        check_code = body.pop('check_code', None)
        check_code = check_code.replace(' ', '', 1)
        if not check_code:
            message = '验证码不能为空'
            self.write_error(404, **{'exc_info': message})
        if code != check_code.encode('utf-8'):
            self.write_error(404, **{'exc_info': message})

        body['login_ip'] = user_ip
        try:
            user = create_user(**body)
        except Exception as e:
            message = e.message
            self.set_status(404, reason=message)
            self.write_error(404)

        self.render('home.html')


class UsersLoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    @check_permission
    @authenticated
    def post(self):
        user_name = self.get_argument('username')
        user_passwd = self.get_argument('userpwd')
        UserManager.login(user_name, user_passwd)
        self.render('home.html')


class UsersLogoutHandler(BaseHandler):
    @check_permission
    @authenticated
    def get(self):
        pass


class SignOutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('signout.html')




class CheckUserHandler(BaseHandler):
    @catch_exce
    def post(self):
        if self.json_args:
            user_name = self.json_args.get("user_name", None)
            user_email = self.json_args.get("email", None)
            user_phone = self.json_args.get("phone", None)
        else:
            user_name = self.get_argument("user_name")
            user_email = self.get_argument("email")
            user_phone = self.get_argument("phone")
        try:
            get_user(user_name=user_name, user_email=user_email, user_phone=user_phone)
        except:
            raise Exception("用户不存在")
        else:
            self.write("用户已存在")
user_handler = [
    (r'/v01/users', UsersHandler),
    (r'/v01/user/([0-9]+)', UserHandler),
    (r'/v01/login', UsersLoginHandler),
    (r'/v01/logout', UsersLogoutHandler),
    (r'/v01/signout', SignOutHandler),
    (r'/v01/check_user', CheckUserHandler),
]
