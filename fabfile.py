from fnpdjango.deploy import *

env.project_name = 'timer'
env.hosts = ['giewont.icm.edu.pl']
env.user = 'timer'
env.app_path = '/srv/timer'
env.services = [
    DebianGunicorn('timer'),
]
