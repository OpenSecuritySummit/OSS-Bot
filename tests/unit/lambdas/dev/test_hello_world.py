from unittest import TestCase

from osbot_aws.apis.Lambda import Lambda
from osbot_aws.apis.Lambdas import Lambdas
from osbot_aws.helpers.Lambda_Package import Lambda_Package

from oss_bot.helpers.Test_Helper import Test_Helper


class test_run_command(Test_Helper):
    def setUp(self):
        self.oss_setup = super().setUp()
        self.aws_lambda = Lambda_Package('oss_bot.lambdas.dev.hello_world')
        self.aws_lambda._lambda.set_s3_bucket(self.oss_setup.s3_bucket_lambdas)         \
                               .set_role     (self.oss_setup.role_lambdas)
        self.aws_lambda.create()  # use when wanting to update lambda function

    def tearDown(self):
        super().tearDown()
        self.aws_lambda.delete()

    def test_invoke(self):
        assert self.aws_lambda.invoke({'name':'abc'}) == 'Hello abc (from lambda)'

    #workflow tests
    def test____check_current_lambdas(self):
        list = Lambdas().list()
        self.result = len(set(list))
