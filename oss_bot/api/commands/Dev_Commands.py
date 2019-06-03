from oss_bot.api.API_OSS_Slack import API_OSS_Slack

class Dev_Commands:

    @staticmethod
    def ping(*event):
        return 'pong : {0}'.format(event)

    @staticmethod
    def my_name(slack_id, channel,params):
        return "your real name is {0}".format(API_OSS_Slack().slack_id_to_slack_full_name(slack_id))

    @staticmethod
    def resolve(slack_id, channel, params):
        slack_id= "".join(params).replace('<@','').replace('>','')
        return API_OSS_Slack().slack_id_to_slack_full_name(slack_id)
