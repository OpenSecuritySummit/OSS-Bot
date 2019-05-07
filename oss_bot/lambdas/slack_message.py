def run(data, context):
    from oss_bot.api.API_OSS_Bot import API_OSS_Bot

    api = API_OSS_Bot()
    api.send_message('DJ8UA0RFT', '{0}'.format(data),[])
    return 'this will be a slack message'