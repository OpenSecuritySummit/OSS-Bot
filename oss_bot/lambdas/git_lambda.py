from pbx_gs_python_utils.utils.Files import Files
from pbx_gs_python_utils.utils.Misc import Misc
from pbx_gs_python_utils.utils.Process import Process

from oss_bot.lambdas.png_to_slack import load_dependency


def run(event, context):
    action = event.get('action')
    name   = event.get('name')
    field  = event.get('field')
    value  = event.get('value')
    user   = event.get('user')

    if user is None:
        user = 'OSS_Bot'

    if action and name and field and value:
        load_dependency('lambda-git')
        load_dependency('frontmatter')

        from oss_bot.api_in_lambda.OSS_Hugo   import OSS_Hugo
        try:
            oss_hugo = OSS_Hugo().setup()
            method   = getattr(oss_hugo,action)
            if method(name, field, value):
                commit_message = 'Lambda change, requested by user: {0} \n' \
                                 ' - action: {1} \n'             \
                                 ' - field: {2}  \n'             \
                                 ' - value: {3}'                 .format(user, action, field, value)
                oss_hugo.git_commit_and_push(commit_message)
                return {'status': 'ok'}
        except Exception as error:
            return {'status': 'error', 'data': "{0}".format(error)}
    return {'status': 'error', 'data': 'error occurred when updating data'}