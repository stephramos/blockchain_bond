# Bond Issuance with Algorand Blockchain

Original code from Zifan Wang: https://developer.algorand.org/solutions/minibond-issuance-pyteal-and-python-sdk/

## Accounts Setup

1) Create (and fund) the buyer and issuer accounts and issue a payment unit (ussing the issuer accnt) https://www.youtube.com/watch?v=ryk-tKyZUpk

2) Opt-in the buyer accnt to your asset and send the buyer a few units of the asset (will be used as payment)

## Environment Setup
https://developer.algorand.org/docs/sdks/python/

1) Install Sandbox
```python
git clone https://github.com/algorand/sandbox.git
cd sandbox
./sandbox up testnet
```

2) Install SDK and other libraries (better to create venv)
```python
cd ..
cd blockchain_bond
pip install -r requirements
```

## Run demo
https://www.youtube.com/watch?v=tKUvcr9ohTM&t=297s

1) Create teal directory
```python
mkdir teal
```

2) Add your publisher address, publisher pass, issuer address, publisher pass and payment id to the parameter section

3) Fetch a recent block number and submit it in the closure field: https://testnet.algoexplorer.io/

3) Run demo
```python
python main_publisher.py
```


