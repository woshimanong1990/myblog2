#!/usr/bin/env python
# coding:utf-8
import sys
from tornado.web import authenticated
from BaseHandler import BaseHandler

from Model.comment_manager import CommentManager
from Model.blog_manager import BlogManager
from Model.user_db_op import get_user, get_user_and_roles
from Model.blog_db_op import get_blogs, get_blog
from Model.role_db_op import role_is_admin
reload(sys)
sys.setdefaultencoding('utf-8')


class BlogsHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        user_name = self.get_current_user()
        if user_name is not None:
            user = get_user(user_name)
            blogs = get_blogs(user)

        self.render('blog.html', blogs=blogs)

    @authenticated
    def post(self, *args, **kwargs):
        user_name = self.get_current_user()
        if self.json_args:
            blog_title = self.json_args.get('title', None)
            blog_tag_class = self.json_args.get('tag_class', None)
            blog_content = self.json_args.get('content', None)
        else:
            blog_title = self.get_argument('title', default=None)
            blog_tag_class = self.get_argument('tag_class', default=None)
            blog_content = self.get_argument('content', default=None)
        user = get_user(user_name=user_name)
        blog_id = None
        try:
            blog_id = BlogManager.create_blog(user=user, title=blog_title, tag_class=blog_tag_class, conten=blog_content)
        except Exception as e:
            print e
        if blog_id is not None:
            self.redirect('/v01/blog/'+str(blog_id))
        else:
            self.redirect('/v01/blogs')



class BlogHandler(BaseHandler):

    def get(self, blog_id):
            blog = get_blog(blog_id=blog_id)

            comments = CommentManager.get_comments(blog_id=blog_id)
            print blog

            self.render('blog_content.html', blog=blog, comments=comments)


    @authenticated
    def put(self, blog_id):
        user_name = self.get_current_user()
        if self.json_args:

            blog_title = self.json_args.get('title', None)
            blog_tag_class = self.json_args.get('tag_class', None)
            blog_content = self.json_args.get('content', None)
        else:

            blog_title = self.get_argument('title', default=None)
            blog_tag_class = self.get_argument('tag_class', default=None)
            blog_content = self.get_argument('content', default=None)
        user = get_user_and_roles(user_name=user_name)
        blog = get_blog(blog_id=blog_id)
        blog_id = None
        if user.id == blog.author_id or role_is_admin(user):
            try:
                blog_id = BlogManager.update_blog(blog=blog, title=blog_title, tag_class=blog_tag_class,
                                                  conten=blog_content)
            except Exception as e:
                print e
                raise e
        else:
            raise Exception('Forbidden')





    @authenticated
    def delete(self, blog_id):
        user_name = self.get_current_user()
        user = get_user_and_roles(user_name=user_name)
        blog = get_blog(blog_id)
        if role_is_admin(user) or user.id == blog.user_id:
            try:
                BlogManager.delete(blog)
            except Exception as e:
                raise e
        else:
            raise Exception('Forbidden')




class CreateBlogHandler(BaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        self.render('create_blog.html')
class EditBlogHandler(BaseHandler):
    @authenticated
    def get(self, blog_id):
        blog = get_blog(blog_id)
        self.render('edit_blog.html', blog=blog)
blog_handelr=[
    (r'/v01/blogs', BlogsHandler),
    (r'/v01/blog/([0-9]+)', BlogHandler),
    (r'/v01/eidt_blog/([0-9]+)', EditBlogHandler),
    (r'/v01/create_blog', CreateBlogHandler),
]
