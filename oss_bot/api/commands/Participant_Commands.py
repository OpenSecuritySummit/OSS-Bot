from osbot_aws.apis.Lambda import Lambda
from pbx_gs_python_utils.utils.Lambdas_Helpers import slack_message

from oss_bot.api.commands import Site_Commands

def send_screenshot_to_slack(path, channel, extra_params: list):
    if path is None: path = ''
    url = 'https://open-security-summit.org/' + path
    from oss_bot.api.commands.OSS_Bot_Commands import OSS_Bot_Commands
    params = ["screenshot", url]
    params.extend(extra_params)
    OSS_Bot_Commands().browser({'channel': channel}, params)



class Participant_Commands:


    @staticmethod
    def info(team_id=None, channel=None, params=None):
        name = " ".join(params)
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action' : 'participant_info' ,
                   'name'   : name               ,
                   'channel': channel            ,
                   'commit' : False              }
        aws_lambda.invoke_async(payload)

    @staticmethod
    def view(team_id=None, channel=None, params=None):
        name = " ".join(params)
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'participant_url',
                   'name'  : name,
                   'commit': False}
        result = aws_lambda.invoke(payload)
        if result.get('status') == 'ok':
            path = result.get('data')
            send_screenshot_to_slack(path,channel,[1200])
        else:
            return ":red_circle: error, couldn't find url for `{0}".format(name)


    @staticmethod
    def edit(team_id=None, channel=None, params=None):
        data = " ".join(params).split(',')
        if len(data) != 3:
            return "error: you need to provide 3 fields to edit the value(comma delimited): `name`, `field name` and `field value`"
        name, field, value = data
        name  = name.strip()
        field = field.strip()
        value = value.strip()
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action' : 'participant_edit_field',
                   'name'   : name,
                   'channel': channel,
                   'field' : field,
                   'value': value}
        aws_lambda.invoke_async(payload)

    @staticmethod
    def append(team_id=None, channel=None, params=None):
        data = " ".join(params).split(',')
        if len(data) != 3:
            return "error: you need to provide 3 fields to append an value (comma delimited): `name`, `field name` and `field value`"
        name, field, value = data
        name = name.strip()
        field = field.strip()
        value = value.strip()
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'participant_append_to_field',
                   'name': name,
                   'channel': channel,
                   'field': field,
                   'value': value}
        aws_lambda.invoke_async(payload)

    @staticmethod
    def remove(team_id=None, channel=None, params=None):
        data = " ".join(params).split(',')
        if len(data) != 3:
            return "error: you need to provide 3 fields to append an value (comma delimited): `name`, `field name` and `field value`"
        name, field, value = data
        name = name.strip()
        field = field.strip()
        value = value.strip()
        aws_lambda = Lambda('oss_bot.lambdas.git_lambda')
        payload = {'action': 'participant_remove_from_field',
                   'name': name,
                   'channel': channel,
                   'field': field,
                   'value': value}
        aws_lambda.invoke_async(payload)