````markdown
# CONSTITUTIONAL LAYER MAP

## NICAI Hydro — Constitutional Runtime Convergence

**Participant:** `NICAI.HYDRO`  
**Repository:** `nicai-validation-layer_1`  
**Path:** `constitutional_runtime/review/CONSTITUTIONAL_LAYER_MAP.md`  
**Document Type:** Constitutional Runtime Validation  
**Purpose:** Map every Hydro capability to its appropriate BHIV constitutional layer.  
**Certification Principle:** Evidence-backed and independently verifiable.

---

# 1. Purpose

This document defines the constitutional layer placement of the NICAI Hydro
runtime and its capabilities.

The purpose of this mapping is to establish:

- where each Hydro capability belongs;
- why each capability belongs in that layer;
- what authority the capability possesses;
- what authority the capability does not possess;
- which constitutional participants interact with the capability;
- which runtime boundaries apply;
- which evidence is required for validation;
- whether the capability is demonstrated or certified.

The mapping is intended to prevent:

- undocumented capabilities;
- duplicate responsibilities;
- ambiguous ownership;
- authority overlap;
- uncontrolled runtime attachment;
- unversioned integration;
- hidden constitutional dependencies.

NICAI Hydro is treated as a **Constitutional Runtime Participant**, not as an
independent constitutional authority.

---

# 2. Constitutional Layer Model

For the purpose of this validation, the BHIV constitutional runtime is
represented through the following layers:

```text
SOVEREIGN FOUNDATION
        |
        v
GOVERNANCE & CONSTITUTION
        |
        v
PLATFORM SERVICES
        |
        v
EXECUTION INFRASTRUCTURE
        |
        v
INTELLIGENCE LAYER
        |
        v
KNOWLEDGE LAYER
        |
        v
TRUST LAYER
        |
        v
MARITIME DOMAIN PRODUCTS
````

These layers are logical constitutional boundaries.

They are not interpreted as independent applications or separate repositories.

A capability may interact with multiple layers while retaining exactly one
primary constitutional placement.

---

# 3. Primary Constitutional Placement Rule

Every Hydro capability must have:

```text
ONE PRIMARY CONSTITUTIONAL LAYER
+
ONE PERMANENT IDENTITY
+
ONE PRIMARY AUTHORITY OWNER
```

Interaction with another layer does not create a second ownership boundary.

For example:

```text
Hydro Intelligence Capability
        |
        +--> PRIMARY: Intelligence Layer
        |
        +--> consumes: Knowledge Layer
        |
        +--> produces evidence for: Trust Layer
        |
        +--> serves: Maritime Domain Products
```

The consuming or producing relationship does not change the primary layer.

---

# 4. Constitutional Placement Principles

Hydro capability placement follows these principles.

## 4.1 Identity Principle

Every capability must be uniquely identifiable.

A capability must not exist simultaneously under multiple constitutional
identities.

---

## 4.2 Authority Principle

A capability may only exercise authority explicitly assigned to it.

Hydro must not assume authority belonging to:

* governance;
* registry ownership;
* sovereign foundation;
* external domain owners;
* downstream operators;
* independent validation authorities.

---

## 4.3 Responsibility Principle

A capability must remain within its documented responsibility.

A runtime participant must not create a duplicate capability merely because
another participant already provides the same responsibility.

---

## 4.4 Evidence Principle

A constitutional placement must be supported by implementation and runtime
evidence where the claim is presented as verified.

Architecture documentation alone does not prove runtime execution.

---

## 4.5 Determinism Principle

Runtime interactions must be deterministic wherever the existing contract
requires deterministic behaviour.

The constitutional layer assignment must therefore identify:

* input boundary;
* execution boundary;
* output boundary;
* event boundary;
* trace boundary.

---

# 5. Hydro Constitutional Participant

The primary participant represented by this document is:

```text
Participant ID:
NICAI.HYDRO

Participant Type:
CONSTITUTIONAL_RUNTIME_PARTICIPANT

Domain:
HYDRO / MARITIME INTELLIGENCE

Primary Constitutional Layer:
INTELLIGENCE_LAYER
```

The participant operates within the constitutional runtime while interacting
with platform, execution, knowledge, trust, and maritime-domain boundaries.

---

# 6. Hydro Capability Classes

The Hydro runtime is mapped into the following capability classes:

| Capability ID         | Capability                      | Primary Layer             |
| --------------------- | ------------------------------- | ------------------------- |
| `HYDRO.RUNTIME`       | Hydro runtime participant       | Execution Infrastructure  |
| `HYDRO.IDENTITY`      | Constitutional runtime identity | Governance & Constitution |
| `HYDRO.EVALUATION`    | Hydro intelligence evaluation   | Intelligence Layer        |
| `HYDRO.VALIDATION`    | Contract/runtime validation     | Governance & Constitution |
| `HYDRO.PERCEPTION`    | Perception evidence processing  | Intelligence Layer        |
| `HYDRO.INTELLIGENCE`  | Intelligence generation         | Intelligence Layer        |
| `HYDRO.STATE`         | Hydro state interpretation      | Intelligence Layer        |
| `HYDRO.PATTERN`       | Pattern/anomaly interpretation  | Intelligence Layer        |
| `HYDRO.ACTION`        | Action eligibility output       | Intelligence Layer        |
| `HYDRO.TRACE`         | Execution trace inspection      | Trust Layer               |
| `HYDRO.REPLAY`        | Replay verification             | Trust Layer               |
| `HYDRO.OBSERVABILITY` | Runtime observability           | Trust Layer               |
| `HYDRO.HEALTH`        | Runtime health                  | Execution Infrastructure  |
| `HYDRO.REGISTRY`      | Registry participation          | Governance & Constitution |
| `HYDRO.KNOWLEDGE`     | Knowledge interaction           | Knowledge Layer           |
| `HYDRO.DOMAIN_OUTPUT` | Maritime consumer output        | Maritime Domain Products  |

---

# 7. Layer 1 — Sovereign Foundation

## 7.1 Layer Definition

The Sovereign Foundation represents the foundational authority and identity
boundary of the constitutional ecosystem.

It establishes the root environment in which constitutional participants operate.

---

## 7.2 Hydro Relationship

NICAI Hydro does **not** own sovereign authority.

Hydro operates under the sovereign foundation rather than replacing or
duplicating it.

---

## 7.3 Hydro Authority Owned

Hydro may own:

* its participant identity reference;
* its declared runtime identity;
* its declared capability metadata.

---

## 7.4 Hydro Authority Not Owned

Hydro does not own:

* sovereign identity;
* ecosystem-wide authority;
* constitutional root authority;
* sovereign governance;
* ecosystem-wide security policy.

---

## 7.5 Hydro Relationship

```text
Sovereign Foundation
        |
        | governs
        v
NICAI.HYDRO
```

---

## 7.6 Validation Requirement

The validation requirement is:

```text
Hydro identity must be compatible with the constitutional runtime identity
model.
```

Evidence must be based on the actual identity and registry structures used by
the runtime.

---

# 8. Layer 2 — Governance & Constitution

## 8.1 Layer Definition

The Governance & Constitution layer defines:

* constitutional rules;
* authority boundaries;
* contract governance;
* participant responsibilities;
* registration requirements;
* review requirements.

---

## 8.2 Hydro Capabilities Assigned

The following Hydro capabilities interact primarily with this layer:

```text
HYDRO.IDENTITY
HYDRO.VALIDATION
HYDRO.REGISTRY
```

---

## 8.3 HYDRO.IDENTITY

### Purpose

Maintain the permanent constitutional identity of the Hydro runtime participant.

### Primary Layer

```text
GOVERNANCE & CONSTITUTION
```

### Authority Owned

* Hydro participant identity;
* Hydro capability identity references;
* Hydro constitutional metadata.

### Authority Not Owned

* ecosystem-wide participant identity;
* constitutional policy;
* sovereign authority;
* identities of external participants.

---

## 8.4 HYDRO.VALIDATION

### Purpose

Validate defined runtime and contract interactions.

### Primary Layer

```text
GOVERNANCE & CONSTITUTION
```

### Authority Owned

* Hydro-side contract validation;
* Hydro-side validation evidence;
* validation status generated by the Hydro runtime.

### Authority Not Owned

* final ecosystem-wide constitutional authority;
* external participant certification;
* sovereign governance decisions.

---

## 8.5 HYDRO.REGISTRY

### Purpose

Participate in required constitutional registries.

### Primary Layer

```text
GOVERNANCE & CONSTITUTION
```

### Required Registry Relationships

```text
Capability Registry
Runtime Registry
Execution Registry
Replay Registry
Repository Registry
Review Registry
Build Registry
Migration Registry
```

Hydro must be represented in each registry only where the registry is part of
the applicable constitutional runtime contract.

---

## 8.6 Governance Relationship

```text
Governance & Constitution
          |
          +--> defines rules
          |
          +--> defines authority
          |
          +--> defines registration
          |
          +--> validates contracts
          |
          v
       NICAI.HYDRO
```

Hydro consumes governance constraints and produces Hydro-specific compliance
evidence.

---

# 9. Layer 3 — Platform Services

## 9.1 Layer Definition

Platform Services provide shared ecosystem services required by constitutional
participants.

These may include shared:

* runtime services;
* registries;
* service discovery;
* attachment mechanisms;
* configuration;
* shared integration infrastructure.

---

## 9.2 Hydro Relationship

Hydro is a consumer and participant of platform services.

Hydro must not duplicate platform capabilities.

---

## 9.3 Hydro Authority Owned

Hydro owns:

* Hydro-specific integration configuration;
* Hydro-specific contract attachment;
* Hydro-specific capability metadata.

---

## 9.4 Hydro Authority Not Owned

Hydro does not own:

* shared platform service governance;
* ecosystem-wide service discovery;
* platform-wide registry semantics;
* platform-wide configuration policy.

---

## 9.5 Platform Relationship

```text
Platform Services
       |
       +--> discovery
       |
       +--> attachment
       |
       +--> shared services
       |
       v
NICAI.HYDRO
```

---

# 10. Layer 4 — Execution Infrastructure

## 10.1 Layer Definition

Execution Infrastructure represents the runtime environment responsible for
running Hydro services and exposing operational runtime surfaces.

---

## 10.2 Hydro Capabilities Assigned

```text
HYDRO.RUNTIME
HYDRO.HEALTH
```

---

## 10.3 HYDRO.RUNTIME

### Purpose

Provide the executable Hydro runtime participant.

### Primary Layer

```text
EXECUTION INFRASTRUCTURE
```

### Runtime Surface

The currently observed runtime includes:

```text
GET /
GET /health
POST /nicai/evaluate
POST /contract/validate
GET /trace/{trace_id}
```

The existence of an endpoint is treated as runtime evidence of availability,
not automatically as proof of constitutional certification.

---

## 10.4 HYDRO.HEALTH

### Purpose

Expose measurable runtime health.

### Primary Layer

```text
EXECUTION INFRASTRUCTURE
```

### Runtime Surface

```text
GET /health
```

### Authority Owned

* Hydro runtime health status;
* Hydro service availability status.

### Authority Not Owned

* health of external participants;
* ecosystem-wide health;
* constitutional certification.

---

# 11. Execution Boundary

The Hydro execution boundary is:

```text
Request
   |
   v
Hydro Runtime
   |
   +--> Evaluation
   |
   +--> Validation
   |
   +--> Event Generation
   |
   +--> Trace Evidence
   |
   v
Response
```

External participants must interact through defined contracts.

Internal implementation details are not constitutional integration contracts
unless explicitly exposed as such.

---

# 12. Layer 5 — Intelligence Layer

## 12.1 Layer Definition

The Intelligence Layer contains capabilities that transform validated input
and available knowledge into explainable Hydro intelligence.

---

## 12.2 Primary Hydro Layer

```text
INTELLIGENCE LAYER
```

This is the primary constitutional domain of NICAI Hydro.

---

## 12.3 Hydro Capabilities Assigned

```text
HYDRO.EVALUATION
HYDRO.PERCEPTION
HYDRO.INTELLIGENCE
HYDRO.STATE
HYDRO.PATTERN
HYDRO.ACTION
```

---

# 13. HYDRO.EVALUATION

## 13.1 Purpose

Execute the Hydro intelligence evaluation workflow.

---

## 13.2 Primary Layer

```text
INTELLIGENCE LAYER
```

---

## 13.3 Runtime Surface

```text
POST /nicai/evaluate
```

---

## 13.4 Inputs

The exact request schema must be taken from the implemented API contract.

The constitutional layer mapping does not invent additional request fields.

---

## 13.5 Outputs

Observed Hydro execution evidence includes structured components such as:

```text
perception_event
validation
intelligence_event
state_event
```

---

## 13.6 Authority Owned

* Hydro intelligence evaluation;
* Hydro-derived intelligence output;
* Hydro-specific interpretation.

---

## 13.7 Authority Not Owned

* sovereign decision authority;
* external operational command authority;
* final human/operator authority;
* authority belonging to external domain participants.

---

# 14. HYDRO.PERCEPTION

## 14.1 Purpose

Represent perception-level evidence entering the Hydro intelligence workflow.

---

## 14.2 Primary Layer

```text
INTELLIGENCE LAYER
```

---

## 14.3 Observed Evidence

Observed output examples include:

```json
{
  "trace_id": "cargo-1",
  "vessel_type": "cargo",
  "confidence_score": 0.6396,
  "dominant_freq_hz": 98.0,
  "anomaly_flag": false
}
```

---

## 14.4 Authority Boundary

Hydro may interpret the perception evidence within its intelligence contract.

Hydro does not automatically become the authoritative owner of the original
sensor or external source.

---

# 15. HYDRO.INTELLIGENCE

## 15.1 Purpose

Generate Hydro intelligence from available validated evidence.

---

## 15.2 Primary Layer

```text
INTELLIGENCE LAYER
```

---

## 15.3 Observed Evidence

Example observed intelligence output:

```json
{
  "trace_id": "cargo-1",
  "vessel_type": "cargo",
  "confidence": 0.6396,
  "risk_level": "MEDIUM",
  "validation_status": "ALLOW"
}
```

---

## 15.4 Authority Owned

* Hydro intelligence interpretation;
* Hydro-specific risk classification;
* Hydro-specific intelligence state.

---

## 15.5 Authority Not Owned

* ecosystem-wide risk authority;
* regulatory authority;
* operational command authority;
* external participant authority.

---

# 16. HYDRO.STATE

## 16.1 Purpose

Translate Hydro intelligence into the defined Hydro state representation.

---

## 16.2 Primary Layer

```text
INTELLIGENCE LAYER
```

---

## 16.3 Observed Evidence

Example:

```json
{
  "trace_id": "cargo-1",
  "vessel_type": "cargo",
  "risk_level": "MEDIUM",
  "state": "WARNING",
  "anomaly_flag": false,
  "short_label": "Watch"
}
```

---

## 16.4 Authority Boundary

The state is a Hydro runtime/intelligence output.

It does not automatically represent a command or regulatory decision.

---

# 17. HYDRO.PATTERN

## 17.1 Purpose

Represent detected or derived anomaly/pattern information.

---

## 17.2 Primary Layer

```text
INTELLIGENCE LAYER
```

---

## 17.3 Observed Evidence

Observed pattern event structures include:

```json
{
  "type": "PATTERN",
  "data": {
    "pattern_id": "PATTERN_7b0ff5",
    "anomaly_count": 3,
    "affected_zones": ["North"],
    "pattern_type": "REPEATED_ANOMALY",
    "severity_trend": "STABLE"
  }
}
```

---

## 17.4 Authority Boundary

Hydro may produce pattern intelligence according to its contract.

Pattern intelligence must not be interpreted as an independent sovereign or
regulatory command.

---

# 18. HYDRO.ACTION

## 18.1 Purpose

Represent Hydro-generated action eligibility or action-related intelligence.

---

## 18.2 Primary Layer

```text
INTELLIGENCE LAYER
```

---

## 18.3 Observed Evidence

An observed action event includes:

```json
{
  "type": "ACTION",
  "data": {
    "action_type": "eligible_for_escalation",
    "target_role": "authority"
  }
}
```

---

## 18.4 Authority Boundary

Hydro may identify an action as eligible according to its intelligence
contract.

Hydro does not automatically execute external authority actions unless an
explicit runtime contract grants that authority.

---

# 19. Intelligence Layer Boundary

The Hydro Intelligence Layer boundary is:

```text
Evidence
   |
   v
Perception
   |
   v
Validation
   |
   v
Intelligence
   |
   v
Pattern / State
   |
   v
Action Eligibility
```

The intelligence layer produces information and intelligence.

Operational authority remains with the designated downstream authority.

---

# 20. Layer 6 — Knowledge Layer

## 20.1 Layer Definition

The Knowledge Layer provides authoritative or governed knowledge required by
intelligence participants.

---

## 20.2 Hydro Relationship

Hydro may consume or contribute knowledge through explicit contracts.

Hydro does not automatically become the owner of ecosystem-wide knowledge.

---

## 20.3 Hydro Capability

```text
HYDRO.KNOWLEDGE
```

Primary layer:

```text
KNOWLEDGE LAYER
```

---

## 20.4 Knowledge Inputs

Potential knowledge relationships must be represented through explicit
contracts.

Examples include:

```text
Hydro intelligence
      |
      +--> consumes governed knowledge
      |
      +--> produces derived intelligence
```

The exact knowledge source must be independently verified before being listed
as a certified dependency.

---

## 20.5 Knowledge Authority

Hydro owns:

* Hydro-derived knowledge contribution;
* Hydro-specific interpretation.

Hydro does not own:

* external authoritative datasets;
* ecosystem-wide semantic governance;
* external knowledge authority.

---

# 21. Layer 7 — Trust Layer

## 21.1 Layer Definition

The Trust Layer provides evidence, traceability, replayability, validation
history, and observability required to establish confidence in runtime
execution.

---

## 21.2 Hydro Capabilities Assigned

```text
HYDRO.TRACE
HYDRO.REPLAY
HYDRO.OBSERVABILITY
```

---

# 22. HYDRO.TRACE

## 22.1 Purpose

Provide trace inspection for Hydro execution evidence.

---

## 22.2 Primary Layer

```text
TRUST LAYER
```

---

## 22.3 Runtime Surface

```text
GET /trace/{trace_id}
```

---

## 22.4 Trace Evidence

The trace inspection endpoint returns information such as:

```text
trace_id
found_stages
missing_stages
ordered_replay
sequence_chain
replay_status
```

---

## 22.5 Certification Boundary

A successful trace lookup demonstrates trace inspection availability.

It does not by itself prove:

* complete trace propagation;
* deterministic trace generation;
* complete replay;
* replay equivalence.

Those require separate evidence.

---

# 23. HYDRO.REPLAY

## 23.1 Purpose

Verify whether a Hydro execution can be reconstructed from available evidence.

---

## 23.2 Primary Layer

```text
TRUST LAYER
```

---

## 23.3 Replay Evidence

Replay evidence may include:

```text
found_stages
missing_stages
ordered_replay
sequence_chain
replay_status
```

---

## 23.4 Replay Boundary

Replay must be distinguished from ordinary trace lookup.

```text
TRACE LOOKUP
     !=
REPLAY RECONSTRUCTION
     !=
REPLAY EQUIVALENCE
```

Each claim requires independent evidence.

---

# 24. HYDRO.OBSERVABILITY

## 24.1 Purpose

Expose structured runtime evidence sufficient to inspect Hydro execution.

---

## 24.2 Primary Layer

```text
TRUST LAYER
```

---

## 24.3 Observed Evidence

Observed structured events include:

```text
PATTERN
ACTION
```

Hydro execution outputs also expose structured intelligence evidence.

---

## 24.4 Observability Boundary

Observability demonstrates runtime evidence availability.

It does not automatically prove complete constitutional execution.

---

````markdown
# 25. Layer 7 — Trust Layer (Continued)

## 25.1 Trust Boundary

The Trust Layer is responsible for preserving confidence in runtime execution
through evidence and traceability.

Hydro participates in this layer through:

```text
HYDRO.TRACE
HYDRO.REPLAY
HYDRO.OBSERVABILITY
````

The Trust Layer does not replace Hydro intelligence.

It records and exposes evidence about Hydro execution.

---

# 26. Layer 8 — Maritime Domain Products

## 26.1 Layer Definition

The Maritime Domain Products layer represents downstream operational and
domain-specific products that consume Hydro intelligence.

---

## 26.2 Hydro Relationship

Hydro acts primarily as an intelligence provider to maritime-domain consumers.

Hydro does not own every downstream maritime product.

---

## 26.3 Hydro Capability

```text
HYDRO.DOMAIN_OUTPUT
```

Primary layer:

```text
MARITIME DOMAIN PRODUCTS
```

---

## 26.4 Domain Output Boundary

The Hydro domain output boundary is:

```text
Hydro Intelligence
        |
        v
Domain Output Contract
        |
        v
Maritime Consumer
```

The downstream consumer remains responsible for its own domain decisions.

---

# 27. Cross-Layer Hydro Architecture

The complete Hydro constitutional relationship can be represented as:

```text
                    SOVEREIGN FOUNDATION
                            |
                            v
                 GOVERNANCE & CONSTITUTION
                            |
                            v
                    PLATFORM SERVICES
                            |
                            v
                 EXECUTION INFRASTRUCTURE
                            |
                            v
                    INTELLIGENCE LAYER
                            |
                +-----------+-----------+
                |           |           |
                v           v           v
           PERCEPTION  INTELLIGENCE   STATE
                |           |           |
                +-----------+-----------+
                            |
                            v
                     PATTERN / ACTION
                            |
                +-----------+-----------+
                |                       |
                v                       v
         KNOWLEDGE LAYER          TRUST LAYER
                |                       |
                |              +--------+--------+
                |              |        |        |
                |              v        v        v
                |           TRACE     REPLAY  OBSERVABILITY
                |                       |
                +-----------+-----------+
                            |
                            v
                MARITIME DOMAIN PRODUCTS
```

---

# 28. Primary Layer Assignment Matrix

| Capability            | Primary Layer             | Secondary Interaction    | Authority                    |
| --------------------- | ------------------------- | ------------------------ | ---------------------------- |
| `HYDRO.RUNTIME`       | Execution Infrastructure  | Platform Services        | Hydro runtime                |
| `HYDRO.IDENTITY`      | Governance & Constitution | Sovereign Foundation     | Hydro identity               |
| `HYDRO.EVALUATION`    | Intelligence Layer        | Execution Infrastructure | Hydro intelligence           |
| `HYDRO.VALIDATION`    | Governance & Constitution | Trust Layer              | Hydro validation             |
| `HYDRO.PERCEPTION`    | Intelligence Layer        | Knowledge / Trust        | Hydro interpretation         |
| `HYDRO.INTELLIGENCE`  | Intelligence Layer        | Knowledge / Trust        | Hydro intelligence           |
| `HYDRO.STATE`         | Intelligence Layer        | Maritime Domain          | Hydro state output           |
| `HYDRO.PATTERN`       | Intelligence Layer        | Trust / Domain           | Hydro pattern intelligence   |
| `HYDRO.ACTION`        | Intelligence Layer        | Maritime Domain          | Action eligibility           |
| `HYDRO.TRACE`         | Trust Layer               | Execution Infrastructure | Trace evidence               |
| `HYDRO.REPLAY`        | Trust Layer               | Execution Infrastructure | Replay evidence              |
| `HYDRO.OBSERVABILITY` | Trust Layer               | Execution Infrastructure | Observability evidence       |
| `HYDRO.HEALTH`        | Execution Infrastructure  | Trust Layer              | Runtime health               |
| `HYDRO.REGISTRY`      | Governance & Constitution | Platform Services        | Hydro registration           |
| `HYDRO.KNOWLEDGE`     | Knowledge Layer           | Intelligence Layer       | Hydro knowledge contribution |
| `HYDRO.DOMAIN_OUTPUT` | Maritime Domain Products  | Intelligence Layer       | Hydro domain output          |

---

# 29. Constitutional Layer Ownership Model

The ownership model is:

```text
Sovereign Foundation
    |
    +-- owns sovereign authority

Governance & Constitution
    |
    +-- owns constitutional governance

Platform Services
    |
    +-- owns shared runtime/platform services

Execution Infrastructure
    |
    +-- owns execution environment

Intelligence Layer
    |
    +-- owns intelligence capabilities

Knowledge Layer
    |
    +-- owns governed knowledge

Trust Layer
    |
    +-- owns evidence/trust mechanisms

Maritime Domain Products
    |
    +-- owns downstream domain products
```

NICAI Hydro participates within these boundaries.

It must not claim ownership of another layer merely because it interacts with
that layer.

---

# 30. Hydro Primary Authority

NICAI Hydro's primary authority is limited to:

```text
Hydro Runtime
+
Hydro Intelligence
+
Hydro Validation
+
Hydro Evidence
+
Hydro Runtime Health
```

This authority is bounded by the applicable constitutional contracts.

---

# 31. Hydro Explicitly Does Not Own

NICAI Hydro does not own:

```text
Sovereign Authority
Constitutional Governance
Ecosystem-wide Registry Governance
External Participant Authority
External Operational Command
External Regulatory Authority
External Dataset Ownership
Downstream Product Ownership
```

Any external authority must remain with its designated owner.

---

# 32. Upstream Dependency Model

Hydro receives dependencies from upstream participants.

The generic dependency model is:

```text
Upstream Participant
        |
        v
Defined Contract
        |
        v
NICAI.HYDRO
```

An upstream dependency must be documented with:

* participant identity;
* capability identity;
* contract;
* version;
* input schema;
* event relationship;
* failure behaviour.

---

# 33. Downstream Dependency Model

Hydro provides intelligence to downstream participants.

The model is:

```text
NICAI.HYDRO
        |
        v
Defined Output Contract
        |
        v
Downstream Consumer
```

The downstream participant remains responsible for its own authority.

---

# 34. Adjacent Participant Model

Hydro may interact with adjacent participants including:

```text
TMS
GC
MDU
GOUDHA Runtime
Namami Gange
SVACS
Bucket
Runtime Registry
Capability Registry
Replay Registry
InsightFlow
PRANA
BHEX Knowledge Layer
```

These names represent integration points specified by the convergence task.

Their exact runtime participation must be independently verified before being
marked as runtime-certified dependencies.

---

# 35. Integration Relationship Classification

Every external relationship should be classified as one of:

```text
PROVIDER
CONSUMER
VALIDATOR
REGISTRY
EXECUTOR
OBSERVER
KNOWLEDGE_SOURCE
KNOWLEDGE_CONSUMER
DOMAIN_CONSUMER
TRUST_PARTICIPANT
```

A participant may have more than one relationship type.

However, each relationship must have an explicit contract.

---

# 36. TMS Relationship

## Role

TMS is treated as an external ecosystem integration point.

## Hydro Boundary

Hydro must not assume TMS authority.

## Relationship

```text
TMS
 |
 | defined integration contract
 v
NICAI.HYDRO
```

## Certification Requirement

The actual runtime contract must be verified before claiming live TMS
integration certification.

---

# 37. GC Relationship

## Role

GC is an external ecosystem integration point.

## Hydro Boundary

Hydro does not own GC responsibilities.

## Relationship

```text
GC
 |
 | governed runtime relationship
 v
NICAI.HYDRO
```

The exact runtime interface must be verified independently.

---

# 38. MDU Relationship

## Role

MDU represents a maritime-domain integration boundary.

## Hydro Relationship

Hydro may provide intelligence to MDU through a defined contract.

```text
NICAI.HYDRO
       |
       v
Hydro Intelligence Output
       |
       v
MDU
```

MDU remains responsible for its own downstream domain authority.

---

# 39. GOUDHA Runtime Relationship

GOUDHA Runtime is an external runtime participant.

Hydro may interact with it only through an explicit runtime contract.

```text
GOUDHA Runtime
       |
       | contract
       v
NICAI.HYDRO
```

or:

```text
NICAI.HYDRO
       |
       | contract
       v
GOUDHA Runtime
```

depending on the verified direction of execution.

The direction must not be inferred from architecture names alone.

---

# 40. Namami Gange Relationship

Namami Gange is an important Hydro domain integration point.

Hydro may provide intelligence relevant to Namami Gange workflows.

The relationship must remain contract-driven:

```text
NICAI.HYDRO
       |
       v
Namami Gange Consumer
```

Hydro does not assume ownership of Namami Gange operational governance.

---

# 41. SVACS Relationship

SVACS represents a validation-related integration boundary.

Hydro may provide evidence to SVACS and may consume validation outcomes where
the contract requires it.

The conceptual relationship is:

```text
NICAI.HYDRO
       |
       +--> validation evidence
       |
       v
SVACS
```

The exact runtime contract must be verified before certification.

---

# 42. Bucket Relationship

Bucket is treated as an ecosystem integration point.

Hydro may interact with Bucket through a defined runtime or data contract.

Hydro must not duplicate Bucket-owned responsibilities.

---

# 43. Registry Relationships

Hydro must participate in applicable constitutional registries.

Required registry classes include:

```text
Capability Registry
Runtime Registry
Execution Registry
Replay Registry
Repository Registry
Review Registry
Build Registry
Migration Registry
```

The constitutional layer assignment is:

```text
Registry Governance
        |
        v
Governance & Constitution
        |
        v
Platform / Registry Services
        |
        v
NICAI.HYDRO
```

---

# 44. InsightFlow Relationship

InsightFlow is treated as an intelligence/insight integration point.

Hydro may provide Hydro intelligence to InsightFlow through an explicit
contract.

```text
NICAI.HYDRO
       |
       v
Hydro Intelligence
       |
       v
InsightFlow
```

The exact interface must be verified before marking the relationship
production-certified.

---

# 45. PRANA Relationship

PRANA is treated as an ecosystem integration point.

Hydro must define the exact provider/consumer relationship before certifying
runtime interoperability.

```text
PRANA
  ^
  |
  | Contract
  |
NICAI.HYDRO
```

The arrow direction shown above is conceptual and must not be treated as
runtime evidence until verified.

---

# 46. BHEX Knowledge Layer Relationship

BHEX Knowledge Layer belongs primarily to the Knowledge Layer.

Hydro interacts with it as a knowledge participant.

```text
BHEX Knowledge Layer
        |
        v
Knowledge Contract
        |
        v
NICAI.HYDRO
        |
        v
Hydro Intelligence
```

Hydro does not become the owner of BHEX knowledge authority.

---

# 47. Duplicate Responsibility Detection

The constitutional layer map must identify possible duplicate responsibilities.

The following categories require explicit review:

| Potential Overlap   | Hydro Position                                                             |
| ------------------- | -------------------------------------------------------------------------- |
| Registry ownership  | Hydro participates; does not own ecosystem registry governance             |
| Validation          | Hydro validates Hydro-side contracts; external validation remains external |
| Runtime execution   | Hydro owns Hydro runtime execution                                         |
| Intelligence        | Hydro owns Hydro intelligence                                              |
| Knowledge           | Hydro consumes/contributes; does not automatically own external knowledge  |
| Operational command | Not owned by Hydro                                                         |
| Sovereign authority | Not owned by Hydro                                                         |
| Domain product      | Hydro provides intelligence; downstream product owns product authority     |
| Trust               | Hydro produces evidence; ecosystem trust governance remains external       |

---

# 48. Duplicate Resolution Rule

When two capabilities appear to perform the same function:

```text
Potential Duplicate
        |
        v
Identify Existing Authority
        |
        v
Compare Contracts
        |
        v
Compare Capability Identity
        |
        v
Determine Primary Owner
        |
        v
Retain One Authority Boundary
        |
        v
Document Integration
```

No parallel capability should be created solely to satisfy constitutional
documentation.

---

# 49. Layer Placement Decision Table

| Question                                         | Decision                  |
| ------------------------------------------------ | ------------------------- |
| Does the capability execute Hydro runtime?       | Execution Infrastructure  |
| Does it govern Hydro identity/contracts?         | Governance & Constitution |
| Does it generate intelligence?                   | Intelligence Layer        |
| Does it consume/provide governed knowledge?      | Knowledge Layer           |
| Does it provide trace/replay/evidence?           | Trust Layer               |
| Does it expose runtime health?                   | Execution Infrastructure  |
| Does it provide output to maritime products?     | Maritime Domain Products  |
| Does it operate shared ecosystem infrastructure? | Not Hydro-owned           |
| Does it exercise sovereign authority?            | Not Hydro-owned           |

---

# 50. Capability Placement Rule

A capability must be assigned according to its actual responsibility rather
than its implementation location.

For example:

```text
A Python endpoint
```

does not automatically belong to:

```text
Execution Infrastructure
```

if its actual constitutional responsibility is:

```text
Intelligence Layer
```

Likewise:

```text
A trace endpoint
```

may execute inside Hydro runtime infrastructure while its constitutional
responsibility belongs to:

```text
Trust Layer
```

---

# 51. Runtime Location vs Constitutional Layer

These concepts must remain separate.

```text
Runtime Location
        !=
Constitutional Responsibility
```

A capability can physically execute inside the same Hydro service while
belonging to a different constitutional layer.

This distinction prevents architecture-level duplication and incorrect
authority assignment.

---

# 52. Hydro Layer Distribution

The Hydro constitutional distribution is:

```text
Governance
    |
    +-- Identity
    +-- Validation
    +-- Registry Participation

Execution
    |
    +-- Runtime
    +-- Health

Intelligence
    |
    +-- Evaluation
    +-- Perception
    +-- Intelligence
    +-- State
    +-- Pattern
    +-- Action

Knowledge
    |
    +-- Knowledge Integration

Trust
    |
    +-- Trace
    +-- Replay
    +-- Observability

Maritime Domain
    |
    +-- Domain Output
```

---

# 53. Constitutional Dependency Graph

The dependency graph is:

```text
                  GOVERNANCE
                      |
                      v
                  PLATFORM
                      |
                      v
                  EXECUTION
                      |
                      v
                 INTELLIGENCE
                  /    |    \
                 /     |     \
                v      v      v
        PERCEPTION  PATTERN  STATE
                \      |      /
                 \     |     /
                  v    v    v
                  ACTION
                     |
          +----------+----------+
          |                     |
          v                     v
      KNOWLEDGE               TRUST
          |                     |
          |          +----------+----------+
          |          |          |          |
          |          v          v          v
          |        TRACE      REPLAY  OBSERVABILITY
          |                     |
          +----------+----------+
                     |
                     v
             MARITIME PRODUCTS
```

---

# 54. Constitutional Boundary Conditions

Hydro must satisfy the following boundary conditions:

### Condition 1

No Hydro capability may exist without a permanent identity.

### Condition 2

No Hydro capability may exercise undocumented authority.

### Condition 3

No Hydro capability may duplicate an existing external authority.

### Condition 4

No external integration may be considered certified without evidence.

### Condition 5

No replay claim may be considered complete without replay evidence.

### Condition 6

No trace claim may be considered complete without trace propagation evidence.

### Condition 7

No registry claim may be considered verified without registry evidence.

---

# 55. Layer Validation Status

| Constitutional Layer      | Hydro Participation                    | Current Status         |
| ------------------------- | -------------------------------------- | ---------------------- |
| Sovereign Foundation      | Identity compatibility                 | DEMONSTRATED           |
| Governance & Constitution | Identity, validation, registry mapping | DEMONSTRATED           |
| Platform Services         | Runtime/platform integration           | DEMONSTRATED           |
| Execution Infrastructure  | Runtime and health                     | VERIFIED               |
| Intelligence Layer        | Evaluation and intelligence            | DEMONSTRATED           |
| Knowledge Layer           | Knowledge integration boundary         | DEMONSTRATED           |
| Trust Layer               | Trace/replay/observability             | PARTIALLY DEMONSTRATED |
| Maritime Domain Products  | Domain output boundary                 | DEMONSTRATED           |

---

# 56. Evidence Qualification

The following distinction is mandatory:

```text
VERIFIED
```

means the claim has directly verifiable evidence.

```text
DEMONSTRATED
```

means runtime or implementation evidence demonstrates the capability but does
not necessarily establish full constitutional certification.

```text
PENDING
```

means required evidence has not yet been completed.

```text
NOT YET CERTIFIED
```

means the available evidence is insufficient for certification.

---

# 57. Current Trust-Layer Qualification

The current Hydro evidence demonstrates that trace inspection and structured
runtime evidence exist.

However, a trace lookup alone does not establish complete constitutional
replay.

Therefore:

```text
Trace Inspection:
DEMONSTRATED

Replay Inspection:
DEMONSTRATED

Complete Replay Equivalence:
NOT YET CERTIFIED

Complete Trace Propagation:
NOT YET CERTIFIED
```

---

# 58. Current Registry Qualification

Registry participation must be evaluated independently for each required
registry.

The layer map establishes the correct constitutional placement of registry
participation.

It does not by itself prove registration.

Therefore:

```text
Registry Layer Mapping:
DEMONSTRATED

Registry Participation:
Requires independent registry evidence
```

---

# 59. Current E2E Qualification

The complete constitutional execution chain requires evidence across:

```text
INGESTION
TANTRA_PARTICIPATION
VALIDATION
ANALYSIS
CLUSTER_ANALYSIS
CONTRACT_VALIDATION
ACTION
TTG_CONSUME
```

Where required stages are absent from replay evidence, full E2E certification
must not be claimed.

Therefore:

```text
Full Constitutional E2E:
NOT YET CERTIFIED
```

unless independently demonstrated by executable evidence.

---

# 60. Constitutional Layer Certification Rule

A layer is considered certification-ready only when:

```text
Layer Assignment
+
Capability Identity
+
Authority Boundary
+
Runtime Contract
+
Evidence
```

are all available.

A documented layer assignment without evidence is an architectural mapping,
not runtime certification.

---

# 61. Final Layer Map Summary

NICAI Hydro's primary constitutional home is:

```text
INTELLIGENCE LAYER
```

with supporting responsibilities in:

```text
GOVERNANCE & CONSTITUTION
EXECUTION INFRASTRUCTURE
KNOWLEDGE LAYER
TRUST LAYER
MARITIME DOMAIN PRODUCTS
```

Hydro does not own:

```text
SOVEREIGN FOUNDATION AUTHORITY
ECOSYSTEM-WIDE GOVERNANCE
EXTERNAL REGISTRY GOVERNANCE
EXTERNAL OPERATIONAL AUTHORITY
EXTERNAL REGULATORY AUTHORITY
```

---

# 62. Final Constitutional Placement

```text
NICAI.HYDRO
    |
    +--> Primary:
    |       INTELLIGENCE LAYER
    |
    +--> Governance:
    |       GOVERNANCE & CONSTITUTION
    |
    +--> Runtime:
    |       EXECUTION INFRASTRUCTURE
    |
    +--> Knowledge:
    |       KNOWLEDGE LAYER
    |
    +--> Trust:
    |       TRUST LAYER
    |
    +--> Consumers:
            MARITIME DOMAIN PRODUCTS
```

---

# 63. Final Audit Position

The constitutional layer mapping establishes a single primary placement for each
Hydro capability while preserving explicit cross-layer interactions.

The map is designed to prevent:

* duplicate capability ownership;
* undocumented authority;
* ambiguous layer assignment;
* uncontrolled cross-layer dependencies;
* unsupported certification claims.

The constitutional layer assignment itself must not be interpreted as proof
that every integration is production-certified.

Production certification remains dependent on executable evidence.

---

````markdown
# 64. Simple Constitutional Layer Explanation

NICAI Hydro works mainly in the **Intelligence Layer**.

It also connects with other constitutional layers when required.

The important point is:

> Hydro can interact with another layer without owning that layer.

For example, Hydro can create replay evidence, but Hydro does not own the complete ecosystem Replay Registry.

---

# 65. Hydro's Main Layer

The main constitutional layer for Hydro is:

```text
INTELLIGENCE LAYER
````

This is where Hydro performs its main job:

```text
Input
  ↓
Evaluation
  ↓
Perception
  ↓
Intelligence
  ↓
Pattern Detection
  ↓
State
  ↓
Action Eligibility
```

These capabilities belong mainly to the Intelligence Layer.

---

# 66. Hydro Runtime Layer

Hydro also runs inside:

```text
EXECUTION INFRASTRUCTURE
```

This layer is responsible for running the Hydro service.

It includes things such as:

```text
Hydro Runtime
Health Endpoint
Runtime Execution
Service Availability
```

The runtime layer runs Hydro.

It does not define what Hydro intelligence means.

---

# 67. Governance Layer

Hydro also participates in:

```text
GOVERNANCE & CONSTITUTION
```

This is required for:

```text
Identity
Authority Boundaries
Contracts
Registry Participation
Validation
Versioning
```

The governance layer controls how Hydro participates in the larger ecosystem.

Hydro must follow these rules.

---

# 68. Knowledge Layer

Hydro can interact with:

```text
KNOWLEDGE LAYER
```

Hydro may:

```text
consume knowledge
contribute knowledge
use knowledge for intelligence
provide intelligence based on governed knowledge
```

But Hydro does not automatically own the complete knowledge system.

---

# 69. Trust Layer

Hydro also participates in:

```text
TRUST LAYER
```

The Trust Layer is important for:

```text
Trace
Replay
Evidence
Observability
Auditability
```

Hydro must produce enough evidence so that its execution can be checked later.

---

# 70. Maritime Domain Products

Hydro can provide intelligence to:

```text
MARITIME DOMAIN PRODUCTS
```

For example:

```text
Hydro Intelligence
       ↓
Domain Output
       ↓
Maritime Product
```

The downstream product decides how it uses that information.

Hydro does not automatically own the downstream product's authority.

---

# 71. Simple Hydro Layer Model

The complete model can be understood like this:

```text
                 BHIV CONSTITUTION
                        |
                        v
                  GOVERNANCE
                        |
                        v
                  HYDRO RUNTIME
                        |
                        v
                 INTELLIGENCE
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
      PERCEPTION     PATTERN        STATE
          |             |             |
          +-------------+-------------+
                        |
                        v
                     ACTION
                        |
              +---------+---------+
              |                   |
              v                   v
          KNOWLEDGE             TRUST
                                  |
                        +---------+---------+
                        |         |         |
                        v         v         v
                      TRACE     REPLAY   OBSERVE
                                  |
                                  v
                         MARITIME PRODUCTS
```

---

# 72. One Identity Rule

Every Hydro capability must have one permanent identity.

Example:

```text
HYDRO.RUNTIME
HYDRO.EVALUATION
HYDRO.VALIDATION
HYDRO.PERCEPTION
HYDRO.INTELLIGENCE
HYDRO.STATE
HYDRO.PATTERN
HYDRO.ACTION
HYDRO.TRACE
HYDRO.REPLAY
HYDRO.OBSERVABILITY
HYDRO.HEALTH
HYDRO.REGISTRY
HYDRO.KNOWLEDGE
HYDRO.DOMAIN_OUTPUT
```

One capability should not have multiple constitutional identities.

---

# 73. Authority Rule

Each capability must clearly define:

```text
WHAT IT OWNS
```

and:

```text
WHAT IT DOES NOT OWN
```

For example:

```text
HYDRO.INTELLIGENCE
```

owns Hydro intelligence processing.

It does not own:

```text
Sovereign Authority
External Regulatory Decisions
External Operational Command
External Product Decisions
```

---

# 74. Provider and Consumer Rule

Every external connection must have a clear direction.

Example:

```text
Provider
   |
   v
Contract
   |
   v
Consumer
```

For Hydro:

```text
NICAI.HYDRO
      |
      v
Intelligence Contract
      |
      v
Consumer
```

or:

```text
Provider
      |
      v
Input Contract
      |
      v
NICAI.HYDRO
```

The actual direction must be verified from runtime evidence.

---

# 75. Contract Rule

Every integration must have a defined contract.

A contract should identify:

```text
Contract ID
Version
Provider
Consumer
Input
Output
Request Format
Response Format
Events
Failure Behaviour
Compatibility
```

Example:

```text
Contract:
HYDRO.INTELLIGENCE.v1

Provider:
NICAI.HYDRO

Consumer:
External Participant

Input:
Hydro evaluation request

Output:
Hydro intelligence result

Version:
v1
```

---

# 76. API Rule

Hydro APIs must have clearly defined responsibilities.

Important API categories include:

```text
Runtime API
Evaluation API
Validation API
Trace API
Health API
```

The API must not silently perform responsibilities belonging to another
constitutional participant.

---

# 77. Event Rule

Hydro runtime events must be structured.

Example:

```json
{
  "trace_id": "example-trace",
  "timestamp": "2026-08-19T05:30:00Z",
  "type": "VALIDATION",
  "data": {
    "status": "ALLOW"
  }
}
```

Every important event should be connected to a trace when the event represents
a traceable execution.

---

# 78. Trace Rule

A trace ID connects execution evidence.

The expected flow is:

```text
Request
   ↓
Trace ID
   ↓
Validation
   ↓
Analysis
   ↓
Action
   ↓
Replay
```

The same trace identity should be propagated through the relevant execution
stages.

---

# 79. Replay Rule

Replay should allow the same execution to be inspected again.

A complete replay should show the required execution stages in the correct
order.

Expected example:

```text
INGESTION
   ↓
TANTRA_PARTICIPATION
   ↓
VALIDATION
   ↓
ANALYSIS
   ↓
CLUSTER_ANALYSIS
   ↓
CONTRACT_VALIDATION
   ↓
ACTION
   ↓
TTG_CONSUME
```

If one or more required stages are missing, the replay should not be marked
fully complete.

---

# 80. Observability Rule

Hydro must make runtime behaviour visible.

Observability should allow inspection of:

```text
Trace ID
Runtime Event
Execution Stage
Timestamp
Status
Error
Health
Replay State
```

This allows an operator to understand what happened.

---

# 81. Runtime Health Rule

Hydro must expose measurable runtime health.

The health check should answer:

```text
Is Hydro running?
```

and, where supported:

```text
Are required runtime dependencies available?
```

A successful health response is evidence that the service is running.

It does not automatically prove that every constitutional integration works.

---

# 82. Registry Rule

Hydro must participate in the required registries.

The required registry categories are:

```text
Capability Registry
Runtime Registry
Execution Registry
Replay Registry
Repository Registry
Review Registry
Build Registry
Migration Registry
```

For each registry, the audit should identify:

```text
Registry
Hydro Identity
Registration ID
Version
Status
Evidence
```

---

# 83. Registry Evidence Rule

A registry entry should be considered verified only when there is actual
evidence.

Examples of evidence:

```text
Registry API response
Registry record
Registration JSON
Execution log
Screenshot
Exported registry data
```

A statement inside a Markdown document alone is not enough to prove live
registry participation.

---

# 84. Integration Rule

Hydro has the following named integration points from the task:

```text
TMS
GC
MDU
GOUDHA Runtime
Namami Gange
SVACS
Bucket
Runtime Registry
Capability Registry
Replay Registry
InsightFlow
PRANA
BHEX Knowledge Layer
```

Each integration must be classified.

Example:

```text
Participant:
SVACS

Relationship:
Validation

Direction:
Hydro → SVACS

Contract:
Validation Evidence Contract

Evidence:
Runtime/API evidence
```

If the direction or contract is not verified, it must not be presented as a
verified runtime fact.

---

# 85. Duplicate Responsibility Rule

Hydro must not create another capability when an existing ecosystem
participant already owns that responsibility.

For example:

```text
Hydro
  |
  +-- Intelligence
  |
  +-- Validation
  |
  +-- Evidence
```

should not become:

```text
Hydro
  |
  +-- New Registry System
  +-- New Governance System
  +-- New Replay System
  +-- New Ecosystem Authority
```

Hydro should connect to existing ecosystem services instead.

---

# 86. Simple Ownership Matrix

| Capability    | Hydro Owns             | Hydro Does Not Own           |
| ------------- | ---------------------- | ---------------------------- |
| Runtime       | Hydro runtime          | Ecosystem runtime            |
| Intelligence  | Hydro intelligence     | External intelligence        |
| Validation    | Hydro-side validation  | External governance          |
| Trace         | Hydro trace evidence   | Ecosystem-wide trust         |
| Replay        | Hydro replay evidence  | Entire replay ecosystem      |
| Health        | Hydro health           | External service health      |
| Knowledge     | Hydro contribution/use | Entire knowledge layer       |
| Domain Output | Hydro output           | Downstream product authority |
| Registry      | Hydro registration     | Registry governance          |

---

# 87. Evidence Status

The audit should use only these statuses:

```text
VERIFIED
DEMONSTRATED
PENDING
NOT YET CERTIFIED
```

Meaning:

### VERIFIED

Direct evidence confirms the claim.

### DEMONSTRATED

The capability is visible and working, but complete certification evidence
may still be required.

### PENDING

The required evidence has not yet been collected.

### NOT YET CERTIFIED

The available evidence is not enough to certify the claim.

---

# 88. Important Certification Rule

Do not convert:

```text
PENDING
```

into:

```text
VERIFIED
```

just because an endpoint exists.

For example:

```text
GET /trace/{trace_id}
```

proves that a trace inspection endpoint exists.

It does not automatically prove:

```text
Complete Replay
```

or:

```text
Complete Trace Propagation
```

---

# 89. Current Replay Interpretation

If the replay endpoint returns:

```text
"replay_status": "INCOMPLETE"
```

then the correct certification status is:

```text
NOT YET CERTIFIED
```

for complete replay equivalence.

For example:

```text
found_stages:
VALIDATION
ANALYSIS
ACTION
```

with missing stages such as:

```text
INGESTION
TANTRA_PARTICIPATION
CLUSTER_ANALYSIS
CONTRACT_VALIDATION
TTG_CONSUME
```

does not represent a complete constitutional replay.

---

# 90. Current Trace Interpretation

A trace endpoint returning a valid trace ID demonstrates trace lookup.

However, complete trace propagation requires evidence that the same trace ID
moves through all required stages.

Therefore:

```text
Trace Endpoint:
DEMONSTRATED

Complete Trace Propagation:
NOT YET CERTIFIED
```

unless complete propagation has been independently demonstrated.

---

# 91. Current Health Interpretation

If:

```text
GET /
```

returns:

```text
NICAI Running
```

with HTTP:

```text
200
```

this demonstrates that the deployed service is reachable and running.

It should not automatically be interpreted as proof of:

```text
Full Constitutional Runtime Health
```

unless the health contract checks the required dependencies.

---

# 92. Current API Interpretation

If the following APIs are working:

```text
POST /nicai/evaluate
POST /contract/validate
GET /trace/{trace_id}
GET /health
```

then the corresponding API functionality is:

```text
DEMONSTRATED
```

This is useful runtime evidence.

However, complete constitutional certification still requires the additional
registry, replay, observability, and E2E evidence defined by the task.

---

# 93. Final Layer Map Decision

The final simple decision is:

```text
PRIMARY:
INTELLIGENCE LAYER
```

Supporting layers:

```text
GOVERNANCE & CONSTITUTION
EXECUTION INFRASTRUCTURE
KNOWLEDGE LAYER
TRUST LAYER
MARITIME DOMAIN PRODUCTS
```

Not owned:

```text
SOVEREIGN AUTHORITY
ECOSYSTEM-WIDE GOVERNANCE
EXTERNAL OPERATIONAL AUTHORITY
EXTERNAL REGULATORY AUTHORITY
EXTERNAL PRODUCT OWNERSHIP
```

---

# 94. Final Audit Principle

The purpose of this document is not to create new Hydro functionality.

The purpose is to clearly show:

```text
WHO HYDRO IS
        ↓
WHAT HYDRO DOES
        ↓
WHAT HYDRO OWNS
        ↓
WHAT HYDRO DOES NOT OWN
        ↓
WHICH CONSTITUTIONAL LAYER IT BELONGS TO
        ↓
WHO IT CONNECTS TO
        ↓
WHAT CONTRACTS IT USES
        ↓
WHAT EVIDENCE IT PRODUCES
```

This keeps Hydro reusable, explainable, governed, and compatible with the BHIV
Constitutional Runtime.

---

# 95. Final Status

```text
Constitutional Layer Mapping:
DEMONSTRATED

Primary Layer:
INTELLIGENCE LAYER

Runtime Layer:
EXECUTION INFRASTRUCTURE

Governance Participation:
DEMONSTRATED

Knowledge Participation:
DEMONSTRATED

Trust Participation:
PARTIALLY DEMONSTRATED

Maritime Domain Integration:
DEMONSTRATED

Complete Replay Certification:
NOT YET CERTIFIED

Complete Trace Propagation Certification:
NOT YET CERTIFIED

Complete Registry Certification:
NOT YET CERTIFIED

Complete E2E Constitutional Certification:
NOT YET CERTIFIED
```

---

# 96. Conclusion

NICAI Hydro is positioned primarily as an **Intelligence Layer participant** in
the BHIV Constitutional Runtime.

It uses execution infrastructure to run, governance to remain controlled,
knowledge to support intelligence, trust mechanisms to produce evidence, and
maritime products to consume its outputs.

No new Hydro feature is required by this layer mapping.

The remaining certification work depends on independently verifiable runtime
evidence for contracts, registries, replay, trace propagation, observability,
health, and complete end-to-end execution.

```

````markdown
# 97. Constitutional Layer Verification Checklist

This section provides the final checklist for verifying that every Hydro
capability has been placed in the correct constitutional layer.

For every capability, verify:

- Permanent identity exists.
- Primary constitutional layer is defined.
- Purpose is documented.
- Authority owned is documented.
- Authority not owned is documented.
- Upstream relationship is documented.
- Downstream relationship is documented.
- Runtime contract is identified.
- API contract is identified.
- Event relationship is identified.
- Registry participation is identified.
- Evidence requirement is identified.
- Replay requirement is identified.
- Observability requirement is identified.
- Runtime health requirement is identified.
- Version and compatibility requirement is identified.

---

# 98. Capability-to-Layer Verification

| Capability | Layer | Identity | Authority Boundary | Contract | Evidence |
|---|---|---|---|---|---|
| `HYDRO.RUNTIME` | Execution Infrastructure | Defined | Defined | Required | Runtime evidence |
| `HYDRO.IDENTITY` | Governance & Constitution | Defined | Defined | Required | Identity evidence |
| `HYDRO.EVALUATION` | Intelligence Layer | Defined | Defined | Required | Evaluation evidence |
| `HYDRO.VALIDATION` | Governance & Constitution | Defined | Defined | Required | Validation evidence |
| `HYDRO.PERCEPTION` | Intelligence Layer | Defined | Defined | Required | Perception evidence |
| `HYDRO.INTELLIGENCE` | Intelligence Layer | Defined | Defined | Required | Intelligence evidence |
| `HYDRO.STATE` | Intelligence Layer | Defined | Defined | Required | State evidence |
| `HYDRO.PATTERN` | Intelligence Layer | Defined | Defined | Required | Pattern evidence |
| `HYDRO.ACTION` | Intelligence Layer | Defined | Defined | Required | Action evidence |
| `HYDRO.TRACE` | Trust Layer | Defined | Defined | Required | Trace evidence |
| `HYDRO.REPLAY` | Trust Layer | Defined | Defined | Required | Replay evidence |
| `HYDRO.OBSERVABILITY` | Trust Layer | Defined | Defined | Required | Observability evidence |
| `HYDRO.HEALTH` | Execution Infrastructure | Defined | Defined | Required | Health evidence |
| `HYDRO.REGISTRY` | Governance & Constitution | Defined | Defined | Required | Registry evidence |
| `HYDRO.KNOWLEDGE` | Knowledge Layer | Defined | Defined | Required | Knowledge evidence |
| `HYDRO.DOMAIN_OUTPUT` | Maritime Domain Products | Defined | Defined | Required | Domain evidence |

---

# 99. Capability Identity Rule

Each capability must have exactly one primary constitutional identity.

The identity must remain stable across versions.

Example:

```text
HYDRO.INTELLIGENCE
````

must continue to represent the Hydro intelligence capability even when its
implementation version changes.

Version changes should be represented through:

```text
Identity
+
Version
+
Compatibility
```

and not by creating unnecessary duplicate identities.

---

# 100. Version Rule

Every runtime contract must have a version.

Example:

```text
HYDRO.INTELLIGENCE.v1
```

A compatible update may use:

```text
HYDRO.INTELLIGENCE.v1.x
```

A breaking contract change should use a new major version.

Example:

```text
HYDRO.INTELLIGENCE.v2
```

The identity remains associated with the capability while compatibility is
explicitly documented.

---

# 101. Constitutional Boundary Verification

The following boundaries must remain clear:

```text
Hydro Intelligence
        !=
Sovereign Authority
```

```text
Hydro Validation
        !=
Ecosystem Governance
```

```text
Hydro Replay Evidence
        !=
Ecosystem Replay Registry Ownership
```

```text
Hydro Runtime Health
        !=
Ecosystem-wide Health Governance
```

```text
Hydro Domain Output
        !=
Downstream Product Authority
```

These boundaries prevent responsibility duplication.

---

# 102. Runtime Dependency Rule

Every dependency must have a known relationship.

The minimum dependency record is:

```text
Participant
Capability
Direction
Contract
Version
Input
Output
Evidence
Status
```

Example:

```text
Participant:
SVACS

Capability:
Validation

Direction:
HYDRO → SVACS

Contract:
Validation Evidence Contract

Version:
v1

Status:
PENDING
```

The status must only become `VERIFIED` after actual evidence is available.

---

# 103. Evidence Rule

Evidence must be connected to the claim it proves.

Example:

```text
Claim:
Hydro runtime is reachable.

Evidence:
HTTP 200 from runtime endpoint.

Status:
VERIFIED
```

Another example:

```text
Claim:
Hydro supports complete replay.

Evidence:
Replay endpoint returns all required stages in correct order.

Status:
VERIFIED
```

If the replay endpoint instead reports missing stages:

```text
Status:
NOT YET CERTIFIED
```

---

# 104. Constitutional Layer Evidence Matrix

| Layer                     | Required Evidence                          |
| ------------------------- | ------------------------------------------ |
| Sovereign Foundation      | Identity compatibility evidence            |
| Governance & Constitution | Identity, authority and registry evidence  |
| Platform Services         | Platform contract evidence                 |
| Execution Infrastructure  | Runtime and health evidence                |
| Intelligence Layer        | Evaluation/intelligence execution evidence |
| Knowledge Layer           | Knowledge contract/evidence                |
| Trust Layer               | Trace/replay/observability evidence        |
| Maritime Domain Products  | Consumer/output evidence                   |

---

# 105. Platform Services Boundary

Hydro may consume platform services.

The relationship should be:

```text
Platform Service
       |
       v
Platform Contract
       |
       v
NICAI.HYDRO
```

Hydro must not create a second platform service if an existing constitutional
service already provides the required capability.

---

# 106. Sovereign Foundation Boundary

The Sovereign Foundation represents authority above Hydro.

Hydro must remain compatible with sovereign rules but must not claim sovereign
authority.

Therefore:

```text
Sovereign Foundation
        |
        v
Constitutional Rules
        |
        v
NICAI.HYDRO
```

Hydro operates within those rules.

---

# 107. Governance Boundary

Governance controls how Hydro is registered, identified, versioned and
validated.

Hydro participates in governance but does not become the ecosystem's
governance authority.

```text
Governance
    |
    +-- Identity
    +-- Registry
    +-- Contract
    +-- Validation
          |
          v
      NICAI.HYDRO
```

---

# 108. Intelligence Boundary

The Intelligence Layer is Hydro's primary operating area.

The expected responsibility is:

```text
Input
  ↓
Evaluation
  ↓
Perception
  ↓
Intelligence
  ↓
Pattern
  ↓
State
  ↓
Action Eligibility
```

Hydro intelligence should remain explainable and traceable.

---

# 109. Knowledge Boundary

Knowledge should support intelligence without creating uncontrolled authority.

The relationship is:

```text
Knowledge
    |
    v
Hydro Processing
    |
    v
Intelligence
```

Knowledge consumed by Hydro should have an identifiable source and version
where the contract requires it.

---

# 110. Trust Boundary

Trust evidence should allow another participant or reviewer to understand:

```text
What happened?
When did it happen?
Which trace was involved?
Which stage executed?
What was the result?
Can the execution be replayed?
Is the runtime healthy?
```

This is the purpose of:

```text
TRACE
REPLAY
OBSERVABILITY
```

---

# 111. Domain Product Boundary

Hydro should provide domain intelligence through explicit outputs.

Example:

```text
NICAI.HYDRO
      |
      v
Domain Intelligence Contract
      |
      v
Maritime Product
```

The maritime product remains responsible for downstream business or operational
authority.

---

# 112. Final External Integration Classification

| Integration          | Expected Relationship             | Certification Rule         |
| -------------------- | --------------------------------- | -------------------------- |
| TMS                  | External participant              | Verify actual contract     |
| GC                   | External participant              | Verify actual contract     |
| MDU                  | Domain consumer/participant       | Verify actual contract     |
| GOUDHA Runtime       | Runtime participant               | Verify runtime direction   |
| Namami Gange         | Domain integration                | Verify actual contract     |
| SVACS                | Validation integration            | Verify validation contract |
| Bucket               | Ecosystem integration             | Verify actual contract     |
| Runtime Registry     | Registry                          | Verify registration        |
| Capability Registry  | Registry                          | Verify registration        |
| Replay Registry      | Registry                          | Verify registration        |
| InsightFlow          | Intelligence consumer/integration | Verify actual contract     |
| PRANA                | Ecosystem integration             | Verify actual contract     |
| BHEX Knowledge Layer | Knowledge integration             | Verify knowledge contract  |

---

# 113. No Assumption Rule

The presence of a participant name in an architecture document does not prove
that a live runtime integration exists.

Therefore:

```text
Architecture Mention
        !=
Runtime Evidence
```

and:

```text
Documented Dependency
        !=
Verified Dependency
```

Runtime certification must always use actual evidence.

---

# 114. Final Constitutional Runtime Model

The final model is:

```text
                 SOVEREIGN FOUNDATION
                         |
                         v
               GOVERNANCE & CONSTITUTION
                         |
                         v
                  PLATFORM SERVICES
                         |
                         v
               EXECUTION INFRASTRUCTURE
                         |
                         v
                  NICAI HYDRO
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
     INTELLIGENCE     KNOWLEDGE       TRUST
          |              |              |
          |              |        +-----+-----+
          |              |        |     |     |
          |              |       TRACE REPLAY OBSERVE
          |              |        |
          +--------------+--------+
                         |
                         v
                MARITIME PRODUCTS
```

---

# 115. Constitutional Participation Principle

NICAI Hydro is not treated as an isolated product.

It is treated as a reusable runtime participant.

The desired model is:

```text
Discover
   ↓
Identify
   ↓
Attach
   ↓
Execute
   ↓
Observe
   ↓
Replay
   ↓
Validate
   ↓
Reuse
```

This is the core constitutional runtime convergence objective.

---

# 116. Plug-and-Play Requirement

A compliant Hydro participant should not require custom integration for every
consumer.

The expected model is:

```text
Consumer
   |
   v
Constitutional Discovery
   |
   v
Hydro Identity
   |
   v
Versioned Contract
   |
   v
Runtime Attachment
   |
   v
Execution
```

The consumer should interact through the defined constitutional contracts.

---

# 117. Replay Requirement

Replay participation must be deterministic.

The replay process should preserve:

```text
Trace Identity
Execution Order
Execution Inputs
Execution Stages
Execution Outputs
Validation Results
Action Results
```

If required stages are missing, replay certification remains incomplete.

---

# 118. Observability Requirement

Observability should provide enough information to inspect runtime behaviour
without modifying the Hydro capability.

Minimum useful information:

```text
trace_id
timestamp
event_type
stage
status
result
error
runtime_health
```

---

# 119. Runtime Health Requirement

Health validation should be repeatable.

Example:

```text
GET /health
```

Expected:

```text
HTTP 200
```

and a structured response indicating runtime status.

Where dependencies are checked, the response should also expose dependency
status.

A simple HTTP success confirms reachability but does not prove full ecosystem
health.

---

# 120. Constitutional Certification Gate

Hydro can move toward final certification only when these gates are satisfied:

```text
[ ] Permanent identities
[ ] Constitutional layer mapping
[ ] Authority boundaries
[ ] Runtime contracts
[ ] API contracts
[ ] Event contracts
[ ] Registry participation
[ ] Trace propagation
[ ] Replay verification
[ ] Observability
[ ] Runtime health
[ ] Integration evidence
[ ] End-to-end execution
[ ] Production certification evidence
```

Each gate must have evidence.

---

# 121. Final Status Classification

Use this exact interpretation:

| Status              | Meaning                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| `VERIFIED`          | Direct evidence proves the requirement                                                   |
| `DEMONSTRATED`      | Working behaviour is demonstrated but full certification may require additional evidence |
| `PENDING`           | Evidence is still required                                                               |
| `NOT YET CERTIFIED` | Current evidence is insufficient for certification                                       |

Do not use `VERIFIED` when the only evidence is a documentation statement.

---

# 122. Audit Conclusion

The constitutional layer mapping confirms that NICAI Hydro belongs primarily
to the:

```text
INTELLIGENCE LAYER
```

with supporting participation in:

```text
GOVERNANCE & CONSTITUTION
EXECUTION INFRASTRUCTURE
KNOWLEDGE LAYER
TRUST LAYER
MARITIME DOMAIN PRODUCTS
```

Hydro must maintain clear authority boundaries and must use explicit contracts
for all external relationships.

---

# 123. Certification Limitation

This document defines the constitutional placement.

It does not by itself certify:

```text
Complete Registry Participation
Complete Trace Propagation
Complete Replay Equivalence
Complete Observability
Complete Ecosystem Health
Complete E2E Constitutional Execution
```

Those claims require independent runtime evidence.

---

# 124. Final Constitutional Position

```text
NICAI HYDRO
│
├── PRIMARY CONSTITUTIONAL LAYER
│   └── Intelligence Layer
│
├── GOVERNANCE
│   └── Governance & Constitution
│
├── RUNTIME
│   └── Execution Infrastructure
│
├── KNOWLEDGE
│   └── Knowledge Layer
│
├── TRUST
│   └── Trust Layer
│
└── CONSUMERS
    └── Maritime Domain Products
```

---

# 125. Final Rule

NICAI Hydro should remain:

```text
ONE PARTICIPANT
ONE IDENTITY PER CAPABILITY
ONE CLEAR AUTHORITY BOUNDARY
VERSIONED CONTRACTS
TRACEABLE EXECUTION
REPLAYABLE EVIDENCE
OBSERVABLE RUNTIME
MEASURABLE HEALTH
```

and should not introduce duplicate ecosystem responsibilities.

---

# 126. Final Review Statement

The constitutional layer map is complete as an architectural and audit
mapping.

Runtime certification remains evidence-driven.

Where executable evidence exists, the capability may be marked:

```text
VERIFIED
```

or:

```text
DEMONSTRATED
```

Where evidence is missing:

```text
PENDING
```

or:

```text
NOT YET CERTIFIED
```

must be retained.

No unsupported certification claim should be introduced.

---
```
