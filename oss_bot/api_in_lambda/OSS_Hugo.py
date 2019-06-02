from pbx_gs_python_utils.utils.Misc import Misc


class OSS_Hugo:
    def __init__(self):
        self.repo_path = '/tmp/oss2019'

    def edit_user(self):
        import sys
        sys.path.append('/tmp/oss2019/notebooks/api')
        from oss_hugo.OSS_Participant import OSS_Participant
        user  = OSS_Participant('/tmp/oss2019/content/participant/oss-bot.md')
        value = Misc.random_string_and_numbers()
        user.field('company', value) \
            .field('sessions', ['Agile Practices for Security Teams']) \
            .save()