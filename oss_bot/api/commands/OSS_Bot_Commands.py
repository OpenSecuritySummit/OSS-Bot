from osbot_aws.apis.Lambda import Lambda
from pbx_gs_python_utils.utils.Misc import Misc
from pbx_gs_python_utils.utils.slack.Slack_Commands_Helper import Slack_Commands_Helper

from oss_bot.api.commands.Maps_Commands         import Maps_Commands
from oss_bot.api.commands.Dev_Commands          import Dev_Commands
from oss_bot.api.commands.Participant_Commands  import Participant_Commands
from oss_bot.api.commands.Schedule_Commands     import Schedule_Commands
from oss_bot.api.commands.Sessions_Commands     import Sessions_Commands
from oss_bot.api.commands.Site_Commands         import Site_Commands
from oss_bot.api.commands.FAQ_Commands          import FAQ_Commands

def use_command_class(slack_event, params, target_class):
    channel = Misc.get_value(slack_event, 'channel')
    user    = Misc.get_value(slack_event, 'user')
    Slack_Commands_Helper(target_class).invoke(team_id=user, channel=channel, params=params)
    return None,None

class OSS_Bot_Commands:                                      # move to separate class

    gsbot_version = 'v0.47'

    @staticmethod
    def browser(slack_event=None, params=None):
        Lambda('osbot_browser.lambdas.lambda_browser').invoke_async({'params':params, 'data':slack_event}),[]
        return None,None

    @staticmethod
    def dev(slack_event=None, params=None):
        return use_command_class(slack_event, params, Dev_Commands)

    @staticmethod
    def jp(slack_event=None, params=None):
        return OSS_Bot_Commands.jupyter(slack_event,params)

    @staticmethod
    def jupyter(slack_event=None, params=None):
        Lambda('osbot_jupyter.lambdas.osbot').invoke_async({'params': params, 'data': slack_event}), []
        return None, None

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
        return use_command_class(slack_event, params, Site_Commands)

    @staticmethod
    def faq(slack_event=None, params=None):
        return use_command_class(slack_event, params, FAQ_Commands)

    @staticmethod
    def maps(slack_event=None, params=None):
        return use_command_class(slack_event, params, Maps_Commands)

    @staticmethod
    def participant(slack_event=None, params=None):
        return use_command_class(slack_event,params,Participant_Commands)

    @staticmethod
    def schedule(slack_event=None, params=None):
        return use_command_class(slack_event, params, Schedule_Commands)

    @staticmethod
    def sessions(slack_event=None, params=None):
        return use_command_class(slack_event, params, Sessions_Commands)

    @staticmethod
    def version(*params):
        return OSS_Bot_Commands.gsbot_version,[]




