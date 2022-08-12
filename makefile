-include .env

install      :; pip3 install eth-brownie

anvil        :; anvil --fork-url $(RPC_URL)
test-anvil   :; python3 generate_proof.py -r http://127.0.0.1:8545
test-alchemy :; python3 generate_proof.py -r $(RPC_URL)
