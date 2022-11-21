from flask import request, Blueprint
from core.response import ResponseSuccess, ResponseFailed
from utility import messages, constants
from model.Assets import Assets

asset_handler = Blueprint('asset_handler', __name__)

@asset_handler.route('', methods = ['GET','POST','PUT','DELETE'])
def assets():
   if request.method == 'GET':
      # processing get data
      return ResponseSuccess(Assets.get(), messages.get_success, constants.http_status_ok)
   elif request.method == 'POST':
      # processing insert data
      asset = Assets(
          request.form['wallet_id'], request.form['name'], request.form['symbol'], 
          request.form['network'], request.form['address'], request.form['balance']
        )
      status = Assets.save(asset)
      if status == True:
         return ResponseSuccess(asset, messages.insert_success, messages.get_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.insert_failed, constants.http_status_bad_request)
   elif request.method == 'PUT':
      # checking if id value is null
      if request.form['id'] is None:
         return ResponseFailed(messages.id_not_null, constants.http_status_bad_request)

      # processing update data
      asset_old = Assets.fetch(request.form['id'])
      asset = Assets(
          request.form['wallet_id'], request.form['name'], request.form['symbol'], 
          request.form['network'], request.form['address'], request.form['balance']
        )
      status = Assets.update(asset_old, asset)
      if status == True:
         return ResponseSuccess(asset, messages.update_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.update_failed, constants.http_status_bad_request)
   else:
      # checking if id value is null
      if request.form['id'] is None:
         return ResponseFailed(messages.id_not_null, constants.http_status_bad_request)

      # processing delete data
      asset = Assets.fetch(request.form['id'])
      status = Assets.delete(asset)
      if status == True:
         return ResponseSuccess(asset, messages.delete_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.delete_failed, constants.http_status_bad_request)