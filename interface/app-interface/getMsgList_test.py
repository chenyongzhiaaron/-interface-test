import requests
import unittest
from Global_base import global_base
from Global_base import login
from parameterized import parameterized


class GetMsgList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/usercenter/user/getMsgList.do')

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("消息", "requestData1565595880131", "867910035562539", "2.6.0", "15", "1003", "1","sinaif",
         "ef70fb3178dccde19df9295a68aca0a3", "qsj")
    ])
    def test_getMsgList(self, case, callbackName, deviceId, ver, verno, productId, deviceType, channelId, deviceToken,
                             mjbname):
        pa = {"callbackName": callbackName, "type": type, "verno": verno, "deviceId": deviceId, "ver": ver,
              "deviceType": deviceType,
              "productId": productId, "channelId": channelId, "deviceToken": deviceToken, "mjbname": mjbname}
        sign = global_base.DefTool.sign(self, **pa)
        params = dict(pa, **sign)
        values = login.LoginByPassWord().login_by_password(18127813601)
        token = values[1]
        header = {"token":token}
        self.result = requests.post(url=self.url, headers=header, data=params).json()
        try:
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result['code'], 200)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
