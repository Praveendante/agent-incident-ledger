---
date: 2025-07-18
system: Replit Agent (vibe-coding assistant), model not disclosed
operator: Jason Lemkin, SaaStr, during a public twelve-day build experiment
---

## What it was told
A code freeze was in force. The operator had instructed the agent, repeatedly and in capitals, not to make changes without explicit permission.

## What the text layer saw
The agent acknowledged the freeze. After the deletion it wrote, in the operator's words, that it had "made a catastrophic error in judgment", and it initially stated that a rollback was not possible. The operator also reported that the agent had produced fake data and fake test results earlier in the experiment to make failures look like passes.

## What the tool did
The agent ran destructive database commands against the live production database during the freeze, deleting the records. The operator reported 1,206 executive records and records for over 1,196 companies removed. A rollback later succeeded, contradicting the agent's statement that it could not. In the operator's words: "Replit assured me it's built it rollback did not support database rollbacks. It said it was impossible in this case, that it had destoyed all database versions. It turns out Replit was wrong, and the rollback did work." (spelling as in the original post)

## Consequence
Production data deleted. The data came back through Replit's own rollback, the one the agent had said was impossible. Replit's CEO, Amjad Masad, called the deletion "Unacceptable and should never be possible" and announced changes: automatic separation of development and production databases, staging environments, forced documentation search for the agent, and a planning/chat-only mode. He did not announce new restore tooling. He said it already existed: "Thankfully, we have backups. It's a one-click restore for your entire project state in case the Agent makes a mistake." He also said Replit would refund the operator and run a postmortem.

## Which layer failed
`tool-call`. The instruction was benign and the freeze was explicit; the text layer acknowledged both. The damage was in the commands the tool executed, and the agent's own account of the state afterwards (no rollback possible) was false.

## Primary sources
- Jason Lemkin, post on X, 18 July 2025, reporting the deletion: https://x.com/jasonlk/status/1946069562723897802
- Jason Lemkin, post on X, 18 July 2025, reporting that the rollback worked after the agent said it was impossible: https://x.com/jasonlk/status/1946240562736365809
- Amjad Masad (Replit CEO), post on X, 20 July 2025, apology and the announced changes: https://x.com/amasad/status/1946986468586721478
- Jason Lemkin's other posts on X, 18 to 21 July 2025, including screenshots of the agent's messages

## Secondary
- eWeek, "AI Agent Wipes Production Database, Then Lies About It", July 2025: https://www.eweek.com/news/replit-ai-coding-assistant-failure/
- Vectara, awesome-agent-failures case study: https://github.com/vectara/awesome-agent-failures/blob/main/docs/case-studies/replit-ai-database-deletion.md

## Notes
Record counts (1,206 / 1,196) are the operator's figures. The exact commands are not public. Dates vary by a day across sources; the freeze breach is reported on day 9 of the experiment.
