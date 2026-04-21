"""Unit tests for FederationRunner."""

from agentforge_federation.agents.federation_test_agent.runner import FederationRunner


def test_runner_returns_federation_ok() -> None:
    runner = FederationRunner()
    assert runner.run("anything") == "federation:ok"


def test_runner_is_deterministic() -> None:
    runner = FederationRunner()
    assert runner.run("foo") == runner.run("bar") == "federation:ok"
