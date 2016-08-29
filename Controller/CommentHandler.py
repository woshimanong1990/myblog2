#!/usr/bin/env python
# coding:utf-8
import sys
from utils.tools import check_permission
from BaseHandler import BaseHandler
from tornado.web import authenticated

reload(sys)
sys.setdefaultencoding('utf-8')


class CommentHandler(BaseHandler):
    @check_permission
    @authenticated
    def get(self, comment_id):
        pass

    @check_permission
    @authenticated
    def put(self, comment_id):
        pass

    @check_permission
    @authenticated
    def delete(self, comment_id):
        pass


class CommentsHandler(BaseHandler):
    @check_permission
    @authenticated
    def get(self):
        pass

    @check_permission
    @authenticated
    def post(self):
        pass

comment_handler = [
    (r'/v01/comments', CommentsHandler),
    (r'/v01/comment/([0-9]+)', CommentsHandler),
]
