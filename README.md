# log-report

A corrected TB2 Harbor task that parses an Apache-style access log into a JSON summary.

## Requirements

- Docker
- Harbor

## Verify

From the directory containing `log-report/`:

```bash
harbor run -p log-report -a oracle
harbor run -p log-report --agent nop
```

The oracle run should receive reward `1`; the no-op agent should receive reward `0`.
