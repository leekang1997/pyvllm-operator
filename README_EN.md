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

## Prerequisites

This repository does not replace `vLLM` itself. It is a Python-side wrapper and launcher layer built on top of `vLLM`.

Before using it, you should already have:

1. a working `vLLM` installation
2. locally available model weights
3. a usable GPU / CUDA runtime
4. a clear idea of which model path, port, and GPU devices you want to use

Without a working `vLLM` environment, this repository can organize the calling pattern, but it cannot run inference by itself.

## Why This Project Exists

For many first-time vLLM users, the real pain point is not inference itself, but how to integrate vLLM cleanly into their own Python workflow.

- the service has to be started manually
- ports, model names, and GPU devices are easy to lose track of
- debugging often jumps between shell commands, HTTP requests, and Python scripts
- once multiple models or experiments are involved, the calling pattern becomes messy

This project exists to turn those repeated startup and invocation steps into a cleaner Python runtime abstraction.

## How To Use It

A common usage path is:

1. Install and validate `vLLM` first.
2. Prepare a local model-weight directory.
3. Define a `VLLMConfig` with model path, served model name, port, and GPU devices.
4. Use `build_vllm_command` or `start_vllm_server` to launch the local service.
5. Confirm that the service is reachable through an OpenAI-compatible endpoint.
6. Use `OpenAICompatClient` to send chat requests.
7. Embed the client into your own experiment, evaluation, or service code.

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

## What Needs To Be Configured

At minimum, you should configure:

- `model_path`
  - the local path to your model weights
- `served_model_name`
  - the public-facing model name served by vLLM
- `port`
  - the local inference port
- `gpu_devices`
  - the GPU ids allowed for the job
- `api_key`
  - the API key used by the OpenAI-compatible client, even if it is only a placeholder
- `activation_command`
  - an optional environment-activation command if you rely on a specific conda setup

The key boundary is:

- this repository makes vLLM easier to launch and call
- `vLLM` still performs the actual inference work

So if the model path, GPU runtime, or vLLM installation is broken, this wrapper layer will not bypass that problem.

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
pip install vllm openai

# prepare your local model path first
pip install -r requirements.txt
python examples/start_server.py
```

## A More Accurate Mental Model

It is best to think about this project as:

- a Python runtime wrapper around `vLLM`
- not a brand-new inference engine

So the practical order is:

- install `vLLM` first
- then use this repository to standardize startup and invocation
