import os
import warnings

from flask import Flask

from core.config import app_config
from core.database import db, migrate
from utility import messages, constants
from core.response import ResponseSuccess, ResponseFailed

from handler.Asset import asset_handler
from handler.Wallet import wallet_handler
from handler.AssetTransaction import asset_transaction_handler

# Initialize The API
warnings.filterwarnings("ignore")
app = Flask(__name__)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])
db.init_app(app)
migrate.init_app(app, db)

# Registering some API handlers
app.register_blueprint(asset_handler, url_prefix='/assets')
app.register_blueprint(wallet_handler, url_prefix='/wallets')
app.register_blueprint(asset_transaction_handler, url_prefix='/asset/transaction')

@app.route('/')
def flask_app():
   return ResponseSuccess({ 
      "status": constants.http_status_ok,
      "message": messages.flask_message
   }, constants.http_status_ok)

@app.errorhandler(404)
def error(e):
    return ResponseFailed(str(e), 404)

@app.errorhandler(500)
def error(e):
    return ResponseFailed(str(e), 500)

if __name__ == '__main__':
   app.run(os.getenv('APP_HOST'), os.getenv('APP_PORT'), os.getenv('APP_DEBUG'))