import os
import git
from osbot_aws.apis.Secrets import Secrets
from pbx_gs_python_utils.utils.Files import Files


class Git_Lambda:

    def __init__(self):
        self.aws_secret     = 'git-oss2019'
        self.git_org        = None
        self.git_repo       = None
        self.path_temp      = '/tmp'
        self.path_repo      = None
        self.remote         = 'origin'
        self.branch         = 'master'
        self.author_name    = 'oss-bot-dinis'
        self.author_email   = 'oss-bot@opensecsummit.org'
        self.commit_message = 'changed in lambda'
        self.set_up_commit_user()


    def git_exec(self, *params,cwd=None):
        if cwd is None:
            cwd = self.path_repo
        stdout, stderr = git.exec_command(*params,cwd=cwd)
        return stdout.decode(),stderr.decode()

    def repo_url(self):
        data = Secrets(self.aws_secret).value_from_json_string()
        #os.environ['GIT_USERNAME'] = data.get('username')      # not working
        #os.environ['GIT_PASSWORD'] = data.get('password')
        self.git_org               = data.get('git_org')
        self.git_repo              = data.get('git_repo')
        self.path_repo             = Files.path_combine(self.path_temp, self.git_repo)
        return 'https://{0}:{1}@github.com/{2}/{3}.git'.format(data.get('username'),data.get('password'),self.git_org, self.git_repo)
        #return 'https://github.com/{2}/{3}.git'.format(data.get('username'),data.get('password'),self.git_org, self.git_repo)

    def repo_files(self):
        return Files.files(Files.path_combine(self.path_repo,'**'))

    def set_up_commit_user(self):
        os.environ['GIT_AUTHOR_NAME'    ] = self.author_name
        os.environ['GIT_AUTHOR_EMAIL'   ] = self.author_email
        os.environ['GIT_COMMITTER_NAME' ] = self.author_name
        os.environ['GIT_COMMITTER_EMAIL'] = self.author_email


    # git commands

    def commit    (self): return self.git_exec('commit', '-a', '-m'         ,self.commit_message        )
    def clone     (self): return self.git_exec('clone' , self.repo_url()    , cwd=self.path_temp        )
    def log_pretty(self): return self.git_exec('log'   ,'--pretty=oneline'  ,'-n10'                     )
    def pull      (self): return self.git_exec('pull'  , '--no-edit'        , self.remote, self.branch  )
    def push      (self): return self.git_exec('push'  , self.remote        , self.branch               )
    def status    (self): return self.git_exec('status')





