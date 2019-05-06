def run(data, context):
    # this Lambda function is triggered by this API GW method https://545ojrb6r0.execute-api.eu-west-2.amazonaws.com/dev/event-handler
    try:
        from oss_bot.api.Slack_Handler import Slack_Handler
        return Slack_Handler().run(data)
    except Exception as error:
        #from osbot.api.API_GS_Bot import log_debug
        #log_debug("Error processing request: {0}".format(error), data=data, category='gs_bot')
        return "500 Error"