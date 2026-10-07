# knos-e2e-202610020610
Knos 0.3.9 release E2E

Knos 0.3.15 rehearsal (neutral re-execution): `.github/workflows/knos.yml` calls the workflows at commit
`202c70754fdfee52dd2f00c614867b0a490c78e5`, which is drexthealpha/knos-workflows-rc@202c70754fdfee52dd2f00c614867b0a490c78e5 (the 0.3.15 tree's workflows built on the staging programs),
pushed here unchanged as the branch `knos-workflows-rc` so that a public repository can call them. Devnet, test money.

Knos 0.3.18 staging run on the PUBLIC program ids: `.github/workflows/knos.yml` and `knos-check.yml` call the workflows at
commit `c4a1f19d4d65f74b47ca3148701cece98a9e30e4`, which is drexthealpha/knos-workflows-rc@c4a1f19d4d65f74b47ca3148701cece98a9e30e4 (the 0.3.18 tree's workflows, knos installed from
drexthealpha/knos-rc@023e6ac), pushed here unchanged as the branch `knos-workflows-0318` so that a repository can call
them. Devnet, test money.
