from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from oss_bot.Deploy import Deploy
from oss_bot.api.Git_Lambda import Git_Lambda
from oss_bot.lambdas.png_to_slack import load_dependency, upload_dependency


class test_Git_Lambda(TestCase):

    def setUp(self):
        self.git_lambda = Git_Lambda()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)


    def test_git_exec(self):
        #self.result = self.git_lambda.git_exec()()
        Deploy().setup()
        upload_dependency('lambda-git')

