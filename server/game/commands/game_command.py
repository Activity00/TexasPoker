# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/27 16:55
"""
from game.commands.base_command import BaseCommand
from utils.response import CommandResponseError


class LoginCommand(BaseCommand):
    def is_valid(self):
        return 'player_id' in self.data, ''

    def run(self):
        token = self.data.get('token')
        if not token:
            response = CommandResponseError('{}_result'.format(self.__class__.__name__[:-7]),
                                            None, 400, message='参数错误', errors='请先登录')
            self.socket.write(response)
            self.socket.close()
            return

        if not self.application.token_mgr.is_token_valid(token):
            response = CommandResponseError('{}_result'.format(self.__class__.__name__[:-7]),
                                            None, 5000, message='参数错误', errors='登录过期')
            self.socket.write(response)
            self.socket.close()

        player_id = token['player_id']
        self.application.player_mgr.login_player(player_id, self.socket)


class EnterSTDCommand(BaseCommand):

    def is_valid(self):
        return 'player_id' in self.data

    def run(self):
        player_id = self.data.pop('player_id')
        self.application.std_mgr.enter_std(player_id, self.data)


class SitDownCommand(BaseCommand):
    def run(self):
        player_id = self.data.pop('player_id')
        self.application.std_mgr.enter_std(player_id)
