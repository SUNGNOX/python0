# -*- coding:utf-8 -*-
#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
import base64

b64_en = base64.b64encode(b"abcd")
b64_de = base64.b64decode(b64_en)

print(b64_en, '=>', b64_de)