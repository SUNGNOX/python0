# -*- coding: utf-8 -*-
import json

def application(environ, start_response):
    start_response('200 0k', [('Content-Type', 'text/html')])#第一个参数为HTTP响应码,不是固定值，第二个参数为HTTP Header
    # env = json.dumps(environ)
    bdy = '<h1>hello %s!!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    # body = (bdy+env)
    return [bdy.encode('utf-8')]
