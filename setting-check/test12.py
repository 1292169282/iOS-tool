#coding=utf-8
import json
import types
import os
import sys
#from sys import argv
#address = argv
#arg0 = sys.argv[1]
#os.system('./test1.sh' + arg0 + '')
with open("converted.json", 'r') as f:
  temp = json.loads(f.read())
  #if(strstr($key,'urls')){
 #$value=urlencode($value);
 #}

  #t = temp['rootObject']
  #t1= temp['rootObject']
  
  #t2 = temp['objects'][t]['attributes']['TargetAttributes']['689C13771DC34C26001D8E6C']['SystemCapabilities']
  #t2 = json.dumps(t2)
with open("project.pbxproj", 'r') as f:
    strr = f.read()
str1 = "libXG-SDK.a";
ret3 = strr.find(str1);
  
    
  #获取字典中的objkey对应的值，适用于字典嵌套
#dict:字典
#objkey:目标key
#default:找不到时返回的默认值
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


def dict_find(dict, obj1, obj2,default):
    tmp1 = dict
    for k,v in tmp1.items():
      if k == obj1:
        if type(v) is types.DictType:
          ret1 = dict_get(v, obj2, default)
          if ret1 is not default:
                    return ret1
      
    return default

def result(ret1,ret2,ret3):
    if ret1 == '0':  
      if ret2 == '0':
          if ret3 == -1:
            print "配置错误：未开启BackgroundModes、apple Push，未添加libXG-SDK.a"
          else:
            print "配置错误：未开启BackgroundModes、apple Push，已添加libXG-SDK.a"
      else: 
        if ret3 == -1:
            print "配置错误：未开启BackgroundModes,已开启apple Push,未添加libXG-SDK.a"
        else:
            print "配置错误：未开启BackgroundModes,已开启apple Push,已添加libXG-SDK.a"
    else:
      if ret2 == '0':
          if ret3 == -1:
            print "配置错误：已开启BackgroundModes,未开启apple Push,未添加libXG-SDK.a"
          else:
            print "配置错误：已开启BackgroundModes,未开启apple Push,已添加libXG-SDK.a"
      else: 
        if ret3 == -1:
            print "配置错误：已开启BackgroundModes,已开启apple Push,未添加libXG-SDK.a"
        else:
            print "配置正确：已开启BackgroundModes,已开启apple Push,已添加libXG-SDK.a"

    

#如
#dicttest={"result":{"code":"110002","msg":"设备设备序列号或验证码错误"}}

ret=dict_get(temp, 'SystemCapabilities', None)

if ret != None:

  ret1=dict_find(ret, 'com.apple.BackgroundModes', 'enabled','未找到BackgroundModes')
  ret2=dict_find(ret, 'com.apple.Push', 'enabled','未找到apple Push')
  result=result(ret1,ret2,ret3)
else:
  print(ret)
# print(ret1)
# print(ret2)




      
