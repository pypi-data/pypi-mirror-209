from requests.models import Response
import re


class NetPingResponseParser:
    """ Служит для парсинга ответов от Непинг. Переводит байты в JSON """

    def get_decoded_res(self, response: Response):
        return response.content.decode()

    def parse_line_request(self, response: Response):
        res_decoded = self.get_decoded_res(response)
        res_decoded = res_decoded.replace(';', '')
        res_tuple = tuple(eval(res_decoded.split('io_result')[1]))
        response = {"status": res_tuple[0],
                    "state": res_tuple[2],
                    "count": res_tuple[-1]}
        return response

    def parse_relay_change(self, response: Response):
        res_decoded = self.get_decoded_res(response)
        res_decoded = res_decoded.replace(';', '')
        res_tuple = res_decoded.split('relay_result')[1]
        response = re.search(r'\((.*?)\)', res_tuple).group(1).replace("'",'')
        response = {'status': response}
        return response
