#!/usr/bin/env python
# coding:utf-8
import sys
import os

import logging.config


from tornado.web import Application
import tornado.httpserver


import tornado.options
from tornado.options import define, options

from IndexHandler import index_handelr
from BlogHandler import blog_handelr
from UserHandler import user_handler
from CommentHandler import comment_handler
from Model.operation_db import init_db
from CheckcodeHandler import checkcode_handelr


reload(sys)
sys.setdefaultencoding('utf-8')

define("port", default=8081, help="Run server on a specific port", type=int)


Handler = index_handelr+comment_handler+blog_handelr+user_handler+checkcode_handelr
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
settings = {
    'cookie_secret' : 'x1OmUXcwRJOjmBAG3Hp44dg3CqsfKEI2orgzBFYu1Yo=',
    'template_path': os.path.join(parent_dir, 'view/templates'),
    'static_path': os.path.join(parent_dir, 'view/static'),
    'login_url': '/v01/login',
    'xsrf_cookies': False
}


def db_init():
    init_db()


def main():
    db_init()
    app = Application(Handler, **settings)
    http_server = tornado.httpserver.HTTPServer(app)



    # This line should be after the parse_command_line()
    http_server.listen(8081)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    import traceback
    try:

        tornado.options.parse_command_line()
        SERVER_LOG = os.path.join(os.path.dirname(__file__), "server_log.conf")
        logging.config.fileConfig(SERVER_LOG)

        main()
    except:
        s = traceback.format_exc()
        print s

