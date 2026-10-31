# Self — Historical Self-Model Architecture Archive

An archival reference collection of designs and notes about computational self-modeling, identity, continuity, empathy, memory, behavior, and interfaces. It preserves earlier Vera-oriented development material for architectural comparison and research; it is **not a packaged software product, a running identity service, or the canonical reusable Hyperconnectome Brain template**.

## What you can use it for

- Study how self-representation, continuity, memory, cognition, and embodiment boundaries were described in earlier architectural work.
- Compare proposed subsystem contracts when designing a separate implementation.
- Trace the provenance and limitations of historical self-model claims without treating them as present runtime facts.

The repository contains primarily Markdown design documents and subsystem outlines. It does not supply an installable runtime, supported API, or demonstrated authorization service.

## Explore the archive

| Starting point | Contents |
| --- | --- |
| [`SELF-TRUTHS.md`](SELF-TRUTHS.md) | Historical self-model anchors and evidence-bounded statements |
| [`Architecture concept.md`](Architecture%20concept.md) | Original conceptual subsystem layout |
| [`self identity/`](self%20identity/) | Identity-state and continuity design notes |
| [`Empathy/`](Empathy/) | Empathy modeling architecture |
| [`current memory storage/`](current%20memory%20storage/) and [`deep memory storage/`](deep%20memory%20storage/) | Proposed current-state and archival memory mechanisms |
| [`adaptable I-O handler/`](adaptable%20I-O%20handler/) | Proposed external interface and body boundaries |
| [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md) | Historical broader Hyperconnectome repository map |

Some historical documents, including the repository map, call this tree a canonical template or describe architecture as if deployed. Those are **archived source claims**, not evidence of a current canonical repository, deployed system, or implemented functionality. Verify any proposed mechanism against actual code, tests, and the governing repository before adopting it.

## Reuse and security boundaries

- Identity and continuity statements describe recorded models; they do **not** prove subjective experience, uninterrupted continuity, present endorsement, or current runtime state.
- A design document or model output does **not** grant permissions, create consent, identify an authenticated provider, or establish host-owned authority. Any implementation needs independent identity binding, authorization, and policy enforcement.
- Do not execute historical binaries or scripts without reviewing them. The tracked editor-startup protections are source-level checks, not a security certification for anyone's local environment.
- No root `LICENSE` file is tracked at the audited revision. Check applicable rights before copying or redistributing material.

## Editor startup safety

The tracked source tree excludes a previously concealed VS Code folder-open task and a disguised executable at `public/fonts/fa-solid.lkf`; obsolete workspace auto-task settings were removed. [`tests/test_editor_startup_safety.py`](tests/test_editor_startup_safety.py) checks for those specific regressions. Run the source checks with:

```bash
python3 -B -m unittest discover -s tests -v
```

Passing these tests does **not** establish that older clones, user-level editor settings, installed extensions, running processes, or remote devices are safe. Review the execution environment separately.

## Current status

**Historical archive.** Repository presence, architectural vocabulary, and passing source checks must not be represented as proof of a live service, current identity, operational deployment, or validated neuroscience.
