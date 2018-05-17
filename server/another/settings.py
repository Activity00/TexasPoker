
DEBUG = True
HALL_IP = '127.0.0.1'
HALL_CLIENT_PORT = 9001
ACCOUNT_PRI_KEY = "^&*#$%()@"
ROOM_PRI_KEY = "~!@#$(*&^%$&"
COOKIE_SECRET = "~!@#$(*&^%$&xxoo&"


# 账号服务器
ACCOUNT_SERVER = {
    'CLIENT_PORT': 9000,
    'HALL_IP': HALL_IP,
    'HALL_CLIENT_PORT': HALL_CLIENT_PORT,
    'ACCOUNT_PRI_KEY': ACCOUNT_PRI_KEY,
    'APP_WEB': 'http://localhost/web/TexasPokser.apk',
    'VERSION': 20171223
}


GAME_SERVER = {
    'HTTP_PORT': 9004,
    'HTTP_TICK_TIME': 5000,  # 定期心跳
    'HALL_IP': HALL_IP,
    'HALL_PORT': HALL_CLIENT_PORT,
    'SOCKET_PORT': 10001,
}