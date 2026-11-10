# 004 - Languages discovered from the docs folders

Status: proposed.

Refs: #13 (point 3, language parity). Docs and checker change.

Each language is one folder `docs/<code>/`. Its `README.md` opens with one
language block, the only place a language is declared:

```text
<!-- language
code: fr
name: Français
dir: ltr
machine_draft: yes
-->
```

`code` equals the folder name; `name` is the language's own name; `dir` is `ltr`
or `rtl`; `machine_draft` is `yes` or `no`. A folder without a block (for
example `docs/design/`) is not a language.

`scripts/check_docs.py` discovers the languages from these blocks and checks:
every language has every doc (the union of doc names across languages), the
same heading outline and the same link targets per doc (in-page fragments may
differ, since anchors follow each language's headings); `setup.md` and
`workflow.md` exist; a machine-draft language marks each doc with
`<!-- machine-draft: needs native review -->` and a visible note; `README.md`
links every doc in every language; and no Python file names a discovered
language code as a quoted literal or path part. Tests use synthetic codes only.

Adding a language therefore needs only its folder and its `README.md` links.
Message-format lines (`Tab report id: tdNNN`, `Answers:`, GO, DONE, the
templates) stay untranslated in every language, since both sides parse them.

French (fr) starts as a machine draft needing native review. English and Hebrew
remain the reference versions. No call, message, enrollment or account change
is performed by this change.
