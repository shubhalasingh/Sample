import os, tornado
from tornado.options import define, options

# Make filepaths relative to settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = ROOT[:ROOT.rindex('/')]

# define the defaults config
define("port", default=8888, help="run on the given port", type=int)
# define("config", default=None, help="tornado config file")
define("debug", default=True, help="debug mode")
tornado.options.parse_command_line()


temp_settings = {}
temp_settings['debug'] = True
temp_settings['cookie_secret'] = "your-cookie-secret"
temp_settings['xsrf_cookies'] = False
