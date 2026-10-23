# MIT Cryptocurrency Engineering and Design

[Plan](../README.md) · [MIT material](https://ocw.mit.edu/courses/mas-s62-cryptocurrency-engineering-and-design-spring-2018/) · [Original code](https://github.com/mit-dci/mas.s62)

Notes, exercises and experiments for MAS.S62, Spring 2018, belong here.
The lecturers are Neha Narula and Tadge Dryja.

## Current plan

- [x] Lecture 1
- [x] Lecture 2
- [x] Lecture 3
- [ ] Lecture 4
- [ ] Lecture 5
- [ ] Lecture 6

[Lecture videos](https://ocw.mit.edu/courses/mas-s62-cryptocurrency-engineering-and-design-spring-2018/video_galleries/lecture-videos/) · [Reading and lecture order](https://ocw.mit.edu/courses/mas-s62-cryptocurrency-engineering-and-design-spring-2018/pages/calendar/)

Arjun confirmed completion of lectures 1, 2 and 3 on 22 October 2026.
The immediate plan is lectures 1–6, then Mastering Bitcoin.
The saved problem sets remain available for practice.

## Notes

- [Bits, bytes, hexadecimal and ASCII](notes/bits-bytes-hex-and-ascii.md) — handwritten notes and SHA-256 questions, 22 October 2026.
- [Lecture 3 — Merkle trees, elliptic curves and signatures](notes/lecture-03.md) — understanding, clarification and open questions, 22 October 2026.
- [Bank accounts and Bitcoin spending conditions](notes/transactions-and-spending-conditions.md) — personal understanding and AI reply, 22 October 2026.
- [Transaction inputs and outputs](notes/transaction-inputs-and-outputs.md) — personal understanding and AI corrections on field sizes, signatures and blockchain storage, 23 October 2026.

## Daily reviews

- [23 October 2026](reviews/2026-10-23.md) — completed; questions, Arjun's answers and AI feedback on double spending, change, hexadecimal digits, Merkle proofs and keys.

## Exercises and projects

| Work | Status |
| --- | --- |
| [Problem set 1 — Hash-based signature schemes](pset01/README.md) | Implementation complete; all five original tests passed on 23 October 2026 |
| [Problem set 2 — Mine your name](pset02/README.md) | Not started |
| [Problem set 3 — UTXOhunt](pset03/README.md) | Not started |
| [Final project](final-project/README.md) | Not started; topic not selected |

Save lecture notes by lecture number when there are notes to keep.
Keep code, explanations and command output in the relevant problem-set folder.

## Setup record

On 2026-10-21, the shared terminal image showed that Homebrew installed Go 1.27.3.
On 2026-10-23, Arjun shared `go version go1.27.3 darwin/arm64`.
He implemented the three signature functions in problem set 1 with guidance.
He supplied passing results for all four signature tests.
The [problem set 1 record](pset01/README.md) separates learner work from the
code completed by Codex at his request.

The starter code's source revision is recorded in [SOURCE.md](SOURCE.md).
Problem set 1 setup fixes are recorded in [SETUP.md](pset01/SETUP.md).
The problem set 2 and 3 starter files have not been built or tested here.
The 2018 instructions need checks before use with current software.
Problem set 2 refers to an old class server.
Problem set 3 uses old Go library paths and Bitcoin test-network instructions.
Its example key phrases are public teaching data.

The downloaded reference pages remain in
`/Users/arjunrajkumar/Downloads/mas.s62-spring-2018`.
That local folder is not part of this repository.
