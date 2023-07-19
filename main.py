from web3 import Web3
import random
import time

from mintABI import mint_ZoraCreator1155
from ZoraConfig import private_key, rpc_Zora, contract_address

web3 = Web3(Web3.HTTPProvider(rpc_Zora))
print(f'Connection is: {web3.is_connected()}')

address = Web3.to_checksum_address(web3.eth.account.from_key(private_key=private_key).address)


def mint():
    nft_contract = web3.to_checksum_address(contract_address)
    contract = web3.eth.contract(nft_contract, abi=mint_ZoraCreator1155)

    pricenft = web3.to_wei (0.0018, 'ether')
    gasPrice = int(web3.eth.gas_price * 1.1)

    mintnft = contract.functions.mint(
        address,
        1,
        1,
        address,

    ).build_transaction({
        'nonce': web3.eth.get_transaction_count(address),
        'gasPrice': gasPrice,
        'value': pricenft,
        'from': address,
    })

    time.sleep(3)
    print('Start TX')

    sign_tx = web3.eth.account.sign_transaction(mintnft, private_key)
    tx_hash = web3.eth.send_raw_transaction(sign_tx.rawTransaction).hex()

    print(f'Mint done with HEX {tx_hash}')



mint()

print('end')
