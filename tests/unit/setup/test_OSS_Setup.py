from oss_bot.helpers.Test_Helper import Test_Helper
from oss_bot.setup.OSS_Setup import OSS_Setup


class test_OSS_Setup(Test_Helper):
    def setUp(self):
        self.oss_setup = OSS_Setup()
        super().setUp()


    def test__init__(self):
        assert self.oss_setup.profile_name == 'gs-detect-aws'


    def test_set_up_buckets(self):
        self.result =self.oss_setup.set_up_buckets()
        assert self.oss_setup.s3_bucket_lambdas in self.oss_setup.s3.buckets()


