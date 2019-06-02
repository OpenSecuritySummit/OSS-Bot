from pbx_gs_python_utils.utils.Misc import Misc
from oss_bot.api_in_lambda.Git_Lambda import Git_Lambda

class OSS_Hugo:
    def __init__(self):
        self.repo_path  = '/tmp/oss2019'
        self.git_lambda = Git_Lambda('oss2019')

    def setup(self):
        self.git_lambda.clone()                     # clone (if needed)
        return self

    def git_commit_and_push(self,commit_message):
        self.git_lambda.pull()
        self.git_lambda.commit(commit_message)
        self.git_lambda.push()
        return self

    def participant_get(self, user_name):
        import sys
        sys.path.append('/tmp/oss2019/notebooks/api'); from oss_hugo.OSS_Participant import OSS_Participant # shows error on PyCharm

        return  OSS_Participant(name=user_name, folder_oss=self.repo_path)

    def participant_edit_field(self, name, field_name,field_value):
        participant = self.participant_get(name)
        if participant.exists():
            participant.field(field_name, field_value)
            participant.save()
            return True
        return False

    def participant_append_to_field(self, name, field_name, field_value):
        participant = self.participant_get(name)
        if participant.exists():
            current_value = participant.field(field_name)
            if current_value:
                if type(current_value) is list:
                    new_value = current_value.append(field_value)
                    participant.field(field_name, new_value)
                else:
                    participant.field(field_name,current_value + field_value)
            else:
                participant.field(field_name, field_value)
            participant.save()
            return True
        return False

    def participant_remove_from_field(self, name, field_name, field_value):
        participant = self.participant_get(name)
        if participant.exists():
            current_value = participant.field(field_name)
            if current_value:
                if type(current_value) is list:
                    if field_value in current_value:
                        current_value.remove(field_value)
                        participant.field(field_name,current_value)
                    else:
                        return False
                else:
                    new_value = current_value.replace(field_value, '')
                    participant.field(field_name,new_value)
            else:
                participant.field(field_name, field_value)
            participant.save()
            return True
        return False