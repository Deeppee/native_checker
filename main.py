from web3 import Web3
import csv

W_3 = {"Ethereum": Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth/")),
       "Arbitrum": Web3(Web3.HTTPProvider("https://rpc.ankr.com/arbitrum/")),
       "Optimism": Web3(Web3.HTTPProvider("https://rpc.ankr.com/optimism/")),
       "Polygon": Web3(Web3.HTTPProvider("https://rpc.ankr.com/polygon/")),
       "BSC": Web3(Web3.HTTPProvider("https://rpc.ankr.com/bsc/")),
       "Avalanch": Web3(Web3.HTTPProvider("https://rpc.ankr.com/avalanche")),
       "Fantom": Web3(Web3.HTTPProvider("https://rpc.ankr.com/fantom/")),
       "ZkSyncEra": Web3(Web3.HTTPProvider("https://mainnet.era.zksync.io"))}

def native_balance_check(address, chain):
    while True:
        try:
            w3 = W_3[chain]
            balance_wei = w3.eth.get_balance(address)
            balance_eth = w3.from_wei( balance_wei, 'ether' )
            return round(balance_eth, 5)
        except Exception as error:
            print(error)
            pass

if __name__ == "__main__":

    file_path = "results.csv"
    result = {}
    counter = 0

    with open( "wallets.txt", "r" ) as f:
        wallets_list = [row.strip() for row in f if row.strip()]

    names = []
    for key, value in W_3.items():
        names.append(key)
    result["Wallet"] = names

    for address in wallets_list:
        counter += 1
        print(f"Wallet: {address} ||| {counter}/{len(wallets_list)} in progress...")
        data = []
        for key in W_3:
            value = native_balance_check(address, key)
            data.append(str(value).replace( '.', ','))
        result[address] = data

    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')

        for key, values in result.items():
            row = [key]
            row.extend(values)
            writer.writerow(row)
    print("DONE!")