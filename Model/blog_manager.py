#!/usr/bin/env python
# coding:utf-8
import sys

import blog_db_op
from utils.tools import escape_replace_str
reload(sys)
sys.setdefaultencoding('utf-8')


class BlogManager(object):
    @staticmethod
    def create_blog(user=None, title=None, tag_class=None, conten=None):
        escape_replace_str(conten)
        if title is None:
            raise Exception('标题不能为空！')
        kwargs = dict()
        kwargs['title'] = title
        kwargs['tag_class'] = tag_class
        kwargs['content'] = conten
        blog_id = None
        try:
            blog_id = blog_db_op.create_blog(user=user, **kwargs)
        except Exception as e:
            raise e
        return blog_id

    @staticmethod
    def update_blog(blog=None, title=None, tag_class=None, conten=None):
        escape_replace_str(conten)
        if title is None:
            raise Exception('标题不能为空！')
        kwargs = dict()
        kwargs['title'] = title
        kwargs['tag_class'] = tag_class
        kwargs['content'] = conten
        blog_id = None
        try:
            blog_id = blog_db_op.update_blog(blog=blog, **kwargs)
        except Exception as e:
            print e,'ma'
            raise e
        return blog_id

    @staticmethod
    def delete(blog):
        try:
            blog_db_op.delete_blog(blog)
        except Exception as e:
            raise e
