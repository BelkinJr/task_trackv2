import os


ENV__LOCAL = 'local'
ENV__DEV = 'dev'

APP_MODES = [ENV__LOCAL, ENV__DEV, ]

CURRENT_ENV = os.environ['APPLICATION_MODE']
