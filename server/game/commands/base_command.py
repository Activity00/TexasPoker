# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/27 16:45
"""


class BaseCommand:
    def __init__(self, socket, data):
        self.socket = socket
        self.data = data
        self.application = socket.application

    def is_valid(self):
        return True

    def run(self):
        raise NotImplementedError
