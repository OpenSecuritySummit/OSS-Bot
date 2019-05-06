class OSS_Bot_Commands:                                      # move to separate class

    gsbot_version = 'v0.10'

    @staticmethod
    def hello(slack_event, params=None):
        user = slack_event.get('user')
        return 'Hello <@{0}>, how can I help you?'.format(user), []

    @staticmethod
    def help(slack_event, params=None):
        commands        = [func for func in dir(OSS_Bot_Commands) if callable(getattr(OSS_Bot_Commands, func)) and not func.startswith("__")]
        title           = "*Here are the commands available*"
        attachment_text = ""
        for command in commands:
            if command is not 'bad_cmd':
                attachment_text += " • {0}\n".format(command)
        return title,[{'text': attachment_text, 'color': 'good'}]
