# Replay Architecture

## Purpose

Replay reconstructs historical execution using recorded runtime logs.

## Components

- replay_engine.py
- replay_divergence_checker.py
- replay_corruption_simulator.py

## Capabilities

- JSONL support
- Trace reconstruction
- Ordered replay
- Stage verification

Replay does not modify runtime behaviour.