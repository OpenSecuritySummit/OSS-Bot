from pbx_gs_python_utils.utils.Files import Files

from oss_bot.lambdas.png_to_slack import load_dependency


def run(event, context):
    command = event.get('command')
    load_dependency('lambda-git')
    import git

    if command == 'clone':
        #stdout,stderr =  git.exec_command(command)
        repo = 'https://github.com/OpenSecuritySummit/oss2019.git'
        stdout,stderr =  git.exec_command('clone', repo)
        #return stdout.decode(), stderr.decode()

    if command == 'pull':
        stdout, stderr = git.exec_command('pull',cwd='/tmp/oss2019')
        return stdout.decode()



    return len(Files.files('/tmp/oss2019/**'))