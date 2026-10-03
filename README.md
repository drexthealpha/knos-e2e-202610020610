# knos-workflows

> **REHEARSAL VARIANT.** These are not the published workflows: knos is installed from
> `git+https://github.com/drexthealpha/knos-rc@f13bf01acccd0aa4320eff2501a7618b96015358`
> instead of the PyPI release. For a staging repository only: a bounty funded through these files is pinned
> to this repository's commit, not to the published one.

The workflows that [Knos](https://github.com/drexthealpha/Knos) bounties pin by commit. A comment funds an issue,
and the pull request that closes it is paid from an escrow on Solana when GitHub itself signs the facts. A bounty on
chain names this repository and one commit of it: the commit its `fund.yml` ran at. Only `prove.yml` of this
repository at that same commit can pay it.

| File | Called for | Runs |
|---|---|---|
| `.github/workflows/fund.yml` | a `/knos` comment, or a new issue that funds itself | `knos command` |
| `.github/workflows/prove.yml` | a merge, a run started by hand, `/knos settle`, and the review after the check | `knos settle`, `knos review`, `knos proof judge` |
| `.github/workflows/check.yml` | every pull request (optional, read-only) | `knos check` |

Call them by a full commit sha, never by a branch or a tag. The workflows take no inputs, and every job installs
knos from the rehearsal source named above, so a caller cannot change which code judges.

The files to copy into your repository (`knos.yml`, and optionally `knos-check.yml`) are in
[drexthealpha/Knos/examples](https://github.com/drexthealpha/Knos/tree/main/examples). Their comments say what each
trigger does and what the file can and cannot do in your repository.

Nothing is edited here. These files are copied from `.github/workflows/` in drexthealpha/Knos at a release, where they
are tested. In a checkout of that repository, `python scripts/pinned_workflows.py check <a checkout of this one>`
shows that this copy is the same, byte for byte.
