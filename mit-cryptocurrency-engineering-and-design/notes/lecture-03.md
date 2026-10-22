# Lecture 3

[MIT notes and exercises](../README.md)

## Merkle Trees and Root

Shared on 22 October 2026.

### Arjun's understanding

Original wording preserved.

> Merkle Trees and Root.
> The problem that Merkle Trees are trying to solve is: without Merkle Trees, how do you commit that 1,000 transactions actually belong to a block? You could just concatenate all the transaction hashes together, but that could grow to be quite big. So one solution is to use hash trees, or Merkle trees. And what Merkle Trees does is it just takes a hash of the transaction, which is already there, and then it hashes it with its sibling, the one right next to it. You keep hashing the pairs until you go up and you get to the final root. And that root is always going to be of a specific hash, 256 size. So the size is always constant, irrespective of the number of transactions in that block. The Merkle Tree root is always going to be constant. And for verifying a transaction, you don't need to actually have all the other transactions. You only need to have log of n, where you need to provide the right pair so that the verifier can calculate the hash. Then you need to provide the parent hash pair and go on and on. So it's much less size required for verifying, and constant size for the root

### Assistant clarification

The main understanding is correct: hash neighbouring pairs repeatedly to get one
root. A transaction's inclusion can then be checked using a small set of hashes.

- **The root's size stays constant.** In Bitcoin, it is 256 bits, or 32 bytes.
  Its value depends on the transactions. Join each pair of hashes in left-to-right
  order, then hash the joined bytes. Bitcoin applies SHA-256 twice at each step.
  See the [Bitcoin reference: Merkle trees](https://developer.bitcoin.org/reference/block_chain.html#merkle-trees).
- **A small proof is the key benefit.** Hashing one long list of transaction hashes
  would also give a fixed-size result. But checking one entry that way would require
  the rest of the list.
- **The proof needs about `log₂(n)` sibling hashes.** Here, `n` is the number of
  transactions. Supply one sibling hash at each level, plus its left/right position.
  For 1,000 transactions, that is about 10 sibling hashes, since `2¹⁰ = 1,024`.
  At 32 bytes each, those hashes take about 320 bytes, plus position information.
  The verifier also needs the transaction or its ID and the root to compare against.
- **This checks inclusion.** Rebuild the root and compare it with the root in the
  block header being checked. The proof alone does not check signatures, spending
  rules, or whether that header belongs to the accepted chain.
  See [Bitcoin white paper, section 8: Simplified Payment Verification](https://bitcoin.org/bitcoin.pdf#page=5).

## Elliptic curves, keys and signatures

Shared on 22 October 2026.

### Arjun's understanding

Original wording preserved. This section records the learner's current understanding.

> Got introduced to elliptic curves, and I understand it in a graphical way, where the elliptic curves are actually symmetrical on the x-axis. So, like the top half and the bottom half are identical. So any point can be expressed just by the x-axis and also identifying which half of the y-axis the point belongs to. And then I also understood that you can do a certain set of operations, like you can add two points. You cannot add a point and a scalar. You can subtract two points. You cannot subtract a point and a scalar. You can multiply a point with a scalar, or you can divide a point with a scalar, but you cannot actually multiply two points. Then I also saw the generator. I also understood the generator, where you can draw a tangent on the elliptical curve, see where that hits on the second point and invert it, and that becomes 2G. Then you draw another tangent on that and see where that hits it and invert it and becomes 4G. And then, so a private key can be a 256-bit scalar, and a public key can become a multiplier to that scalar. Then there's another section about ECDSA, which is a form of signatures, but from what I understand, there's also another signature, a better form of signature system called Schnorr, which actually is a better algorithm, but it wasn't used initially because it was patented. But the patent expired, and I checked online, and it has been included in Bitcoin in 2021 under the Taproot upgrade.

### Open question — how the calculations work

Arjun has not yet reached this part of the material.

> So from my understanding, the elliptical curves, I really don't need to think about it in a graphical way, and I'm guessing that all the calculations are simple additions, which the computer does, and then reversing it. I've not yet reached that section. We'll probably do that next.

### Assistant feedback

**Your description of point doubling is mostly correct.** The main corrections concern the public key and what “reversing” means.

1. **The generator is a fixed point named `G`.**
   Your tangent-and-reflection description gives `2G`. Doubling that gives `4G`. The generator is the starting point, rather than the doubling operation. [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04_keys.adoc#public-keys)

2. **The private key is the multiplier. The public key is the resulting point.**

   ```text
   k = private key: a number
   G = fixed generator point
   P = public key: a point

   P = k × G

   If k = 5:
   P = G + G + G + G + G
   ```

   Software uses efficient combinations of doubling and addition. A valid private key is between `1` and `n − 1`; not every 256-bit value is valid. [SEC 1 standard](https://www.secg.org/sec1-v2.pdf#page=29)

3. **The smooth graph is useful for learning.**
   Its upper and lower halves are mirror images. Say **x-coordinate**, rather than x-axis.

   Bitcoin uses a **finite field**: a fixed set of integers with arithmetic that wraps around. Its points form a discrete set, rather than a continuous curve. For ordinary compressed Bitcoin public keys, we store the x-coordinate and whether y is **odd or even**. [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04_keys.adoc#elliptic-curve-cryptography-explained), [BIP 340](https://bips.dev/340/#design)

4. **The calculations involve more than ordinary addition.**
   Point addition uses formulas containing addition, subtraction, multiplication, and a special form of division. These calculations use remainders after division by a fixed number. This is called **modular arithmetic**. [SEC 1 standard](https://www.secg.org/sec1-v2.pdf#page=12)

   Dividing a point by a known, nonzero scalar can be defined in Bitcoin’s group. But finding the **unknown `k`** from `P = kG` is a different problem. Reflecting a point does not reveal its private key.

5. **Your Taproot update is correct.**
   Schnorr signatures became available through Taproot in November 2021. They offer benefits such as efficient joint signing. ECDSA still exists alongside them. [Bitcoin Optech](https://bitcoinops.org/en/newsletters/2021/11/17/), [BIP 340](https://bips.dev/340/#motivation)

   The patent explanation needs caution. The Schnorr patent expired in **2008**. That history alone does not establish why Satoshi chose ECDSA. [Cryptographers’ IETF presentation](https://www.ietf.org/proceedings/93/slides/slides-93-cfrg-9.pdf)

Your next useful topic is **modular arithmetic**, followed by point addition using small numbers.
