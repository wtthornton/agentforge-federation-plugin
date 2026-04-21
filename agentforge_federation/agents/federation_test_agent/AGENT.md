---
name: federation-test-agent
namespace: project.federation-test.federation-test-agent
description: Test agent for AgentForge frontend federation/iframe rig.
keywords: [federation, iframe, frontend, test]
runner: agentforge_federation.agents.federation_test_agent.runner:FederationRunner
---

# Federation Test Agent

Deterministic test fixture for the AgentForge frontend federation/iframe surface.

Returns a fixed "federation:ok" token to confirm the plugin agent pipeline is
wired correctly — no LLM, no network, no flake.

Exists to exercise `AgentLoader.load_external()`, namespace registration under
`project.federation-test`, and the plugin agent list surface alongside the
iframe widget route.
