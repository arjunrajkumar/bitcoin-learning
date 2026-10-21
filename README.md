# Bitcoin learning

My record of learning how Bitcoin works and learning to build with it.
The work is grouped by content. Start with Bitshala's Mastering Bitcoin course.

| Learning resource and questions | Test 1 result | Test 2 result — after a gap | Test 3 result — after another gap |
| --- | --- | --- | --- |
| [Mastering Bitcoin — Introduction & how Bitcoin works](courses/bitshala-mastering-bitcoin/introduction-and-how-bitcoin-works/questions.md) | [2/8 correct; 6 partial; 0 incorrect; 0 unanswered](courses/bitshala-mastering-bitcoin/introduction-and-how-bitcoin-works/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/introduction-and-how-bitcoin-works/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/introduction-and-how-bitcoin-works/test-3.md) |
| [Mastering Bitcoin — Bitcoin Core, keys & addresses](courses/bitshala-mastering-bitcoin/bitcoin-core-keys-and-addresses/questions.md) | [Not started](courses/bitshala-mastering-bitcoin/bitcoin-core-keys-and-addresses/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/bitcoin-core-keys-and-addresses/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/bitcoin-core-keys-and-addresses/test-3.md) |
| [Mastering Bitcoin — Wallet recovery & transactions](courses/bitshala-mastering-bitcoin/wallet-recovery-and-transactions/questions.md) | [Not started](courses/bitshala-mastering-bitcoin/wallet-recovery-and-transactions/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/wallet-recovery-and-transactions/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/wallet-recovery-and-transactions/test-3.md) |
| [Mastering Bitcoin — Scripts & digital signatures](courses/bitshala-mastering-bitcoin/scripts-and-digital-signatures/questions.md) | [Not started](courses/bitshala-mastering-bitcoin/scripts-and-digital-signatures/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/scripts-and-digital-signatures/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/scripts-and-digital-signatures/test-3.md) |
| [Mastering Bitcoin — Transaction fees & the Bitcoin network](courses/bitshala-mastering-bitcoin/transaction-fees-and-the-network/questions.md) | [Not started](courses/bitshala-mastering-bitcoin/transaction-fees-and-the-network/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/transaction-fees-and-the-network/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/transaction-fees-and-the-network/test-3.md) |
| [Mastering Bitcoin — Blockchain, mining & consensus](courses/bitshala-mastering-bitcoin/blockchain-mining-and-consensus/questions.md) | [Not started](courses/bitshala-mastering-bitcoin/blockchain-mining-and-consensus/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/blockchain-mining-and-consensus/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/blockchain-mining-and-consensus/test-3.md) |
| [Mastering Bitcoin — Security & second-layer applications](courses/bitshala-mastering-bitcoin/security-and-second-layer-applications/questions.md) | [Not started](courses/bitshala-mastering-bitcoin/security-and-second-layer-applications/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/security-and-second-layer-applications/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/security-and-second-layer-applications/test-3.md) |
| [Mastering Bitcoin — Sparrow wallet practice](courses/bitshala-mastering-bitcoin/sparrow-wallet-practice/questions.md) | [Not started](courses/bitshala-mastering-bitcoin/sparrow-wallet-practice/test-1.md) | [Not started](courses/bitshala-mastering-bitcoin/sparrow-wallet-practice/test-2.md) | [Not started](courses/bitshala-mastering-bitcoin/sparrow-wallet-practice/test-3.md) |

Click a topic to open its questions. Click a test result to open my answers,
the review, and my corrections. Introduction Test 1 and its corrections have
been reviewed. On 2026-10-20, the learner chose to move on to the next topic.
The remaining Q4 and Q8 review points stay recorded in Test 1 for later.

Results use **fully correct / total questions**. Partial, incorrect and
unanswered counts are reported separately. Scores are personal review results,
not Bitshala grades. Corrections do not change an original attempt score.

On 2026-10-21, the learner paused Chapter 4 to build the foundations with MIT's
Cryptocurrency Engineering and Design course. The Bitshala Bitcoin Core,
keys & addresses test has not started.
Return to the [assigned reading](courses/bitshala-mastering-bitcoin/bitcoin-core-keys-and-addresses/questions.md#reading)
when ready.

## MIT — Cryptocurrency Engineering and Design

[Course material and current position](courses/mit-cryptocurrency-engineering/README.md).
Use this same private repository for the Go exercises.
The original starter files are saved. No MIT attempts have been submitted.

| Content | Status |
| --- | --- |
| [Problem set 1 — Hash-based signature schemes](courses/mit-cryptocurrency-engineering/pset01/README.md) | Not started |
| [Problem set 2 — Mine your name](courses/mit-cryptocurrency-engineering/pset02/README.md) | Not started |
| [Problem set 3 — UTXOhunt](courses/mit-cryptocurrency-engineering/pset03/README.md) | Not started |
| [Final project](courses/mit-cryptocurrency-engineering/final-project/README.md) | Not started; topic not selected |

Next setup step: run `go version` and share the output.
Homebrew's completion message for Go 1.27.3 was shown on 2026-10-21.
The course code has not been built or tested with this version.

## How I use this record

For Bitshala topic tests:

1. Read a small section and study examples.
2. Answer all topic questions in one batch from memory. Record confidence and help used.
3. Submit the full batch for review. Allow spelling fixes only in the saved answers.
4. Write a corrected explanation in my own words.
5. Return after a gap and answer again with earlier answers and reviews closed.
6. Apply the idea to a fresh example when useful.

Each test keeps all answers together. Assistant feedback is at the end.
Each review gives only **Outcome**, **Why**, and **Read again**.
Reading links point to the main matching section in the assigned material.
Book links use the rendered `develop` chapter and its section heading.
Factual corrections stay separate from the original answers.

There are no fixed weekly deadlines. Tests 2 and 3 are later memory attempts.
Three attempts are a starting point; unresolved gaps can need more practice.
[Review method and scoring](learning-method.md) explains how results are recorded.

For MIT, write the code attempts and explanations in the relevant problem-set
folder. Keep command results and help used with that work. Review each assignment
against its full source prompt. These coding assignments have separate progress
records and do not change Bitshala test scores.

Save source code, diagrams and command results in the topic's `experiments/`
folder when there is work to keep. Commit and push local work before changing
devices. This repository is private.

## Use this project in Codex

Add the local `bitcoin-learning` repository folder as a Codex project. Make it
the primary folder. Start learning chats inside that project.

The project instructions are in [AGENTS.md](AGENTS.md). The review and scoring
rules are in [learning-method.md](learning-method.md). Codex uses the primary
folder to find repository instructions. A synced conversation does not transfer
the local repository to a second laptop.
[Official OpenAI project guidance](https://learn.chatgpt.com/docs/projects#use-local-projects-for-folders-and-codebases)
explains these boundaries.

Use a separate local checkout on each laptop. Push completed work before
switching laptops. On the next laptop, inspect local changes and fetch the
latest version before continuing. Preserve and resolve any conflicts.

### Copy into Codex on another laptop

```text
Set up my Bitcoin learning workspace on this laptop.

Use my existing private repository:
https://github.com/arjunrajkumar/bitcoin-learning

Reuse an existing checkout of this repository if present. Otherwise clone it
into a suitable local folder. Do not create a new GitHub repository or overwrite
an existing folder. Add the checkout as a local Codex project named
bitcoin-learning if the app tools support it. Otherwise give me the exact folder
to add manually. The repository folder must be the project's primary folder.

Read AGENTS.md, README.md and learning-method.md before teaching or editing.
Follow those files and use the saved topic attempts to find my current position.

I know Ruby and Rails well. I am learning Bitcoin fundamentals through Bitshala's
Mastering Bitcoin course. My goal is to understand Bitcoin deeply and build with
it. Organise learning by content. Use three attempts per topic: a first attempt
after reading, then two later attempts from memory after gaps. No fixed weekly
deadlines are needed.

I write the answers, predictions, code attempts and corrected explanations.
Present all topic questions in one batch. Include full prompts and all subparts.
Wait for my full submission before giving feedback. Keep my answers in full.
Correct only clear spelling and typing errors. Keep my wording and meaning.
For each question, give only Outcome, Why, and Read again.
Link to the main matching section in the assigned reading.
For Mastering Bitcoin, use rendered develop-branch links with section headings.
Do not use commit hashes, plain source view or line numbers in reading links.
Use no other reading sources. State when those materials do not cover a point.
Do not explain the correct answer unless I ask.
Do not fill in my answers or invent progress.

Keep all my answers together at the start of the relevant test file.
Keep my corrections in a separate section. Put all your feedback at the end.
Update the README with fully correct / total only after review is complete.
Show partial answers separately. Corrections do not change the original score.
Follow the full scoring rules in learning-method.md.

Check Git status and remote changes before editing. Preserve local work.
Never force-push or discard answers. When I ask you to save learning work,
review the scoped diff, commit and push it to this repository. Tell me whether
the push succeeded. Keep secrets and private account data out of this private repo.

Use short, clear English. Handle routine repository setup without assigning me
Bitcoin exercises. Finish setup by showing my current topic and next action.
Do not start a quiz until I ask.
```
