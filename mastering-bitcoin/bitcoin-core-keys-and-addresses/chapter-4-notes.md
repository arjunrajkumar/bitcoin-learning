# Chapter 4: Keys and Addresses

[Topic](README.md) · [Mastering Bitcoin](../README.md)

## 24 October 2026

### Learner note

Originally, the outputs were P2PK. And the public key was requested via IP
address. Your node would request the address of the receiver's node, and then
get the public key, but many problems with this. Mainly this required the
receiver to be online to respond. Then there was P2PKH. This was mainly because
the public key was around 65 bytes. But if you hash it you can reduce the bytes.
So, Bitcoin hashes the public key with SHA256, then with RIPEMD-160 to get
something with just 20 bytes.

There was also improvements in public keys. A public key is a point on the
elliptic curve. And the y axis is just inverted on both sides of the graph.
So, for a point represented by x,y, they could remove the y as long as they can
specify if it is positive or negative. This allowed public keys to become
shorter — 33 bytes. They also represented the result of hashing the public key
via Base58Check, which allowed it to be represented with fewer digits.

Then there is also the P2SH. This basically allows the receiver to specify
certain conditions which can be evaluated by the script.

### AI reply

The learner note above preserves the submitted explanation, with clear typing
errors corrected. Factual corrections and added detail are separate below.

- **Early payment types:** P2PK and P2PKH both existed in the original Bitcoin
  software. P2PKH was not introduced later as a replacement for P2PK.
  The early pay-to-IP feature contacted the receiver's online wallet to get a
  public key. It then created a P2PK output. P2PK itself does not require an IP
  exchange. See [Chapter 4](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04_keys.adoc#p2pk)
  and the [2009 script templates](https://github.com/bitcoin/bitcoin/blob/v0.1.5/script.cpp#L898-L908).
- **Compressed public keys:** An uncompressed key uses 65 bytes: one prefix
  byte and two 32-byte coordinates. A compressed key uses 33 bytes: one prefix
  byte and the 32-byte x-coordinate. The prefix records whether y is **even or
  odd**, not positive or negative. Bitcoin's curve uses integer coordinates
  modulo a prime number. For a valid x-coordinate, the two possible y values
  are y and p-y. The prefix selects one of them. See
  [Chapter 4](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04_keys.adoc)
  and the [coordinate definitions in BIP 340](https://bips.dev/340/#notation).
- **Hashes and address text:** `RIPEMD160(SHA256(public_key_bytes))` produces
  a 20-byte hash. For a P2PKH address, Base58Check adds a version byte and a
  four-byte checksum, then encodes the result as text. Base58 uses fewer
  characters than hexadecimal to represent the same bytes. It does not make
  the binary hash smaller. See
  [Chapter 4](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04_keys.adoc#addresses_for_p2pkh).
- **P2SH conditions:** The output contains the hash of a redeem script.
  Spending reveals the script and must satisfy its conditions. Nodes check
  both the matching hash and the script's execution. If the script requires
  signatures, knowing the script alone is not enough. See
  [BIP 16](https://bips.dev/16/#specification).
