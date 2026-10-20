# Introduction & how Bitcoin works — Test 1

[Questions](questions.md) · [Learning results](../../../README.md)

- Status: Corrections reviewed; Q2 typo clarified; Q4 needs revision; Q8 needs verification
- Started: 2026-10-20
- Submitted and reviewed: 2026-10-20
- Corrections submitted and reviewed: 2026-10-20
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

Submitted on 2026-10-20 for Q1, Q2, Q3, Q4, Q7 and Q8.
Only clear spelling, typing, punctuation and spacing errors have been corrected.
The learner did not report confidence or help used for these corrections.
These corrections belong to Test 1. They do not change its original score.

### Q1 correction

They were dependent on a central organisation to issue new money, and also to validate transactions between people. There was no distributed system, and hence any government or organisation could kill the digital currency by attacking that central source. Also, double spending could only be stopped before Bitcoin with a central authority verifying the payments. Bitcoin solves this with a combination of a public blockchain (list all past transactions), peer to peer network of nodes (decentralised, no single authority) that verifies every transaction according to set of rules, and a proof-of-work algorithm that solves double spending via a method of reaching a global decentralised consensus.

### Q2 correction

There are some advantages and disadvantages with reversibility. Current electronic payment methods like credit cards, net banking etc. are reversible. So someone could buy Bitcoin from you via a credit card, and then reverse the credit card payment after they received the Bitcoin. So, because bitcoins are reversible this risk is there. To solve this risk, lots of exchanges require KYC, and do credit checks. Also if something is reversible, a fraudulent seller would not benefit, as the buyer can reverse it. Bitcoin has these drawbacks. But Bitcoin would not be better if transactions are reversible because then you need someone to decide which transaction, the conditions etc. for reversibility etc. Also, the public blockchain would require additional changes from what it is.

#### Q2 typo clarification — 2026-10-20

The learner confirmed that "reversible" was a typo for "irreversible".
The full resubmitted answer follows. This is part of the same Test 1 correction.

There are some advantages and disadvantages with reversibility. Current electronic payment methods like credit cards, net banking etc. are reversible. So someone could buy Bitcoin from you via a credit card, and then reverse the credit card payment after they received the Bitcoin. So, because bitcoins are irreversible this risk is there. To solve this risk, lots of exchanges require KYC, and do credit checks. Also if something is reversible, a fraudulent seller would not benefit, as the buyer can reverse it. Bitcoin has these drawbacks. But Bitcoin would not be better if transactions are reversible because then you need someone to decide which transaction, the conditions etc. for reversibility etc. Also, the public blockchain would require additional changes from what it is.

### Q3 correction

The Bitcoin issuance rate is the rate of bitcoins given to a miner when their candidate block is included to the blockchain, after they complete the proof of work. Initially it started with 50 bitcoins per new block that was mined, and this reduces every 4 years by half, until it becomes 0. A block is mined approximately around every 10 minutes, which makes it roughly **210,000 blocks every 4 years**. All this would work out to around 21 million bitcoin in total: 210000 \* (50 + 25 + 12.5 ... ) \~= 21 million

### Q4 correction

Bitcoin is not private in the sense that every transaction is publicly viewable by one who looks into the blockchain. Anyone can view the amount of bitcoins that a transaction transferred to another bitcoin address. These days most bitcoin exchanges require KYC, and therefore it is possible to identify the person associated to an address. Hence, if a user withdraws bitcoin via an exchange to convert bitcoin into currency like a dollar, their identity will be exposed to that company, and from there, one can know the amount of bitcoins associated with that specific address. Bitcoin is not fungible because one bitcoin is not equivalent to any other bitcoin. For e.g. someone who has access to a stolen bitcoin address, could be barred from spending that specific bitcoin on exchanges.

### Q5 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q6 correction

<!-- Learner: explain in your own words. Say what changed and why. This is not a new test attempt. -->

### Q7 correction

The first confirmation is when a miner includes the transaction in their candidate block, and after completion of proof-of-work, includes their candidate block into the blockchain. As more and more blocks are confirmed above it, the confirmations increase. Usually, 6 confirmations are acceptable. It is better to not accept unconfirmed transactions because the transaction has not yet been included into the blockchain which means a fraudulent person could double spend - or make another transaction with that same bitcoin to another address, and if that is included first in a valid blockchain, it has the higher likelihood of being considered as true as more and more blocks are built on it.

### Q8 correction

Transactions are a chain of digital signatures, because each transaction's input is made of an output from an earlier transaction. So, it is a chain of transactions in that sense. UTXO stands for unspent transaction outputs. It's basically all the outputs from confirmed transactions that have not yet been spent. Bitcoin chose UTXO model because with the UTXO model one only need to sign a digital signature associated to that transaction to spend it. There is no need to have an account model - and then have to store all the transactions that belong to that account etc. Here there is no identity required.

## Extra practice

<!-- Optional: a fresh question, prediction, diagram, code or command result.
Keep these results separate from the repeated-question score. -->

## Questions for the cohort

<!-- Record any unresolved questions to discuss with Bitshala. -->

## Assistant feedback

**Result:** 2/8 correct; 6 partial; 0 incorrect; 0 unanswered

### Q1 feedback

Outcome: Partial

Why: You identify central control, but do not explain how Bitcoin solved the problems.
The double-spending problem is also missing.

Read again: [Chapter 1 — Introduction](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#introduction);
[Chapter 1 — History of Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#history-of-bitcoin).

### Q2 feedback

Outcome: Partial

Why: You discuss drawbacks of reversibility, but omit its potential benefits.
Your confirmation requirement is too absolute. The reading describes the seller
risk and warns about mistakes; it does not give a full list of buyer protections.

Read again: [Chapter 1 — Getting Your First Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#getting-your-first-bitcoin);
[Chapter 1 — Sending and Receiving Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#sending-and-receiving-bitcoin);
[Chapter 2 — Bitcoin Mining](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#bitcoin-mining).

### Q3 feedback

Outcome: Partial

Why: You describe falling issuance, but do not state how much it falls.
You state the supply cap without showing how the schedule gives that total.

Read again: [Chapter 1 — Introduction](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#introduction).

### Q4 feedback

Outcome: Partial

Why: You identify public transaction data and identity links, but do not explain
why privacy matters. The assigned chapters do not define fungibility, so the
links below support only the privacy part of this question.

Read again: [Chapter 1 — Bitcoin Addresses](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#bitcoin-addresses);
[Chapter 1 — Getting Your First Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#getting-your-first-bitcoin).

### Q5 feedback

Outcome: Correct

Why: You give the fee calculation, identify who receives it, and describe its
general effect on confirmation at the level used in Chapter 1.

Read again: [Chapter 2 — Transaction Inputs and Outputs](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#transaction-inputs-and-outputs);
[Chapter 1 — Sending and Receiving Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#sending-and-receiving-bitcoin).

### Q6 feedback

Outcome: Correct

Why: You cover the purpose of change, when it is needed, and the effect of omitting
it. Your stated condition also covers when no change is needed.

Read again: [Chapter 2 — Making Change](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#making-change);
[Chapter 2 — Coin Selection](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#coin-selection);
[Chapter 2 — Transaction Inputs and Outputs](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#transaction-inputs-and-outputs).

### Q7 feedback

Outcome: Partial

Why: You count confirmations correctly. You do not explain the risk of accepting
an unconfirmed payment. Your reason only repeats that it is unconfirmed.

Read again: [Chapter 1 — Sending and Receiving Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#sending-and-receiving-bitcoin);
[Chapter 2 — Bitcoin Mining](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#bitcoin-mining).

### Q8 feedback

Outcome: Partial

Why: You identify spending permission and unspent outputs, but do not explain
how transactions link together. The account-model comparison is missing.
The assigned chapters describe UTXOs, but do not cover that comparison or
establish the historical reasons for choosing the model.

Read again: [Chapter 2 — Transaction Inputs and Outputs](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#transaction-inputs-and-outputs);
[Chapter 2 — Transaction Chains](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#transaction-chains);
[Chapter 2 — Getting the Right Inputs](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#getting-the-right-inputs).

### Correction review — 2026-10-20

This review covers the six submitted corrections above.
The original Test 1 result remains **2/8 correct; 6 partial; 0 incorrect; 0 unanswered**.
These corrections are not a new memory test.
The Q2 review below predates the learner's typo clarification.
See the [latest Q2 review](#q2-typo-clarification-review--2026-10-20).

#### Q1 correction feedback

Outcome: Correct

Why: You now explain central control, double spending, and how Bitcoin addresses them.

Read again: [Chapter 1 — Introduction](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#introduction);
[Chapter 1 — History of Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#history-of-bitcoin).

#### Q2 correction feedback

Outcome: Partial

Why: You now discuss benefits and drawbacks. Your claim that "bitcoins are reversible"
conflicts with the assigned reading.

Read again: [Chapter 1 — Getting Your First Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#getting-your-first-bitcoin).

#### Q3 correction feedback

Outcome: Correct

Why: You now state the halving rate and show how the supply total follows.

Read again: [Chapter 1 — Introduction](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#introduction).

#### Q4 correction feedback

Outcome: Partial

Why: You still omit why privacy matters. Chapters 1 and 2 do not establish the
question's claim about fungibility or your example.

Read again: [Chapter 1 — Bitcoin Addresses](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#bitcoin-addresses);
[Chapter 1 — Getting Your First Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#getting-your-first-bitcoin).

#### Q7 correction feedback

Outcome: Correct

Why: You explain confirmation counts and now identify the risk of accepting
an unconfirmed payment.

Read again: [Chapter 2 — Bitcoin Mining](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#bitcoin-mining).

#### Q8 correction feedback

Outcome: Needs verification

Why: You now explain the transaction links and UTXOs. The assigned chapters do
not compare account models or support your reasons for Bitcoin's choice.

Read again: [Chapter 2 — Transaction Chains](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#transaction-chains);
[Chapter 2 — Getting the Right Inputs](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch02_overview.adoc#getting-the-right-inputs).

### Q2 typo clarification review — 2026-10-20

Outcome: Correct

Why: Your typo clarification resolves the issue in the earlier review.
Your answer covers benefits, drawbacks, and your reasons for opposing reversibility.

Read again: [Chapter 1 — Getting Your First Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch01_intro.adoc#getting-your-first-bitcoin).
