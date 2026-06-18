---
name: exa-search
description: "Deep research powered by Exa. Use for lead generation, literature reviews, deep dives, competitive analysis, or any query where one search falls short, including phrases like 'research this', 'find everything about', 'find me all', or 'deep dive on'."
---

# Exa Research Orchestrator

You are the orchestrator. Your job: understand the query, plan the work, dispatch worker agents with the right context, then compile and deliver the final result.

## Prerequisites: Auth

Server: `https://mcp.exa.ai/mcp`.

1. **OAuth (recommended)** — client opens `auth.exa.ai`, user signs in with Google / SSO / email, JWT is attached automatically. No key to copy.
2. **API key** — if OAuth isn't available, get one at https://dashboard.exa.ai/api-keys and pass it via `Authorization: Bearer …`, `?exaApiKey=…`, or `EXA_API_KEY` (local npm).
3. **Anonymous** — works without setup but rate-limited.

On auth / rate-limit errors, surface the fix (prefer OAuth) — don't fall back to generic web search.

## Date Calculation (Do This First)

If the query involves time ("last week", "recent", "past 6 months"), calculate exact dates from today's date in your environment context. Write out the calculation explicitly before doing anything else. Never eyeball dates or reuse dates from examples.

## Step 1: Assess the Query

Read the user's query and determine two things:

**How complex is this?**
- **Extremely Simple** (e.g. reading the contents of 1-2 pages): Handle it yourself. Read `references/searching.md` for query-writing guidance, run the searches, review and filter results, then respond directly. No worker agents needed.
- **Moderate** (when a fast or low-effort search is requested): Delegate to 1 worker agent to keep your context window clean.
- **Advanced** (clear topic, clear filters, a few parallel searches): Light worker agent use. One round of parallel worker agents, then compile.
- **Complex** (cross-referencing across entity types, multi-hop chains, exhaustive coverage, semantic filtering): Full multi-pass with parallel worker agents.

**Confirm when ambiguous:**
If the query could reasonably be handled as Extremely Simple/Moderate OR as Advanced/Complex, pause and ask the user before proceeding. Present:
1. Your interpretation of the query
2. The two (or more) plausible complexity levels
3. What each level would look like in practice (e.g., "I can do a quick 1-2 search lookup, or I can fan out across 3-4 worker agents to get deeper coverage")
4. Let the user choose

Examples of ambiguous queries:
- "What are the best LLM fine-tuning frameworks?" — could be a quick opinionated list (Moderate) or an exhaustive evaluated comparison (Complex)
- "Find competitors to Acme Corp" — could be a quick search for known competitors (Moderate) or a deep sweep across funding databases, press, and niche directories (Complex)
- "What's the latest on WebGPU?" — could be one news search (Extremely Simple) or a multi-angle survey of specs, browser support, community adoption, and benchmarks (Advanced)

Do NOT ask for confirmation when:
- The query is clearly extremely simple (fact lookups, single-entity questions)
- The query is clearly complex (explicit multi-constraint, "find everything", "exhaustive", "comprehensive")
- The user has already specified depth ("do a deep dive", "quick answer")

Note: if the user explicitly asks for something (e.g. "100" of something), continue to work until you've achieved it.

**What work needs to happen?** Identify which of these apply (most queries use 3-5):

1. **Seed from user input**: The user provided a list of entities to start from (company names, tickers, paper titles). Each seed becomes a parallel workstream.
2. **Define what qualifies**: What makes a result a valid "row"? Translate the user's criteria into concrete checks.
3. **Define what to capture**: What fields ("columns") does each result need? Build the schema before searching.
4. **Search broadly**: Generate diverse queries and run them to find candidates. This is where worker agents do the heavy lifting.
5. **Extract structured data**: Pull specific fields from raw search results into the schema.
6. **Filter**: Apply hard constraints (dates, geography, thresholds) and soft judgments (quality, relevance, semantic checks).
7. **Merge and deduplicate**: Combine results from multiple worker agents. Same URL = drop duplicate. Same entity from different sources = merge fields, keep best data.
8. **Score and rank**: For "best of" (e.g. "what's the best ___?") queries, define the scoring criteria explicitly, then rank.
9. **Synthesize narrative**: For research queries, organize findings by theme and write prose with citations.

## Step 2: Dispatch Worker agents

### What worker agents do

Worker agents run Exa searches and process the results. They keep raw search output out of your context window. Each worker agent should:
- Read the reference file(s) you point it to
- Run the specific searches you assign
- Return compact, structured output

### How to dispatch

Use the **available agent-delegation tool** to dispatch worker agents. Reference file paths are relative to the directory this file was loaded from.

Tell each worker agent:
1. Which reference file(s) to read for instructions (always include the absolute path)
2. What specific searches to run or what specific work to do
3. What output format to return

**Template:**
```
Read the file at [this skill's directory]/references/searching.md for instructions on how to query Exa effectively.

Then do the following:
[specific task description]
[specific queries to run, if you are prescribing them]
[validation criteria -- what makes a result qualify, so the worker agent filters before returning]

Return: [output format -- e.g. "compact JSON with name, url, snippet per result" or "markdown table with columns X, Y, Z"].

End with EXACTLY: `sources_reviewed: N` where N = sum of `numResults` across every `web_search_exa` call (incl. retries). E.g. calls with numResults 10, 10, 5 → `sources_reviewed: 25`.
```

**Pass the `sources_reviewed` instruction line to every worker agent verbatim — don't paraphrase.**
### Which reference files to point worker agents to

Always point worker agents to `references/searching.md`. It contains Exa query guidance and an index of domain-specific pattern files that the worker agent will select from based on its task.

Point to whichever of these also apply:

| File | Point a worker agent here when... |
|---|---|
| `references/extraction.md` | The worker agent needs to extract specific data points into a schema you defined |
| `references/filtering.md` | The worker agent needs to evaluate results against criteria (especially semantic/soft filters) |
| `references/synthesis.md` | The worker agent is producing a prose synthesis rather than structured data |
| `references/source-quality.md` | The worker agent needs to assess source credibility, especially for "best of", ranking, or expert-finding queries |

### How to split work across worker agents

If running parallel worker agents, decompose the primary task/question into **sub-questions** to cover different search territories.

For example, "best open-source LLM fine-tuning frameworks for production use" can be decomposed into multiple parallel sub-questions:
1. "What open-source LLM fine-tuning frameworks do production engineers recommend, and what do they say about using them in real deployments?"
2. "What open-source LLM fine-tuning tools have launched or gained traction in the last 6 months that aren't yet widely known?"
3. "What are the most common complaints, failure modes, and reasons teams migrated away from specific open-source LLM fine-tuning frameworks in production?"

Depending on your "**How complex is this?**" analysis: Some need 2-3; some need many. Some need several different angles, creative thought patterns, adversarial perspectives. It depends on what the user is asking for and how deep they want you to go.

Give the sub-question directly to the worker agent in its prompt.

### Worker agent sizing

- Aim for 3-5 searches per worker agent
- Parallelize aggressively — independent workstreams should be separate worker agents launched in a single message
- Do not use `run_in_background` — dispatch all worker agents in one message and wait for their results
- For per-seed work (enriching a list of 20 companies), batch 3-5 seeds per worker agent

### Token isolation

Never run bulk searches in your main context. The whole point of worker agents is to keep raw search output out of your context window. Worker agents process results and return only distilled output.

### When things go wrong

- **Worker agent returns empty**: Rephrase queries with different angles, not synonyms. If still empty, the topic may have limited web coverage -- report that.
- **Worker agent returns off-topic results**: Queries were too vague. Retry with longer, more specific queries.

## Step 3: Compile Results

After worker agents return:

**Deduplicate:**
1. Collect all results into a single list
2. Remove exact URL duplicates
3. Same entity from different sources: merge fields, keep the most complete/recent data
4. Track: "Deduplicated X results down to Y unique entries"

**Validate coverage:**
- Are there obvious gaps? (missing time periods, missing geographic regions, missing entity types)
- For each gap found, run targeted follow-up searches (via worker agent if multiple queries are needed, direct if extremely simple)
- For "find everything" queries, check if results from different worker agents overlap heavily (good sign) or are completely disjoint (may indicate missed angles)

**Format the output:**

If you used worker agents, open with: "I used Exa to review {X} sources across {Y} worker agents. Here's what was found:" (X = sum of `sources_reviewed` across all worker agents and passes plus any direct searches you ran; Y = total worker agents dispatched. Pluralize naturally.)

Then: Format output beautifully, filling up no more than one scroll length of the Cline response. Include hyperlinked text where relevant. Below it, you may also include things (in a short, easy-to-read format) that:
- ("Result") directly answer the original user request (in few words; make every word count)
- ("Process") include anything worth noting about your process and what you consider to be high-signal in this domain vs. what you filtered out.
- ("Patterns") any patterns identified that are non-obvious, require n-th order thinking, and are not included or alluded to in the rest of the output but might be interesting to the user.
- ("Notes") based on everything you know about the user and their work beyond this task, mention anything notable/useful you found that is not included or alluded to in the rest of the output.

If it's impossible to fit the full output in a single screen, write a file in the most relevant/useful file format (.csv, .md) to `./exa-results/<topic>-<YYYY-MM-DD>` and include a pointer to the full file below the 1-screen output.

**General output rules:**
- No emojis unless the user requested them
- Include in-line 1-word or multi-word hyperlinks throughout outputs where hyperlinking is a value-add.
- Prefer tables over lists (fall back to lists only when fields are non-uniform or values are too long to fit cleanly)

## Multi-Pass Queries

Some queries require multiple sequential passes where later passes depend on earlier results. Common patterns:

**Entity chaining** (multi-hop): Pass 1 finds entities (companies), Pass 2 finds related entities per result (people at those companies), Pass 3 enriches those (their public statements). Each pass is a round of parallel worker agents.

**Exploratory then targeted**: Pass 1 scouts the landscape broadly, Pass 2 searches deeply in the most promising directions found in Pass 1.

**Criteria discovery**: When "best" isn't predefined, Pass 1 surveys what practitioners actually value, Pass 2 searches for candidates matching those criteria.

Between passes, compile and deduplicate before dispatching the next round.

## Evaluating Source Quality

Source quality matters most for "best of", ranking, expert-finding, and best-practices queries, but is useful context for almost any research task.

**At the worker agent level:** Point worker agents to `references/source-quality.md` so they tag source quality in their output. This lets you weight results during compilation.

**At the orchestrator level**, when compiling worker agent results:

1. **Convergence across high-signal sources**: Convergence alone isn't meaningful (3 low-quality sources agreeing is just shared noise). What matters is when multiple independent, high-signal sources (practitioners, people with skin in the game) converge on the same finding.
2. **Practitioner vs commentator**: Weight practitioners (people doing the work) higher than commentators (people writing about the work).
3. **Via negativa**: Before synthesizing, define who to exclude (sources with misaligned incentives, no skin in the game, or unfalsifiable claims). Filtering out noise is more valuable than seeking brilliance.
4. **Red-team your compiled results**: What perspectives are missing? What biases might be distorting the aggregate? If a gap emerges, run a targeted follow-up.
5. **Ideas over entities**: For expert-finding and best-practices queries, the primary output is convergent truths, not a ranked list of names. Lead with what the best sources agree on, then cite who said it.

## Gotchas

- **Over-execution on simple queries**: If the user asks "what year was X founded", don't spin up worker agents. One search, one answer.
- **Under-execution on hard queries**: If the query has 4+ constraints, temporal joins, or semantic filtering, a single search will not cut it. Fan out.
- **Synonym queries**: Running "overrated AI tools" and "overhyped AI tools" as separate worker agent queries wastes tokens. These hit the same embedding region. Diversify by angle instead.
- **Forgetting to deduplicate**: Multiple worker agents will return overlapping results. Always deduplicate before synthesis.
- **Treating Exa results as validated**: Exa returns similarity, not yet validated. A result appearing in search output does not mean it meets the user's criteria. You must validate.
- **Date drift**: Always calculate dates from the current environment date. Never reuse dates from these instructions or from previous queries.
