from unittest import TestCase

from osbot_aws.apis.Lambda import Lambda
from osbot_aws.apis.Lambdas import Lambdas
from osbot_aws.helpers.Lambda_Package import Lambda_Package
from pbx_gs_python_utils.utils.Dev import Dev

from oss_bot.helpers.Test_Helper import Test_Helper


class test_git_lambda(Test_Helper):
    def setUp(self):
        self.oss_setup = super().setUp()
        self.aws_lambda = Lambda_Package('oss_bot.lambdas.git_lambda')
        self.aws_lambda._lambda.set_s3_bucket(self.oss_setup.s3_bucket_lambdas)         \
                               .set_role     (self.oss_setup.role_lambdas)
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_update_lambda(self):
        return self.aws_lambda.update_code()

    def test_invoke_version(self):
        self.test_update_lambda()
        payload = {'command': 'version' }
        self.result = self.aws_lambda.invoke(payload)

    def test_invoke_clone(self):
        #self.test_update_lambda()
        payload = {'command': 'clone' } #,'https://github.com/OpenSecuritySummit/oss2019.git' }
        self.result = self.aws_lambda.invoke(payload)

    def test_invoke_pull(self):
        #self.test_update_lambda()
        payload = {'command': 'pull'}  # ,'https://github.com/OpenSecuritySummit/oss2019.git' }
        self.result = self.aws_lambda.invoke(payload)

    def test_invoke_files(self):
        payload = {'command': ''}  # ,'https://github.com/OpenSecuritySummit/oss2019.git' }
        self.result = self.aws_lambda.invoke(payload)