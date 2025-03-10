import os

from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://redis:6379/0'

redis = FlaskRedis(app)


@app.route('/')
def counter():
    return '{0} {1}'.format(str(redis.incr('web2_counter hfehe')),
                            os.getenv('WEB2_COUNTER_MSG', ''))
