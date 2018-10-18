import os
project_directory =os.path.dirname(os.path.abspath(__file__))
RINKEBY_SOCKET_FILE_PATH = '/tmp/rinkeby/geth.ipc'
MAINNET_SOCKET_FILE_PATH = ''
NETWORK_TO_USE = 'local'  # choose between 'local' --> ganache (use this if you are developing with truffle and start
# the local blockchain with truffle develop) 'in_memory_test_rpc' --> simple in memory blockchain (use this if you are
# not using truffle to start the development blockchain)  or 'rinkeby' --> rinkeby testnet
CONTRACTS_FOLDER = contracts_folder = os.path.join(os.path.join(project_directory, 'truffle_project'), 'contracts')
CONTRACTS_ABI_FOLDER = os.path.join(
    os.path.join(os.path.join(project_directory, 'truffle_project'), 'build'), 'contracts')
print(CONTRACTS_ABI_FOLDER)

ETHER_WALLET_ID_TO_USE = 0

UPGRADABLE_VOTING_PROXY_SMART_CONTRACT_ADDRESS = '0xb742f3242a0bea9d19076f8357da10184782ce1b'
PROVIDER_RATING_CONTRACT_EXISTING_ON_BLOCKCHAIN = False
PROVIDER_RATING_CONTRACT_ADDRESS = '0x8DA7eB4Ec3A4c1291797e13DB723f9046afF4a1C'
