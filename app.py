from flask import Flask
from opencensus.ext.azure.log_exporter import AzureLogHandler
from azure.identity import DefaultAzureCredential
import logging

app = Flask(__name__)

# Set up logging
credential = DefaultAzureCredential()
logger = logging.getLogger(__name__)
logger.setLevel("INFO")
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=562bb4b7-82f0-4cf1-bd03-c739c2a94e28',
    credential=credential
))

@app.route('/')
def home():
    logger.info("Hello, World! endpoint was called")
    return "Hello, My World!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)

