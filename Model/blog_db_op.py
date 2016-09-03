#!/usr/bin/env python
# coding:utf-8
import sys

from sqlalchemy.orm import sessionmaker
from operation_db import ENGINE

from create_db import Blog

Session = sessionmaker(bind=ENGINE)
reload(sys)
sys.setdefaultencoding('utf-8')


def create_blog(user=None, **kwargs):
    #  保证传入的参数是干净的，转义后的
    session = Session()
    blog = Blog(**kwargs)
    '''
    user.user_info.blog.append(blog)
    session.merge(user.user_info)  # 用add显示is already attached to session '1' (this is '2')，、
                                    # 可能用user_info时重新创建了一个session，并且关联了blog
    '''
    blog.author_id = user.user_info.id
    session.add(blog)
    session.commit()
    return blog.id




def get_blog(blog_id=None):
    session = Session()
    blog = None

    if blog_id is not None:
        blog = session.query(Blog).filter(Blog.id == blog_id).first()

    else:
        raise Exception("没有找到所需要的博客")
    return blog


def get_blogs(user=None):
    session = Session()
    if user is not None:
        blogs = user.user_info.blog
    else:
        raise Exception("没有找到所需要的博客")
    return blogs


def update_blog():
    pass



