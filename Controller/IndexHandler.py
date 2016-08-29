#!/usr/bin/env python
# coding:utf-8
import sys
from BaseHandler import BaseHandler

reload(sys)
sys.setdefaultencoding('utf-8')


class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):

        self.render('index.html')
index_handelr = [
    (r'/', IndexHandler)
]
