from osbot_aws.apis.Lambda import Lambda

class Maps_Commands:

    @staticmethod
    def ping(*event):
        return 'pong : {0}'.format(event)

    @staticmethod
    def cup_of_tea(*event):
        aws_lambda = Lambda('osbot_browser.lambdas.lambda_browser')
        payload = {"params": ["render", "examples/wardley_map/cup-of-tea.html"],
                   'data': {'channel': event[1]}}
        return aws_lambda.invoke_async(payload)

    @staticmethod
    def simple(*event):
        aws_lambda = Lambda('osbot_browser.lambdas.lambda_browser')
        payload = {"params": ["render", "examples/wardley_map/simple.html"],
                   'data': {'channel': event[1]}}
        return aws_lambda.invoke_async(payload)


