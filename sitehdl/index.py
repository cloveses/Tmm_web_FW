# -*- coding: utf-8 -*-

from mylib.web import BaseHandler, route

@route('/')
class IndexHdl(BaseHandler):
    def get(self):
        self.render('index.html',{"hint_info":self.hint_info})