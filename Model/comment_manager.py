#!/usr/bin/env python
# coding:utf-8
import sys

from Model.comment_db_op import create_comment, get_comments, delete_comment, get_comment
from utils.tools import escape_replace_str

reload(sys)
sys.setdefaultencoding('utf-8')

class CommentManager(object):
    @staticmethod
    def create_comment(user=None, blog_id=None, commnet_content=None, commnet_id=None):
        commnet_content = escape_replace_str(commnet_content)
        try:
            create_comment(user=user, blog_id=blog_id, commnet_content=commnet_content, commnet_id=None)
        except Exception as e:
            raise e

    @staticmethod
    def get_comments(blog_id=None):
        comments = None
        try:
            comments = get_comments(blog_id=blog_id)
        except Exception as e:
            raise e
        return comments


    @staticmethod
    def get_replays(comment_id=None):
        pass
    @staticmethod
    def delete_comment(comment=None):
        try:
            delete_comment(comment=comment)
        except Exception as e:
            raise e
    @staticmethod
    def get_comment(comment_id=None):
        comment = None
        try:
            comment = get_comment(comment_id=comment_id)
        except Exception as e:
            raise e
        return comment


