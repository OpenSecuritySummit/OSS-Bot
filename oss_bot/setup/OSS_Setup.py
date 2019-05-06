from osbot_aws.Globals import Globals
from osbot_aws.apis.IAM import IAM
from osbot_aws.apis.S3 import S3


class OSS_Setup:

    def __init__(self):
        self.bot_name          = 'oss_bot'
        self.profile_name      = 'gs-detect-aws'  # 654386450934
        self.region_name       = 'eu-west-2'
        self.account_id        = '654386450934'
        self.role_lambdas      = "arn:aws:iam::{0}:role/service-role/osbot-lambdas".format(self.account_id)
        self.s3_bucket_lambdas = '{0}-lambdas'.format(self.bot_name).replace('_','-')
        self.s3                = S3()

    def setup_test_environment(self):
        # todo: add check when running in AWS
        Globals.aws_session_profile_name = self.profile_name
        Globals.aws_session_region_name = self.region_name
        return self

    def set_up_buckets(self):
        if self.s3_bucket_lambdas not in self.s3.buckets():
            result = self.s3.bucket_create(self.s3_bucket_lambdas,self.region_name)
            assert result.get('status') == 'ok'
        return self


