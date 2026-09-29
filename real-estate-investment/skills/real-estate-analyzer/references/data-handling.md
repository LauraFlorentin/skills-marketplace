# Data Handling

Use this reference whenever a request includes deal documents, tenant or
investor information, financial records, credentials, or an external data
service.

## Minimize and classify

Collect only information needed for the stated decision. Classify each item as
public, confidential business information, personal information, financial
account information, credential, or regulated/sensitive information under the
applicable policy and law.

Prefer a property identifier, summarized operating data, and redacted document
excerpt over full rent rolls, bank statements, investor lists, tax returns,
identity documents, or account numbers. Do not request passwords, API keys,
government ID numbers, full bank details, or sensitive personal information.

## Before external use

Before uploading, transmitting, or querying an external service:

1. Confirm the user is authorized to share the information.
2. Confirm the provider's terms, data location, retention, and permitted use.
3. Send the minimum necessary data; remove personal and account identifiers.
4. Record which source was used, why it was needed, and when it was retrieved.
5. Never place credentials in prompts, repository files, templates, logs, or
   generated deliverables.

Use public sources for public facts. Treat a listing, broker presentation, or
platform entry as non-public only if its owner and terms permit the intended
use; otherwise corroborate it without redistributing it.

## Storage and outputs

Keep completed deal materials in an authorized private location, not the
plugin repository. In analysis outputs, replace names and account numbers with
roles or redacted identifiers unless their inclusion is necessary and approved.
State the source date, retrieval date, and any redaction that affects the
analysis.

If a user asks to retain, share, or publish sensitive material, explain the
scope, recipients, and irreversible effects first. Never treat this plugin as
a secure data room, a document-management system, or a substitute for a
privacy, security, legal, or compliance review.
