#!/usr/bin/env python
# coding:utf-8

from io import BytesIO
import traceback

from Controller.BaseHandler import BaseHandler

from utils.check_code import ImageChar
from utils.tools import catch_exce

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

    @catch_exce
    def post(self):
        code = self.get_secure_cookie('check_code')
        if self.json_args:
            check_code = self.json_args.get('check_code', None)
        if check_code:
            check_code = check_code.replace(' ', '', 1).encode('utf-8')
        if code and check_code and code == check_code:
            self.write({'message': 'right'})
        else:
            raise Exception("验证码不正确")


checkcode_handelr = [
    (r'/v01/check_code', CheckcodeHandler)
]