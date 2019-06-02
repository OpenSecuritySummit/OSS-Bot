from pbx_gs_python_utils.utils.Files import Files
from pbx_gs_python_utils.utils.Misc import Misc
from pbx_gs_python_utils.utils.Process import Process

from oss_bot.lambdas.png_to_slack import load_dependency


def run(event, context):
    load_dependency('lambda-git')
    load_dependency('frontmatter')

    command = event.get('command')

    from oss_bot.api_in_lambda.Git_Lambda import Git_Lambda
    from oss_bot.api_in_lambda.OSS_Hugo   import OSS_Hugo
    git_lambda = Git_Lambda('oss2019')
    git_lambda.clone().exists()

    #return git_lambda.repo_files()
    #return git_lambda.status()
    #return git_lambda.log_pretty()
    #return git_lambda.pull()

    OSS_Hugo().edit_user()
    git_lambda.commit()
    git_lambda.push()
    return 'all done'