# Exploring Bitcoin workspace

## Purpose and plan

This repository is a collection of Arjun's Bitcoin notes, exercises, code,
questions and progress. The goal is to understand Bitcoin deeply and build
with it. Contributing to Bitcoin Core is a longer-term goal.

Follow the order in README.md:

1. MIT lectures 1–6.
2. Mastering Bitcoin.
3. Bitshala Programming Bitcoin.
4. Bitshala Bitcoin Protocol Development.

Keep README.md limited to its heading, four checklist links, total time
and green calendar. Do not add a daily log table or a weekly total.
Put details in the matching folder.
Use the resource names, or refer to lectures, reading, exercises and projects.
Do not restore the retired Weightless material or its deleted repository.

## Communication and learning support

- Use ASD-STE100 Simplified Technical English.
- Use short, direct sentences with one main idea in each sentence.
- Use common words. Define necessary technical terms.
- Arjun knows Ruby and Rails. Use those examples when useful.
- Explain the limits of an analogy.
- Keep exact code, commands, file names and error messages unchanged.
- Guide practical work one small step at a time when asked.
- Let Arjun run setup commands and exercise code unless he asks you to run them.
- Explain concepts and help with problems when asked.
- Do not start quizzes, assign scores, require confidence ratings or schedule
  repeated tests unless Arjun explicitly asks.
- Do not impose deadlines or add a study plan beyond the requested checklist.

## Start or resume a session

- Confirm the repository is arjunrajkumar/exploring-bitcoin.
- Read this file, README.md and the relevant area files.
- Use saved notes and actual submitted output to find the current position.
  Do not assume access to another chat.
- Inspect Git status before edits. Fetch origin when network access is available.
  If the checkout is clean and only behind, use a fast-forward update.
- Preserve local work. Inspect divergence before combining changes.
  Never reset, overwrite, force-push or silently discard learner work.
- Report the next useful action when relevant.
  State whether changes are local, committed or pushed.

## Where work belongs

- `mastering-bitcoin/`: all Mastering Bitcoin notes, exercises and earlier work.
- `mit-cryptocurrency-engineering-and-design/`: MIT lecture notes, problem sets and experiments.
- `bitshala-programming-bitcoin/`: Programming Bitcoin notes and exercises.
- `bitshala-bitcoin-protocol-development/`: protocol development notes and exercises.

Keep code, notes and useful command output near the topic they concern.
Use simple files and add folders when there is work to save.
Keep shared repository instructions at the root.
The root checklist tracks the four broad steps.
Mark a step complete only when the learner confirms completion.

## Learner work and records

- The learner writes first exercise attempts and personal explanations.
  Do not supply a complete exercise solution unless asked.
- Preserve submitted wording, meaning, code, numbers and technical claims.
  Correct only clear typing errors when editing a submitted answer.
  Put factual corrections in a separate explanation.
- Label assistant summaries and explanations. Do not present them as learner work.
- Preserve earlier submissions and results.
- Keep the older reviews and unused templates in
  `mastering-bitcoin/earlier-reviews/` as historical records.
  Their old testing instructions do not define the current workflow.
  Do not treat them as tasks to complete.
- Record progress from actual work or shared output.
  A file's presence does not prove it ran or that its topic is understood.
- State uncertainty. Check full source instructions before reviewing an exercise.
  Link to relevant reading or primary documentation when it supports an explanation.
- Keep source attribution for imported examples.
  Record setup fixes separately from learner solutions.

## Saving and publishing

### Learning time

- Save confirmed daily minutes in `data/learning-time.json`.
  Dates use India time (`Asia/Kolkata`).
- Read dates from the supplied evidence, including the year.
  The older screenshot explicitly shows 2025 for the October 6–8 entries.
- A missing date means no entry. Record zero only when the learner reports zero.
  Never infer study time from commits, chat length or a running node.
- Update one entry per date. Replace a corrected daily total instead of adding
  it twice. Do not add an unfinished day's time unless the learner asks.
- Set `as_of` to the current date in India when updating the calendar.
- Run `python3 scripts/render_learning_time.py` from the repository root.
  This updates the total and both calendar images without changing the checklist.
- Start the calendar at the first day of the earliest recorded month.
  Include year labels so entries from different years remain distinct.
- Use the label `Total time: H hrs M min` above the calendar.
  Keep extra space between the checklist and this label.
- Commit and push the data, generated images and README together.

### Repository files

This repository is public. Keep private keys, wallet recovery phrases,
credentials, authentication cookies and private account data out of it.
Public example data from the original material must be identified as such.
Link to external reading. Do not copy whole websites or large downloads.

A request to save or update this record includes committing and pushing,
unless Arjun asks to keep the changes local.

Before publishing:

- Check the files for secrets and private data.
- Check links and confirm that moved work is preserved.
- Inspect Git status and review the scoped diff.
- Stage explicit paths. Include only the requested work.
- Commit and push to the intended branch. Never force-push.
- Confirm the push result and link to the saved work.
  If it fails, report the actual reason and what remains local.
