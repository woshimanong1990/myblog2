#!/usr/bin/env python
# coding:utf-8
import json
import sys
from tornado.web import RequestHandler

reload(sys)
sys.setdefaultencoding('utf-8')


class BaseHandler(RequestHandler):
    def initialize(self):
        super(BaseHandler, self).initialize()

    def prepare(self):
        content_type = self.request.headers.get("Content-Type",None)

        if content_type and content_type.startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args=None


