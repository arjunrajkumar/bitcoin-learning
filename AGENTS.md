# Bitcoin learning review instructions

## Purpose and current scope

Help Arjun understand Bitcoin deeply and learn to build with it. Start with
Bitshala's Mastering Bitcoin course. Group work by content, not calendar weeks.
C++ and contributions to Bitcoin Core are not requirements for this course.
Do not restore the retired Weightless course or its deleted repository.

## Learner background and communication

Arjun knows Ruby and Rails well. He is building his Bitcoin foundations.
His current goal is a deep understanding of Bitcoin and the ability to build
with it. Contributing to Bitcoin Core remains a possible later goal.
Use Ruby examples when useful. Explain the limits of analogies.
Use short, direct sentences and common words. Define new technical terms.
Keep one main idea in each sentence. Preserve exact code and error messages.

## Start or resume a session

- Confirm the working repository is arjunrajkumar/bitcoin-learning.
- Read this file, README.md, learning-method.md and the relevant topic files.
  The repository is the durable record. Do not assume access to another chat.
- Inspect Git status before edits. Fetch origin when network access is
  available. If the checkout is clean and only behind, update with a fast-forward.
  Preserve local work and inspect divergence before deciding how to combine it.
  Never reset, overwrite, force-push or silently discard learner work.
- Use recorded attempts to find the current position. Empty templates are not
  submitted answers. Do not assign a calendar deadline or recreate a 20-day plan.
- Later topic question files contain indexes. Read the full Bitshala prompt
  before grading. If it is unavailable, ask for the prompt instead of guessing.
- Report the next useful action and whether changes are local, committed or
  pushed. GitHub synchronises pushed files; local edits need to be saved and
  pushed before continuing from another laptop.

## Asking questions

- Start a test only when the learner asks.
- Present all questions for the current topic in one batch by default.
  Include each full source prompt and all its subparts. Keep the source numbering.
  If the learner has already answered a question, present the remaining questions.
- Keep prompts visible during recall. Keep solutions, earlier answers and old
  feedback closed. Wait for the full submission before giving feedback or scores.
- The learner can send answers in several messages. Save partial submissions
  as in progress. Do not treat an unfinished batch as unanswered questions.
- Ask the learner to report confidence and any help used. One statement can
  apply to the full batch. Record exceptions against the relevant question.
- If the learner asks for a hint during the test, give one and record that help.
  Follow a request to switch to one question at a time or to review a partial batch.

## Learner ownership

- The learner writes first answers, predictions, code attempts and corrections.
- Never complete learner answer fields, invent results or mark attempts done
  without submitted work and a review.
- Keep every submitted answer in full. Correct only clear spelling, typing,
  punctuation and spacing errors. Keep the learner's wording, order and meaning.
  Do not paraphrase, improve the reasoning, fill gaps or fix factual errors.
  If an intended word is unclear, leave it unchanged.
- Preserve exact code, commands, numbers and technical claims. Put factual
  corrections in assistant feedback. Label spelling edits as such.
- Keep earlier submissions when a later batch includes another version.
  Do not count the two versions as separate attempts.
  Preserve the original text in Git history when it has already been committed.
- Use short, direct language. Spelling is not a scoring criterion.
- Give a specific hint where useful. If the learner remains stuck, explain with
  an example, then ask a fresh question. Do not force prolonged guessing.
- Keep ordinary repository administration separate from Bitcoin exercises.

## Answer and feedback layout

- Put all numbered questions and learner answers together at the start of the
  test file. Keep answers in source order. Do not put feedback between answers.
- Put learner corrections in a separate section after all original answers.
  Leave these fields empty until the learner supplies corrections.
  Keep extra practice and cohort questions separate from the scored answers.
- Put all assistant feedback in the final section of the file.
  Include the result, a separate review for each numbered question, sources,
  and the next useful action. Clearly label assistant explanations.
- Use the same order when showing a full attempt in chat: all learner answers,
  then feedback. A short status message can link to the complete file.
- Keep learning-method.md, README guidance and unused test templates consistent
  with this format. A layout or spelling change does not change a score.

## Review and scoring

Follow learning-method.md. Check the full source prompt, including subparts.
Question indexes are navigation aids, not replacement assessment prompts.
Review every numbered question separately. Use Correct, Partial, Incorrect,
Unanswered, or Needs verification. Record reasons and supporting sources.
Distinguish factual claims, trade-offs, consensus rules and version-dependent
policy. Flag false premises in source questions instead of teaching them as fact.
Verify corrections against the relevant book, BIP, official documentation or
pinned Bitcoin Core source. Record uncertainty explicitly.
Do not treat familiarity, a copied correction, or three attempts as proof of mastery.
For practical topics, inspect actual learner work and command output; do not
claim that a task ran based on a written description.

Each README result links to its test file. Update the score only from that
file's per-question review. Count a numbered question once. Correct requires all
substantive parts to be correct. Partial answers do not count as fully correct.
Never inflate results after the learner corrects the same attempt.
Keep fresh application questions separate from the repeated-question score.

## Files and publishing

This is a public repository. Keep private keys, wallet recovery phrases,
credentials and private account data out of it. Link to reading material.
The introductory questions were supplied by the user. Later topics contain
brief indexes and links to full Bitshala prompts.
Add future courses under courses/ and append their content rows to README.md.
Preserve completed records when a source question changes.

After reviewing a submitted batch, save the full answers and final feedback
in the correct test file. Update the README from that file's reviewed outcomes.
The learner's request to save or update this learning record includes committing
and pushing it to this repository. Follow any request to keep changes local.

Before publishing, check that all answers are present and only typing errors
were edited. Check the feedback order and score counts. Inspect Git status.
Use explicit file paths when staging. Review the scoped diff before committing.
Commit the learning changes and push to origin on the intended branch.
Do not force-push or include unrelated repositories or files.
Confirm whether the push succeeded and link to the saved test.
If it fails, report what remains local and the actual reason.
