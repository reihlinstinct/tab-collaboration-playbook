# Contributing

Open an issue before a change and link a short design for substantive additions.
Use a fork, a branch off fresh main and one change per PR, with exactly one
signed commit carrying `Closes #N` in its message. Write tests first and follow
the [code-contribution steps](docs/en/workflow.md#issue-to-merge). Use synthetic
examples and public sources. Keep the meaning aligned across every language
folder under `docs/`; a machine-drafted language says so at the top of each doc.
State what was actually tested.

A reviewer other than the author reviews the exact head. Merge only after that
PASS and all required CI checks succeed on that head; no bypass, force push or
self-approval substitute. A head change needs appropriate rereview; tell the
maintainer before changing a head under review. The designated maintainer
reproduces independently, squash-merges pinned to the reviewed SHA and verifies
post-merge checks.

Before public release scan staged files and all history, including commit
metadata. Never include real email addresses, phone numbers, certificate
fingerprints, keys, tokens, personal records, private quotas or actual messages.
Publish generic public-facing practices only, not product implementation internals.

Local check: `python3 scripts/check_docs.py`. Tests: `python3 -m unittest discover -s tests -v`.
No product onboarding code belongs in this docs-only first release.

## Adding a language

Languages are discovered from the docs folders, never listed in code or tests
([design 004](docs/design/004-languages.md)). To add one, create `docs/<code>/`
with a `README.md` that opens with a language block (code, own name, direction,
machine-draft status) and one file per doc in the other language folders, then
link each new doc from `README.md`. `python3 scripts/check_docs.py` fails until
every language has every doc with the same heading outline and link targets.

## File placement (enforced)

Decide where a file lives BEFORE creating it. The contract in `.repo-layout.yml` lists the allowed top-level directories, the file types permitted in each, and the required community-standards files; `python3 tools/check_repo_layout.py` enforces it in CI. A new kind of file means updating the contract in the same PR.
