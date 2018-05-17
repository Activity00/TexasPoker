# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/26 13:15
"""


class APIResponse(dict):
    def __init__(self, status, message, result, errors, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['status'] = status
        self['message'] = message
        if result:
            self['result'] = result
        if errors:
            self['errors'] = errors


class APIResponseSuccess(APIResponse):
    def __init__(self, result=None):
        super(APIResponseSuccess, self).__init__(0, 'OK', result, None)


class APIResponseError(APIResponse):
    def __init__(self, status, message, errors=None):
        super(APIResponseError, self).__init__(status, message, None, errors)


class CommandResponse(dict):
    def __init__(self, command, commander, seq, status, message, _type, result, errors, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['command'] = command
        self['commander'] = commander
        self['seq'] = seq
        self['status'] = status
        self['message'] = message
        self['type'] = _type
        if result:
            self['result'] = result
        if errors:
            self['errors'] = errors


class CommandResponseSuccess(CommandResponse):
    def __init__(self, command, commander, seq, result=None, *args, **kwargs):
        super().__init__(command, commander, seq, 0, 'OK', 'command_result', result, None, *args, **kwargs)


class CommandResponseError(CommandResponse):
    def __init__(self, command, commander, status, message, errors=None, *args, **kwargs):
        super().__init__(command, commander, status, message, 'command_result', None, errors, *args, **kwargs)


class CommandResponseNotice(CommandResponse):
    def __init__(self, command, commander, result, *args, **kwargs):
        super().__init__(command, commander, '', 0, 'OK', 'notice', result, None, *args, **kwargs)


class CommandResponseBroadcast(CommandResponse):
    def __init__(self, command, commander, result, *args, **kwargs):
        super().__init__(command, commander, '', 0, 'OK', 'broadcast', result, None, *args, **kwargs)
