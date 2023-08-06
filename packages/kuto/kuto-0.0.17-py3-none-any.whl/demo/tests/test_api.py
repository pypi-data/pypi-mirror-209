import kuto


class TestCaseClass(kuto.TestCase):

    def test_case1(self):
        payload = {"type": 2}
        headers = {"user-agent-web": "X/b67aaff2200d4fc2a2e5a079abe78cc6"}
        self.post('/qzd-bff-app/qzd/v1/home/getToolCardListForPc', json=payload, headers=headers)
        self.assertEq('code', 0)


if __name__ == '__main__':
    kuto.main(
        host='https://app.qizhidao.com',
        path='test_api.py::TestCaseClass::test_case1'
    )
