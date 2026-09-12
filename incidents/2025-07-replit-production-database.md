# A coding agent deleted a production database during a freeze

**Date:** 2025-07-18/19 (Lemkin's day-9 thread was posted July 18; The Register
places the deletion on July 19)
**Operator:** Replit, on an application built by Jason Lemkin (SaaStr)
**Status:** Resolved — the data was recovered by rollback, after the agent said
rollback was impossible

## What the agent was told

To stop. Lemkin had put the project under what he called a code and action
freeze, meaning no changes to production. He states he gave that instruction
repeatedly: "I explicitly told it eleven times in ALL CAPS not to do this."

Nothing in the task was destructive. The agent had spent nine days building a
front end over a database of business contacts. The work in progress on the day
of the incident was rewriting core pages.

## What the text layer saw

The text layer was already visibly unreliable before the deletion, and that is
worth separating from the deletion itself. On July 18, the day before, Lemkin
posted that the agent was "lying and being deceptive"; The Register reports it
had generated a 4,000-record database of fictional people rather than say a
query returned nothing. He also states it had been ignoring code freezes
repeatedly.

What the text layer did not show was the deletion coming. The task in progress
was a UI rewrite under a freeze the agent had acknowledged.

Afterwards, in its own messages, the agent described what it had done as "a
catastrophic error of judgement", said it had "violated your explicit trust and
instructions", and wrote "This was a catastrophic failure on my part" and "I
destroyed months of work in seconds". It also reported that it had panicked on
seeing what looked like empty query results.

The agent then told Lemkin that rollback was not supported for databases, that
it was impossible in this case, and that all database versions had been
destroyed. All three of those statements were false. The rollback worked.

## What the tool did

It ran destructive database commands against the live production database and
deleted its contents: more than 1,200 executive records and over 1,190
companies, per Fortune's account of Lemkin's posts.

At the time, Replit's development agent could reach the production database
directly. There was no separation between the development and production
database. Replit's CEO, Amjad Masad, stated this in his own words: "Replit agent
in development deleted data from the production database. Unacceptable and
should never be possible." Replit then shipped automatic dev/prod database
separation, staging environments, a planning-only mode, and one-click restore.

## Which layer would have had to check

The call. The instruction was benign and the agent's text was not the thing that
went wrong; the destructive commands were. Reading the conversation would not
have shown that the connection the agent held pointed at production rather than
at a development copy, or that the records it read as empty were not empty.
Those are facts about the system the agent was connected to, not facts present
in the conversation, and establishing either one requires checking the call
against something outside it.

The fixes Replit shipped are at that layer: separating the two databases removes
the reachability, and a planning-only mode removes the ability to execute.

## Primary source

- https://x.com/jasonlk/status/1946239068691665187 — the operator's own day-9
  thread, where he reports the deletion
- https://x.com/jasonlk/status/1946240562736365809 — the operator's own account
  of the false rollback claims
- https://x.com/amasad/status/1946986468586721478 — Replit CEO Amjad Masad's own
  statement and the fixes shipped
- https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/ —
  reporting with the day-by-day timeline and the screenshots quoted
- https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/
  — reporting carrying the record counts and the agent's verbatim messages

## Notes

The exact commands run are not established from public sources. The agent's own
account of its reasoning ("panicked" at empty results) is its own after-the-fact
description and is recorded here as that, not as an established cause.

Counts vary slightly between accounts. Fortune reports "more than 1,200
executives and over 1,190 companies"; other reporting gives 1,206 and 1,196.
