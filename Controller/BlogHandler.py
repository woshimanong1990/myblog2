#!/usr/bin/env python
# coding:utf-8
import sys
from tornado.web import authenticated
from BaseHandler import BaseHandler
from utils.tools import check_permission
reload(sys)
sys.setdefaultencoding('utf-8')

class BlogsHandler(BaseHandler):
    @check_permission
    @authenticated
    def get(self, *args, **kwargs):
        pass

    @check_permission
    @authenticated
    def post(self, *args, **kwargs):
        pass


class BlogHandler(BaseHandler):
    @check_permission
    @authenticated
    def get(self,blog_id):
        pass

    @check_permission
    @authenticated
    def put(self):
        pass

    def delete(self, blog_id):
        pass

blog_handelr=[
    (r'/v01/blogs', BlogsHandler),
    (r'/v01/blog/([0-9]+)', BlogsHandler),
]
