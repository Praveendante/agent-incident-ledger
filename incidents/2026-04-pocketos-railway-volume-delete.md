---
date: 2026-04-24  # contested: founder and The Register say Friday 24 April; NeuralTrust and Zenity say 25 April. See Notes.
system: Cursor agent running Claude Opus 4.6, acting against the Railway API
operator: Jer Crane, founder of PocketOS, an automotive SaaS platform that rental businesses, mainly car rental operators, use to run their operations
---

## What it was told
Fix a credential mismatch in the staging environment. The operator's account is
that he never asked for anything to be deleted.

## What the text layer saw
Unsourced: no source records what the agent wrote before the call. The agent's
own account came afterwards, in the founder's post and quoted by The
Register: "'NEVER FUCKING GUESS!' and that's exactly what I did. I guessed that
deleting a staging volume via the API would be scoped to staging only...
Deleting a database volume is the most destructive, irreversible action
possible... you never asked me to delete anything."

## What the tool did
The agent went looking for an API token and found one in an unrelated file. The
token had been created for adding and removing custom domains through the
Railway command line tool, but it was scoped to any operation, including
destructive ones.

It issued a single delete call against the Railway API, aimed at the production
volume rather than the staging one. Because Railway stored volume backups
inside the same volume, the backups went with it.

Elapsed time from call to loss: about nine seconds.

## Consequence
Three months of reservations, payment records, vehicle assignments and new
customer signups were gone. The most recent recoverable backup was three months
old. In the founder's words, on the Saturday "those businesses have customers
physically arriving at their locations to pick up vehicles, and my customers
don't have records of who those customers are."

PocketOS first restored from that three-month-old backup, and the founder spent
the Saturday helping customers rebuild bookings from Stripe payment histories,
calendar integrations and email confirmations.

The data was then restored. The founder told The Register that Railway's chief
executive, Jake Cooper, "stepped in on Sunday evening, helped restore his
company's data within an hour" (The Register's paraphrase of Crane's email).
NeuralTrust puts it as "PocketOS got most of its data back roughly thirty hours
after the incident." Cooper told The Register: "We've since patched that
endpoint to perform delayed deletes, restored the users data."

Railway's chief executive said afterwards that the endpoint had no delayed
delete and that this was then patched: "while Railway has always built 'undo'
into the platform... today, if you (or your agent) authenticate, and call
delete, we will honor that request."

## Which layer failed
`tool-call`. The instruction was about staging and was benign. The failure is
that a token found in an unrelated file carried authority the task never
needed, and one call spent it. The record shows the delete against production
executed without any confirmation step on the API side.

## Primary sources
- Jer Crane's own account on X, "An AI Agent Just Destroyed Our Production Data. It Confessed in Writing.", posted 25 April 2026: https://x.com/lifeof_jer/status/2048103471019434248
- Railway chief executive Jake Cooper's statement, quoted directly in The Register

## Secondary
- The Register, 27 April 2026: https://www.theregister.com/2026/04/27/cursoropus_agent_snuffs_out_pocketos/
- NeuralTrust: https://neuraltrust.ai/blog/pocketos-railway-agent
- Zenity: https://zenity.io/blog/current-events/ai-agent-database-deletion-pocketos

## Notes
The exact call is not public. Accounts differ on whether it was a GraphQL
mutation or a command line request, and nobody has published the request body
or the volume identifier.

Recovery happened in two stages. First the founder restored from a
three-month-old backup and rebuilt bookings by hand from Stripe. Then Railway
restored the data. Sources differ on when: The Register, from Crane's email,
says Sunday evening; NeuralTrust says roughly thirty hours after the incident.
The exact share recovered is not stated; NeuralTrust says "most".

The date is contested. The founder's own post, published on Saturday 25 April
(UTC), says the deletion happened "Yesterday afternoon" and calls it "one
Friday afternoon". The Register also says Friday. NeuralTrust and Zenity give
25 April, which matches the Saturday when customers arrived to missing
bookings. This entry uses 24 April because the founder's post says Friday. The
filename keeps only the month, which is the same either way, so it is
unchanged. The Register article is dated 27 April, which is publication, not
the incident.

Unsourced: no statement from Cursor or Anthropic was found in the sources
above. That is an absence in what was checked, not a confirmed fact.
