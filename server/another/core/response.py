# coding: utf-8

"""
@author: 武明辉 
@time: 2017/12/23 15:21
"""


class Response(dict):
    def __init__(self, status, message, result, errors):
        if not result:
            if errors:
                self.data = {
                    'status': status,
                    'message': message,
                    'errors': errors
                }
            else:
                self.data = {
                    'status': status,
                    'message': message,
                }
        else:
            self.data = {
                'status': status,
                'message': message,
                'result': result,
            }
        super(Response, self).__init__(self.data)


class ResponseSuccess(Response):
    def __init__(self, result=None):
        super(ResponseSuccess, self).__init__(0, 'OK', result, errors=None)


class ResponseError(Response):
    def __init__(self, status, message, result=None, errors=None):
        super(ResponseError, self).__init__(status, message, result, errors)
