from oss_bot.api.OSS_Bot_Commands import OSS_Bot_Commands
from oss_bot.helpers.Test_Helper import Test_Helper


class test_OSS_Bot_Commands(Test_Helper):

    def setUp(self):
        super().setUp()

    def test_browser(self):
        self.result = OSS_Bot_Commands.browser()

    def test_hello(self):
        assert OSS_Bot_Commands.hello() == ('Hello <@None>, how can I help you?', [])

    def test_help(self):
        assert OSS_Bot_Commands.help()[0] ==  '*Here are the commands available*'

    def test_version(self):
        assert OSS_Bot_Commands.version()[0] == OSS_Bot_Commands.gsbot_version