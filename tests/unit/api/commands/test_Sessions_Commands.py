from pbx_gs_python_utils.utils.Dev import Dev

from oss_bot.Deploy import Deploy
from oss_bot.api.commands.Sessions_Commands import Sessions_Commands
from oss_bot.helpers.Test_Helper import Test_Helper


class test_Sessions_Commands(Test_Helper):

    def setUp(self):
        super().setUp()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_list(self):
        self.result = Sessions_Commands.list('UAULZ1T98','DJ8UA0RFT')


    # deploy helpers

    def test_deploy_lambda__oss_bot(self):
        Deploy().setup().deploy_lambda__oss_bot()


    def test_deploy_lambda__git_lambda(self):
        Deploy().setup().deploy_lambda__git_lambda()
