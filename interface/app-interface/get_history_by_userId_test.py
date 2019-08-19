import unittest
import requests
from Global_base import global_base
from Global_base import login
from parameterized import parameterized


class HistoryByUserId(unittest.TestCase):
    def setUp(self):
        self.url = global_base.DefTool.url(self, '/app/productRecord/getHistoryByUserId.do')

    @parameterized.expand([
        ('查询历史纪录成功', "867910035562539", "1003", "1", "1", "1", "50"),
    ])
    def test_get_history_by_userId(self, caase, deviceId, productId, deviceType, actType, pageIndex, pageSize):
        value = login.LoginByPassWord().login_by_password(18127813601)
        token = value[1]
        accountId = value[0]
        params = {"deviceId": deviceId, "accountId": accountId, "productId": productId, "deviceType": deviceType,
                  "actType": actType, "token": token, "pageIndex": pageIndex, "pageSize": pageSize}
        try:
            self.result = requests.post(url=self.url, data=params).json()
            self.assertEqual(self.result["msg"], "ok")
            self.assertEqual(self.result["code"], '200')
        except Exception as e:
            print(e)

    def tearDown(self):
        print(self.result)


if __name__ == '__main__':
    unittest.main()
