#!/usr/bin/env python
# coding:utf-8

from io import BytesIO
import traceback

from Controller.BaseHandler import BaseHandler

from utils.check_code import ImageChar


class CheckcodeHandler(BaseHandler):
    def get(self, *args, **kwargs):

        image = ImageChar()
        code_img, capacha_code = image.randChinese()
        msstream = BytesIO()
        code_img.save(msstream,"jpeg")
        code_img.close()
        self.set_header('Content-Type', 'image/jpg')
        self.set_secure_cookie('check_code', capacha_code)
        self.write(msstream.getvalue())



checkcode_handelr = [
    (r'/v01/check_code', CheckcodeHandler)
]