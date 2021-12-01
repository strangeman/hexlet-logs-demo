import logging
from pythonjsonlogger import jsonlogger
from flask import Flask
from requests import get
import sys
from datetime import datetime

logger = logging.getLogger()
formatter = jsonlogger.JsonFormatter()

# раскомментируйте для добавления в логи полей level и timestamp
# class CustomJsonFormatter(jsonlogger.JsonFormatter):
#     def add_fields(self, log_record, record, message_dict):
#         super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
#         if not log_record.get('timestamp'):
#             # this doesn't use record.created, so it is slightly off
#             now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
#             log_record['timestamp'] = now
#         if log_record.get('level'):
#             log_record['level'] = log_record['level'].upper()
#         else:
#             log_record['level'] = record.levelname

# formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')

logHandler = logging.StreamHandler(sys.stdout)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, service_a!</p>"

@app.route("/<int:id>")
def multiply_id(id: int):
    logger.info(f'Got request to /{id}')
    logger.info(f'Send multiplied request to /{id*2}')
    r = get(f"http://service_b:5000/{id*2}")
    return f"Success {r.text}"
