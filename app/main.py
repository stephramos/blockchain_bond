from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from algosdk.future.transaction import LogicSig, PaymentTxn, AssetConfigTxn, AssetTransferTxn, LogicSigTransaction
from algosdk import mnemonic
from algosdk.v2client import algod
import os
import base64

from publisher import main_pub, algod_client
from buyer import purchase_bond, claim_interest, claim_par

#GJEZXKN5ZF4IF3TAKTDW5WPK2MLME7ATU4TE6M4UUB5VK7HPTDKMJL4AOM
passphrase = "area eagle alert poverty purchase annual mention join accuse message distance gasp clog find trust become limb cart isolate barrel vivid future hundred absent crumble"


class Item(BaseModel):
    passphrase: str
    par: int
    coupon: int 
    vol: int 
    total_payments: int 
    bond_name: str 
    url: Optional[str] = None
    
app=FastAPI()

@app.get("/")
def read_root():
    return {"hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    #http://127.0.0.1:8000/items/6?q=steph
    return {"item_id":  item_id, "q":q}

@app.get("/funds/{accnt_key}")
def check_funds(accnt_key: str):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)
    account_info = algod_client.account_info(accnt_key)
    resp_dict = {'data': []}
    resp_dict['data'].append({'asset-id': 'microAlgos', 'balance': account_info.get('amount')})
    
    for asset in account_info.get('assets'):
        resp_dict['data'].append({'asset-id': asset.get('asset-id'), 'balance': asset.get('amount')})
    
    return resp_dict    
 
    
@app.post("/issue_bond/")
def issue_bond(item: Item):
    '''
    {
  "passphrase": "area eagle alert poverty purchase annual mention join accuse message distance gasp clog find trust become limb cart isolate barrel vivid future hundred absent crumble",
  "par": 5,
  "coupon": 1,
  "vol": 1000,
  "total_payments": 5,
  "bond_name": "first_bond"}
    '''
    
    print(item)
    print(item.par)
    payment_id = 81122413
    closure =  20788590 + 20
    first_coupon_payment = closure + 1
    period = 10
    span = 500
    holdup = 120000000
    client = algod_client()
    
    
    interest_id, par_id, escrow_result, escrow_id = main_pub(item.passphrase, item.bond_name, 
            item.vol, item.url, item.par, item.coupon, payment_id,
             closure, first_coupon_payment, period, item.total_payments, span, holdup, client)
    
    return {
        'interest_id': interest_id,
        'par_id': par_id,
        'escrow_result': escrow_result,
        'escrow_id': escrow_id
    }
    
    
@app.get("/bond/{passphrase}")
def buy_bond(passphrase: str):
        
        
    resp_dict = {}   
    
    
    return resp_dict

