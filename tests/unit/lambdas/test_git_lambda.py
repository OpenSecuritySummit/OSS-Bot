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
        payload = {'command': 'version' }
        self.result = self.aws_lambda.invoke(payload)

    def test_invoke_clone(self):
        payload = {'command': 'clone' }
        self.result = self.aws_lambda.invoke(payload)

    def test_invoke_pull(self):
        payload = {'command': 'pull'}
        self.result = self.aws_lambda.invoke(payload)

    def test_invoke_change(self):
        self.test_update_lambda()
        self.aws_lambda.invoke({'command': 'clone'})
        self.result = self.aws_lambda.invoke({'command': 'change'} )
        print(self.aws_lambda.invoke({'command': 'status'}))
        self.result = self.aws_lambda.invoke({'command': 'commit'})
        print(self.aws_lambda.invoke({'command': 'status'}))
        #self.result = self.aws_lambda.invoke({'command': 'push'})

    def test_ssh_setup(self):
        self.test_update_lambda()

        print(self.aws_lambda.invoke({'command': 'ssh-create'}))
        print(self.aws_lambda.invoke({'command': 'ssh-public-key'}))

    def test_remote_setup(self):
        self.test_update_lambda()
        self.aws_lambda.invoke({'command': 'clone'})
        print(self.aws_lambda.invoke({'command': 'remote-setup'}))

    def test_invoke_files(self):
        self.test_update_lambda()
        self.aws_lambda.invoke({'command': 'clone'})
        #self.aws_lambda.invoke({'command': 'clone'})
        payload = {'command': '__files'}
        self.result = self.aws_lambda.invoke(payload)

    def test_set_ssh_config(self):
        self.test_update_lambda()
        print(self.aws_lambda.invoke({'command': 'clone'}))
        #print(self.aws_lambda.invoke({'command': 'ssh-public-key'}))
        print(self.aws_lambda.invoke({'command': 'remote-setup'}))
        print(self.aws_lambda.invoke({'command': 'ssh-config'}))
        print(self.aws_lambda.invoke({'command': 'push'}))

    def test_workflow(self):
        self.test_update_lambda()
        print(self.aws_lambda.invoke({'command': 'clone'}))
        print(self.aws_lambda.invoke({'command': 'status'}))
        print(self.aws_lambda.invoke({'command': 'change'}))
        print(self.aws_lambda.invoke({'command': 'status'}))
        print(self.aws_lambda.invoke({'command': 'commit'}))
        print(self.aws_lambda.invoke({'command': 'status'}))
        print(self.aws_lambda.invoke({'command': 'push'}))
        #print(self.aws_lambda.invoke({'command': 'ssh-create'}))
        #print(self.aws_lambda.invoke({'command': 'remote-setup'}))
        #print(self.aws_lambda.invoke({'command': 'ssh-config'}))
        #print(self.aws_lambda.invoke({'command': 'ssh-public-key'}))


    def test_push(self):
        self.test_update_lambda()
        self.result = self.aws_lambda.invoke({'command': 'status'})
        #print(self.aws_lambda.invoke({'command': 'push'}))