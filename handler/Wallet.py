from flask import request, Blueprint
from core.response import ResponseSuccess, ResponseFailed
from utility import messages, constants
from model.Wallets import Wallets

wallet_handler = Blueprint('wallet_handler', __name__)

@wallet_handler.route('', methods = ['GET','POST','PUT','DELETE'])
def wallets():
   if request.method == 'GET':
      # processing get data
      return ResponseSuccess(Wallets.get(), messages.get_success, constants.http_status_ok)
   elif request.method == 'POST':
      # processing insert data
      wallet = Wallets(request.form['name'])
      status = Wallets.save(wallet)
      if status == True:
         return ResponseSuccess(wallet, messages.insert_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.insert_failed, constants.http_status_bad_request)
   elif request.method == 'PUT':
       # checking if id value is null
      if request.form['id'] is None:
         return ResponseFailed(messages.id_not_null, constants.http_status_bad_request)

      # processing update data
      wallet_old = Wallets.fetch(request.form['id'])
      wallet = Wallets(request.form['name'])
      status = Wallets.update(wallet_old, wallet)
      if status == True:
         return ResponseSuccess(wallet, messages.update_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.update_failed, constants.http_status_bad_request)
   else:
      # checking if id value is null
      if request.form['id'] is None:
         return ResponseFailed(messages.id_not_null, constants.http_status_bad_request)

      # processing delete data
      wallet = Wallets.fetch(request.form['id'])
      status = Wallets.delete(wallet)
      if status == True:
         return ResponseSuccess(wallet, messages.delete_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.delete_failed, constants.http_status_bad_request)
