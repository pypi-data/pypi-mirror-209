"""
@Author: kang.yang
@Date: 2023/5/16 14:37
"""
import kuto
from kuto import WebElem, config


class IndexPage(kuto.Page):
    login = WebElem(text='登录/注册')
    enterprise = WebElem(text='查专利')


class LoginPage(kuto.Page):
    pwdLogin = WebElem(text='帐号密码登录')
    userInput = WebElem(placeholder='请输入手机号码')
    pwdInput = WebElem(placeholder='请输入密码')
    licenseBtn = WebElem(css="span.el-checkbox__inner", index=1)
    loginBtn = WebElem(text='立即登录')


class LoginFunc:

    def __init__(self, driver):
        self.driver = driver
        self.page1 = IndexPage(driver)
        self.page2 = LoginPage(driver)

    def login_with_pwd(self, phone, password):
        base_url = config.get_web("base_url")
        self.driver.visit(base_url)
        self.page1.login.click()
        self.page2.pwdLogin.click()
        self.page2.userInput.input(phone)
        self.page2.pwdInput.input(password)
        self.page2.licenseBtn.click()
        self.page2.loginBtn.click()
        self.page1.enterprise.assert_visible()


class TestLogin(kuto.TestCase):

    def start(self):
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_1(self):
        self.open()
        self.index_page.login.click()
        self.login_page.pwdLogin.click()
        self.login_page.userInput.input('13652435335')
        self.login_page.pwdInput.input('wz123456@QZD')
        self.login_page.licenseBtn.click()
        self.login_page.loginBtn.click()
        self.driver.screenshot("登录成功")


if __name__ == '__main__':
    # with open("state.json", "r") as f:
    #     state = json.loads(f.read())

    kuto.main(
        platform="web",
        host="https://www.qizhidao.com"
    )
