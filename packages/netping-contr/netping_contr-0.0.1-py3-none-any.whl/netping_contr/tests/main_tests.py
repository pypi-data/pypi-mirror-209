import unittest
from netping_contr.main import NetPingDevice


class TestCase(unittest.TestCase):
    inst = NetPingDevice("192.168.60.103")

    def test_get_io_info(self):
        response = self.inst.get_di_status(1)
        response = self.inst.parse_line_request(response)
        print(response)
        return response

    def test_change_relay(self):
        res = self.inst.change_relay_status(1, 0)
        res = self.inst.parse_relay_change(res)
        print(res)

if __name__ == "__main__":
    unittest.main()
