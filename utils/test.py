# coding:utf-8
import hashlib


def create_passwd(passwd):
    if passwd is None:
        raise Exception('密码为空')
    return hashlib.sha256(passwd + "good,good,stdy").hexdigest()
print len(create_passwd('165464656@qq.com'))
