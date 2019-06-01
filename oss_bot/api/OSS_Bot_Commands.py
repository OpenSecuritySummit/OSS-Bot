from osbot_aws.apis.Lambda import Lambda
from pbx_gs_python_utils.utils.Misc import Misc
from pbx_gs_python_utils.utils.slack.Slack_Commands_Helper import Slack_Commands_Helper

from oss_bot.api.commands.Site_Commands import Site_Commands
from oss_bot.api.commands.FAQ_Commands import FAQ_Commands


class OSS_Bot_Commands:                                      # move to separate class

    gsbot_version = 'v0.22'

    @staticmethod
    def browser(slack_event=None, params=None):
        Lambda('osbot_browser.lambdas.lambda_browser').invoke_async({'params':params, 'data':slack_event}),[]
        return None,None

    @staticmethod
    def hello(slack_event=None, params=None):
        user = Misc.get_value(slack_event, 'user')
        return 'Hello <@{0}>, how can I help you?'.format(user), []

    @staticmethod
    def help(*params):
        commands        = [func for func in dir(OSS_Bot_Commands) if callable(getattr(OSS_Bot_Commands, func)) and not func.startswith("__")]
        title           = "*Here are the commands available*"
        attachment_text = ""
        for command in commands:
            if command is not 'bad_cmd':
                attachment_text += " • {0}\n".format(command)
        return title,[{'text': attachment_text, 'color': 'good'}]

    @staticmethod
    def screenshot(slack_event=None, params=None):
        params.insert(0,'screenshot')
        Lambda('osbot_browser.lambdas.lambda_browser').invoke_async({'params': params, 'data': slack_event}), []
        return None, None

    @staticmethod
    def site(slack_event=None, params=None):
        team_id = Misc.get_value(slack_event, 'team_id')
        channel = Misc.get_value(slack_event, 'channel')
        Slack_Commands_Helper(Site_Commands).invoke(team_id, channel, params)
        return None,None

    @staticmethod
    def faq(slack_event=None, params=None):
        team_id = Misc.get_value(slack_event, 'team_id')
        channel = Misc.get_value(slack_event, 'channel')
        Slack_Commands_Helper(FAQ_Commands).invoke(team_id, channel, params)
        return None,None

    @staticmethod
    def version(*params):
        return OSS_Bot_Commands.gsbot_version,[]


