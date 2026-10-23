# Transaction inputs and outputs

[MIT notes and exercises](../README.md) · [Earlier note on spending conditions](transactions-and-spending-conditions.md)

Shared on 23 October 2026.

## Arjun's understanding

Original wording preserved, including the repeated statements about storage.
Corrections appear separately under **AI reply**.

> Transactions inputs and outputs. The transaction input has a transaction ID and the signature. The transaction ID will have the transaction hash, which is 32 bits, and will also have the output, the index of the output of the previous output. So that is a 4-bit. So in total it's 36 bits. The transaction ID part is 36 bits. Of this 4-bit, that means you can have options of 4 bits, which are around 4 billion options, which is actually an overkill because normally in Bitcoin transaction the output is maybe 100 outputs max. I mean, you could go more, but usually on the max side usually it's even lesser. So having 4 billion is an overkill. And then you also have the signature of your... which is required to match to spend that input, and that's around 100 bits. And the key thing to note is that the inputs are not stored on the blockchain. So the transaction ID, the inputs... sorry, the inputs are stored in the blockchain. Inputs are not stored in the blockchain. It's only the funds and the output condition to spend the fund. That's it. The inputs are evaluated by a wallet when you actually want to spend that fund. So let's look at actually what's stored in the blockchain, the output. The output has a script, which is around 25 bits, and an amount, which is 8 bits.

### Clarification after discussion

> the signature is stored, but the result of checking it is calculated by each node.

## AI reply

### Field sizes and names

One **byte** contains eight bits.
The sizes you gave mainly refer to bytes.
**P2PKH** means pay to public key hash.
It is one form of spending condition.

| Part | Bytes | Bits |
| --- | ---: | ---: |
| Previous transaction ID (`txid`) | 32 | 256 |
| Previous output index (`vout`) | 4 | 32 |
| These two fields together | 36 | 288 |
| Output amount | 8 | 64 |
| P2PKH output script | 25 | 200 |

An **outpoint** identifies one previous output.
It combines the transaction ID with the output index.
The transaction ID alone is 32 bytes.
The index starts at zero.
For example, `vout = 2` selects the third output of that transaction.

An input also contains a script-length field, a signature script and a 4-byte sequence field.
The sequence field supports additional spending rules.
Thus, 36 bytes is only the outpoint size.

The P2PKH output script is 25 bytes long.
Other script types have different sizes.
An output also stores its script length.
The amount is in **satoshis**: one satoshi is 0.00000001 BTC.
See the [Bitcoin transaction format](https://developer.bitcoin.org/reference/transactions.html#raw-transaction-format).

### Index capacity

Four bits allow `2⁴ = 16` values.
Four bytes allow `2³² = 4,294,967,296` values.
The index field has more capacity than a transaction can use.
This does not allow four billion actual outputs.
There is no fixed limit of 100 outputs per transaction.
Block capacity limits how many outputs can fit.
Bitcoin measures this capacity with **block weight**, a size measure that gives different costs to different data.
See [BIP 141: block size](https://bips.dev/141/#block-size).

### Signatures and storage

The signature is not a fixed 100-bit field.
For P2PKH, the signature script includes a signature and a public key.
The public key's hash must match the hash in the previous output.
The signature must pass a check with that public key and the required transaction data.
See the [Bitcoin guide: spending an output](https://developer.bitcoin.org/devguide/transactions.html#introduction).

**Confirmed transactions contain both inputs and outputs in the blockchain.**
An output does not contain its future spending input.
That input is created in a later transaction.
The wallet builds and signs the spending transaction.
Full nodes also check its inputs and spending conditions.

The signature checked by a node is stored in the confirmed spending transaction.
Each node calculates the result of the check itself.
The blockchain does not store a separate “signature valid” field.
See the [Bitcoin guide: signature checks](https://developer.bitcoin.org/devguide/transactions.html#p2pkh-script-validation).

The **UTXO set** is the current collection of unspent transaction outputs.
It is separate from the full transaction history.
An entry identifies an unspent output and records its amount and spending script.
When that output is spent, it leaves the UTXO set.
The original transaction and the spending transaction remain in the blockchain history.
See the [Bitcoin transaction guide](https://developer.bitcoin.org/devguide/transactions.html#introduction).

**SegWit**, short for Segregated Witness, changes where spending proof is stored within a transaction.
Its **witness** is the separate field for that proof, such as signatures.
Witness data is included in blocks too.
See [BIP 141: transaction format](https://bips.dev/141/#transaction-id).
