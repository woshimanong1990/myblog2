#!/usr/bin/env python
# coding:utf-8
import sys
import logging
from BaseHandler import BaseHandler
import tornado
reload(sys)
sys.setdefaultencoding('utf-8')


class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        logging.info("请求主页")
        self.render('index.html')
class PersonHomeHandler(BaseHandler):

    def get(self, *args, **kwargs):
        logging.info("访问个人主页")

        self.render('home.html')
index_handelr = [
    (r'/', IndexHandler),
    (r'/v01/home', PersonHomeHandler)
]
