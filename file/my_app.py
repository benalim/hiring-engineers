# This file was created in the /etc/datadog-agent directory and then I ran the dd-trace on it. Please see answers.md for additional information

from ddtrace import patch_all
patch_all()
from ddtrace import config
config.flask['service name'] = 'my_app'


from flask import Flask
import logging
import sys

# Have flask use stdout as the logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)
c = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c.setFormatter(formatter)
main_logger.addHandler(c)

app = Flask(__name__)

@app.route('/')
def api_entry():
     return 'Entrypoint to the Application'

@app.route('/api/apm')
def apm_endpoint():
     return 'Getting APM Started'

@app.route('/api/trace')
def trace_endpoint():
     return 'Posting Traces'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050')
