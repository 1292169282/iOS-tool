#!/usr/bin/python
#coding=utf-8
import sys, re
import json
import types
import os
import plistlib;
import binascii
import datetime
from cStringIO import StringIO
import re
import warnings

# def pythonPlistToDict():
    
#     # with  open('/Users/admin/Documents/脚本资料/测试t3/20190725/2.plist', 'r') as f:
#     # # with  open(sys.argv[1], 'r') as f:
#     #     plistStr = f.read()
#     # convertedDict = plistlib.readPlistFromString(plistStr);# 返回一个OrderedDict类型的对象
#     # # jsonStr = json.dumps(convertedDict, indent=2);# 使用内置的json模块转换成json,带缩进
#     # # file = open('/Users/admin/Documents/脚本资料/测试t3/1.json','w')
#     # # file.write(jsonStr)
#     # tempstr = json.dumps(temp.decode('utf8'), indent=2);
#     # file = open('/Users/admin/Documents/脚本资料/测试t3/20190725/2.json','w')
#     # file.write(temp)
#     print(temp)


# with open("2.txt", 'r') as f:
#   t = f.read()
#   temp=eval(t)
def dict_get(dict, objkey, default):
    tmp = dict
    for k,v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v) is types.DictType:
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
    return default


    
temp = plistlib.readPlist('2.plist')
ret=dict_get(temp, 'Entitlements', None)
if ret != None:
    ret1=dict_get(ret, 'aps-environment', None)
    if ret1 != None:
        if ret1 == 'development':
            print "aps-environment为development"
        else:
            print "aps-environment为production"
    else:
        print "没有找到aps-environment" 
else:
  print "没有找到Entitlements"
