#!/usr/bin/env python
# coding:utf-8
import sys
from tornado.web import RequestHandler

reload(sys)
sys.setdefaultencoding('utf-8')


class BaseHandler(RequestHandler):
    def initialize(self):
        super(BaseHandler, self).initialize()


