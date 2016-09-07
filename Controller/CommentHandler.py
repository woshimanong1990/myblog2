#!/usr/bin/env python
# coding:utf-8
import sys

from BaseHandler import BaseHandler
from tornado.web import authenticated

from Model.role_db_op import role_is_admin
from Model.user_db_op import get_user, get_user_and_roles
from Model.comment_manager import CommentManager
from utils.tools import catch_exce

reload(sys)
sys.setdefaultencoding('utf-8')


class CommentHandler(BaseHandler):

    @authenticated
    def get(self, comment_id):
        pass




    @authenticated
    def delete(self, comment_id):
        user_name = self.get_current_user()
        user = get_user_and_roles(user_name=user_name)
        comment = CommentManager.get_comment(comment_id=comment_id)
        if role_is_admin(user) or user.id == comment.user_id:
            try:
                CommentManager.delete_comment(comment)
            except Exception as e:
                raise e
        else:
            raise Exception('Forbidden')



class CommentsHandler(BaseHandler):
    @catch_exce
    def get(self):
        blog_id = self.get_argument('blog_id', default=None)
        comments = []
        if blog_id is not None:
            try:
                comments = CommentManager.get_comments(blog_id)
            except Exception as e:
                raise e

        return comments

    @catch_exce
    @authenticated
    def post(self):
        user_name = self.get_current_user()
        if self.json_args:
            blog_id = self.json_args.get('blog_id', None)
            commnet_content = self.json_args.get('commnet_content', None)
            commnet_id = self.json_args.get('commnet_id', None)
        else:
            blog_id = self.get_argument('blog_id', default=None)
            commnet_content = self.get_argument('commnet_content', default=None)
            commnet_id = self.get_argument('commnet_id', default=None)
        if blog_id is None or commnet_content is None:
            raise ValueError('评论参数有误')
        user = get_user(user_name=user_name)
        try:
            CommentManager.create_comment(user=user, blog_id=blog_id, commnet_content=commnet_content, commnet_id=commnet_id)
        except Exception as e:
            raise e
        self.redirect('/v01/blog/'+blog_id)


comment_handler = [
    (r'/v01/comments', CommentsHandler),
    (r'/v01/comment/([0-9]+)', CommentsHandler),
]
