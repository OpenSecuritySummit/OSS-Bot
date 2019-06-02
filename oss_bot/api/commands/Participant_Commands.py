from osbot_aws.apis.Lambda import Lambda

class Participant_Commands:

    @staticmethod
    def info(*event):
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'participant_info',
                   'name': 'OSS Bot'           ,
                   'commit': False             }
        return aws_lambda.invoke(payload)

