from pbx_gs_python_utils.utils.Dev import Dev

from oss_bot.api_in_lambda.Git_Lambda import Git_Lambda
from oss_bot.helpers.Test_Helper import Test_Helper


class test_Git_Lambda(Test_Helper):

    def setUp(self):
        super().setUp()
        self.git_lambda = Git_Lambda()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_repo_url(self):
        self.result = self.git_lambda.repo_url()



