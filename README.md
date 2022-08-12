## Anvil eth_getProof POC

Basic account and storage proof retrieval for an arbitrary mainnet contract: https://etherscan.io/address/0x68e21390E57612170f2a62Eb96aCd8579230c62c

## Requirements

- [Foundry](https://github.com/gakonst/foundry)
- [pip3](https://stackoverflow.com/questions/34573159/how-can-i-install-pythons-pip3-on-my-mac)

1. Run `make` to install eth-brownie.
2. Set a valid alchemy `RPC_URL` in .env (see `example.env`)

## Steps to reproduce

1. Run anvil in forked mode by running `make anvil` in a separate terminal window
2. Run `make test-alchemy` to verify that `eth_getProof` will return the correct proofs
3. Run `make test-anvil` which fails with `requests.exceptions.RequestException: RPC error -32603: Required data unavailable`
