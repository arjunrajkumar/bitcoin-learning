# Bank accounts and Bitcoin spending conditions

[MIT notes and exercises](../README.md)

Shared on 22 October 2026.

## Arjun's understanding

Wording preserved. Typing edit: “satisy” changed to “satisfy”.

> In a bank, if I have 100 dollars, there is some database in the bank which has 100 dollars associated with my name. So when I send 50 dollars to someone else, the bank checks under my name to see if I have 100 dollars, then sends 50 dollars of that to someone else, updates my balance as 50. So the bank has some record in their database saying that I have 50 dollars to my name.
>
> In Bitcoin, there is no identity. There is no me or someone else. All there is, is a record that 100 Bitcoins can be spent by anyone who can satisfy a certain condition. There are no accounts. There are no identities. It's just a record that says anyone who can satisfy this condition can spend this 100 Bitcoins. So if I can prove that I can satisfy the condition, then I can spend it. I can send 30 Bitcoins to someone else. So now there are still 100 Bitcoins, but the 100 bitcoin with one spending rule before is now converted into two. Anyone who can satisfy the condition requires for the 30 bitcoins can spend the 30 Bitcoins, and anyone who can satisfy the condition for the remaining 70 Bitcoins can spend the 70 bitcoins.
>
> It takes a little to get used to the idea that there is no identity or account. Each record (transactions) is simply stating that they have X number of Bitcoins, and if you can satisfy this condition, you can spend it.

## AI reply

The main idea is correct. The record with an amount and a spending condition is
a **transaction output**. While it remains unspent, it is a **UTXO: Unspent
Transaction Output**. A transaction spends existing outputs and creates new ones.
Your wallet calculates a balance from the relevant unspent outputs.
See the [Bitcoin transaction guide](https://developer.bitcoin.org/devguide/transactions.html#introduction).

The original 100 BTC output is spent in full. It cannot be spent again.
Its history remains on the blockchain. Your 30 BTC and 70 BTC example works
when fees are ignored. The 70 BTC is a new output called **change**.
With a fee, the amounts must satisfy `100 BTC = 30 BTC payment + change + fee`.
See [Bitcoin: transaction fees and change](https://developer.bitcoin.org/devguide/transactions.html#transaction-fees-and-change).

Bitcoin's spending rules do not require a person's name. Outside information can
still link transactions to people. This does not imply complete anonymity.
See [Bitcoin: avoiding key reuse](https://developer.bitcoin.org/devguide/transactions.html#avoiding-key-reuse).
