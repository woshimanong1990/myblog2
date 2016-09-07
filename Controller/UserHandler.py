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

    @authenticated
    def get(self, user_id):
        pass


    @authenticated
    def put(self, user_id):
        pass

    @authenticated
    def delete(self, user_id):
        pass


class UsersHandler(BaseHandler):

    @authenticated
    def get(self):
        pass

    @catch_exce
    def post(self):
        if self.json_args:
            user_name = self.json_args.get('user_name',None)
            passwd = self.json_args.get('password', None)
            check_passwd = self.json_args.pop('check_passwd', None)
            check_code = self.json_args.pop('check_code', None)
            body = self.json_args
        else:
            raise Exception('参数有误')
        user_ip = self.request.headers.get('X-Real-Ip', None)
        message = None
        if not user_name:
            raise Exception('用户名不能为空')
        if not passwd:
            raise Exception('密码不能为空')
        if not check_passwd:
            message = '确认密码不能为空'
            self.write_error(404, **{'exc_info': message})
        if passwd != check_passwd:
            message = '两次密码不一致'
            self.write_error(404, **{'exc_info': message})

        code = self.get_secure_cookie('check_code')
        check_code = check_code.replace(' ', '', 1)
        if not check_code:
            message = '验证码不能为空'
            self.write_error(404, **{'exc_info': message})
        if code != check_code.encode('utf-8'):
            message = '验证码错误'
            self.write_error(404, **{'exc_info': message})

        body['login_ip'] = user_ip
        try:
            user = create_user(**body)
        except Exception as e:
            raise e
        self.set_secure_cookie('user_name', user_name)
        self.redirect('/v01/home')


class UsersLoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    @catch_exce
    def post(self):
        user_ip = self.request.headers.get('X-Real-Ip', None)
        if self.json_args:
            user_name = self.json_args.get('user_name', None)
            user_passwd = self.json_args.get('password', None)
            check_code = self.json_args.get('check_code', None)
        else:
            user_name = self.get_argument('username', default=None)
            user_passwd = self.get_argument('password', default=None)
            check_code = self.get_argument('check_code',  default=None)
        if not user_name:
            raise Exception('用户名不能为空')
        if not user_passwd:
            raise Exception('密码不能为空')
        code = self.get_secure_cookie('check_code')
        check_code = check_code.replace(' ', '', 1)
        if not check_code:
            message = '验证码不能为空'
            self.write_error(404, **{'exc_info': message})
        if code != check_code.encode('utf-8'):
            message = '验证码错误'
            self.write_error(404, **{'exc_info': message})
        try:
            UserManager.login(user_name=user_name, user_password=user_passwd, user_ip=user_ip)
        except:
            s = traceback.format_exc()
            print s
            raise Exception('抱歉，登录失败')
        self.set_secure_cookie('user_name', user_name)
        self.redirect('/v01/home')


class UsersLogoutHandler(BaseHandler):
    @authenticated
    def get(self):
        if self.get_argument('logout', None):
            self.clear_cookie("user_name")
            self.redirect("/")


class SignUpHandler(BaseHandler):
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
            user_name = self.get_argument("user_name", default=None)
            user_email = self.get_argument("email", default=None)
            user_phone = self.get_argument("phone", default=None)
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
    (r'/v01/signup', SignUpHandler),
    (r'/v01/check_user', CheckUserHandler),
]
