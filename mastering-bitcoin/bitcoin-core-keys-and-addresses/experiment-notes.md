# Experiments and discussion

[Topic](README.md)

Assistant summary of the learner's Chapter 3 experiments and discussion.
Recorded on 2026-10-21.

## API and Python examples

The learner used both `bitcoin-cli` and a JSON-RPC request with `curl`.

- Python version shown: 3.15.0.
- Virtual environment: `~/.venvs/bitcoin-learning`.
- Installed library: `python-bitcoinlib` 0.12.2.
- Import check output: `Library loaded`.

[Library source](https://github.com/petertodd/python-bitcoinlib).

The learner shared successful output from `rpc_example.py`.

The shared output from `rpc_transaction.py` was:

```text
bc1p8dqa4wjvnt890qmfws83te0v3qxzsfu7ul63kp7u56w8qc0qwp5qv995qn 0.00020000
bc1qwafvze0200nh9vkq4jmlf4sy0tn0ga5w0zpkpg 0.00075000
```

These are public example addresses from the book.
The script decodes transaction data copied from Chapter 3.
It does not retrieve that transaction by ID.

`rpc_block.py` is saved.
It selects the node's latest block and supplies its hash when requesting transactions.
No result from running this script has been shared.

## Questions discussed

- Pruning and the transaction index.
- JSON-RPC and API access.
- Transaction inputs, output references and output values.
- Public keys, private keys and addresses.
- Random key generation and the private key range.
- Signatures, repeated transactions and spending an output once.

These entries record discussion topics, not completed assessments.
The learner paused Chapter 4 because the concepts still needed more explanation.
