from bitcoin.rpc import RawProxy

p = RawProxy()

# Choose the latest block validated by your node.
blockhash = p.getbestblockhash()
block = p.getblock(blockhash)

block_value = 0

for txid in block["tx"]:
    # Supply the block hash because txindex is disabled.
    raw_tx = p.getrawtransaction(txid, False, blockhash)
    decoded_tx = p.decoderawtransaction(raw_tx)

    for output in decoded_tx["vout"]:
        block_value += output["value"]

print("Block height:", block["height"])
print(f"Total value in block: {block_value:.8f} BTC")
