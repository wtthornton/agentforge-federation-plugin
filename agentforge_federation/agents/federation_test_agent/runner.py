"""Deterministic runner for federation-test-agent. Pure function, no side effects."""

from __future__ import annotations


class FederationRunner:
    def run(self, input_text: str) -> str:  # noqa: ARG002
        return "federation:ok"
