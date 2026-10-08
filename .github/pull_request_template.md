## What and why
<!-- one paragraph; reference finding IDs (F-xx) and runbook step -->

## Gates (transformation-gates.md TG-1..TG-9)
- [ ] TG-1 characterization suite green, or each difference listed as an APPROVED CHANGE with a spec clause
- [ ] TG-2 tests green (`make test`)
- [ ] TG-3 `make lint` and `make type` clean (or waiver with owner)
- [ ] TG-4 `make secrets` clean
- [ ] TG-5 semantic-layer tests green
- [ ] TG-6 fixture `data/synthetic` untouched
- [ ] TG-8 evidence produced and registered in the folder MANIFEST.md
- [ ] TG-9 `make smoke` (includes OpenAPI route diff)

## Behaviour change?
<!-- If yes: flag name, rollback step, entry in docs/15-modernization/approved-behavior-changes.md -->

## Risk and rollback
