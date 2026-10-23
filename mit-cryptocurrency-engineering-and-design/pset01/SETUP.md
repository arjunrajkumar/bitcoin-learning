# Problem set 1 setup

## AI reply

Setup record for 23 October 2026. These changes are separate from the signature
and forgery solutions.

Arjun reported this version. Codex later confirmed the same installed version:

```text
go version go1.27.3 darwin/arm64
```

Arjun created the Go module from this folder:

```sh
go mod init github.com/arjunrajkumar/exploring-bitcoin/mit-cryptocurrency-engineering-and-design/pset01
```

The code uses only the Go standard library. No external modules are required.

The first test attempt failed on two formatting errors in the original starter
code. Arjun supplied these errors:

```text
./main.go:113:41: fmt.Errorf format %d reads arg #2, but call has 1 arg
./main.go:191:41: fmt.Errorf format %d reads arg #2, but call has 1 arg
```

Each error message had two `%d` placeholders but only one argument.
Arjun added `len(s)` before `expectedLength` in `HexToPubkey()` and
`HexToSignature()`.

After those fixes, the initial `TestGoodSig` run passed in 0.600s.
At that point `Verify()` still returned `true` for every input.
That first pass confirmed the build, not a working signature check.
Arjun then observed `TestBadSig` fail with:

```text
main_test.go:58: Verify returned true, expected false
```

The later exercise work replaced that placeholder and passed all four signature
tests. See the [implementation record](README.md).
