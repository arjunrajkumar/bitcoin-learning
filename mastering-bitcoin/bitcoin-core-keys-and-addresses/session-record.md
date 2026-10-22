# Setup and session record

[Topic](README.md)

Assistant summary of the learner's commands, output and discussion.
First recorded on 2026-10-21. Later updates are dated below.
This record is based on shared output. It is not a live check of the node.

## Bitcoin Core setup

- Built Bitcoin Core v24.0.1 on an Apple Silicon Mac.
- Followed `doc/build-osx.md`.
- Included the graphical interface, modern wallets and older wallet support.
- Ran `make check && sudo make install`.
- The shared test summaries showed zero failures and zero errors.
- Verified `bitcoind` and `bitcoin-cli` as v24.0.1.
- Installed `bitcoind`, `bitcoin-cli` and `bitcoin-qt` in `/usr/local/bin`.

The source checkout is separate from this repository.
Its remote is [bitcoin/bitcoin](https://github.com/bitcoin/bitcoin).
Do not repeat the completed build without a reason.

Two build fixes were needed:

1. Select the installed macOS 26.5 SDK:

   ```sh
   export SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk
   ```

2. Disable the optional feature that was incompatible with miniupnpc 2.3.3:

   ```sh
   ./configure --with-gui=yes --without-miniupnpc
   ```

## Node settings

The learner chose the internal drive.
The data folder is `~/Library/Application Support/Bitcoin`.
The saved `bitcoin.conf` contains:

```ini
prune=10000
txindex=0
```

The learner started with `bitcoind -printtoconsole`.
The output confirmed a target of 10000 MiB for block and undo files.
The `getblockchaininfo` output showed `pruned: true` and
`automatic_pruning: true`.

The learner stopped that process with Ctrl-C.
After `Shutdown: done`, the learner ran `bitcoind -daemon`.
Later output showed the initial blockchain download in progress.
No later completion has been recorded.

## Download progress — 22 October 2026

The learner shared a screenshot of `bitcoin-cli getblockchaininfo` at 09:12
India time. Selected values from that output:

```json
{
  "chain": "main",
  "blocks": 632682,
  "headers": 972562,
  "verificationprogress": 0.468052002607328,
  "initialblockdownload": true,
  "size_on_disk": 9986304347,
  "pruned": true,
  "pruneheight": 625784,
  "automatic_pruning": true,
  "prune_target_size": 10485760000,
  "warnings": ""
}
```

Assistant explanation: the node had reached block 632,682.
Estimated verification progress was about 46.8%.
This is not a percentage of elapsed time.
Pruning was enabled, and the output contained no warnings.
The reported block and undo file size was about 9.99 GB.
That value does not include the whole Bitcoin data folder.

### Stop and resume — guidance

The learner asked how to stop the node for a while.
No shutdown result has been shared yet.

Request a clean shutdown:

```sh
bitcoin-cli stop
```

The reply `Bitcoin Core stopping` means shutdown has started.
Wait for the process to exit before restarting it or turning off the computer.
Check whether it is still running:

```sh
pgrep -x bitcoind
```

No output means there is no running process named `bitcoind`.
To resume later, use the same data folder and settings:

```sh
bitcoind -daemon
```

The node resumes from its saved progress.
The assistant did not run these stop or start commands.

## API and Python examples

The learner used both `bitcoin-cli` and a JSON-RPC request with `curl`.
The successful request used the node's local authentication cookie.
The cookie value is not saved here.

- Python version shown: 3.15.0.
- Virtual environment: `~/.venvs/bitcoin-learning`.
- Installed library: `python-bitcoinlib` 0.12.2.
- Import check output: `Library loaded`.

[Library source](https://github.com/petertodd/python-bitcoinlib).

The shared output from `rpc_example.py` was `256079`.
This was the node's block height at that time.

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
- JSON-RPC and reading node status.
- Transaction inputs, output references and output values.
- Public keys, private keys and addresses.
- Random key generation and the private key range.
- Signatures, repeated transactions and spending an output once.

These entries record discussion topics, not completed assessments.
The learner paused Chapter 4 because the concepts still needed more explanation.
