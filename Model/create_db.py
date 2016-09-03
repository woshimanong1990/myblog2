#!/usr/bin/env python
# coding:utf-8
import sys

from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, BigInteger, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from utils.tools import get_uuid, get_time
import random
import hashlib


reload(sys)
sys.setdefaultencoding('utf-8')


Base = declarative_base()
role_user = Table('role_user', Base.metadata,
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('role_id', Integer, ForeignKey('role.id'))
                  )

class UserLogin(Base):
    __tablename__ = 'users_login'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(30))
    password = Column(String(70))
    login_ip = Column(String(12))
    login_time = Column(BigInteger)
    email = Column(String(20))
    phone = Column(BigInteger)
    activate_status = Column(Boolean)
    activate_code = Column(String(50))
    bad_login_ip = Column(String(12))
    bad_login_time = Column(BigInteger)
    bad_login_count = Column(Integer)
    modify_time = Column(BigInteger)
    # 1 启用，0，禁用
    status = Column(Integer, default=1)
    user_info = relationship('User', uselist=False, back_populates='user_login')

    def __init__(self, **kwargs):
        self.login_time = self.modify_time = get_time()
        self.activate_code = get_uuid()
        passwd = kwargs.pop('password', None)
        self.password = self.create_passwd(passwd)
        for k, v in kwargs.items():
            setattr(self, k, v)
        super(UserLogin, self).__init__()

    @staticmethod
    def create_passwd(passwd):
        if passwd is None:
            raise Exception('密码为空')
        return hashlib.sha256(passwd+"good,good,stdy").hexdigest()

    def check_passwd(self,passwd):
        ss_userpwd = hashlib.sha256(passwd+"good,good,stdy").hexdigest()
        return ss_userpwd == self.password


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    points = Column(BigInteger)
    favorite = Column(String(100))
    birthday = Column(Date)
    hometown = Column(String(30))
    gender = Column(String(2))

    user_id = Column(Integer, ForeignKey('users_login.id', ondelete='CASCADE', onupdate='CASCADE'))

    user_login = relationship('UserLogin', back_populates='user_info')
    blog = relationship('Blog', back_populates='author')
    role = relationship('Role', secondary=role_user)

    def __init__(self, **kwargs):

        for k, v in kwargs.items():
            setattr(self, k, v)
        super(User, self).__init__()


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(Text)
    create_time = Column(BigInteger)
    modify_time = Column(BigInteger)
    reading_count = Column(Integer)
    tag_class = Column(String(20))

    author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))

    author = relationship('User', back_populates='blog')
    comments = relationship('Comment', back_populates='blog')

    def __init__(self, **kwargs):
        self.create_time = self.modify_time = get_time()

        for k, v in kwargs.items():
            setattr(self, k, v)
        super(Blog, self).__init__()


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    create_time = Column(BigInteger)
    modify_time = Column(BigInteger)
    reply_status = Column(Boolean, default=False)
    content = Column(Text)

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))
    comment_id = Column(Integer, ForeignKey('comment.id', ondelete='CASCADE', onupdate='CASCADE'))
    blog_id = Column(Integer, ForeignKey('blog.id', ondelete='CASCADE', onupdate='CASCADE'))

    blog = relationship('Blog', back_populates='comments')
    user = relationship('User')
    reply = relationship('Comment')

    def __init__(self, **kwargs):
        self.create_time = self.modify_time = get_time()

        for k, v in kwargs.items():
            setattr(self, k, v)
        super(Comment, self).__init__()


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    # 1 admin, 2 common user,3
    rolename = Column(String(10), default=2)


    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        super(Role, self).__init__()

    @property
    def is_admin(self):
        return str(self.rolename) == '1'




if __name__ == '__main__':
    print get_uuid()



