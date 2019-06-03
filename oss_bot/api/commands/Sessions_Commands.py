import json

from osbot_aws.apis.Lambda import Lambda
from pbx_gs_python_utils.utils.Lambdas_Helpers import slack_message

from oss_bot.api.API_OSS_Slack import API_OSS_Slack
from oss_bot.api.commands.Participant_Commands import Participant_Commands
from oss_bot.api.commands.Site_Commands import send_screenshot_to_slack


class Sessions_Commands:

    @staticmethod
    def view_all(slack_id=None, channel=None, params=None):
        send_screenshot_to_slack('sessions', channel , [1400])

    @staticmethod
    def list(slack_id=None, channel=None, params=None):
        name = API_OSS_Slack().slack_id_to_slack_full_name(slack_id)
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'participant_info',
                   'name': name,
                   'commit': False}
        result = aws_lambda.invoke(payload)
        if result.get('status') == 'ok':
            data = result.get('data')
            text=  "Hi {0}, here are the sessions you are current participating: " \
                   "(note that this doesn't include the sessions you are an organiser)".format(name)
            sessions = json.loads(data.replace('```','')).get('sessions')
            list_text = ""
            for session in sorted(sessions):
                list_text += " ° " + session +"\n"
            attachments = [{ 'text': list_text , 'color': 'good'}]

            slack_message(text, attachments,channel)

    @staticmethod
    def _add_thread(slack_id=None, channel=None, params=None):
        slack_message('in _add_thread', [], channel)

    @staticmethod
    def add(slack_id=None, channel=None, params=None):
        if len(params) == 0:
            return ":red_circle: Hi, you need to provide the title of session to add"

        name = API_OSS_Slack().slack_id_to_slack_full_name(slack_id)
        if name is None:
            return ":red_circle: Sorry, could not find a participant page for you"
        value = " ".join(params).strip()

        text = ":point_right: adding the session `{0}` to the user `{1}`".format(value, name)
        slack_message(text, [], channel)

        command = "participant append {0},sessions,{1}".format(name, value)
        aws_lambda = Lambda('oss_bot.lambdas.oss_bot')
        aws_lambda.invoke_async({'event': {'type': 'message', 'text': command, "channel": channel}})


        # text       = ":point_right: adding the session `{0}` to the user `{1}`".format(value, name)
        # slack_message(text, [], channel)
        #
        # aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        # payload    = {'action': 'participant_append_to_field',
        #            'name'   : name,
        #            #'channel': channel,
        #            'field'  : 'sessions',
        #            'value'  : value}
        # result = aws_lambda.invoke(payload)
        # text = ":point_right: result = {0}".format(result)
        # slack_message(text, [], channel)
        # Sessions_Commands.list(slack_id,channel,None)

    @staticmethod
    def remove(slack_id=None, channel=None, params=None):
        if len(params) == 0:
            return ":red_circle: Hi, you need to provide the title of session to add"

        name = API_OSS_Slack().slack_id_to_slack_full_name(slack_id)
        if name is None:
            return ":red_circle: Sorry, could not find a participant page for you"
        value = " ".join(params).strip()

        text = ":point_right: Removing the session `{0}` from the user `{1}`".format(value, name)
        slack_message(text, [], channel)

        command = "participant remove {0},sessions,{1}".format(name, value)
        aws_lambda = Lambda('oss_bot.lambdas.oss_bot')
        aws_lambda.invoke_async({'event': {'type': 'message', 'text': command, "channel": channel}})


    @staticmethod
    def git_diff(team_id=None, channel=None, params=None):
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action' : 'git_dff' ,
                   'channel': channel            ,
                   'commit' : False              }
        aws_lambda.invoke_async(payload)

    @staticmethod
    def git_status(team_id=None, channel=None, params=None):
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'git_status',
                   'channel': channel,
                   'commit': False}
        aws_lambda.invoke_async(payload)

    @staticmethod
    def git_pull(team_id=None, channel=None, params=None):
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'git_pull',
                   'channel': channel,
                   'commit': False}
        aws_lambda.invoke_async(payload)

    @staticmethod
    def git_reset(team_id=None, channel=None, params=None):
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'git_reset',
                   'channel': channel,
                   'commit': False}
        aws_lambda.invoke_async(payload)
