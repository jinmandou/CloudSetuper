#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basehandlers import BaseHandler

class RegisterHandler(BaseHandler):

    def get(self):
        self.render("register.html", title="Join Cloud Setuper")

    def post(self):
        username = self.get_argument("username", "")
        email = self.get_argument("email", "")
        password = self.get_argument("password", "")

        user = {
                'username': username,
                'email': email,
                'password': password
            }
        flag = self.checkUser(user)
        if flag:
            self.saveUser2DB(user)
            self.set_secure_cookie("user", username)
            print user
            response = {
                'status': "success"
            }
            self.write(response)
        else:
            pass

    def checkUser(self, user):
        return True

    def saveUser2DB(self, user):
        # print user
        return True
