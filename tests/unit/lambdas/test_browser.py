from unittest import TestCase

from osbot_aws.apis.Lambda import Lambda
from osbot_aws.apis.Lambdas import Lambdas
from osbot_aws.helpers.Lambda_Package import Lambda_Package
from pbx_gs_python_utils.utils.Dev import Dev

from oss_bot.helpers.Test_Helper import Test_Helper


class test_run_command(Test_Helper):
    def setUp(self):
        self.oss_setup = super().setUp()
        self.aws_lambda = Lambda('osbot_browser.lambdas.lambda_browser')

    def test__invoke__directly(self):
        # import pbx_gs_python_utils.utils.Lambdas_Helpers
        #
        # def my_slack_message(text, attachments =[], channel = 'GDL2EC3EE', team_id='T7F3AUXGV'):
        #     print('\n\nin my_slack_message')
        #     print(text)
        #
        # pbx_gs_python_utils.utils.Lambdas_Helpers.slack_message = my_slack_message
        #
        # Dev.pprint(pbx_gs_python_utils.utils.Lambdas_Helpers.slack_message('abc'))
        from osbot_browser.lambdas.lambda_browser import run
        self.result = run({},{})

    def test__invoke__no_params(self):
        assert self.aws_lambda.invoke() == '*Here are the `Browser_Commands` commands available:*'
