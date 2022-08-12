import math
import json
import argparse

from pprint import pprint
from web3 import Web3
from web3.logs import DISCARD
from eth_abi import encode
import requests
import rlp

from eth_utils import decode_hex, to_canonical_address, to_bytes, to_int, to_hex

def main():
    parser = argparse.ArgumentParser(
        description="Proof Test",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-r", "--rpc",
        default="http://localhost:8545",
        help="URL of a full node RPC endpoint, e.g. http://localhost:8545")

    args = parser.parse_args()
    w3 = Web3(Web3.HTTPProvider(args.rpc))

    block_number = w3.eth.block_number
    test_params = ['0x68e21390E57612170f2a62Eb96aCd8579230c62c',(0).to_bytes(32, byteorder='big')]

    (response) = request_account_proof(
        rpc_endpoint=args.rpc,
        block_number=block_number,
        address=test_params[0],
        slots=[test_params[1]]
    )

    print(f"response ={response}\n")

def request_account_proof(rpc_endpoint, block_number, address, slots):
    hex_slots = [to_0x_string(s) for s in slots]

    params = [address.lower(), hex_slots, to_0x_string(block_number)]

    r = requests.post(rpc_endpoint, json={
        "jsonrpc": "2.0",
        "method": "eth_getProof",
        "params": params,
        "id": 1,
    })

    #pprint(f"{vars(r)}")

    return (get_json_rpc_result(r))

def to_0x_string(x):
    if isinstance(x, str) and not x.startswith("0x"):
        x = int(x)
    return to_hex(x)

def get_json_rpc_result(response):
    response.raise_for_status()
    json_dict = response.json()
    if "error" in json_dict:
        raise requests.RequestException(
            f"RPC error { json_dict['error']['code'] }: { json_dict['error']['message'] }",
            response=response
        )
    return json_dict["result"]

if __name__ == "__main__":
    main()
    exit(0)