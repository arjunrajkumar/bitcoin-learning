# Introduction & how Bitcoin works — Test 1

[Questions](questions.md) · [Learning results](../../../README.md)

- Status: Reviewed; learner corrections pending
- Started: 2026-10-20
- Submitted and reviewed: 2026-10-20
- Confidence: Medium/high for the full submission, as reported.
- Help used while answering: None, as reported.
- Gap since the previous attempt: Not applicable


All 8 numbered questions count towards this attempt.
The learner requested batch questions and feedback after the full submission.
All answers are kept in full. Only clear typing errors have been corrected.
The earlier Q1 submission and its batch version belong to the same attempt.

The learner's statement for the full submission, with spelling corrected:

> No help used. Medium/high confidence.

## My answers

### Q1

**Source prompt:** What were the major problems of Digital Currencies before Bitcoin? How did Bitcoin solve them?

Major problems of digital currencies before bitcoin

1. They were dependent on a central organisation to issue new money, and also to validate transactions between people. There was no distributed system, and hence any government or organisation could kill the digital currency by attacking that central source.
2. They were usually backed by gold or other forms of money.

No help used. Medium/high confidence.

- Confidence: Medium/high (as reported above).
- Help used: None while answering (as reported above).

#### Q1 wording in the full submission

- They were dependent on a central organisation to issue new money, and also to validate transactions between people. There was no distributed system, and hence any government or organisation could kill the digital currency by attacking that central source. They were usually backed by gold or other forms of money.

This is the learner's batch version of the same answer, not a new attempt.

### Q2

**Source prompt:** Do you think it would be better if bitcoin transactions were reversible? What are the potential benefits and drawbacks?

- It would be worse if transactions are reversible because then you need someone to decide which transaction, the conditions etc for reversibility. Any fraudulent buyer can reverse the transaction after they receive the goods. The benefits of bitcoin transactions being irreversible is that once the transactions are included in the blockchain, it requires more effort to reverse. The drawbacks are that a seller has to wait for around 6 confirmations to be confident that the transaction went through. There it is not as instantaneous as exchanging cash.

- Confidence: Medium/high (reported for the full submission).
- Help used: None while answering (reported for the full submission).

### Q3

**Source prompt:** What is the Bitcoin Issuance Rate? How do we know the supply cap of Bitcoin is 21 million?

- The Bitcoin issuance rate is the rate of bitcoins given to a miner when their candidate block is included to the blockchain, after they complete the proof of work. Initially it started with 50 bitcoins per new block that was mined, and this reduces every 4 years, until it becomes 0. A block is mined approximately around every 10 minutes. All this would work out to around 21 million bitcoin in total after which a new block would only get the fees from transactions included in the block.

- Confidence: Medium/high (reported for the full submission).
- Help used: None while answering (reported for the full submission).

### Q4

**Source prompt:** Is Bitcoin private? Does Bitcoin need to be private? Why isn't Bitcoin fungible?

- Bitcoin is not private in the sense that every transaction is publicly viewable by one who looks into the blockchain. Anyone can view the amount of bitcoins that a transaction transferred to another bitcoin address. These days most bitcoin exchanges require KYC, and therefore it is possible to identify the person associated to an address. Hence, if a user withdraws bitcoin via an exchange to convert bitcoin into currency like a dollar, their identity will be exposed. From there, one can know the amount of bitcoins associated with that address. Bitcoin is not fungible because each bitcoin in a transaction requires a valid signature (related to the bitcoin address) to unlock that bitcoin in that address.

- Confidence: Medium/high (reported for the full submission).
- Help used: None while answering (reported for the full submission).

### Q5

**Source prompt:** What is a transaction fee? How is it calculated? What's the effect of transaction fee on transaction confirmation?

- A transaction fee is the difference between the total inputs value and the total output value. The fee goes to the miner that solves the proof of work, and is implied in the transaction in their candidate block. It is the difference and is only implied in the block. Usually, higher the fees, the greater the chance of getting included by a miner in their candidate block.

- Confidence: Medium/high (reported for the full submission).
- Help used: None while answering (reported for the full submission).

### Q6

**Source prompt:** What are change addresses? When are change addresses required? What happens if the user (or wallet software) forgets to include the change address in a transaction? When will we not require a change address?

- Change addresses are the addresses that take the remaining payment that has to be sent back to the sender. They are required when the sender's inputs are greater than the receiver's payment amount and the fee. The remaining balance after the payment amount and the fee is the change amount, which is sent back to the change address. If the user or wallet forgets to include the change address, then all of the balance money (that is the money remaining after subtracting payment to receiver), will be included as fees to the miner.

- Confidence: Medium/high (reported for the full submission).
- Help used: None while answering (reported for the full submission).

### Q7

**Source prompt:** What does it mean by a transaction to be "confirmed"? How many confirmation is usually acceptable? Is it okay to accept unconfirmed transactions? Why or why not?

The first confirmation is when a miner includes the transaction in their candidate block, and after completion of proof-of-work, includes their candidate block into the blockchain. As more and more blocks are confirmed above it, the confirmations increase. Usually, 6 confirmations are acceptable. It is better to not accept unconfirmed transactions because the transaction has not yet been included into the blockchain.

- Confidence: Medium/high (reported for the full submission).
- Help used: None while answering (reported for the full submission).

### Q8

**Source prompt:** Why did Satoshi said transactions are "chain of digital signatures"? What is a UTXO? Whats the difference between UTXO and Account based model? Why did Bitcoin choose to stick with UTXO model?

Transactions are a chain of digital signatures, because only someone who can sign a digital signature associated with that transaction's bitcoin address can use the funds. UTXO stands for unspent transaction outputs. It's basically all the outputs from confirmed transactions that have not yet been spent. Bitcoin chose UTXO model because each transaction is included in the blockchain, and Bitcoin provides a decentralised way to verify and spend those transactions.

- Confidence: Medium/high (reported for the full submission).
- Help used: None while answering (reported for the full submission).

## My corrections

### Q1 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q2 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q3 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q4 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q5 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q6 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q7 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q8 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

## Extra practice

<!-- Optional: a fresh question, prediction, diagram, code or command result.
Keep these results separate from the repeated-question score. -->

## Questions for the cohort

<!-- Record any unresolved questions to discuss with Bitshala. -->

## Assistant feedback

**Result:** 2/8 correct; 6 partial; 0 incorrect; 0 unanswered

The review compares all subparts with the prompts in [questions.md](questions.md).
It uses Chapters 1 and 2 at book revision
`275c4eb8eab8800c6adc39f8def8e8f8fa356a57`.
Other primary sources support details beyond those chapters.
Spelling is not scored. Spelling edits and learner corrections do not change
this attempt's original score.

### Q1 feedback

Outcome: Partial

**Assistant review:** You identify the central operator and its failure risk.
The book also describes backing by gold or national currency. Backing itself
is not necessarily a fault. It creates reliance on the issuer and its reserves.

The answer does not explain how Bitcoin solves these problems. It also omits
double spending: trying to spend the same funds twice. A distributed system
uses several computers. Those computers can still have one controlling owner.
The key issue here is central control.

**Assistant explanation:** Digital signatures prove permission to spend.
Full nodes independently check transactions and the rules for new coins.
Nodes reject attempts to spend an already spent output in the same history.
Proof of work lets nodes select the valid chain with the most accumulated work.
This gives a shared transaction history without a central clearing company.
Bitcoin does not promise redemption for gold or national currency.

Sources: [Chapter 1, digital currencies before Bitcoin][book1-history];
[Chapter 2, Bitcoin Mining][book2-mining];
[Bitcoin white paper, sections 2–5][whitepaper].

### Q2 feedback

Outcome: Partial

**Assistant review:** Your preference is defensible. You identify a risk to
sellers and the problem of deciding which payments to reverse. You also
recognise that more confirmations make a payment harder to remove.

The missing part is the benefit of reversibility. A dispute process could
help with a mistaken payment, theft, or goods that never arrive. A fraudulent
buyer could try to abuse it, but success would depend on that process.

**Assistant explanation:** Reversibility trades some seller certainty for
buyer protection. Bitcoin has no built-in authority that can order a chargeback.
A seller can still return funds through a new transaction. A change to which
valid chain a node follows is called a chain reorganisation. This is different
from a refund. Waiting reduces the risk of losing a payment through such a
change. Six confirmations is a convention, not a rule for every payment.
The key drawback of no chargebacks is the lack of a built-in remedy for mistakes
or fraud. Waiting is a separate settlement concern.

Sources: [Bitcoin white paper, section 1][whitepaper];
[Chapter 2, Bitcoin Mining][book2-mining];
[Developer Guide, Verifying Payment][confirmations].

### Q3 feedback

Outcome: Partial

**Assistant review:** You correctly recall the initial 50 BTC, the approximate
10-minute interval, the falling issuance, and the eventual reliance on fees.
You state the cap, but do not show why that schedule gives it. Saying the reward
reduces does not specify how much it reduces.

**Assistant explanation:** The block subsidy is the new bitcoin allowed in a
block. It halves every 210,000 blocks: 50, 25, 12.5 BTC, and so on. Four years is
an estimate for that number of blocks. Fees are separate from new issuance.

The ideal sum is:

```text
210,000 × (50 + 25 + 12.5 + ...) BTC
= 210,000 × 100 BTC
= 21,000,000 BTC
```

A satoshi is 0.00000001 BTC. The subsidy uses whole satoshis and rounds down at
each halving. Thus the schedule permits slightly less than 21 million BTC.
This is a limit under the consensus rules: the rules nodes use to accept blocks.
A miner cannot make compliant nodes accept an excessive subsidy merely by
finding valid proof of work.

Sources: [Chapter 1, issuance overview][book1-issuance];
[Bitcoin Core v29.0, subsidy calculation][core-subsidy];
[Bitcoin Core v29.0, mainnet halving interval][core-interval].

### Q4 feedback

Outcome: Partial

**Assistant review:** You correctly identify public transaction data and the
risk of linking an address to a person. Know Your Customer (KYC) checks give an
exchange identity information. They do not automatically publish that identity
to everyone. One linked address also need not reveal every fund a person owns.
You do not answer why privacy matters. The signature explanation of fungibility
is incorrect.

**Assistant explanation:** Fungibility means that equal amounts of a currency
can be accepted interchangeably. A signature proves permission to spend. It does
not determine whether recipients treat two equal amounts equally.

**Source premise:** “Why isn't Bitcoin fungible?” is too absolute. Bitcoin
accounts for value in the same units. Public transaction history can let a
recipient reject funds associated with unwanted activity. This can weaken
fungibility in practice. It is not a consequence of different signatures.

Privacy protects payment details, personal safety, and business information.
It also limits discrimination based on transaction history. The need for these
protections is a reasoned position, not a separate consensus rule.

Sources: [Chapter 1, privacy warning][book1-privacy];
[Gregory Maxwell, Confidential Transactions investigation][privacy];
[Chapter 2, Transaction Inputs and Outputs][book2-inputs].

### Q5 feedback

Outcome: Correct

**Assistant review:** You give the fee formula, identify the miner as its
recipient, and describe its general effect on inclusion. This covers the
question at the level used in Chapter 1. That chapter also uses the broad
“higher fee” description. Your word “usually” does not claim a guarantee.

**Assistant clarification:** The fee is implicit in each transaction. It can
be calculated before mining from its inputs and outputs. It does not first
exist when the transaction enters a block.

Chapter 2 gives a more precise selection rule: miners generally prioritise
fee rate. This is the fee per unit of transaction size. A virtual byte (vB)
is Bitcoin's size unit for this purpose. Fee rate is commonly measured in
satoshis per vB. For example:

```text
A: 2,000 satoshis / 200 vB = 10 sat/vB
B: 3,000 satoshis / 600 vB =  5 sat/vB
```

A offers more fee per unit of space despite paying a smaller total fee.
Increasing the fee for an otherwise unchanged transaction raises its fee rate.
Miner choices and competing transactions still affect confirmation time.
Fee preference is miner policy, not a consensus rule that forces an order.

Sources: [Chapter 1, Sending and Receiving Bitcoin][book1-fees];
[Chapter 2, Transaction Inputs and Outputs][book2-inputs];
[Chapter 2, miner selection by fee rate][book2-feerate].

### Q6 feedback

Outcome: Correct

**Assistant review:** You explain the purpose of change and when it is needed.
You also explain the consequence of omitting it. Your condition already covers
the last subpart: no change is needed when inputs equal the payment plus the
intended fee. A separate sentence was not required to earn credit.

**Assistant explanation:** An input spends a whole previous output. The
transaction returns any intended change through a new output controlled by the
sender. The change address tells the wallet where to send that output.
For example:

```text
Input: 100,000 satoshis
Payment: 60,000 satoshis
Intended fee: 1,000 satoshis
Change: 39,000 satoshis
```

If the only output pays 60,000 satoshis, the actual fee is 40,000 satoshis.
The network does not create change automatically. A fresh change address is a
privacy practice. It is not a consensus requirement to use a never-used address.

Sources: [Chapter 2, Making Change and Coin Selection][book2-change];
[Chapter 2, Transaction Inputs and Outputs][book2-inputs].

### Q7 feedback

Outcome: Partial

**Assistant review:** You correctly count the containing block as the first
confirmation. Each later block adds one. You also recall the six-confirmation
convention. Your reason for avoiding unconfirmed payments stops at their
status. It needs to explain the risk that follows from that status.

**Assistant explanation:** The containing block must be valid and part of the
chain the node follows. A miner's candidate alone gives no confirmation.
Before confirmation, a conflicting transaction can spend the same inputs and
confirm instead. The expected payment might never confirm.

A recipient can choose to accept this risk for a small payment. It is not a
consensus violation to accept an unconfirmed payment. For larger payments, the
recipient may require more confirmations. Six is a common convention, not a
universal requirement or a guarantee. The choice depends on the value and the
risk the recipient can bear.

Sources: [Chapter 2, Bitcoin Mining][book2-mining];
[Developer Guide, Verifying Payment][confirmations].

### Q8 feedback

Outcome: Partial

**Assistant review:** You connect signatures with permission to spend. Your
UTXO definition matches the confirmed outputs tracked in the chain's UTXO set.
The answer does not explain the links in the chain, the account model, or a
specific benefit of the UTXO model. Recording transactions in a blockchain does
not distinguish the two models.

**Assistant explanation:** A transaction input refers to a particular output
of an earlier transaction. For an ordinary signed payment, the spender signs
to authorise its use in a new transaction. Those references and authorisations
link successive transfers. Strictly, Satoshi described an electronic coin as
a chain of signatures. This is a simplified model of Bitcoin's more general
spending conditions.

A UTXO is one unspent transaction output. Spending it consumes the whole output
and creates new outputs. A wallet calculates its balance from outputs it can
spend. An account model stores a balance for each account and updates balances
when money moves. Account systems can also operate without one central owner.

The UTXO model makes each spending dependency explicit. Nodes can check that
an output exists, is unspent, and meets its spending conditions. Wallets can
use fresh addresses for new outputs. These are useful design properties.
They do not establish every historical reason for Satoshi's choice.

Unconfirmed transactions can also create outputs that later transactions spend.
Those outputs are not yet in the confirmed chain's UTXO set.

Sources: [Chapter 2, Transaction Chains and Making Change][book2-chains];
[Chapter 2, Getting the Right Inputs][book2-utxos];
[Bitcoin white paper, section 2][whitepaper];
[Ethereum documentation, account balances][accounts].

### Next action

Write corrections in your own words. Start with Q4 and Q8, where the main
concepts need work. Then complete the missing parts of Q1, Q2, Q3 and Q7.
Include what changed and why. Return to Test 2 after a gap with this review closed.

### Review sources

The book and Bitcoin Core links below use fixed revisions. Core v29.0 is used
to check the subsidy rule. It is not a claim about the latest release.
The Developer Guide is used for confirmation risk, not its older wallet or
network policy advice. The account comparison is supporting reading.

[book1-history]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch01_intro.adoc#L78-L96
[book1-issuance]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch01_intro.adoc#L35-L65
[book1-privacy]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch01_intro.adoc#L413-L429
[book1-fees]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch01_intro.adoc#L463-L474
[book2-inputs]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch02_overview.adoc#L159-L182
[book2-chains]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch02_overview.adoc#L184-L274
[book2-change]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch02_overview.adoc#L242-L290
[book2-utxos]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch02_overview.adoc#L335-L357
[book2-mining]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch02_overview.adoc#L447-L588
[book2-feerate]: https://github.com/bitcoinbook/bitcoinbook/blob/275c4eb8eab8800c6adc39f8def8e8f8fa356a57/ch02_overview.adoc#L508-L524
[core-subsidy]: https://github.com/bitcoin/bitcoin/blob/f490f5562d4b20857ef8d042c050763795fd43da/src/validation.cpp#L1940-L1951
[core-interval]: https://github.com/bitcoin/bitcoin/blob/f490f5562d4b20857ef8d042c050763795fd43da/src/kernel/chainparams.cpp#L81-L89
[whitepaper]: https://bitcoin.org/bitcoin.pdf
[confirmations]: https://developer.bitcoin.org/devguide/payment_processing.html#verifying-payment
[privacy]: https://elementsproject.org/features/confidential-transactions/investigation
[accounts]: https://ethereum.org/developers/docs/accounts/#an-account-examined
