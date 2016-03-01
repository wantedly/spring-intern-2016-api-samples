#!/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import json
import requests

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        _user_id = self.get_argument('user_id', 0)
        if _user_id == 0:
            return
        url = 'http://spring:intern_2016@www.wantedlyapp.com/api/intern/portal/show_supplement?user_id='+str(_user_id)
        username = "spring"
        password = "intern_2016"
        print url
        response = requests.get(url,
                        auth=requests.auth.HTTPBasicAuth(
                          username,
                          password
            ),
            verify=False
        )
        response = json.loads(response.text)
        print
        return_json= json.dumps(response["data"]["sections"][1]["keywords"], ensure_ascii=False)
        self.write(return_json)

application = tornado.web.Application([
    (r"/api/keywords", MainHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
