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
