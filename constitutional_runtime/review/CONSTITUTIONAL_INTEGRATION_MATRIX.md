````markdown
# NICAI Hydro — Constitutional Integration Matrix

## 1. Document Purpose

This document defines the constitutional integration position of the NICAI Hydro runtime within the BHIV/TANTRA Constitutional Runtime.

The purpose of this matrix is to establish:

- where Hydro participates;
- which constitutional layers Hydro interacts with;
- which Hydro capability participates;
- the upstream participant;
- the downstream participant;
- the runtime interaction;
- the contract boundary;
- the event relationship;
- the authority boundary;
- the evidence required for certification.

This document is an integration audit artifact.

It does not create new Hydro features.

It does not redesign the Hydro architecture.

It does not create duplicate ecosystem capabilities.

It does not transfer authority from another constitutional participant to NICAI Hydro.

---

# 2. Constitutional Integration Objective

NICAI Hydro must operate as a reusable Constitutional Runtime Participant.

The target integration model is:

```text
BHIV Constitutional Runtime
            |
            v
    NICAI Hydro Participant
            |
    +-------+-------+
    |       |       |
    v       v       v
 Runtime  Registry Evidence
    |
    +-----------------------------+
    |             |               |
    v             v               v
 Intelligence   Knowledge      Trust/Replay
    |
    v
Maritime Domain Consumers
````

The integration boundary must remain explicit and deterministic.

---

# 3. Constitutional Layers

The integration matrix evaluates Hydro against the following constitutional layers:

1. Sovereign Foundation
2. Governance & Constitution
3. Platform Services
4. Execution Infrastructure
5. Intelligence Layer
6. Knowledge Layer
7. Trust Layer
8. Maritime Domain Products

The layers describe integration relationships.

They do not imply that Hydro owns every layer in which it participates.

---

# 4. Hydro Permanent Capability Identities

The integration matrix uses the following Hydro capability identities:

| Capability ID | Permanent Identity                   |
| ------------- | ------------------------------------ |
| HYDRO-CAP-001 | `NICAI.HYDRO.RUNTIME_API`            |
| HYDRO-CAP-002 | `NICAI.HYDRO.CONTRACT_VALIDATION`    |
| HYDRO-CAP-003 | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` |
| HYDRO-CAP-004 | `NICAI.HYDRO.TRACE_CORRELATION`      |
| HYDRO-CAP-005 | `NICAI.HYDRO.REPLAY_VERIFICATION`    |
| HYDRO-CAP-006 | `NICAI.HYDRO.REGISTRY_PARTICIPATION` |
| HYDRO-CAP-007 | `NICAI.HYDRO.OBSERVABILITY`          |
| HYDRO-CAP-008 | `NICAI.HYDRO.RUNTIME_INTEGRATION`    |
| HYDRO-CAP-009 | `NICAI.HYDRO.ECOSYSTEM_ATTACHMENTS`  |
| HYDRO-CAP-010 | `NICAI.HYDRO.KNOWLEDGE_REGISTRY`     |

These identities represent existing Hydro runtime responsibilities.

---

# 5. Constitutional Layer Integration Summary

| Constitutional Layer      | Hydro Participation                      | Primary Hydro Capability             |
| ------------------------- | ---------------------------------------- | ------------------------------------ |
| Sovereign Foundation      | Participant boundary only                | Runtime identity                     |
| Governance & Constitution | Contract and authority compliance        | `NICAI.HYDRO.CONTRACT_VALIDATION`    |
| Platform Services         | Registry and integration participation   | `NICAI.HYDRO.REGISTRY_PARTICIPATION` |
| Execution Infrastructure  | API, execution and telemetry             | `NICAI.HYDRO.RUNTIME_API`            |
| Intelligence Layer        | Hydro validation/intelligence processing | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` |
| Knowledge Layer           | Dataset/knowledge registration           | `NICAI.HYDRO.KNOWLEDGE_REGISTRY`     |
| Trust Layer               | Trace, replay and evidence               | `NICAI.HYDRO.TRACE_CORRELATION`      |
| Maritime Domain Products  | Downstream intelligence consumption      | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` |

---

# 6. Sovereign Foundation Integration

## Integration Position

NICAI Hydro does not claim ownership of the Sovereign Foundation.

Hydro participates as a constitutional runtime participant operating under the ecosystem's identity and authority model.

## Hydro Responsibility

Hydro is responsible for maintaining its own permanent runtime identity.

The permanent participant identity is:

```text
NICAI.HYDRO
```

## Integration Direction

```text
Sovereign Foundation
        |
        v
Constitutional Runtime Identity
        |
        v
NICAI.HYDRO
```

## Authority Boundary

### Hydro Owns

* Hydro participant identity;
* Hydro runtime identity;
* Hydro capability identity.

### Hydro Does Not Own

* sovereign authority;
* ecosystem-wide identity governance;
* constitutional authority outside Hydro;
* identity governance of other participants.

## Integration Type

`IDENTITY / GOVERNANCE`

---

# 7. Governance & Constitution Integration

## Purpose

Hydro participates in constitutional governance through explicit contracts, authority boundaries, validation rules, evidence requirements, and certification controls.

## Primary Capability

```text
NICAI.HYDRO.CONTRACT_VALIDATION
```

## Supporting Capabilities

```text
NICAI.HYDRO.RUNTIME_API
NICAI.HYDRO.TRACE_CORRELATION
NICAI.HYDRO.REPLAY_VERIFICATION
NICAI.HYDRO.REGISTRY_PARTICIPATION
```

## Integration Flow

```text
Constitutional Rules
        |
        v
Runtime Contract
        |
        v
Hydro Contract Validation
        |
        v
Validation Result
        |
        v
Runtime Evidence
```

## Authority Owned

Hydro owns validation of its own defined runtime contracts.

## Authority Not Owned

Hydro does not own:

* ecosystem constitution;
* external participant governance;
* constitutional policy;
* external registry governance;
* external authority decisions.

## Evidence

Contract validation is exposed through:

```text
POST /contract/validate
```

## Integration Type

`CONTRACT / GOVERNANCE`

---

# 8. Platform Services Integration

## Participating Capabilities

```text
NICAI.HYDRO.REGISTRY_PARTICIPATION
NICAI.HYDRO.RUNTIME_INTEGRATION
NICAI.HYDRO.ECOSYSTEM_ATTACHMENTS
```

## Purpose

Platform integration provides reusable infrastructure for:

* registry participation;
* runtime attachment;
* participant integration;
* metadata exchange;
* ecosystem connectivity.

## Registry Interfaces

The convergence task identifies:

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

## Integration Model

```text
NICAI Hydro
     |
     +---- Capability Registry
     |
     +---- Runtime Registry
     |
     +---- Execution Registry
     |
     +---- Replay Registry
     |
     +---- Repository Registry
     |
     +---- Review Registry
     |
     +---- Build Registry
     |
     +---- Migration Registry
```

## Authority Boundary

Hydro owns its registry participation behaviour.

Hydro does not own the registries.

## Evidence Rule

Repository implementation is evidence of registry infrastructure.

Actual registry registration requires independent registry evidence.

## Integration Type

`PLATFORM / REGISTRY / ATTACHMENT`

---

# 9. Execution Infrastructure Integration

## Primary Capabilities

```text
NICAI.HYDRO.RUNTIME_API
NICAI.HYDRO.OBSERVABILITY
NICAI.HYDRO.TRACE_CORRELATION
```

## Runtime API

The existing runtime exposes:

```text
GET /
GET /health
POST /nicai/evaluate
POST /contract/validate
GET /trace/{trace_id}
```

## Execution Flow

```text
External Request
       |
       v
NICAI Hydro Runtime API
       |
       v
Hydro Execution
       |
       +--------> Trace
       |
       +--------> Events
       |
       +--------> Validation
       |
       +--------> Intelligence
       |
       +--------> State
```

## Authority Owned

Hydro owns:

* its runtime execution;
* its API surface;
* its execution correlation;
* its runtime telemetry.

## Authority Not Owned

Hydro does not own:

* external execution infrastructure;
* external runtime governance;
* external consumer decisions.

## Health Interface

```text
GET /health
```

The health endpoint represents Hydro runtime health.

It does not certify constitutional integration.

## Integration Type

`EXECUTION / RUNTIME`

---

# 10. Intelligence Layer Integration

## Primary Capability

```text
NICAI.HYDRO.INTELLIGENCE_EXECUTION
```

## Purpose

This capability performs the existing Hydro validation and intelligence processing.

## Observed Runtime Flow

```text
Input
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
State
```

Observed runtime evidence also includes structured:

```text
PATTERN
ACTION
```

events.

## Integration Inputs

Potential inputs include:

* Hydro runtime requests;
* perception information;
* validation inputs;
* configured knowledge references;
* execution context.

## Integration Outputs

Hydro may produce:

* validation results;
* confidence;
* risk level;
* state;
* pattern evidence;
* action eligibility;
* structured runtime events.

## Authority Owned

Hydro owns Hydro-specific intelligence processing.

## Authority Not Owned

Hydro does not own:

* downstream operational command;
* external maritime product decisions;
* external authority approval;
* ecosystem-wide intelligence governance.

## Integration Type

`INTELLIGENCE`

---

# 11. Knowledge Layer Integration

## Primary Capability

```text
NICAI.HYDRO.KNOWLEDGE_REGISTRY
```

## Purpose

Hydro participates in the Knowledge Layer through existing dataset and knowledge registration mechanisms.

## Existing Repository Evidence

The repository contains dataset registry infrastructure.

The knowledge capability is therefore treated as a registry/attachment responsibility rather than as ownership of the complete BHEX Knowledge Layer.

## Integration Flow

```text
Dataset / Knowledge Source
          |
          v
Hydro Knowledge Registry
          |
          v
Hydro Runtime Context
          |
          v
Hydro Intelligence Execution
```

## Authority Owned

Hydro owns:

* Hydro dataset registration;
* Hydro-side dataset metadata;
* Hydro-side knowledge references.

## Authority Not Owned

Hydro does not own:

* BHEX Knowledge Layer governance;
* external dataset ownership;
* global knowledge semantics;
* external knowledge authority.

## Versioning

Knowledge and dataset references must preserve:

* identity;
* version;
* source;
* schema;
* provenance;
* compatibility.

## Integration Type

`KNOWLEDGE / DATASET`

---

# 12. Trust Layer Integration

## Primary Capabilities

```text
NICAI.HYDRO.TRACE_CORRELATION
NICAI.HYDRO.REPLAY_VERIFICATION
NICAI.HYDRO.OBSERVABILITY
```

## Purpose

The Trust Layer integration provides:

* execution identity;
* traceability;
* replay inspection;
* evidence correlation;
* observability.

## Trace Flow

```text
Execution
   |
   v
Trace ID
   |
   +----> Events
   |
   +----> Validation
   |
   +----> Analysis
   |
   +----> Action
   |
   +----> Replay
```

## Replay Interface

```text
GET /trace/{trace_id}
```

## Replay Response

The trace response can contain:

```text
trace_id
found_stages
missing_stages
ordered_replay
sequence_chain
replay_status
```

## Important Boundary

Trace inspection is not equivalent to complete replay equivalence.

A replay may be ordered while still being incomplete because required stages are missing.

## Authority Owned

Hydro owns:

* Hydro trace correlation;
* Hydro replay verification;
* Hydro observability.

## Authority Not Owned

Hydro does not own:

* global trust governance;
* external replay registries;
* external evidence governance.

## Integration Type

`TRUST / EVIDENCE / REPLAY`

---

# 13. Maritime Domain Product Integration

## Purpose

Hydro intelligence may be consumed by maritime-domain products and operational systems.

The Hydro runtime remains the intelligence/runtime participant.

It does not automatically become the owner of downstream maritime products.

## Potential Consumers

The convergence task identifies:

```text
TMS
GC
MDU
GOUDHA Runtime
Namami Gange
```

as ecosystem integration points.

## Integration Model

```text
NICAI Hydro
     |
     v
Hydro Intelligence Output
     |
     v
Maritime Domain Consumer
     |
     v
Operational Product / Surface
```

## Authority Owned

Hydro owns:

* Hydro intelligence output;
* Hydro validation output;
* Hydro runtime evidence.

## Authority Not Owned

Hydro does not own:

* downstream product UX;
* operational command;
* external maritime decision authority;
* consumer-specific business rules.

## Integration Type

`DOMAIN PRODUCT / CONSUMPTION`

---

# 14. Part 1 Integration Matrix

| Layer                     | Hydro Capability                     | Integration Direction    | Primary Contract     | Evidence                   |
| ------------------------- | ------------------------------------ | ------------------------ | -------------------- | -------------------------- |
| Sovereign Foundation      | `NICAI.HYDRO.RUNTIME_API`            | Foundation → Hydro       | Runtime Identity     | Runtime identity           |
| Governance & Constitution | `NICAI.HYDRO.CONTRACT_VALIDATION`    | Governance ↔ Hydro       | Contract             | `/contract/validate`       |
| Platform Services         | `NICAI.HYDRO.REGISTRY_PARTICIPATION` | Hydro ↔ Registries       | Registry Contract    | Registry implementation    |
| Platform Services         | `NICAI.HYDRO.RUNTIME_INTEGRATION`    | Hydro ↔ Participants     | Integration Contract | Integration implementation |
| Platform Services         | `NICAI.HYDRO.ECOSYSTEM_ATTACHMENTS`  | Hydro ↔ Participants     | Attachment Contract  | Adapter implementation     |
| Execution Infrastructure  | `NICAI.HYDRO.RUNTIME_API`            | Consumer → Hydro         | HTTP API             | Live API                   |
| Execution Infrastructure  | `NICAI.HYDRO.OBSERVABILITY`          | Hydro → Observability    | Event Contract       | Runtime events             |
| Intelligence Layer        | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Input → Hydro → Consumer | Evaluation Contract  | `/nicai/evaluate`          |
| Knowledge Layer           | `NICAI.HYDRO.KNOWLEDGE_REGISTRY`     | Knowledge ↔ Hydro        | Dataset Contract     | Registry implementation    |
| Trust Layer               | `NICAI.HYDRO.TRACE_CORRELATION`      | Execution ↔ Trace        | Trace Contract       | `trace_id`                 |
| Trust Layer               | `NICAI.HYDRO.REPLAY_VERIFICATION`    | Trace → Replay           | Replay Contract      | `/trace/{trace_id}`        |
| Maritime Domain Products  | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Hydro → Consumer         | Consumer Contract    | Runtime output             |

---

# 15. Integration Direction Rules

The following direction rules apply to every integration.

## Provider

The participant producing the contracted resource.

## Consumer

The participant consuming the contracted resource.

## Hydro as Provider

Hydro may provide:

* validation results;
* intelligence results;
* state information;
* runtime events;
* trace evidence;
* health information.

## Hydro as Consumer

Hydro may consume:

* runtime inputs;
* contract requests;
* dataset/knowledge references;
* external participant responses;
* registry services.

## Boundary Rule

Being a provider or consumer does not automatically transfer authority.

---

# 16. Integration Contract Requirements

Every constitutional integration must define:

```text
Participant Identity
Capability Identity
Contract Identity
Provider
Consumer
Version
Request Schema
Response Schema
Event Schema
Trace Behaviour
Failure Behaviour
Compatibility
Evidence
```

The contract must be deterministic and versioned.

---

# 17. Integration Evidence Rules

Evidence must be classified according to what was actually demonstrated.

### Verified

Directly verified through executable runtime evidence.

### Demonstrated

Runtime behaviour successfully executed and observed.

### Infrastructure Demonstrated

Implementation exists and can be identified, but external execution evidence is not yet sufficient.

### Not Yet Certified

The required evidence does not yet support certification.

No integration is marked certified merely because an adapter or configuration file exists.

---

# 18. Part 1 Certification Boundary

The constitutional integration matrix establishes the intended integration topology and authority boundaries.

It does not by itself certify:

* complete registry participation;
* complete replay equivalence;
* universal deterministic trace propagation;
* complete ecosystem interoperability;
* complete end-to-end constitutional execution.

Those claims require independent executable evidence.

---

````markdown
# 19. Cross-Ecosystem Integration Matrix

The NICAI Hydro runtime participates in the BHIV ecosystem through defined runtime, validation, evidence, registry, and intelligence boundaries.

The following matrix records the identified ecosystem integration points.

| Participant / System | Hydro Relationship | Direction | Primary Hydro Capability | Integration Purpose | Authority Boundary |
|---|---|---|---|---|---|
| TMS | Runtime / Intelligence Consumer | Hydro → TMS | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Consume Hydro intelligence output | TMS owns its operational decisions |
| GC | Runtime / Intelligence Consumer | Hydro → GC | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Consume Hydro intelligence | GC retains its own authority |
| MDU | Maritime Domain Consumer | Hydro → MDU | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Provide Hydro intelligence | MDU owns domain-product decisions |
| GOUDHA Runtime | Runtime Participant | Bidirectional | `NICAI.HYDRO.RUNTIME_INTEGRATION` | Runtime interoperability | GOUDHA owns its runtime responsibilities |
| Namami Gange | Domain Consumer | Hydro → Namami Gange | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Provide Hydro intelligence to domain surfaces | Namami Gange owns its domain decisions |
| SVACS | Validation / Trust Participant | Bidirectional | `NICAI.HYDRO.TRACE_CORRELATION` | Validation and evidence exchange | SVACS owns validation governance |
| Bucket | Platform / Runtime Participant | Bidirectional | `NICAI.HYDRO.RUNTIME_INTEGRATION` | Runtime attachment | Bucket owns its platform responsibility |
| Runtime Registry | Constitutional Registry | Bidirectional | `NICAI.HYDRO.REGISTRY_PARTICIPATION` | Runtime registration | Registry governance remains external |
| Capability Registry | Constitutional Registry | Bidirectional | `NICAI.HYDRO.REGISTRY_PARTICIPATION` | Capability registration | Registry governance remains external |
| Replay Registry | Trust Registry | Bidirectional | `NICAI.HYDRO.REPLAY_VERIFICATION` | Replay participation | Replay registry governance remains external |
| InsightFlow | Intelligence Consumer | Hydro → InsightFlow | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Intelligence consumption | InsightFlow owns downstream processing |
| PRANA | Platform / Intelligence Participant | Bidirectional | `NICAI.HYDRO.RUNTIME_INTEGRATION` | Runtime interoperability | PRANA retains its own authority |
| BHEX Knowledge Layer | Knowledge Participant | Bidirectional | `NICAI.HYDRO.KNOWLEDGE_REGISTRY` | Knowledge registration and consumption | BHEX owns Knowledge Layer governance |

---

# 20. TMS Integration Boundary

## Relationship

TMS is treated as an external ecosystem participant that may consume Hydro intelligence.

## Integration

```text
NICAI Hydro
     |
     | Intelligence Contract
     v
TMS
````

## Hydro Provides

* Hydro intelligence output;
* validation status;
* confidence information;
* risk information;
* state information;
* applicable runtime evidence.

## Hydro Does Not Provide

* TMS operational authority;
* TMS policy decisions;
* TMS-specific governance;
* TMS-owned business logic.

## Evidence Requirement

A complete TMS certification requires executable evidence showing the actual TMS runtime interaction.

Repository references alone are not sufficient for full integration certification.

---

# 21. GC Integration Boundary

## Relationship

GC is an external participant consuming or interacting with Hydro runtime intelligence.

## Integration

```text
NICAI Hydro
     |
     | Runtime / Intelligence Contract
     v
GC
```

## Hydro Responsibility

Hydro is responsible for:

* producing its defined intelligence output;
* preserving contract semantics;
* preserving trace context;
* preserving evidence.

## GC Responsibility

GC remains responsible for:

* its own runtime behaviour;
* its own operational authority;
* its own downstream decisions.

---

# 22. MDU Integration Boundary

## Relationship

MDU represents a maritime-domain consumer boundary.

## Integration

```text
NICAI Hydro
      |
      v
Hydro Intelligence
      |
      v
MDU
      |
      v
Maritime Domain Surface
```

Hydro provides intelligence.

MDU determines how that intelligence is consumed within its own domain responsibilities.

Hydro does not become the owner of MDU.

---

# 23. GOUDHA Runtime Integration

## Relationship

GOUDHA Runtime is an ecosystem runtime participant.

Hydro must interact with GOUDHA only through explicit runtime contracts.

## Contract Model

```text
Hydro Identity
      |
      v
Runtime Contract
      |
      v
GOUDHA Runtime
```

## Required Contract Properties

* participant identity;
* capability identity;
* contract version;
* request structure;
* response structure;
* failure behaviour;
* trace behaviour;
* compatibility boundary.

## Authority Boundary

Hydro owns Hydro runtime behaviour.

GOUDHA owns GOUDHA runtime behaviour.

Neither participant should silently absorb the responsibility of the other.

---

# 24. Namami Gange Integration

## Relationship

Namami Gange is an identified domain integration point.

## Integration

```text
NICAI Hydro
      |
      v
Hydro Intelligence
      |
      v
Namami Gange
```

## Hydro Responsibility

Hydro provides the existing Hydro intelligence capability.

## Namami Gange Responsibility

Namami Gange remains responsible for its own domain product and operational interpretation.

## Non-Goal

This integration does not authorize development of new Namami Gange features inside the Hydro runtime.

---

# 25. SVACS Integration

## Relationship

SVACS provides a validation/trust integration boundary.

## Integration

```text
Hydro Runtime
      |
      +---- Trace
      |
      +---- Evidence
      |
      v
SVACS
      |
      v
Validation
```

## Hydro Responsibility

Hydro must expose sufficient execution evidence to permit independent validation.

## SVACS Responsibility

SVACS retains responsibility for its own validation framework and governance.

## Certification Boundary

Hydro cannot self-certify SVACS validation.

Independent evidence is required.

---

# 26. Bucket Integration

Bucket is treated as a platform/runtime integration participant.

## Integration

```text
NICAI Hydro
      |
      | Runtime Attachment
      v
Bucket
```

The attachment must preserve:

* participant identity;
* capability identity;
* contract version;
* trace context;
* execution semantics.

Hydro does not assume ownership of Bucket infrastructure.

---

# 27. Runtime Registry Integration

The Runtime Registry is an external constitutional registry.

## Hydro Role

Hydro provides the information necessary to identify its runtime participant.

## Required Registration Information

```text
Participant Identity
Runtime Identity
Capability Identity
Repository Reference
Version
Compatibility
Runtime Endpoint
Health Endpoint
Evidence Reference
```

## Authority Boundary

```text
Hydro
  |
  | Registration Data
  v
Runtime Registry
```

Hydro owns the registration data it supplies.

The Runtime Registry owns registry governance.

---

# 28. Capability Registry Integration

The Capability Registry identifies reusable runtime capabilities.

Hydro must expose each permanent capability identity consistently.

Example:

```text
HYDRO-CAP-001
NICAI.HYDRO.RUNTIME_API
```

The capability registry relationship must preserve:

* permanent identity;
* capability description;
* owner;
* version;
* compatibility;
* runtime attachment;
* evidence reference.

The registry remains the authoritative registry surface.

---

# 29. Replay Registry Integration

Replay participation must preserve execution evidence associated with a trace.

## Integration Model

```text
Hydro Execution
      |
      v
Trace ID
      |
      v
Replay Evidence
      |
      v
Replay Registry
```

## Required Replay Evidence

Where available:

* trace identifier;
* execution stages;
* event sequence;
* timestamps;
* replay status;
* missing stages;
* sequence information.

## Important Rule

A replay registry record must not be interpreted as proof of replay equivalence unless the replay itself has been independently demonstrated.

---

# 30. InsightFlow Integration

InsightFlow may consume Hydro intelligence outputs.

The integration boundary is:

```text
Hydro Intelligence
       |
       v
InsightFlow
```

Hydro remains responsible for the correctness and contract of its own output.

InsightFlow remains responsible for downstream processing.

---

# 31. PRANA Integration

PRANA is treated as an ecosystem participant.

The Hydro integration boundary is:

```text
NICAI Hydro
      |
      | Runtime / Intelligence Contract
      v
PRANA
```

Hydro must not duplicate PRANA-owned functionality.

Any interaction must use an explicit contract and preserve participant ownership.

---

# 32. BHEX Knowledge Layer Integration

BHEX Knowledge Layer is the external knowledge governance boundary.

Hydro participates through:

```text
NICAI.HYDRO.KNOWLEDGE_REGISTRY
```

The integration model is:

```text
BHEX Knowledge Layer
          |
          v
Knowledge Contract
          |
          v
NICAI Hydro
          |
          v
Hydro Intelligence
```

Hydro may consume or register knowledge required for its own runtime responsibilities.

Hydro does not become the owner of BHEX Knowledge Layer governance.

---

# 33. Runtime Dependency Matrix

| Dependency          | Type            | Required For               | Hydro Responsibility           |
| ------------------- | --------------- | -------------------------- | ------------------------------ |
| Runtime API         | Runtime         | Execution                  | Expose deterministic API       |
| Contract Validation | Governance      | Contract compliance        | Validate Hydro contracts       |
| Capability Registry | Registry        | Discovery                  | Provide capability metadata    |
| Runtime Registry    | Registry        | Runtime discovery          | Provide runtime metadata       |
| Replay Registry     | Trust           | Replay participation       | Provide replay evidence        |
| Knowledge Layer     | Knowledge       | Intelligence context       | Use defined knowledge contract |
| SVACS               | Validation      | Independent validation     | Provide evidence               |
| TMS                 | Consumer        | Intelligence consumption   | Provide defined output         |
| GC                  | Consumer        | Intelligence consumption   | Provide defined output         |
| MDU                 | Consumer        | Domain consumption         | Provide defined output         |
| GOUDHA              | Runtime         | Interoperability           | Preserve runtime contract      |
| Bucket              | Platform        | Attachment                 | Preserve participant boundary  |
| InsightFlow         | Consumer        | Intelligence consumption   | Provide defined output         |
| PRANA               | Participant     | Ecosystem interoperability | Preserve contract boundary     |
| Namami Gange        | Domain Consumer | Domain intelligence        | Provide defined output         |

---

# 34. Integration Contract Categories

All Hydro ecosystem interactions fall into the following contract categories:

| Contract Category   | Purpose                                     |
| ------------------- | ------------------------------------------- |
| Identity Contract   | Identifies Hydro as a permanent participant |
| Capability Contract | Describes a Hydro capability                |
| Runtime Contract    | Defines runtime interaction                 |
| API Contract        | Defines HTTP/API behaviour                  |
| Event Contract      | Defines structured runtime events           |
| Trace Contract      | Defines execution correlation               |
| Replay Contract     | Defines replay evidence                     |
| Registry Contract   | Defines registry participation              |
| Knowledge Contract  | Defines knowledge interaction               |
| Health Contract     | Defines runtime health                      |
| Attachment Contract | Defines participant attachment              |
| Evidence Contract   | Defines verifiable proof                    |

---

# 35. Cross-Layer Interaction Model

The constitutional integration model is:

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
                    NICAI HYDRO RUNTIME
                             |
             +---------------+---------------+
             |               |               |
             v               v               v
       INTELLIGENCE       KNOWLEDGE        TRUST
          LAYER             LAYER          LAYER
             |               |               |
             +---------------+---------------+
                             |
                             v
                  MARITIME DOMAIN PRODUCTS
```

This represents integration relationships, not ownership transfer.

---

# 36. Upstream Dependency Chain

The general upstream chain is:

```text
External Participant
        |
        v
Runtime / API Request
        |
        v
NICAI Hydro Runtime
        |
        v
Validation
        |
        v
Intelligence Processing
```

Where knowledge or configuration is required:

```text
Knowledge / Dataset
        |
        v
Knowledge Contract
        |
        v
Hydro Runtime Context
```

---

# 37. Downstream Dependency Chain

The general downstream chain is:

```text
Hydro Intelligence
        |
        +----> Runtime Consumer
        |
        +----> Maritime Domain Product
        |
        +----> InsightFlow
        |
        +----> Operational Surface
```

Downstream consumers retain their own decision authority.

---

# 38. Trust Dependency Chain

```text
Hydro Execution
      |
      v
Trace ID
      |
      v
Structured Events
      |
      v
Execution Evidence
      |
      v
Replay Verification
      |
      v
Independent Validation
```

This chain is required to support evidence-backed constitutional certification.

---

# 39. Integration Failure Boundaries

Each integration must define its failure boundary.

Examples include:

```text
API Failure
Contract Failure
Dependency Failure
Registry Failure
Event Failure
Trace Failure
Replay Failure
Knowledge Failure
Health Failure
Consumer Failure
```

A failure in an external participant must not be represented as a successful Hydro execution.

Similarly, a Hydro failure must not be attributed to an external participant without evidence.

---

# 40. Determinism Requirement

All constitutional runtime interactions must be deterministic.

For identical valid inputs and identical runtime configuration, the runtime should produce reproducible contract behaviour.

Determinism applies to:

* API contract interpretation;
* validation;
* event structure;
* state transitions;
* trace handling;
* replay processing.

Any nondeterministic behaviour discovered during validation must be recorded as an evidence item.

---

# 41. Version Compatibility Matrix

| Contract            | Compatibility Requirement |
| ------------------- | ------------------------- |
| Runtime API         | Versioned                 |
| Contract Validation | Versioned                 |
| Evaluation Contract | Versioned                 |
| Event Contract      | Versioned                 |
| Trace Contract      | Versioned                 |
| Replay Contract     | Versioned                 |
| Registry Contract   | Versioned                 |
| Knowledge Contract  | Versioned                 |
| Attachment Contract | Versioned                 |
| Health Contract     | Versioned                 |

Breaking contract changes require an explicit compatibility decision.

---

# 42. Evidence Ownership Matrix

| Evidence           | Producer                      | Consumer                      |
| ------------------ | ----------------------------- | ----------------------------- |
| API Response       | Hydro Runtime                 | Validator                     |
| Validation Event   | Hydro Runtime                 | Validation Layer              |
| Intelligence Event | Hydro Runtime                 | Intelligence Consumer         |
| State Event        | Hydro Runtime                 | Runtime Consumer              |
| Pattern Event      | Hydro Runtime                 | Pattern/Intelligence Consumer |
| Action Event       | Hydro Runtime                 | Operational Validator         |
| Trace Record       | Hydro Runtime                 | Replay / Trust                |
| Health Response    | Hydro Runtime                 | Runtime Validator             |
| Registry Record    | Registry                      | Certification                 |
| Replay Result      | Hydro Runtime / Replay System | Certification                 |

---

# 43. Constitutional Non-Duplication Rules

The Hydro runtime must not duplicate:

* registry governance;
* external participant governance;
* downstream product authority;
* global knowledge governance;
* external validation ownership;
* sovereign authority;
* ecosystem-wide operational command.

Hydro should expose integration contracts rather than absorb responsibilities owned by other participants.

---

# 44. Integration Certification Rules

An integration may be classified as:

| Status                      | Definition                                          |
| --------------------------- | --------------------------------------------------- |
| VERIFIED                    | Direct executable evidence confirms the integration |
| DEMONSTRATED                | Runtime interaction was successfully demonstrated   |
| OBSERVED                    | Relevant runtime evidence was observed              |
| INFRASTRUCTURE DEMONSTRATED | Integration infrastructure exists                   |
| PENDING                     | Required evidence is not yet complete               |
| NOT YET CERTIFIED           | Evidence does not support certification             |

The status must describe the evidence state, not the desired architecture.

---

# 45. Evidence vs Architecture Rule

The existence of an integration point in this matrix does not prove that the integration is operational.

The following distinction must always be maintained:

```text
Architecture Definition
        ≠
Runtime Implementation
        ≠
Runtime Demonstration
        ≠
Independent Certification
```

Only the highest level supported by evidence may be claimed.

---

# 46. Current Integration Evidence Boundary

The deployed Hydro runtime has demonstrated runtime surfaces including:

```text
GET /
GET /health
POST /nicai/evaluate
POST /contract/validate
GET /trace/{trace_id}
```

These demonstrate that the corresponding runtime interfaces are available.

They do not, by themselves, prove complete ecosystem integration.

---

# 47. Replay Evidence Boundary

A successful response from:

```text
GET /trace/{trace_id}
```

demonstrates that the trace/replay inspection endpoint is available.

A response containing:

```text
"replay_status": "INCOMPLETE"
```

must be classified as incomplete replay evidence.

Likewise, missing stages such as:

```text
INGESTION
TANTRA_PARTICIPATION
CLUSTER_ANALYSIS
CONTRACT_VALIDATION
TTG_CONSUME
```

must remain visible in the audit record rather than being interpreted as successful execution.

---

# 48. Trace Evidence Boundary

A trace response containing a valid `trace_id` demonstrates trace lookup capability.

It does not automatically prove:

* deterministic trace generation;
* complete trace propagation;
* complete stage coverage;
* replay equivalence.

These require separate evidence.

---

# 49. End-to-End Constitutional Execution

The complete target execution path is:

```text
External Input
      |
      v
INGESTION
      |
      v
TANTRA PARTICIPATION
      |
      v
VALIDATION
      |
      v
ANALYSIS
      |
      v
CLUSTER ANALYSIS
      |
      v
CONTRACT VALIDATION
      |
      v
ACTION
      |
      v
TTG CONSUME
      |
      v
Replay / Evidence
```

The presence of individual Hydro endpoints does not prove that this complete chain has executed successfully.

---

# 50. Constitutional Integration Completion Rule

The constitutional integration work is complete only when:

* every Hydro capability has one permanent identity;
* every capability has a primary constitutional layer;
* every authority boundary is explicit;
* every runtime dependency is documented;
* every API contract is documented;
* every event contract is documented;
* registry participation is evidenced;
* trace propagation is demonstrated;
* replay equivalence is demonstrated;
* observability is demonstrated;
* runtime health is measurable;
* end-to-end constitutional execution is demonstrated;
* production certification is supported by independent evidence.

---

# 51. Final Integration Governance Statement

NICAI Hydro is treated as a reusable Constitutional Runtime Participant.

Its integration model is based on:

```text
Permanent Identity
        +
Explicit Authority
        +
Deterministic Contracts
        +
Registry Participation
        +
Traceability
        +
Replayability
        +
Observability
        +
Runtime Health
        +
Evidence-Based Certification
```

No integration described in this document transfers ownership of another participant's authority to NICAI Hydro.

No new Hydro feature is introduced by this integration matrix.

No unsupported certification claim is made.

---

# 52. Document Continuation

The remaining certification evidence must be maintained through the corresponding validation artifacts:

* `API_EVENT_CONTRACT_MATRIX.md`
* `REGISTRY_PARTICIPATION_REPORT.md`
* `REPLAY_OBSERVABILITY_REPORT.md`
* `RUNTIME_HEALTH_REPORT.md`
* `PRODUCTION_CERTIFICATION_REPORT.md`
* `FINAL_CONSTITUTIONAL_RUNTIME_HANDOVER.md`

These documents must reference executable evidence where certification is claimed.

---

````markdown
# 53. Constitutional Integration Evidence Model

The constitutional integration matrix requires evidence to be connected to the exact
participant, capability, contract, execution, and validation activity being claimed.

The minimum evidence relationship is:

```text
Participant
    |
    v
Capability
    |
    v
Contract
    |
    v
Execution
    |
    v
Trace
    |
    v
Event Evidence
    |
    v
Replay Evidence
    |
    v
Independent Validation
````

Evidence without a traceable relationship to an execution must not be treated as
runtime proof.

---

# 54. Evidence Identity Requirements

Each evidence item should preserve the following identity information:

| Evidence Field       | Requirement                                |
| -------------------- | ------------------------------------------ |
| Evidence ID          | Unique identifier                          |
| Participant ID       | Constitutional participant identity        |
| Capability ID        | Permanent Hydro capability identity        |
| Contract ID          | Contract being validated                   |
| Trace ID             | Runtime execution correlation              |
| Timestamp            | Execution/evidence timestamp               |
| Evidence Type        | API, event, replay, health, registry, etc. |
| Source               | Producing runtime or registry              |
| Result               | Observed result                            |
| Status               | Evidence classification                    |
| Version              | Runtime/contract version                   |
| Validation Reference | Independent validation reference           |

The evidence identity must remain stable enough to support audit and replay.

---

# 55. API Integration Evidence

The deployed Hydro runtime exposes the following API surfaces:

```text
GET /
GET /health
POST /nicai/evaluate
POST /contract/validate
GET /trace/{trace_id}
```

These endpoints represent the currently observed runtime interface.

## API Evidence Classification

| Endpoint                  | Capability                           | Evidence Meaning        |
| ------------------------- | ------------------------------------ | ----------------------- |
| `GET /`                   | `NICAI.HYDRO.RUNTIME_API`            | Runtime availability    |
| `GET /health`             | `NICAI.HYDRO.OBSERVABILITY`          | Runtime health surface  |
| `POST /nicai/evaluate`    | `NICAI.HYDRO.INTELLIGENCE_EXECUTION` | Intelligence execution  |
| `POST /contract/validate` | `NICAI.HYDRO.CONTRACT_VALIDATION`    | Contract validation     |
| `GET /trace/{trace_id}`   | `NICAI.HYDRO.REPLAY_VERIFICATION`    | Trace/replay inspection |

Successful HTTP responses demonstrate API availability.

They do not automatically certify complete constitutional execution.

---

# 56. Root Runtime Evidence

The root endpoint has been observed returning HTTP `200`.

Observed runtime response:

```html
<html>
    <body>
        <h2>NICAI Running ✅</h2>
        <a href="/dashboard">Open Dashboard</a>
    </body>
</html>
```

This demonstrates that the deployed runtime is reachable.

It does not certify:

* registry participation;
* replay equivalence;
* complete trace propagation;
* complete ecosystem execution.

---

# 57. Runtime Health Evidence

The health endpoint is:

```text
GET /health
```

The health endpoint is the primary Hydro runtime health surface.

Health validation must distinguish:

```text
Runtime reachable
        ≠
Runtime healthy
        ≠
Constitutionally integrated
        ≠
Production certified
```

The health response must therefore be recorded as runtime evidence rather than
being interpreted as complete certification.

---

# 58. Intelligence Execution Evidence

The Hydro evaluation endpoint is:

```text
POST /nicai/evaluate
```

Observed Hydro execution outputs include:

```json
{
  "trace_id": "cargo-1",
  "perception_event": {
    "trace_id": "cargo-1",
    "vessel_type": "cargo",
    "confidence_score": 0.6396,
    "dominant_freq_hz": 98.0,
    "anomaly_flag": false
  },
  "validation": {
    "status": "ALLOW",
    "reason": "Valid signal"
  },
  "intelligence_event": {
    "trace_id": "cargo-1",
    "vessel_type": "cargo",
    "confidence": 0.6396,
    "risk_level": "MEDIUM",
    "validation_status": "ALLOW"
  },
  "state_event": {
    "trace_id": "cargo-1",
    "vessel_type": "cargo",
    "risk_level": "MEDIUM",
    "state": "WARNING",
    "anomaly_flag": false,
    "short_label": "Watch"
  }
}
```

This demonstrates that Hydro can produce correlated perception, validation,
intelligence, and state information for an execution.

---

# 59. Intelligence Output Evidence — Additional Cases

Observed execution cases include:

### Speedboat

```json
{
  "trace_id": "speedboat-1",
  "vessel_type": "speedboat",
  "risk_level": "HIGH",
  "state": "ALERT",
  "short_label": "Concern"
}
```

### Submarine

```json
{
  "trace_id": "submarine-1",
  "vessel_type": "submarine",
  "risk_level": "CRITICAL",
  "state": "CRITICAL",
  "anomaly_flag": true,
  "short_label": "Threat"
}
```

### Unknown / Low Confidence

```json
{
  "trace_id": "low-1",
  "vessel_type": "unknown",
  "risk_level": "HIGH",
  "state": "ALERT",
  "short_label": "Concern"
}
```

### Unknown / Anomalous

```json
{
  "trace_id": "anomaly-1",
  "vessel_type": "unknown",
  "risk_level": "CRITICAL",
  "state": "CRITICAL",
  "anomaly_flag": true,
  "short_label": "Threat"
}
```

These outputs demonstrate differentiated Hydro runtime behaviour.

They do not by themselves demonstrate deterministic replay equivalence.

---

# 60. Structured Event Evidence

Observed Hydro runtime evidence includes structured event types such as:

```text
PATTERN
ACTION
```

An observed pattern event has the structure:

```json
{
  "trace_id": null,
  "timestamp": "2026-04-18T10:23:19.473281",
  "type": "PATTERN",
  "data": {
    "pattern_id": "PATTERN_7b0ff5",
    "anomaly_count": 3,
    "affected_zones": [
      "North"
    ],
    "pattern_summary": "Moderate anomalies in North",
    "pattern_type": "REPEATED_ANOMALY",
    "severity_trend": "STABLE",
    "linked_traces": [
      "1bf64f439fff8c00cae14c760bd37ee71663d78c38aaadb8d0a700e5a46e393f",
      "c8fa7d305a5d166ee9e2d03f407d013242abde02cafdca321c6f407c7b8f99d6",
      "8f7df363efdb4c37f9030eaf383abf7f2697858c98e95cf1ef82c7ec706856a4"
    ]
  }
}
```

The observed pattern event demonstrates structured pattern output and linked
trace references.

However, the `trace_id` at the event envelope level is `null`.

Therefore, this evidence should not be interpreted as complete envelope-level
trace propagation.

---

# 61. Action Event Evidence

An observed action event has the following structure:

```json
{
  "trace_id": "acf999a9afdfaabee481b750fc75e0ffa1648ba14cb38b9187776d30e85a3bf9",
  "timestamp": "2026-04-18T10:25:31.642378",
  "type": "ACTION",
  "data": {
    "trace_id": "acf999a9afdfaabee481b750fc75e0ffa1648ba14cb38b9187776d30e85a3bf9",
    "action_type": "eligible_for_escalation",
    "target_role": "authority",
    "timestamp": "2026-04-18T10:25:31.642359",
    "context": {}
  }
}
```

This demonstrates an action event carrying a trace identifier.

The action event is evidence of runtime event production.

It is not evidence that an external authority actually executed the action.

---

# 62. Trace Correlation Model

The expected trace propagation model is:

```text
Request
   |
   v
Trace ID
   |
   +--> INGESTION
   |
   +--> TANTRA_PARTICIPATION
   |
   +--> VALIDATION
   |
   +--> ANALYSIS
   |
   +--> CLUSTER_ANALYSIS
   |
   +--> CONTRACT_VALIDATION
   |
   +--> ACTION
   |
   +--> TTG_CONSUME
   |
   v
Replay
```

The same execution correlation must be preserved across all applicable stages.

---

# 63. Trace Propagation Audit Rule

Trace propagation is considered complete only when:

1. one execution receives a trace identifier;
2. the identifier remains associated with the execution;
3. each required stage records the same execution identity;
4. emitted events preserve the trace identity;
5. downstream consumption preserves the trace identity;
6. replay lookup resolves the same execution;
7. the complete stage chain is reconstructable.

If any required stage is absent, complete trace propagation is not certified.

---

# 64. Deterministic Trace ID Requirement

A deterministic trace identifier must be generated or propagated according to a
documented deterministic rule.

The rule must specify:

```text
Input Identity
+
Execution Context
+
Canonicalization
+
Trace ID Generation Rule
=
Deterministic Trace ID
```

The same canonical execution input must resolve to the same trace identifier
where deterministic identity is required.

Random identifiers must not be described as deterministic identifiers.

---

# 65. Deterministic Trace Validation Procedure

The validation procedure is:

```text
Execution A
    |
    v
Record Input
    |
    v
Record Trace ID A
    |
    v
Replay Same Input
    |
    v
Record Trace ID B
    |
    v
Compare A and B
```

Result interpretation:

| Result            | Classification                                 |
| ----------------- | ---------------------------------------------- |
| Trace A = Trace B | Deterministic trace behaviour demonstrated     |
| Trace A ≠ Trace B | Deterministic trace behaviour not demonstrated |
| Trace unavailable | Trace behaviour not demonstrated               |
| Input differs     | Test invalid for deterministic comparison      |

The test must use identical canonical input and equivalent runtime configuration.

---

# 66. Replay Verification Model

The replay endpoint is:

```text
GET /trace/{trace_id}
```

The expected replay response contains:

```text
trace_id
found_stages
missing_stages
ordered_replay
sequence_chain
replay_status
```

The replay status must be interpreted exactly as returned by the runtime.

---

# 67. Replay Status Classification

| Runtime Result          | Audit Classification                                |
| ----------------------- | --------------------------------------------------- |
| `COMPLETE`              | Replay completion demonstrated                      |
| `INCOMPLETE`            | Replay incomplete                                   |
| Missing required stages | Replay incomplete                                   |
| Empty sequence chain    | Sequence reconstruction not demonstrated            |
| Unknown trace           | Replay lookup failed                                |
| Ordered but incomplete  | Ordering demonstrated, equivalence not demonstrated |

`ordered_replay: true` alone is not sufficient for replay certification.

---

# 68. Observed Replay Result

A replay query for:

```text
acf999a9afdfaabee481b750fc75e0ffa1648ba14cb38b9187776d30e85a3bf9
```

returned:

```json
{
  "trace_id": "acf999a9afdfaabee481b750fc75e0ffa1648ba14cb38b9187776d30e85a3bf9",
  "found_stages": [
    "VALIDATION",
    "VALIDATION",
    "VALIDATION",
    "ANALYSIS",
    "ANALYSIS",
    "ANALYSIS",
    "ACTION",
    "ACTION",
    "ACTION"
  ],
  "missing_stages": [
    "INGESTION",
    "TANTRA_PARTICIPATION",
    "CLUSTER_ANALYSIS",
    "CONTRACT_VALIDATION",
    "TTG_CONSUME"
  ],
  "ordered_replay": true,
  "sequence_chain": [],
  "replay_status": "INCOMPLETE"
}
```

The observed result demonstrates:

* trace lookup works;
* replay inspection works;
* some execution stages are recorded;
* missing stages are reported;
* ordered replay status is exposed.

The observed result does not demonstrate complete replay equivalence.

---

# 69. Replay Certification Decision

Based on the observed replay response:

```text
Replay verification = INCOMPLETE
```

Therefore:

```text
Replay equivalence = NOT YET CERTIFIED
```

The correct audit statement is not:

```text
Replay verified
```

The correct statement is:

```text
Replay inspection demonstrated; complete replay equivalence not yet certified.
```

---

# 70. Required Replay Stage Coverage

The target replay chain identifies the following stages:

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

A complete replay requires all required stages relevant to the execution.

A stage must not be artificially added merely to make replay appear complete.

---

# 71. Sequence Chain Requirement

The replay response currently shows:

```json
"sequence_chain": []
```

An empty sequence chain means that ordered replay may be reported without a
complete reconstructed sequence.

Therefore:

```text
ordered_replay = true
```

must not be interpreted as:

```text
replay_equivalence = true
```

The distinction must remain explicit in certification.

---

# 72. Registry Evidence Model

Registry participation must be validated independently for each registry.

Required registries:

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

For each registry, evidence must identify:

```text
Registry Name
Participant Identity
Capability Identity
Registration Identifier
Registration Version
Registration Status
Registration Timestamp
Evidence Reference
Validation Result
```

---

# 73. Registry Status Rules

| Status                 | Meaning                                                   |
| ---------------------- | --------------------------------------------------------- |
| REGISTERED             | Registry confirms participant registration                |
| VERIFIED               | Registration independently verified                       |
| DEMONSTRATED           | Registration flow demonstrated                            |
| INFRASTRUCTURE PRESENT | Registry integration exists but registration not verified |
| PENDING                | Evidence not available                                    |
| NOT YET CERTIFIED      | Required evidence insufficient                            |

Repository files alone must not be treated as external registry confirmation.

---

# 74. Registry Evidence Boundary

The presence of registry-related implementation in the Hydro repository demonstrates
that registry participation infrastructure exists.

It does not automatically prove that Hydro is registered in every external
constitutional registry.

Therefore, registry claims must be separated into:

```text
Implementation Evidence
        |
        v
Runtime Demonstration
        |
        v
External Registry Confirmation
```

Only the appropriate evidence level may be claimed.

---

# 75. Capability Registry Audit

The Capability Registry audit must verify:

```text
HYDRO-CAP-001
HYDRO-CAP-002
HYDRO-CAP-003
HYDRO-CAP-004
HYDRO-CAP-005
HYDRO-CAP-006
HYDRO-CAP-007
HYDRO-CAP-008
HYDRO-CAP-009
HYDRO-CAP-010
```

Each capability must resolve to exactly one permanent identity.

No capability may have multiple competing constitutional identities.

---

# 76. Runtime Registry Audit

The Runtime Registry audit must verify:

```text
NICAI.HYDRO
```

and its associated:

* runtime endpoint;
* health endpoint;
* version;
* compatibility;
* repository;
* capability references;
* evidence references.

The runtime identity must remain stable across compatible versions.

---

# 77. Execution Registry Audit

Execution Registry participation must preserve:

```text
Participant
Capability
Execution
Trace
Timestamp
Version
Result
```

The registry must allow the execution to be correlated with the Hydro runtime
participant.

---

# 78. Replay Registry Audit

Replay Registry participation must correlate:

```text
Trace ID
Execution
Replay Evidence
Replay Status
Sequence Evidence
```

A replay registry entry without replay evidence does not certify replay equivalence.

---

# 79. Repository Registry Audit

Repository registration must identify:

```text
Repository
Branch
Commit
Version
Runtime Participant
Capability Set
Evidence Package
```

The authoritative repository for this validation layer is:

```text
blackholeinfiverse116-ship-it/nicai-validation-layer_1
```

The repository reference must be versioned when used for certification.

---

# 80. Review Registry Audit

Review Registry participation should preserve:

```text
Review ID
Participant
Capability
Reviewer
Review Version
Review Result
Evidence Reference
```

A review document alone does not replace executable evidence.

---

# 81. Build Registry Audit

Build participation must identify:

```text
Build ID
Repository
Commit
Build Timestamp
Runtime Version
Artifact
Deployment Reference
```

The deployed runtime must be traceable back to a reproducible build where
production certification depends on that build.

---

# 82. Migration Registry Audit

Migration participation must preserve:

```text
Migration ID
Source Version
Target Version
Migration Status
Compatibility
Migration Evidence
```

No migration should be represented as successful without migration evidence.

---

# 83. Part 3 Evidence Classification

The constitutional runtime audit must maintain the following separation:

```text
DOCUMENTED
    |
    v
IMPLEMENTED
    |
    v
EXECUTED
    |
    v
OBSERVED
    |
    v
INDEPENDENTLY VERIFIED
    |
    v
CERTIFIED
```

A claim may only move to the next level when supporting evidence exists.

---

# 84. Current Evidence Interpretation

Based on the observed runtime evidence:

| Claim                               | Evidence Interpretation |
| ----------------------------------- | ----------------------- |
| Runtime reachable                   | Demonstrated            |
| Root endpoint available             | Demonstrated            |
| Health endpoint exists              | Demonstrated            |
| Evaluation endpoint exists          | Demonstrated            |
| Contract validation endpoint exists | Demonstrated            |
| Trace endpoint exists               | Demonstrated            |
| Structured intelligence output      | Demonstrated            |
| Pattern events observed             | Demonstrated            |
| Action events observed              | Demonstrated            |
| Complete trace propagation          | Not Yet Certified       |
| Deterministic Trace IDs             | Not Yet Certified       |
| Replay equivalence                  | Not Yet Certified       |
| Complete registry participation     | Not Yet Certified       |
| Full E2E constitutional execution   | Not Yet Certified       |

These classifications reflect evidence boundaries rather than desired architecture.

---

# 85. Certification Integrity Rule

No certification document may upgrade:

```text
Pending
```

to:

```text
Verified
```

without new evidence.

Likewise:

```text
Demonstrated
```

must not be silently converted into:

```text
Certified
```

unless the certification requirement explicitly accepts that evidence level.

---

# 86. Evidence Reproducibility

Every executable validation should record:

```text
Test ID
Test Date
Runtime URL
Request
Response
Trace ID
Expected Result
Observed Result
Status
Evidence Reference
```

A reviewer must be able to reproduce the test using the same runtime contract.

---

# 87. Constitutional Runtime Test Set

The minimum executable test set is:

```text
TEST-CR-001  Runtime Availability
TEST-CR-002  Runtime Health
TEST-CR-003  Intelligence Evaluation
TEST-CR-004  Contract Validation
TEST-CR-005  Trace Lookup
TEST-CR-006  Trace Propagation
TEST-CR-007  Deterministic Trace
TEST-CR-008  Replay Verification
TEST-CR-009  Registry Participation
TEST-CR-010  Observability
TEST-CR-011  Runtime Health Monitoring
TEST-CR-012  End-to-End Constitutional Execution
```

Each test must have independent evidence.

---

# 88. Minimum Test Evidence Format

Each test should be recorded using:

```markdown
### TEST-CR-XXX — <Test Name>

**Objective:**  
<what is being verified>

**Runtime:**  
<runtime URL>

**Input:**  
<request/input>

**Expected:**  
<expected behaviour>

**Observed:**  
<actual behaviour>

**Trace ID:**  
<trace identifier>

**Evidence:**  
<response/log/reference>

**Status:**  
VERIFIED / DEMONSTRATED / PENDING / NOT YET CERTIFIED
```

---

````markdown
# 89. Observability Integration Model

NICAI Hydro observability must provide sufficient runtime evidence to understand
what the participant executed, which capability executed, which trace was involved,
and what runtime result was produced.

The minimum observability relationship is:

```text
Execution
   |
   +--> Trace ID
   |
   +--> Timestamp
   |
   +--> Capability
   |
   +--> Event
   |
   +--> Result
   |
   +--> Runtime Health
````

Observability must remain structured and machine-readable wherever the runtime
already exposes structured events.

---

# 90. Required Observability Fields

Where applicable, Hydro runtime events should preserve:

| Field            | Purpose                    |
| ---------------- | -------------------------- |
| `trace_id`       | Execution correlation      |
| `timestamp`      | Temporal ordering          |
| `type`           | Event classification       |
| `capability_id`  | Capability identification  |
| `participant_id` | Constitutional participant |
| `data`           | Event-specific payload     |
| `version`        | Contract/runtime version   |
| `status`         | Execution status           |
| `source`         | Event producer             |

The exact fields must follow the implemented runtime contract.

No undocumented field should be represented as mandatory certification evidence.

---

# 91. Event Observability Model

The currently observed event categories include:

```text
PATTERN
ACTION
```

Hydro execution outputs also expose structured:

```text
perception_event
validation
intelligence_event
state_event
```

These should be treated as separate evidence surfaces.

The distinction is:

```text
Runtime Output
      |
      +--> Perception Evidence
      |
      +--> Validation Evidence
      |
      +--> Intelligence Evidence
      |
      +--> State Evidence
      |
      +--> Pattern Evidence
      |
      +--> Action Evidence
```

---

# 92. Trace Observability Boundary

A trace ID provides correlation.

It does not automatically provide complete observability.

Complete observability requires sufficient evidence to reconstruct:

```text
Who executed?
What capability executed?
When did it execute?
What input was used?
What validation occurred?
What intelligence was produced?
What state resulted?
What events were emitted?
What action was produced?
What downstream stage consumed it?
```

If any required information is unavailable, the observability claim must be
limited accordingly.

---

# 93. Runtime Health Model

The Hydro runtime health model consists of:

```text
Availability
+
Health Endpoint
+
Execution Availability
+
Contract Availability
+
Trace Availability
+
Event Availability
```

The primary health surface is:

```text
GET /health
```

Runtime health must be evaluated separately from constitutional certification.

---

# 94. Health State Interpretation

| Health Observation                              | Interpretation                      |
| ----------------------------------------------- | ----------------------------------- |
| HTTP success from `/health`                     | Health endpoint reachable           |
| Runtime process available                       | Runtime availability demonstrated   |
| Evaluation succeeds                             | Intelligence execution demonstrated |
| Contract validation succeeds                    | Contract endpoint demonstrated      |
| Trace lookup succeeds                           | Trace inspection demonstrated       |
| All required constitutional stages execute      | E2E execution demonstrated          |
| All required evidence is independently verified | Certification supported             |

A healthy runtime is not automatically a constitutionally certified runtime.

---

# 95. Runtime Failure Model

Hydro integration failures must be classified according to the failed boundary.

```text
API Failure
    |
    +--> Request rejected / unavailable

Contract Failure
    |
    +--> Contract not accepted

Execution Failure
    |
    +--> Intelligence execution failed

Event Failure
    |
    +--> Required event unavailable

Trace Failure
    |
    +--> Execution correlation unavailable

Replay Failure
    |
    +--> Replay cannot reconstruct execution

Registry Failure
    |
    +--> Registration unavailable or unverified

Health Failure
    |
    +--> Runtime unhealthy/unavailable

Consumer Failure
    |
    +--> Downstream participant unavailable
```

Failures must not be hidden by converting them into successful statuses.

---

# 96. Constitutional Integration Control Points

The following control points are mandatory:

| Control Point | Validation Question                                     |
| ------------- | ------------------------------------------------------- |
| Identity      | Does the capability have one permanent identity?        |
| Layer         | Is the capability assigned to one constitutional layer? |
| Authority     | Is ownership explicit?                                  |
| Contract      | Is the interaction deterministic and versioned?         |
| API           | Does the API follow its documented contract?            |
| Event         | Are events structured and correlated?                   |
| Registry      | Is registry participation evidenced?                    |
| Trace         | Can execution be correlated?                            |
| Replay        | Can execution evidence be reconstructed?                |
| Observability | Can runtime behaviour be inspected?                     |
| Health        | Can runtime health be measured?                         |
| E2E           | Can the constitutional chain be executed?               |
| Certification | Is the claim supported by independent evidence?         |

---

# 97. Constitutional Integration Gate

A Hydro capability passes the constitutional integration gate only when:

```text
Permanent Identity
        AND
Layer Assignment
        AND
Authority Boundary
        AND
Runtime Contract
        AND
API Contract
        AND
Event Contract
        AND
Registry Participation
        AND
Traceability
        AND
Replayability
        AND
Observability
        AND
Runtime Health
        AND
Evidence
```

If one mandatory requirement is absent, the capability remains incomplete for
constitutional certification.

---

# 98. Capability-Level Integration Gate

Each capability must independently satisfy:

```text
Capability Identity
       |
       v
Constitutional Layer
       |
       v
Authority Boundary
       |
       v
Runtime Contract
       |
       v
Registry Participation
       |
       v
Evidence
```

The entire Hydro runtime must not be certified solely because one capability
passes validation.

---

# 99. No Duplicate Responsibility Rule

Every Hydro capability must have:

```text
ONE
|
+-- Permanent Identity
|
+-- Owner
|
+-- Primary Constitutional Layer
|
+-- Primary Authority
|
+-- Primary Runtime Contract
```

Where another ecosystem participant already owns a responsibility, Hydro must
integrate with that participant instead of creating a duplicate capability.

---

# 100. Authority Resolution Model

When overlapping responsibilities are discovered:

```text
Potential Overlap
       |
       v
Identify Existing Owner
       |
       v
Compare Authority Boundaries
       |
       v
Determine Primary Owner
       |
       v
Define Hydro Integration Boundary
       |
       v
Document Resolution
```

Hydro must not silently assume ownership of an external responsibility.

---

# 101. Integration Contract Lifecycle

Every runtime integration follows:

```text
DEFINED
   |
   v
VERSIONED
   |
   v
IMPLEMENTED
   |
   v
EXECUTED
   |
   v
OBSERVED
   |
   v
VALIDATED
   |
   v
CERTIFIED
```

A contract cannot skip directly from `DEFINED` to `CERTIFIED`.

---

# 102. Contract Compatibility Rule

A compatible contract change must preserve:

* permanent identity;
* required semantics;
* required fields;
* authority boundary;
* trace behaviour;
* evidence semantics.

A breaking change requires:

```text
Version Change
+
Compatibility Decision
+
Migration Evidence
```

---

# 103. API Contract Governance

The API contract must preserve:

```text
HTTP Method
Path
Request Schema
Response Schema
Status Codes
Error Behaviour
Trace Behaviour
Version
```

Current runtime surfaces:

```text
GET /
GET /health
POST /nicai/evaluate
POST /contract/validate
GET /trace/{trace_id}
```

Any future change must update the corresponding contract documentation.

---

# 104. Event Contract Governance

Event contracts must preserve:

```text
Event Type
Trace Context
Timestamp
Payload Schema
Producer
Consumer
Version
Ordering Semantics
Failure Behaviour
```

Observed event types include:

```text
PATTERN
ACTION
```

Additional event types may exist in the runtime, but they should only be added
to the certified event catalogue when independently verified.

---

# 105. Replay Contract Governance

Replay validation must preserve:

```text
Trace ID
Execution Stages
Stage Ordering
Sequence
Missing Stages
Replay Status
```

Replay inspection must distinguish:

```text
Lookup
```

from:

```text
Reconstruction
```

and:

```text
Reconstruction
```

from:

```text
Equivalence
```

These are separate certification claims.

---

# 106. Registry Contract Governance

Registry interactions must preserve:

```text
Registry Identity
Participant Identity
Capability Identity
Registration Identity
Version
Status
Evidence
```

Registry implementation cannot be used as a substitute for registry confirmation.

---

# 107. Knowledge Contract Governance

Knowledge interactions must preserve:

```text
Knowledge Identity
Source
Version
Schema
Provenance
Compatibility
Authority
```

Hydro must not change the meaning of an external authoritative knowledge source
without an explicit governance decision.

---

# 108. Downstream Consumer Contract

A downstream consumer must receive only the output defined by the Hydro contract.

The consumer contract should define:

```text
Input
Output
Version
Trace
Event Behaviour
Error Behaviour
Compatibility
```

Hydro must not expose internal implementation details as a required consumer
contract unless explicitly defined.

---

# 109. Constitutional Integration Matrix — Final View

| Layer                     | Provider / Consumer    | Hydro Role                  | Evidence Surface            |
| ------------------------- | ---------------------- | --------------------------- | --------------------------- |
| Sovereign Foundation      | Provider               | Identity participant        | Participant identity        |
| Governance & Constitution | Provider / Consumer    | Contract compliance         | Contract validation         |
| Platform Services         | Provider / Consumer    | Registry/runtime attachment | Registry/runtime interfaces |
| Execution Infrastructure  | Provider               | Runtime execution           | API / health                |
| Intelligence Layer        | Provider               | Intelligence processing     | Evaluation output           |
| Knowledge Layer           | Consumer / Participant | Knowledge integration       | Knowledge registry          |
| Trust Layer               | Provider               | Trace/replay/evidence       | Trace endpoint/events       |
| Maritime Domain Products  | Provider               | Intelligence output         | Consumer integration        |

---

# 110. Integration Evidence Summary

The current evidence supports the following conclusions:

### Demonstrated

* Hydro runtime is deployed and reachable.
* Root runtime endpoint responds.
* Health endpoint exists.
* Intelligence evaluation endpoint exists.
* Contract validation endpoint exists.
* Trace/replay inspection endpoint exists.
* Hydro produces structured intelligence output.
* Hydro produces validation information.
* Hydro produces state information.
* Pattern events have been observed.
* Action events have been observed.

### Not Yet Certified

* Complete trace propagation.
* Deterministic Trace IDs.
* Complete replay equivalence.
* Complete registry participation across all required registries.
* Complete constitutional end-to-end execution.
* Independent certification of every external ecosystem integration.

---

# 111. Evidence-Based Certification Matrix

| Certification Requirement               | Current Evidence                      | Status            |
| --------------------------------------- | ------------------------------------- | ----------------- |
| Permanent Hydro identity                | Runtime/review identity definition    | DEMONSTRATED      |
| Capability inventory                    | Capability identity catalogue         | DEMONSTRATED      |
| Constitutional layer mapping            | Integration matrix                    | DEMONSTRATED      |
| Authority boundaries                    | Authority definitions                 | DEMONSTRATED      |
| Runtime API                             | Live runtime endpoints                | VERIFIED          |
| Contract API                            | `/contract/validate`                  | VERIFIED          |
| Intelligence execution                  | `/nicai/evaluate`                     | DEMONSTRATED      |
| Structured events                       | PATTERN/ACTION evidence               | DEMONSTRATED      |
| Runtime health                          | `/health`                             | DEMONSTRATED      |
| Trace lookup                            | `/trace/{trace_id}`                   | DEMONSTRATED      |
| Complete trace propagation              | Missing stage evidence                | NOT YET CERTIFIED |
| Deterministic Trace IDs                 | Repeatability test required           | NOT YET CERTIFIED |
| Replay equivalence                      | `INCOMPLETE` replay observed          | NOT YET CERTIFIED |
| Registry participation                  | External registry evidence required   | NOT YET CERTIFIED |
| Observability                           | Structured runtime evidence           | DEMONSTRATED      |
| Full E2E constitutional execution       | Complete stage chain not demonstrated | NOT YET CERTIFIED |
| Production constitutional certification | Dependent on unresolved evidence      | NOT YET CERTIFIED |

---

# 112. Certification Evidence Rule

The certification package must never claim more than the evidence proves.

The following mapping is mandatory:

```text
Evidence exists
     |
     v
Claim is demonstrated
```

but:

```text
Evidence exists
     |
     X
Automatic certification
```

Certification requires the evidence to satisfy the specific certification
criterion.

---

# 113. Required Final Validation Sequence

The final validation sequence is:

```text
1. Validate Runtime Identity
          |
          v
2. Validate Capability Inventory
          |
          v
3. Validate Constitutional Layer Mapping
          |
          v
4. Validate Authority Boundaries
          |
          v
5. Validate Runtime Contracts
          |
          v
6. Validate API Contracts
          |
          v
7. Validate Event Contracts
          |
          v
8. Validate Registry Participation
          |
          v
9. Validate Trace Propagation
          |
          v
10. Validate Deterministic Trace Behaviour
          |
          v
11. Validate Replay
          |
          v
12. Validate Observability
          |
          v
13. Validate Runtime Health
          |
          v
14. Validate E2E Constitutional Execution
          |
          v
15. Update Production Certification
          |
          v
16. Final Constitutional Handover
```

---

# 114. Final Handover Preconditions

The final constitutional handover should be issued only after the following
artifacts are available:

```text
Runtime Identity Cards
Constitutional Layer Map
Authority Boundary Report
Runtime Contract Catalogue
API & Event Contract Matrix
Registry Participation Report
Replay & Observability Report
Runtime Health Report
Constitutional Integration Matrix
Production Certification Report
Executable Evidence Package
```

The handover must reference the exact evidence used for each certification claim.

---

# 115. Final Constitutional Runtime Participant Definition

NICAI Hydro is defined as:

```text
Participant:
NICAI.HYDRO

Role:
Constitutional Runtime Participant

Primary Domain:
Hydro / Maritime Intelligence

Primary Responsibilities:
Runtime execution
Contract validation
Hydro intelligence execution
Trace correlation
Replay verification
Registry participation
Observability
Runtime health
Knowledge integration

Authority Boundary:
Hydro-specific runtime and intelligence responsibilities only

External Authority:
Retained by the owning constitutional participant
```

---

# 116. Plug-and-Play Integration Principle

The constitutional runtime participant model is:

```text
Discover
   |
   v
Identify
   |
   v
Attach
   |
   v
Execute
   |
   v
Observe
   |
   v
Replay
   |
   v
Validate
   |
   v
Reuse
```

A consumer should not require a bespoke Hydro architecture redesign merely to
discover or attach the participant.

Integration must use the defined constitutional contracts.

---

# 117. Final Authority Statement

NICAI Hydro does not become the constitutional authority for the BHIV ecosystem.

NICAI Hydro remains a governed participant.

The participant:

* exposes defined capabilities;
* accepts defined runtime contracts;
* produces defined intelligence;
* produces execution evidence;
* participates in registries;
* supports traceability;
* supports replay inspection;
* exposes observability;
* exposes runtime health;
* remains subject to independent validation.

---

# 118. Final Certification Principle

The final certification principle is:

```text
NO EVIDENCE
    =
NO CERTIFICATION

PARTIAL EVIDENCE
    =
PARTIAL / DEMONSTRATED STATUS

COMPLETE REPRODUCIBLE EVIDENCE
    =
CERTIFICATION ELIGIBILITY
```

Certification must remain evidence-backed and independently verifiable.

---

# 119. Final Constitutional Integration Statement

NICAI Hydro is architecturally positioned to operate as a reusable Constitutional
Runtime Participant within the BHIV/TANTRA ecosystem.

The integration model establishes:

```text
Permanent Identity
+
Explicit Authority
+
Constitutional Layer
+
Runtime Contracts
+
API Contracts
+
Event Contracts
+
Registry Participation
+
Traceability
+
Replayability
+
Observability
+
Runtime Health
+
Evidence-Based Certification
```

The remaining certification status is governed by executable evidence.

Where evidence is incomplete, the status remains:

```text
NOT YET CERTIFIED
```

No unsupported claim is promoted to verified status.

---

# 120. Final Audit Position

The Constitutional Integration Matrix is complete as an architecture and evidence
mapping document.

It establishes the intended constitutional integration topology and identifies
the evidence required for final certification.

The matrix itself does not substitute for executable validation.

The final certification package must therefore use this matrix together with the
runtime validation, registry, replay, observability, health, and handover artifacts.

---

# 121. Final Deliverable Cross-Reference

| Required Deliverable                  | Supporting Artifact                        |
| ------------------------------------- | ------------------------------------------ |
| Runtime Identity Cards                | `RUNTIME_IDENTITY_CARDS.md`                |
| Constitutional Layer Map              | `CONSTITUTIONAL_LAYER_MAP.md`              |
| Authority Boundary Report             | `AUTHORITY_BOUNDARY_REPORT.md`             |
| Runtime Contract Catalogue            | `RUNTIME_CONTRACT_CATALOGUE.md`            |
| API & Event Contract Matrix           | `API_EVENT_CONTRACT_MATRIX.md`             |
| Registry Participation Report         | `REGISTRY_PARTICIPATION_REPORT.md`         |
| Replay & Observability Report         | `REPLAY_OBSERVABILITY_REPORT.md`           |
| Runtime Health Report                 | `RUNTIME_HEALTH_REPORT.md`                 |
| Constitutional Integration Matrix     | `CONSTITUTIONAL_INTEGRATION_MATRIX.md`     |
| Production Certification Report       | `PRODUCTION_CERTIFICATION_REPORT.md`       |
| Final Constitutional Runtime Handover | `FINAL_CONSTITUTIONAL_RUNTIME_HANDOVER.md` |

---

# 122. Document Status

```text
Document:
CONSTITUTIONAL_INTEGRATION_MATRIX.md

Participant:
NICAI.HYDRO

Purpose:
Constitutional Runtime Integration Mapping

Classification:
Architecture / Runtime Validation / Evidence Mapping

Certification Principle:
Evidence-backed only

Unsupported Claims:
Not certified

Replay Equivalence:
Not Yet Certified unless independently demonstrated

Complete Trace Propagation:
Not Yet Certified unless independently demonstrated

Complete Registry Participation:
Not Yet Certified unless independently demonstrated

Full E2E Constitutional Execution:
Not Yet Certified unless independently demonstrated
```

---

# 123. Final Constitutional Runtime Handover Boundary

This document may be used as the integration reference for the final handover.

The handover must distinguish between:

```text
WHAT HYDRO IS
```

and:

```text
WHAT HYDRO HAS PROVEN
```

Hydro's constitutional identity and integration architecture may be documented
completely even when some runtime certification evidence remains incomplete.

The final certification state must always follow the executable evidence.

---

# END OF CONSTITUTIONAL INTEGRATION MATRIX

```

