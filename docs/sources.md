# Sources and validation limits

Checked 2026-11-04. These URLs were read as public pages. Product descriptions
are vendor claims, not independent tests. The workflow is this project's
recommendation. This guide does not reproduce private account records.

| Source | What it supports | Limits |
| --- | --- | --- |
| https://tab.bot/ | Private-beta form: name, mobile, country, consent, Sign up; one text to start. Public examples of calls and approved email/calendar work. | Does not establish mailbox provisioning, S/MIME UI, prices or access for every account. |
| https://tab.bot/updates | Tab's public capability announcements, including calls and timezone handling. | Claims are Tab's own. No private account quotas or guaranteed interoperability inferred. |
| https://guide.actalis.com/smime/features | S/MIME purpose, MV mailbox control, free once-only/no-support wording, issuing stages. | Recheck eligibility and terms before enrollment. |
| https://guide.actalis.com/faq/S-MIME/S-MIME | Single-address certificates, ASCII address restriction, generic client import, validation-link lifecycle, free PKCS#12 delivery. | Client UI and current enrollment may vary. |
| https://extrassl.actalis.it/portal/uapub/doProcess?lang=en | Free Email Certificate entry and first email validity-check page. | No fresh enrollment beyond public entry was performed. |
| https://docs.openssl.org/4.0/man1/openssl-smime/ | Command-line verification example; CMS recommendation for newer formats. | Version-specific; command alone does not check actor binding or current revocation. |

## Verification labels

- Public-source checked: the linked provider documentation supports the stated
  claim on the check date, not a successful account operation.
- Recommended protocol: our generic task/review/channel method.
- Provider-dependent / untested: fresh signup, later certificate-enrollment
  screens, each account's mailbox/S/MIME capability and actual two-way delivery.
- Verified operation: reserved for a reader's own completed acceptance tests.

No current universal Tab mailbox API, S/MIME enrollment API or automatic
certificate import endpoint was established by these sources. Do not invent one.
There is no promise that an arbitrary agent can complete enrollment unattended.
The checklist gives concrete pages, inputs, outputs and stop conditions where
public evidence ends. Recheck UI and document any change with a new issue.

## Calls: additional evidence limits

The calls pages distinguish Tab's public calling claims from generalized prior
use and unverified Tab reports. No private call records or identifiers are
published. US origin, Hebrew quality, reported cost/plan consumption, duration
cap, DTMF limitations, short numbers, text-only audio, messaging availability,
spam/busy/silent outcomes and transcript access are account-dependent. They are
not public-provider guarantees. No fresh test call, cost verification, recording
audit or verbatim-transcript export was performed for this update.

The public 2026-09-09 update says hold calls can last an hour, in conflict with
a later setup-specific report of roughly ten minutes. The calls pages preserve
that conflict and require an account-specific check before promising a duration.
