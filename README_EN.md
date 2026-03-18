# PyVLLM-Operator

[中文](./README.md) | [English](./README_EN.md)

`PyVLLM-Operator` is a lightweight Python wrapper for vLLM aimed at lowering the cost of local experiments, service startup, and script-level inference integration.

## Project Positioning

vLLM is strong at high-performance inference, but in practice developers still need to manually handle:

- service launch commands
- model path and port management
- GPU device selection
- OpenAI-compatible request wrapping
- decoupling inference services from upper-layer business logic

This project packages those repeated steps into a simpler Python interface.

## Current Capabilities

- starts a local OpenAI-compatible vLLM service
- wraps inference calls through the `OpenAI` SDK
- centralizes model path, port, and GPU configuration
- supports embedding inference services directly into experiment scripts

## Why This Project Exists

For many first-time vLLM users, the real pain point is not inference itself, but how to integrate vLLM cleanly into their own Python workflow.

- the service has to be started manually
- ports, model names, and GPU devices are easy to lose track of
- debugging often jumps between shell commands, HTTP requests, and Python scripts
- once multiple models or experiments are involved, the calling pattern becomes messy

This project exists to turn those repeated startup and invocation steps into a cleaner Python runtime abstraction.

## How To Use It

A common usage path is:

1. Define a `VLLMConfig` with model path, served model name, port, and GPU devices.
2. Use `build_vllm_command` or `start_vllm_server` to launch the local service.
3. Use `OpenAICompatClient` to send chat requests.
4. Embed the client into your own experiment, evaluation, or service code.

It is especially useful for:

- local single-node experiments
- prompt iteration and inference benchmarking
- lightweight research-side inference wrappers
- teams that want to integrate vLLM into an existing Python codebase quickly

## How The Project Works

The current repository is intentionally lightweight and organized around three layers:

- `config.py`
  - defines model path, port, device, and API-related runtime parameters
- `launcher.py`
  - builds the vLLM launch command and starts the service process
- `client.py`
  - sends requests through an OpenAI-compatible interface so upper-layer code does not need to manage low-level details directly

This separation lets your experiment code focus on which model to call, instead of repeatedly reimplementing startup and request logic.

## How It Helps Others

- helps researchers plug vLLM into experiments faster
- helps engineers standardize how inference is invoked across scripts
- helps teams separate the inference runtime layer from business logic
- helps newcomers understand the vLLM usage path with less friction

## What Is Already Included In This Repo

- `pyvllm_operator/config.py`
  - centralized model, port, GPU, and API configuration
- `pyvllm_operator/launcher.py`
  - builds and starts the vLLM process
- `pyvllm_operator/client.py`
  - lightweight OpenAI-compatible chat client
- `examples/start_server.py`
  - preview the launch command
- `examples/quick_chat.py`
  - send one minimal chat request

## Source Origin

- derived from internal prototypes for vLLM automation and local server launch
- representative scripts:
  - `talk_big_model.py`
  - `vllm_use_rp1.py`

## Good Technical Highlights

- vLLM service startup automation
- OpenAI-compatible request abstraction
- better separation between inference runtime and upper-layer code
- script-level inference integration for experimentation

## One-Line Resume Version

Built a Python-native runtime wrapper around vLLM with local service startup, OpenAI-compatible request handling, and unified GPU/port configuration, reducing friction for complex inference experiments and production-like integration.

## Remaining Cleanup Work

- remove hard-coded absolute model paths
- remove local conda-environment assumptions
- expose port and device settings more clearly
- add a minimal runnable example
- complete dependency and license metadata

## Recommended Initial Repo Structure

```text
pyvllm-operator/
├── README.md
├── README_EN.md
├── LICENSE
├── requirements.txt
├── pyvllm_operator/
│   ├── __init__.py
│   ├── launcher.py
│   ├── client.py
│   └── config.py
└── examples/
    ├── start_server.py
    └── quick_chat.py
```

## Quick Start

```bash
pip install -r requirements.txt
python examples/start_server.py
```
