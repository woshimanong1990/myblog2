#!/usr/bin/env python
# coding:utf-8
import sys
from sqlalchemy.orm import sessionmaker


from operation_db import ENGINE
from Model.create_db import Comment
Session = sessionmaker(bind=ENGINE)
reload(sys)
sys.setdefaultencoding('utf-8')


def create_comment(user=None, blog_id=None, commnet_content=None, commnet_id=None):
    session = Session()
    kwargs = dict()

    if user is None:
        raise Exception('用户不能为空')
    if is_commentted_for_blog(user_id=user.id, blog_id=blog_id):
        raise Exception('你已经评论过了，请不要再次评论')
    kwargs['user_id'] = user.id
    kwargs['blog_id'] = blog_id
    kwargs['content'] = commnet_content
    if commnet_id is not None:
        # 创建回复
        comment = Comment(**kwargs)
        comment.commnet_id = commnet_id
        comment_reply = get_comment(commnet_id=commnet_id)
        comment_reply.reply_status = True
        session.merge(comment_reply)
    else:
        # 创建评论
        comment = Comment(**kwargs)
    session.add(comment)
    session.commit()


def get_comments(blog_id=None):
    session = Session()
    comments = None
    if blog_id is not None:
        try:
            comments = session.query(Comment).filter(Comment.blog_id == blog_id).all()
        except:
            raise Exception('获取评论失败')
    else:
        raise ValueError('获取评论的参数有误')
    return comments






def get_replys(comment_id=None):
    # 获取某个评论的回复
    session = Session()
    comments = None

    try:
        comments = session.query(Comment).filter(Comment.comment_id == comment_id).all()
    except:
        raise Exception('获取评论的回复失败')
    return comments


def get_comment(comment_id=None):
    # 获取具体某个评论
    session = Session()
    comment = None

    try:
        comment = session.query(Comment).filter(Comment.id == comment_id).first()
    except:
        raise Exception('获取评论的回复失败')
    return comment


def get_comment_by_user_blog(user_id=None, blog_id=None):
    session = Session()
    comment = None
    if user_id is not None and blog_id is not None:
        comment = session.query(Comment).filter(Comment.user_id == user_id). \
            filter(Comment.blog_id == blog_id).all()
    else:
        raise ValueError('获取评论的参数错误')
    return comment

def is_commentted_for_blog(user_id=None,blog_id=None):
    comment = None
    try:
        comment = get_comment_by_user_blog(user_id=user_id, blog_id=blog_id)
    except Exception as e:
        raise e
    else:
        if comment is not None and comment:
            return True
        else:
            return False


def delete_comment(comment=None):
    if comment is None:
        raise Exception('评论删除失败')
    session = sessionmaker.object_session(comment)
    if session is None:
        session = Session()
    try:
        session.delete(comment)
    except:
        raise Exception('评论删除失败')


