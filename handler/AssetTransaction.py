from flask import request, Blueprint
from core.response import ResponseSuccess, ResponseFailed
from utility import messages, constants
from model.AssetTransaction import AssetTransaction

asset_transaction_handler = Blueprint('asset_transaction_handler', __name__)

@asset_transaction_handler.route('', methods = ['GET','POST','PUT','DELETE'])
def asset_transaction():
   if request.method == 'GET':
      # processing get data
      return ResponseSuccess(AssetTransaction.get(), messages.get_success, constants.http_status_ok)
   elif request.method == 'POST':
      # processing insert data
      asset_trx = AssetTransaction(
          request.form['src_wallet_id'], request.form['src_asset_id'], request.form['dest_wallet_id'], 
          request.form['dest_asset_id'], request.form['amount'], request.form['gas_fee'],
          request.form['total']
        )
      status = AssetTransaction.save(asset_trx)
      if status == True:
         return ResponseSuccess(asset_trx, messages.insert_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.insert_failed, constants.http_status_bad_request)
   elif request.method == 'PUT':
      # checking if id value is null
      if request.form['id'] is None:
         return ResponseFailed(messages.id_not_null, constants.http_status_bad_request)

      # processing update data
      asset_trx_old = AssetTransaction.fetch(request.form['id'])
      asset_trx = AssetTransaction(
          request.form['src_wallet_id'], request.form['src_asset_id'], request.form['dest_wallet_id'], 
          request.form['dest_asset_id'], request.form['amount'], request.form['gas_fee'],
          request.form['total']
        )
      status = AssetTransaction.update(asset_trx_old, asset_trx)
      if status == True:
         return ResponseSuccess(asset_trx, messages.update_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.update_failed, constants.http_status_bad_request)
   else:
      # checking if id value is null
      if request.form['id'] is None:
         return ResponseFailed(messages.id_not_null, constants.http_status_bad_request)

      # processing delete data
      asset_trx = AssetTransaction.fetch(request.form['id'])
      status = AssetTransaction.delete(asset_trx)
      if status == True:
         return ResponseSuccess(asset_trx,messages.delete_success, constants.http_status_ok)
      else:
         return ResponseFailed(messages.delete_failed, constants.http_status_bad_request)
