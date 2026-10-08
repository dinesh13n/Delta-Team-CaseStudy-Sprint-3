# Prompt given to Model B (verbatim), Stage Q1
Agent type general-purpose, model override `haiku` (resolved by the runtime to `claude-haiku-5-5`, see EVD-Q-05-model-b-transcript.jsonl), foreground, single attempt.
Sampling settings: runtime defaults (not set by the operator). UNKNOWN beyond that.

You are "Model B" in a controlled software portability test. Read and follow this file completely first:
<scratchpad>/q1/bundle/BUILD-BRIEF.md   (preserved as EVD-Q-04-build-brief.md)

The input bundle (the ONLY source material you may read) is the directory <scratchpad>/q1/bundle (referred to in the brief as "this directory").
Your build directory (<BUILD>) is: <scratchpad>/q1/modelb_build (create it; write everything you produce only there).
Python interpreter with all allowed packages: /tmp/v311/bin/python (use `/tmp/v311/bin/python -m pytest`, `/tmp/v311/bin/python -m uvicorn`). No network access.

Hard rules: read nothing outside the bundle directory, your build directory and the installed Python packages. In particular do not search the filesystem for any existing implementation, repository, evidence, evaluation or test files of this system; do not run git. Do not ask questions; make the most defensible decision when the specification is silent and record it in <BUILD>/NOTES.md. Build all four behaviours and the delivery contract exactly as the brief fixes it (app/main.py exposing `app`, app/adapter.py with summarize_case, your own tests, NOTES.md). Run your own tests and make sure `uvicorn app.main:app` actually starts with the environment variables listed in the brief (APP_ENV=local, AUTH_SECRET, DATA_DIR pointing at a directory containing curated/*.csv, SEMANTIC_LAYER_DIR, AUDIT_PATH, APPROVALS_PATH).

When done, reply with: (1) the list of files you created, (2) the paths you read (directories are fine), (3) your own test result summary, (4) anything you did not implement, (5) the top ambiguities you hit. Keep the reply under 400 words.

(<scratchpad> stands for the session scratchpad directory. Run: started 2026-10-08T13:09Z, finished 13:47Z; 31 tool calls; 235,628 tokens; 37.6 minutes wall.)
