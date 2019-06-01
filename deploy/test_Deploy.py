
from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from oss_bot.Deploy import Deploy


class test_Deploy(TestCase):

    def setUp(self):
        self.deploy = Deploy()
        self.deploy.oss_setup.setup_test_environment()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_deploy_lambda__oss_bot(self):
        self.deploy.deploy_lambda__oss_bot()

    def test_deploy_lambda__browser(self):
        self.deploy.deploy_lambda__browser()

    def test_deploy_lambda__slack_message(self):
        result = self.deploy.deploy_lambda__slack_message()
        Dev.pprint(result)

    def test_deploy_lambda_log_to_elk(self):
        lambda_package = self.deploy.deploy_lambda_log_to_elk()
        self.result  = lambda_package._lambda.invoke()


