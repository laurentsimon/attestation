# Predicate type: Deployment

Type URI: https://in-toto.io/attestation/deployment

Version 1.0

## Purpose

To authoritatively express which environment an artifact is allowed to be deployed to.

## Use Cases

When deploying an artifact (e.g., a container), we want to restrict which environment
the artifact is allowed to be deployed / run. The environment has access
to resources we want to protect, such as a service account, a Spiffe ID, a Kubernetes pod ID, etc.
The deployment attestation authoritatively binds an artifact to a deployment environment
where an artifact is allowed to be deployed. 

The ability to bind an artifact to an environment is paramount to reduce the blast radius
if vulnerabilties are exploited or environments are compromised. Attackers who gain access
to an environment will pivot based on the privileges of this environment, so it is imperative to
follow the privilege of least principle and restrict _which_ code is allowed to run on _which_ evironment.
For example, we would not want to deploy a container with remote shell capabilities on a pod that processes
user credentials, even if this container is integrity protected at the highest SLSA level.
Conceptually, this is similar to how we think about sandboxing and least-privilege principle on
operating systems. The same concepts apply to different types of environments, including cloud environments.

These use cases are not hypothetical. Binding an artifact to its expected deployment environment is
one of the principles used internally at Google; it is also a feature provided by [Google Cloud Binauthz](https://cloud.google.com/binary-authorization/).

The decision to allow or deny a deployment request may happen "real-time", i.e. the control plane
may query an online authorization service at the time of the deployment. Such an authorization service
requires low-latency / high-availability SLOs to avoid deployment outage. This is exarcebated in systems
like Kubernetes where admission webhooks run for every pod deployed. Thus it is often desirable
to "shift-left" and perform an authorization evaluation ahead of time _before_ a deployment request
reaches the control plane. The deployment attestation _is_ the proof of authorization that the control plane may
use to make its final decision, instead of querying an online service itself. 
Verification of the deployment attestation is simple, fast and may be performed entirely offline.
Overall, this shift-left strategy has the following advantages: less likely to cause production issues,
better debugging UX for devs, less auditing and production noise for SREs and security teams.

## Prerequisites

This predicate depends on the [in-toto Attestation Framework].

## Model

This predicate is for the deployment stage of the software supply chain, where
consumers want to bind an atifact to a deployment environment.

## Schema

```jsonc
{
  // Standard attestation fields:
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{ ... }],

  // Predicate:
  "predicateType": "https://in-toto.io/attestation/deployment/v1",
  "predicate": {

    // Required: creation time.
    "creationTime": "...",

    // Optional: decision details.
    "decisionDetails": {
       "evidence": []<ResourceDescriptor>,
       "policy": []<ResourceDescriptor>
     },

    // Optional: scopes.
    "scopes": map[string]string{
        "<scope-name1>/<version>": "value1",
        "<scope-name2>/<version>": "value2"
    }
  }
}

```

### Fields

**`creationTime`, required** string ([Timestamp](https://github.com/in-toto/attestation/blob/main/spec/v1/field_types.md#Timestamp))

The timestamp indicating what time the attesttion was created.

**`decisionDetails.evidence`, optional** (list of [ResourceDescriptor](https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md))

List of evidence used to make a decision. Resources may include attestations or other relevant evidence. 

**`decisionDetails.policy`, optional** (list of [ResourceDescriptor](https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md))

List of policies used to make the decision, if any. 

**`scopes`, optional** map of string to string (scope type to scope value)

A set of protection scopes of different types. A protection scope is set of properties that identifies the deployment environment to be protected.
A scope defines the target environment that the attestation subject (image, artifact) is bound to.
A scope has a type and a value. A type ends with its version encoded with `/version`, such as `/v1`. Examples of scope types include Kubernetes's objects such as a pod's cluster ID or a GCP service account.
Let's see some examples:

- If we want to "restrict an image to run only on GKE cluster X", the scope type is a "Kubernetes cluster" and "X" is the scope value.
- If we want to "restrict an image to run only under service account Y", the scope type is "service account" and the scope value is "Y".
- If we want to "run an image only if it has been vuln scanned", the scope is empty in the sense that the image is allowed to run in any target environment.

### Parsing Rules

This predicate follows the in-toto attestation [parsing rules](https://github.com/in-toto/attestation/blob/main/spec/v1/README.md#parsing-rules). 
Summary:

- Consumers MUST ignore the `decisionDetails` field during verification. The field is purely informational and is intended only
for troubleshooting and logging.
- The `predicateType` URI includes the major version number and will always change whenever there is a backwards incompatible change.
- Minor version changes are always backwards compatible and "monotonic". Such changes do not update the `predicateType`.
- Producers MAY add custom scope types to the `scopes` field. To avoid type name collisions, a scope type MUST be an URI. See [custom scopes](#custom-scopes).

### Verification

#### Configuration
Verification of a deployment attestation is typically performed by an admisson controller prior to deploying an artifact / container.
The verification configuration MUST be done out-of-band and contain the following pieces of information:

1. Required: The "trusted roots". A trusted root defines an entity that is trusted to generate attestations. A trusted root MUST be configured with at least the following pieces of information:
    - Required: Which identity is trusted to generate the attestation. The identity may be a cryptographic public key, a Fulcio identity, etc.
    - Required: Which scope types the attestation generator is authoritative for.
2. Optional: Required scopes, which is a set of mandatory scope types that must be non-empty for verification to pass. Images must have attestation(s) over each scope type in the set in order to be admitted. Required scopes are necessary in an attestation, but not sufficient; other scopes present in the attestation must match the current environment in order for it to be considered valid. 

#### Logic

Verification happens in two phases:

1. Attestation authenticity verification. Performed by the "attestation layer", it takes as input an image, an attestation, an attestation signature and the trusted roots. It verifies the authenticity of the attestation using the trusted roots. If this verification fails, the attestation is considered invalid and MUST be rejected. If a scope type is unknown or not supported by the verifier, verification MUST fail. 
2. Environment verification. Performed by the "environment layer", it takes as input the intoto payload and matches the scope fields against the deployment environment. Non-empty fields add constraints to the scope and are always interpreted as a logical "AND". The admission controller MUST compare each scope values to its corresponding environment values using an equality comparison. If the values are all equal, verification MUST pass. Otherwise, it MUST fail. Unset scopes (either a scope type with an empty value or a non-present scope) are interpreted as "any value" and are ignored.

### Supported Scopes

#### Kubernetes pod scope

A Kubernetes's pod scope can be represented by (a subset of) the following fields:

```shell
kubernetes.io/pod/service_account/v1  string: A k8 service account
kubernetes.io/pod/cluster_id/v1	      string: A cluster ID
kubernetes.io/pod/namespace/	        string: A namespace
kubernetes.io/pod/cluster_name/v1	    string: A cluster name
...
```

If a scope type is unknown or not supported by the verifier, verification MUST fail.
If the scope matches the environment, verification passes. Otherwise, it MUST fail. A match is positive if all the (non-empty) scope values are equal to the environment values. In the example above:

```shell
attestation's "kubernetes.io/pod/service_account" == environment's "k8's service_account" AND 
attestation's "kubernetes.io/pod/cluster_id" == environment's "k8'scluster_id" AND 
...
```

#### GCP scope

A GCP scope can be represented by (a subset of) the following fields:

```shell
cloud.google.com/service_account/v1 string: A GCP service account
cloud.google.com/location/v1		    string: A location
cloud.google.com/project_id/v1      string: A project id
... 
```

If a scope type is unknown or not supported by the verifier, verification MUST fail.
If the scope matches the environment, verification passes. Otherwise, it MUST fail. A match is positive if all the (non-empty) scope values are equal to the environment values. In the example above:

```shell
attestation's "cloud.google.com/service_account" == environment's "GCP service_account" AND 
attestation's "cloud.google.com/project_id" == environment's "GCP project ID" AND 
...
```

#### Spiffe

A Spiffe scope can be represented by (a subset of) the following fields:

```shell
spiffe.io/id/v1 string: The Spiffe ID
```

If a scope type is unknown or not supported by the verifier, verification MUST fail.
If the scope matches the environment, verification passes. Otherwise, it MUST fail. A match is positive if all the (non-empty) scope values are equal to the environment values. In the example above:

```shell
attestation's "spiffe.io/id" == environment's "Spiffe ID" AND 
...
```

#### Custom scopes

Anyone can define their own scope. To avoid scope name collisions, the scope name must follow a "URI" convention, such as:

```shell
my.myproject.com/resource/v1   string: resource for environment my.myproject.com
```

If a scope type is unknown or not supported by the verifier, verification MUST fail.

## Examples

### Service Account

The attestation below intends to restrict the deployment of an image to run under GCP service account "sa-name@project.iam.gserviceaccount.com".

```jsonc
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{ ... }],

  "predicateType": "https://in-toto.io/attestation/deployment/v1",
  "predicate": {

    "creationTime": "...",

    "scopes": {
      "cloud.google.com/service_account/v1": "sa-name@project.iam.gserviceaccount.com"
    }
}
```

Assume the admisson controller is authoritative for scope type "cloud.google.com/service_account/v1", then the attestation authentication layer verification passes,
because the only scope in the attestation is "cloud.google.com/service_account/v1". If the environment the image is about to be deployed runs under service account "sa-name@project.iam.gserviceaccount.com", the environment verification passes. Otherwise it fails.

If the generator is _not_ authoritative for scope type "cloud.google.com/service_account/v1", then the attestation
layer verification would not pass and the attestation is rejected as invalid.

### Cluster ID and Service Account

The attestation below intends to restrict the deployment of an image to run under GCP service account "sa-name@project.iam.gserviceaccount.com"
and cluster ID "some-unique@clusterid".

```jsonc
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{ ... }],

  "predicateType": "https://in-toto.io/attestation/deployment/v1",
  "predicate": {

    "creationTime": "...",

    "scopes": {
      "cloud.google.com/service_account/v1": "sa-name@project.iam.gserviceaccount.com",
      "kubernetes.io/pod/cluster_id/v1": "some-unique@clusterid"
    }
}
```

Assume the admisson controller is authoritative for scope type "cloud.google.com/service_account/v1" and "kubernetes.io/pod/*", then the attestation authentication layer verification passes, because the only scopes in the attestation are of types "cloud.google.com/service_account/v1" and "kubernetes.io/pod/cluster_id/v1". If the environment the image is about to be deployed runs under service account "sa-name@project.iam.gserviceaccount.com" _AND_ the cluster ID is "some-unique@clusterid", the environment verification passes. Otherwise it fails.

If the generator is configured such that scopes "cloud.google.com/service_account/v1" and "kubernetes.io/pod/cluster_name" are required scopes and the only attestation available is the one above, then the attestation layer verification fails, because scope "kubernetes.io/pod/cluster_name" is not present in the attestation.

### Unrecognized scope

```jsonc
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{ ... }],

  "predicateType": "https://in-toto.io/attestation/deployment/v1",
  "predicate": {

    "creationTime": "...",

    "scopes": {
      "cloud.google.com/service_account/v1": "sa-name@project.iam.gserviceaccount.com",
      "my.custom-scope.com/some-field/v1": "some-value"
    }
}
```

Assume the admisson controller is authoritative for scope type "cloud.google.com/service_account/v1", then the attestation authentication layer verification fails, because the attestation contains an nnon-authoritative (and unrecognized) scope of type "my.custom-scope.com/some-field/v1".

### No scope

```jsonc
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{ ... }],

  "predicateType": "https://in-toto.io/attestation/deployment/v1",
  "predicate": {

    "creationTime": "...",
}
```

The attestation above would pass verification regardless of the deployment environment.

if there was a required scope type conrigured for verification, the environment verification would fail because the attestation contains
no scopes.