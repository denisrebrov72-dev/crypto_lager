from models import TransactionCreate,TransactionOut,BlockCreate,BlockOut
from storage import transactions
import random
from datetime import datetime
import hashlib

def create_transaction(transaction: TransactionCreate):
    new_t = {"id": random.randint(10**7,10**9),
            "timestamp":datetime.now()}
    new_t.update(transaction.model_dump())

    transactions.append(TransactionOut(**new_t))
    return new_t

def get_transactions():
    return transactions

def create_block(block: BlockCreate):
    hash = hashlib.sha256(str(block.model_dump()).encode())
    new_b = {
        "id": random.randint(10**7,10**9),
        "hash": f"hash_{hash.hexdigest()}",
        "timestamp": datetime.now(),
        "is_mined": False
        }
    new_b.update(block.model_dump())
    return new_b

# b1=BlockCreate(previous_hash="",transactions_ids=[1,2,3],miner = "Майнер Тест")
# b1_full = create_block(b1)

# b2 = BlockCreate(previous_hash=b1_full["hash"],transactions_ids=[45279,986788,967],miner = "Майнер Тест2")
# b2_full = create_block(b2)



