from pbx_gs_python_utils.utils.Dev import Dev

from oss_bot.Deploy import Deploy
from oss_bot.api.commands.Participant_Commands import Participant_Commands
from oss_bot.helpers.Test_Helper import Test_Helper


class test_Participant_Commands(Test_Helper):

    def setUp(self):
        super().setUp()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_info(self):
        self.result = Participant_Commands.info()

    # deploy helpers

    def test_deploy_lambda__oss_bot(self):
        Deploy().setup().deploy_lambda__oss_bot()