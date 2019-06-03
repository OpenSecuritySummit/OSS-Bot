from oss_bot.api.API_OSS_Slack import API_OSS_Slack
from oss_bot.api.commands.Participant_Commands import Participant_Commands
from oss_bot.api.commands.Participant_Commands import send_screenshot_to_slack


class Schedule_Commands:

    @staticmethod
    def today(*event):
        send_screenshot_to_slack('schedule/day/mon', event[1], [1200])

    @staticmethod
    def tuesday(*event):
        send_screenshot_to_slack('schedule/day/tue', event[1], [1200])

    @staticmethod
    def wednesday(*event):
        send_screenshot_to_slack('schedule/day/wed', event[1], [1200])

    @staticmethod
    def mine(slack_id, channel,params):
        name = API_OSS_Slack().slack_id_to_slack_full_name(slack_id)
        Participant_Commands.view(slack_id, channel, [name])

    @staticmethod
    def of_participant(slack_id, channel, params):
        slack_id= "".join(params).replace('<@','').replace('>','')
        name = API_OSS_Slack().slack_id_to_slack_full_name(slack_id)
        Participant_Commands.view(slack_id, channel, [name])
