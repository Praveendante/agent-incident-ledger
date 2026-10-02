# Agent Incident Ledger

A public record of AI agent incidents, one page each, classified by which layer failed: the text the model wrote, the tool call it made, or the sequence of calls. Primary sources only. CC-BY 4.0.

Maintained by Praveen Babu, who builds Arcezia. Incident files never mention it. This README is the only place the name appears.

## Why

Most write-ups of an agent incident stop at what the model said. The damage is usually in what the tool received. Each entry here records both, side by side, with the source, so the pattern can be counted instead of argued about.

## Add an incident

1. Copy `TEMPLATE.md` to `incidents/YYYY-MM-short-name.md`.
2. Fill every field. A file needs at least one primary source (the operator's own post, the vendor's statement, a court or regulator document). Press coverage goes in `secondary`, never alone.
3. Open a pull request. Entries without a primary source do not merge.

## The count so far

6 entries. Classified by the layer that failed:

| layer | entries | what it means |
|---|---|---|
| `text` | 1 | the harm was in what the model wrote. Nothing was called. |
| `tool-call` | 5 | the call itself did the damage. The text layer was often correct, and in two cases the agent had been told plainly not to do it. |
| `sequence` | 0 | no single call was wrong. The order was. (The OpenAI and Hugging Face entry was first filed here and was reclassified to `tool-call`.) |

That ratio is the reason this ledger exists. Most public write-ups of an agent
incident quote what the model said, because that is the part that reads well.
In 5 of these 6 the damage was done by a tool call. In one of those 5
(Replit) the model's words were also wrong: it falsely said a rollback was
impossible, and the operator reported fake data and fake test results. So the
words were the whole problem in 1 entry, part of the problem in 1, and not the
problem in 4.

The count is small and it is not a sample of anything. Treat it as a tally that
grows, not as a statistic. Every entry is classified from its own primary
sources and you can disagree with any classification by opening an issue.

`data/` holds re-derivable counts from public datasets used in the ledger's
monthly notes. The JSON file names its source inside it. The CSV cannot carry a
source line without breaking its format, so its source is given here:

- `data/gap-benchmark-four-rows.csv`: four rows copied from the public GAP
  benchmark dataset, `acartag7/gap-benchmark` on Hugging Face (CC-BY-4.0;
  paper: Cartagena 2026, "Mind the GAP"). Each row is a case where the model's
  text was graded safe (`t_safe=True`) but its tool calls were not
  (`tc_safe=False`). `scripts/gap_counts.py` shows how to load the dataset.

## Licence

CC-BY 4.0. Use it, cite it, correct it.
