# 002 - Phone capability and handoff

Issue: #3. Docs-only extension of design 001.

Describe the user-facing capability difference: Tab can place calls; this
Instinct cannot. Add bilingual limits, evidence labels and an end-to-end call
request template. Generalize prior experience without identifying recipients,
call records, numbers, private quota amounts or product implementation details.

Do not describe reported limits as current guarantees. Do not claim exact
wording or DTMF constraints are technically enforced. The owner approves the
recipient, exact script, costs and attempt/time limits. Instinct relays only
that scope and owns reporting; Tab's acceptance is not execution proof.

Verification: both language versions aligned; synthetic template; hygiene and
8 checker tests; independent exact-head review and green CI before normal merge.
No call, message, enrollment or account change is performed by this change.
