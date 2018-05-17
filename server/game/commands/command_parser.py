import json

from game import commands


class CommandParser:
    @classmethod
    def parse(cls, socket, message):
        try:
            if isinstance(message, bytes):
                data = json.loads(str(message, encoding='utf8'))
            else:
                data = json.loads(message)
        except:
            message = 'json解析错误'
            return None, 400, message

        if 'command' not in data:
            message = '缺少command属性'
            return None, 400, message

        Command = getattr(commands, data['command'] + 'Command', None)
        if not Command:
            message = '对应command不存在: %s' % (data['command'] + 'Command')
            return None, 400, message
        
        command = Command(socket, data)
        is_valid, errors = command.is_valid()
        if not is_valid:
            return None, 400, errors
        
        return command, 200, None
