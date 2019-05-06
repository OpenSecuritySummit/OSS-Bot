from pbx_gs_python_utils.utils.Misc import Misc


def run(event, context):
    return "Hello {0} (from lambda)".format(Misc.get_value(event,'name','_'))