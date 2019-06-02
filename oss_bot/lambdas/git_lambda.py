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
    git_lambda = Git_Lambda()
    git_lambda.clone()
    #return git_lambda.repo_files()
    #return git_lambda.status()
    #return git_lambda.log_pretty()
    #return git_lambda.pull()

    OSS_Hugo().edit_user()
    git_lambda.commit()
    git_lambda.push()

    #import git
    if command == 'clone':
        #repo = 'git@github.com:OpenSecuritySummit/oss2019.git'
        stdout,stderr =  git.exec_command('clone', repo)
        return stdout.decode()

    if command == 'pull':
        stdout, stderr = git.exec_command('pull',cwd='/tmp/oss2019')
        return stdout.decode()


    if command == 'change':
        import sys
        sys.path.append('/tmp/oss2019/notebooks/api')
        from oss_hugo.OSS_Participant import OSS_Participant
        user = OSS_Participant('/tmp/oss2019/content/participant/oss-bot.md')
        value = Misc.random_string_and_numbers()
        user.field('company', value)                                   \
            .field('sessions', ['Agile Practices for Security Teams']) \
            .save()

    if command == 'pull':
        stdout, stderr = git.exec_command('pull', cwd='/tmp/oss2019')
        return stdout.decode()

    if command == 'commit':
        import os
        commit_env = os.environ
        commit_env['GIT_AUTHOR_NAME'    ] = 'oss-bot-dinis'
        commit_env['GIT_AUTHOR_EMAIL'   ] = 'dinis@opensecsummit.org'
        commit_env['GIT_COMMITTER_NAME' ] = 'oss-bot-dinis'
        commit_env['GIT_COMMITTER_EMAIL'] = 'dinis@opensecsummit.org'
        stdout, stderr = git.exec_command('commit','-a','-m','changes in lambda', cwd='/tmp/oss2019')
        return stdout.decode()

    if command == 'status':
        stdout, stderr = git.exec_command('status', cwd='/tmp/oss2019')
        return stdout.decode()

    if command == 'files':
        return Files.files('/tmp/oss2019/notebooks/**')

    if command == 'push':
        stdout, stderr = git.exec_command('push','origin','master', cwd='/tmp/oss2019')
        return stdout.decode()

    if command == 'ssh-create':
        #from pbx_gs_python_utils.utils.Process import Process
        return Process.run('ssh-keygen',['-f', '/tmp/id_rsa','-t','rsa' ,'-N', ''])

    if command == 'ssh-public-key':
        return Files.contents('/tmp/id_rsa.pub')

    if command == 'ssh-config':
        import os
        commit_env = os.environ
        commit_env['HOME'] = '/tmp'
        #git.exec_command('config','--local','core.sshCommand',"'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'", cwd='/tmp/oss2019')
        #stdout, stderr = git.exec_command('config', '--local', 'core.sshCommand')
        #stdout, stderr = git.exec_command('config', 'http.sslVerify', 'false', cwd='/tmp/oss2019')
        #return stdout.decode()

    if command == 'remote-setup':
        git.exec_command('remote', 'set-url','origin','git@github.com:OpenSecuritySummit/oss2019.git', cwd='/tmp/oss2019')
        stdout, stderr = git.exec_command('remote','-v',cwd='/tmp/oss2019')
        return stdout.decode()

    return len(Files.files('/tmp/oss2019/**'))