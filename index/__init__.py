import json
import os

INDEX_FILE_NAME = 'data/block-index.json'
BLOCK_FILE_NAME = 'data/block-{}.json'

if os.path.isfile(INDEX_FILE_NAME) is False:
    with open(INDEX_FILE_NAME, 'w+') as f:
        json.dump({}, f)


def index_new_data_to_block_index(block_id: int, transaction_cat: str):
    with open(INDEX_FILE_NAME, 'r') as index_file:
        file_data = json.load(index_file)
        old_cat_index = file_data[transaction_cat] if transaction_cat in file_data else 0
        new_cat_index = old_cat_index | (1 << block_id)
        file_data[transaction_cat] = new_cat_index

    with open(INDEX_FILE_NAME, 'w') as index_file:
        json.dump(file_data, index_file, indent=2)


def index_new_data_to_transaction_index(block_id: int, transaction_id: int, transaction_cat: str):
    with open(BLOCK_FILE_NAME.format(block_id), 'r') as file:
        file_data = json.load(file)
        old_cat_index = file_data['indexes'][transaction_cat] if transaction_cat in file_data['indexes'] else 0
        new_cat_index = old_cat_index | (1 << transaction_id)
        file_data['indexes'][transaction_cat] = new_cat_index

    with open(BLOCK_FILE_NAME.format(block_id), 'w+') as trans_index_file:
        json.dump(file_data, trans_index_file, indent=2)


def index_new_data(block_id: int, transaction_id: int, transaction_cat: str) -> None:
    if transaction_cat is not None:
        index_new_data_to_block_index(block_id, transaction_cat)
        index_new_data_to_transaction_index(block_id, transaction_id, transaction_cat)


def find_ids_from_index(index: int) -> list:
    ids_list = []
    id_idx = 0
    while index:
        if index & 1:
            ids_list.append(id_idx)
        index >>= 1
        id_idx += 1

    return ids_list


def retrieve_block_ids_index_from_index_by_cat(category: str) -> int:
    with open(INDEX_FILE_NAME, 'r') as indexFile:
        file_data = json.load(indexFile)
        if category in file_data:
            return file_data[category]

        return 0


def retrieve_transactions_from_block_id_by_cat(block_id: int, category: str) -> list:
    tx_list = []
    with open(BLOCK_FILE_NAME.format(block_id), 'r') as tx_file:
        file_data = json.load(tx_file)
        index = file_data['indexes'][category] if category in file_data['indexes'] else 0
        if index:
            ids = find_ids_from_index(index)
            for i in ids:
                tx_list.append(file_data['data'][i])

    return tx_list


def retrieve_transactions_by_category(category: str) -> list:
    retrieved_txs = []
    block_ids_idx = retrieve_block_ids_index_from_index_by_cat(category)
    block_ids = find_ids_from_index(block_ids_idx)
    for block_id in block_ids:
        retrieved_txs = [*retrieved_txs, *retrieve_transactions_from_block_id_by_cat(block_id, category)]

    return retrieved_txs
