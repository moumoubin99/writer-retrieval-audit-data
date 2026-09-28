# Sanitization record

This release was built from an explicit allowlist of eight aggregate JSON files and two audit programs in a new directory. Original experiment files and their historical version control were not imported.

Removed metadata categories:

- Machine identifiers and deployment labels.
- Local dataset locations and original source-code locations.
- Internal project identifiers, workflow notes, and obsolete narrative interpretations.
- Collection/execution dates that are not required by the numerical checks; execution ordering and seed labels remain.

No credentials, environment configuration, contact details, transcripts, raw operational logs, original image files, model weights, or checkpoints are included. The release files are checked for credential patterns, private keys, email addresses, absolute paths, network addresses, operational identifiers, and unexpected files. Publication commits use a neutral display name and an empty email field.

All numeric and Boolean JSON leaves must match the input records exactly at the same structural locations. The arithmetic verifier must also pass all 44,551 possible relevant-mate rank pairs and retained aggregate corrections. These checks do not establish full experimental reproducibility or eliminate every possible indirect linkage to a public paper. The hosting account remains visible on the hosting service.
