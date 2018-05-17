# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/27 14:00
"""
from game.commands.command_parser import CommandParser
from game.commands.game_command import LoginCommand
from scat.service import ws_service
from utils.response import CommandResponseError

URL_MAPPINGS = {
    'Game': r'/game/'
}


@ws_service
class Game:
    player_room_mapping = {}  # { 用户id: 房间id }

    def prepare(self):
        pass
        # if self.request.headers['Content-Type'].startswith('applications/json'):
        #     self.json_args = json.loads(self.request.body)
        # else:
        #     self.json_args = None

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        pass

    def on_close(self):
        # self.application.player_mgr.exit_player(self)
        pass

    def on_message(self, message):
        command, status, data = CommandParser.parse(self, message)
        if status != 200:
            self.write_message(data)
            self.close()
            return

        if not isinstance(command, LoginCommand) and not self.player_id:
            response = CommandResponseError('{}_result'.format(command.__class__.__name__[:-7]),
                                            None, 400, message='参数错误', errors='请先登录')
            self.write(response)
            self.close()
            return

        command.run()
