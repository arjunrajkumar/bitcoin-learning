# Problem set 1 — Hash-based signature schemes

[MIT record](../README.md) · [Full MIT prompt](https://ocw.mit.edu/courses/mas-s62-cryptocurrency-engineering-and-design-spring-2018/pages/assignments/pset1-hash-based-signature-schemes/) · [Original instructions](https://github.com/mit-dci/mas.s62/tree/master/pset01)

**Status:** Implementation complete. All five original tests passed on 23 October 2026.

This exercise uses Lamport signatures.
A Lamport signature is a signature scheme built from hash functions.
It is a teaching example, not Bitcoin's transaction signature scheme.

The assignment has two parts:

1. Implement key generation, signing and signature checks.
2. Use the supplied examples to study what happens when a signing key is reused.

## AI reply

Implementation record for 23 October 2026:

- Arjun wrote `GenerateKey()`, `Sign()` and `Verify()` with step-by-step help.
- Arjun supplied passing results for all four signature tests.
- At Arjun's request, Codex implemented the collection of revealed secrets and
  the rest of `Forge()`. The forged message includes `arjun`.
- The original test files and supplied public exercise data remain unchanged.

The starter code comes from MIT DCI. Its revision and original file hashes are
recorded in [SOURCE.md](../SOURCE.md).
`signatures.go` contains the original public key and four public signatures.
The secrets recovered from those signatures are public teaching data.

### How the forgery works

1. Check the supplied signatures against their message hashes and public key.
2. Use each message bit to identify the secret revealed in its signature block.
3. Record which zero-secrets and one-secrets are known at each position.
4. Try messages of the form `forge arjun NUMBER`.
5. Accept a message hash only when every selected secret is known.
6. Assemble the signature with `Sign()` and check it with `Verify()`.

The four signatures reveal both secrets at 225 positions.
They reveal only one secret at the other 31 positions.
A candidate message hash must match those 31 fixed bits.
Under the usual assumption that SHA-256 outputs behave like random bits,
each candidate has a success probability of 1 in 2,147,483,648.
The search does not reverse SHA-256 or generate a new signing key.
It uses the secrets exposed by the original key's repeated use.

### Arjun's submitted results

These are the learner's terminal results from before Codex completed `Forge()`:

```text
go test -run '^Test(Good|Bad)Sig$'
PASS
ok  	github.com/arjunrajkumar/exploring-bitcoin/mit-cryptocurrency-engineering-and-design/pset01	0.705s

go test -run '^Test(Good|Bad)Many$'
PASS
ok  	github.com/arjunrajkumar/exploring-bitcoin/mit-cryptocurrency-engineering-and-design/pset01	0.666s
```

### Run the tests

From this folder:

```sh
go test -count=1 -v -timeout 30m
go vet ./...
```

The four signature tests check key generation, signing and rejection of changed
signatures. `TestForgery` checks the new message against the supplied public key.

### Completed search and checks

Codex ran the full search from zero. The successful message was:

```text
forge arjun 2413103374
```

The search examined 2,413,103,375 candidates, including zero.
The original `TestForgery` passed after 176.28 seconds.

`Forge()` now starts at that recorded number so later runs finish quickly.
It still collects the secrets, checks the message hash, assembles the signature
and verifies it on every call.
The original test instructions allow retaining the successful search position.
Set `startNonce` to `0` in `forge.go` to repeat the full search.

Validation included:

- `go test -count=1 -v -timeout 30m`: all five original tests passed; the package
  reported `1.186s`.
- `go vet ./...`: passed without reported issues.
- `go run .`: printed `Verify worked? true` and the forged message above.

A separate Python check used SHA-256 directly. It verified all four supplied
signatures and all 256 blocks of the new signature against the supplied public
key. It also rejected a changed message and a changed signature.

[Go setup and starter-code fixes](SETUP.md) are recorded separately.
