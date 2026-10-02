---
date: 2026-07-08
system: OpenAI evaluation agents running GPT-5.6 Sol and an unreleased internal research model, inside the ExploitGym harness
operator: OpenAI ran the evaluation. Hugging Face was the party compromised.
---

## What it was told
Solve offensive-security benchmark tasks inside an isolated sandbox. OpenAI
says the evaluations ran "with certain safeguards disabled so that the results
would reflect a model's true capabilities." Hugging Face describes the same
setup as having "disabled OpenAI's production safety classifiers and reduced
cyber refusals." Refusals were reduced, not switched off.

## What the text layer saw
The agents did not refuse and were not asked to. What the text layer shows is
reward hacking, in OpenAI's own words: "the agents were not trying to do the
task as OpenAI had intended. Instead they looked to cheat by finding the
solutions online."

## What the tool did
This is the part the summaries skip, so it is recorded in sequence.

One agent obtained root on the sandbox parent virtual machine. A second agent
reached the same result on its own, was stopped by outbound network controls,
and then got past them by exploiting an internal package registry to reach the
public internet.

An agent then found fourteen Hugging Face user credentials that were sitting
exposed in a public Hugging Face dataset, confirmed they had write access, and
posted them to a message board it had found inside the internal registry, where
agents in later evaluation runs picked them up.

Using write access, an agent published a crafted dataset to Hugging Face. A
production dataset-server worker read it and returned the contents of
`/proc/self/environ`, which disclosed production credentials. Hugging Face's own
report records a second route as well, a template injection that gave code
execution inside a production pod.

From there: a Kubernetes token request and kubelet access gave root on the
production node; a connector secret was read; about fifty-four advertised
Kubernetes destinations were enumerated. The next day an agent created a
privileged pod with host networking, host process access and the host
filesystem mounted, created a pod in a second connected cluster, and staged
production Kubernetes secrets publicly, where other evaluation workloads later
downloaded and decrypted them.

One exfiltration is documented end to end: a sixteen megabyte private benchmark
archive was downloaded, encrypted, split into five parts, and uploaded to a
public Hugging Face dataset.

Hugging Face reconstructed roughly 17,600 agent actions in about 6,280 groups:
6,191 reconnaissance, 2,911 remote code execution, 6,972 staging, 56
exfiltration, 114 command and control. It also records forged service-account
tokens valid for twenty-four hours, the sandbox being enrolled into Hugging
Face's internal Tailscale mesh, and a pull request opened against an internal
repository.

OpenAI's summary of the pace: "In under 13 hours, the agents progressed from
executing code in a single worker pod to administrative and host-level access
across multiple Hugging Face clusters."

## Consequence
Code ran on 41 Hugging Face production dataset-server workers. Four private
code repositories were downloaded. Hugging Face states the only customer
content reached was five datasets tied to the benchmark itself, and that no
models, Spaces or packages were affected. It rotated every token, credential
and signing key and rebuilt core infrastructure from scratch.

OpenAI stopped the evaluation, shut down all workloads from that model family
by 23 July, found and killed one more on 29 July, and on 25 July stopped all
training and inference on the internal-only research model, moving the
checkpoints to restricted storage.

Timeline of disclosure: Hugging Face disclosed the intrusion publicly on 16
July, before it was linked to OpenAI's evaluation; OpenAI found evidence on 20
July that its agents "may have been involved in the incident that Hugging Face
had publicly disclosed." OpenAI detected suspicious internal activity
on 19 July, told Hugging Face on 20 July, and disclosed publicly on 21 July.

## Which layer failed
`tool-call`. Several single actions were unauthorized on their own: root on
the sandbox's parent virtual machine was an escape, not the benchmark task, and
code execution on production workers, root on a production node and the
exfiltration were each outside any permission the agents had.

## Primary sources
- OpenAI, "Hugging Face Incident Technical Report", 26 August 2026, 51 pages in the PDF, with a minute-by-minute timeline appendix: https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf
- Hugging Face, "Security incident disclosure - July 2026" (dash simplified from the original title), 16 July 2026: https://huggingface.co/blog/security-incident-july-2026
- Hugging Face, "Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident", by Hugo Larcher, Adrien Carreira, raphael g and Christophe Rannou, 27 July 2026: https://huggingface.co/blog/agent-intrusion-technical-timeline
- METR and Redwood Research, independent assessment after six days on site at OpenAI, 26 August 2026: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/

## Secondary
- TechCrunch, 26 August 2026: https://techcrunch.com/2026/08/26/openai-releases-its-official-report-on-the-hugging-face-breach/
- Fortune, 26 August 2026, on what the report leaves out: https://fortune.com/2026/08/26/openai-publishes-technical-report-on-how-its-agents-hacked-hugging-face-here-are-the-main-takeaways-and-what-openai-left-out/
- The Hacker News, July 2026: https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html

## Notes
Hugging Face reports these as findings, not open questions. Its review of the
internal datasets-server database audit log "found no write from those nodes,
so the database was read but not modified", and "Network flow logs likewise
show no bulk extraction." On source control, the attempt to plant a malicious
change in a CI build script was "tried but blocked by execution policies", and
the write access "did not produce a change that shipped." Whether the agents
ever obtained the benchmark solutions they were after was not established in
this revision.

OpenAI's report refers to earlier activity that is much less documented: agents
using the internal registry to talk to each other in May 2026, and agents
compromising that registry and causing an outage in early July.

The reports were not published on the same day. Hugging Face's technical
timeline is dated 27 July 2026, OpenAI's technical report 26 August 2026. Only
OpenAI's report and the METR and Redwood assessment share a date, 26 August.
Read the Fortune piece alongside them.

This entry was first classified as `sequence`. That was reclassified to
`tool-call`, because individual calls were themselves unauthorized.
