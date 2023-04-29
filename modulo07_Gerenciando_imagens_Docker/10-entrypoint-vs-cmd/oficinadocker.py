import os
import logging.config
from flask import Flask
from flask import render_template

LOGFILE = os.getenv('LOGFILE', 'example.log')

# Clear prev config
LOGGING_CONFIG = None

# Get loglevel from env
LOGLEVEL = os.getenv('LOGLEVEL', 'INFO').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{LOGFILE}',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console','file'],
            'propagete': True,
        },
    },
})

logger = logging.getLogger('')
level = logging.getLevelName('DEBUG')
logger.setLevel(level)

app = Flask(__name__)

@app.route("/")
@app.route('/<name>')
def home(name=None):
    color = os.getenv('COLOR')
    if color:
        return render_template('index.html', name=name, color=color)
    else:
        return render_template('index.html', name=name)