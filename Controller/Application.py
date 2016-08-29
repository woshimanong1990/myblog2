#!/usr/bin/env python
# coding:utf-8
import sys
import os

import logging
from logging import FileHandler


from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import tornado.options
from tornado.log import access_log,gen_log

from IndexHandler import index_handelr
from BlogHandler import blog_handelr
from UserHandler import user_handler
from CommentHandler import comment_handler
from Model.operation_db import init_db
from CheckcodeHandler import checkcode_handelr


reload(sys)
sys.setdefaultencoding('utf-8')

Handler = index_handelr+comment_handler+blog_handelr+user_handler+checkcode_handelr
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
settings = {
    'cookie_secret' : 'x1OmUXcwRJOjmBAG3Hp44dg3CqsfKEI2orgzBFYu1Yo=',
    'template_path': os.path.join(parent_dir, 'view/templates'),
    'static_path': os.path.join(parent_dir, 'view/static'),
    'login_url': '/v01/login',
    'xsrf_cookies': True
}


def db_init():
    init_db()


def main():
    db_init()
    app = Application(Handler, **settings)

    args = sys.argv
    args.append("--log_file_prefix=./server.log")
    tornado.options.parse_command_line(args)

    gen_log.setLevel(logging.INFO)

    server = HTTPServer(app)
    server.listen(8080)
    IOLoop.instance().start()
if __name__ == '__main__':
    main()
