# -*- coding:utf-8 -*-
#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
#什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
import hashlib
MD5 = hashlib.md5()
MD5.update('python hashlib?'.encode('utf-8'))
MD5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(MD5.hexdigest())
#217d5bb7a80fa0c7563d472b666154a8
#96d6435af29080206748361f033e118d

#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
#比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
