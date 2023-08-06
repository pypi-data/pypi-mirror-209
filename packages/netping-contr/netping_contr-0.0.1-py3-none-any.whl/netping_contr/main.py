import requests
from requests.auth import HTTPBasicAuth
from netping_contr import mixins


class NetPingDevice(mixins.NetPingResponseParser):
    ip = None
    port = None
    username = None
    password = None
    index = None
    schema = "http://"
    status_on = 1
    status_off = 0

    def __init__(self, ip, port=80, index=None, username="visor",
                 password="ping", schema="http://", status_on=1, status_off=0):
        self.ip = ip
        self.port = port
        self.index = index
        self.username = username
        self.password = password
        self.schema = schema
        self.status_on = status_on
        self.status_off = status_off

    def get_full_url(self):
        return f"{self.schema}{self.ip}:{self.port}"

    def get_relay_info(self, relay_num=None):
        """
        Запрос состояния реле

        :param relay_num: номер реле
        :return:relay_result('ok')
                relay_result('error')
        """
        if not relay_num:
            relay_num = self.index
        return requests.get(
            url=f"{self.get_full_url()}/relay.cgi?r{relay_num}",
            auth=HTTPBasicAuth(self.username, self.password)
        )

    def change_relay_status(self, relay_num, status):
        """
        Управление реле

        :param relay_num: Номер реле
        :param status: Новое состояние реле (1 - включено, 0 - выключено)
        :return:relay_result('ok')
                relay_result('error')
        """
        return requests.get(
            url=f"{self.get_full_url()}/relay.cgi?r{relay_num}={status}",
            auth=HTTPBasicAuth(self.username, self.password)
        )

    def get_di_status(self, line_num=None):
        """
        Запрос состояния линии

        :param line_num: номер линии
        :return:io_result('error')
                io_result('ok', -1, 1, 339)

            Первый аргумент: всегда 'ok' (при ошибке запроса — 'error').
            Второй аргумент: всегда «-1», для расширения API в будущем.
            Третий аргумент: текущее моментальное состояние IO-линии,
            включая состояние сброса.
            Четвертый аргумент: счетчик импульсов на данной IO-линии,
            считается по фронту.
        """
        if not line_num:
            line_num = self.index
        return requests.get(
            url=f"{self.get_full_url()}/io.cgi?io{line_num}",
            auth=HTTPBasicAuth(self.username, self.password)
        )
