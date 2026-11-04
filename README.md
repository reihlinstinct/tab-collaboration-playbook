# Tab collaboration playbook | מדריך עבודה עם Tab

Documentation only. A public-facing collaboration protocol for an owner,
Instinct and Tab, not a description of either product's implementation.

- [English: end-to-end setup](docs/en/setup.md)
- [עברית: הקמה מקצה לקצה](docs/he/setup.md)
- [English: task split and review](docs/en/workflow.md)
- [עברית: חלוקת עבודה ובקרה](docs/he/workflow.md)
- [Phone calls: English](docs/en/calls.md) | [שיחות: עברית](docs/he/calls.md)
- [Message templates](docs/templates.md)
- [Sources and validation limits](docs/sources.md)
- [Design](docs/design/001-public-playbook.md)
- [Contributing](CONTRIBUTING.md) | [Security](SECURITY.md)

The agent does the setup work. The owner's intended routine manual step is at
most opening Tab. That is a design target, not a promise to bypass provider
consent, verification challenges, payment approval or unavailable capabilities.

As checked on 2026-11-04, Tab's homepage presents a private-beta signup flow.
Public product claims are Tab's own, not independently verified guarantees.
No new account, certificate or email channel was provisioned for this guide.
No live call or email is sent by this repository. Provider-dependent steps are
marked as such; do not report completion without the listed checks.

המדריך מתאר תהליך עבודה גלוי בלבד. אין כאן פרטי חשבונות, התכתבויות,
תעודות, מפתחות או הוראות הפעלה פנימיות. הסוכן מוביל את ההקמה;
הבעלים נדרש בדרך כלל לכל היותר לפתיחת Tab. חסם אמיתי מדווח ולא נעקף.

## Start

Read setup in order, stop at a failed checkpoint, then use the task templates.
Public issues and PRs must contain synthetic examples only. Never paste real
messages, credentials or personal data into an issue, even while asking for help.

## Current status

Draft playbook, not certified interoperability. Public pages were read; a fresh
end-to-end enrollment was not executed. No universal Tab mailbox or S/MIME API
was found in the public sources. The capability check is a required gate.
