import os
import shlex
import subprocess
from typing import Sequence

from .config import VLLMConfig


def build_vllm_command(config: VLLMConfig) -> list[str]:
    command = [
        config.python_executable,
        "-m",
        "vllm.entrypoints.openai.api_server",
        "--model",
        config.model_path,
        "--served-model-name",
        config.served_model_name,
        "--gpu_memory_utilization",
        str(config.gpu_memory_utilization),
        "--max_model_len",
        str(config.max_model_len),
        "--port",
        str(config.port),
    ]
    if config.trust_remote_code:
        command.append("--trust-remote-code")
    if config.tensor_parallel_size:
        command.extend(["--tensor_parallel_size", str(config.tensor_parallel_size)])
    return command


def start_vllm_server(
    config: VLLMConfig,
    *,
    extra_env: dict[str, str] | None = None,
    stdout=None,
    stderr=None,
) -> subprocess.Popen:
    env = os.environ.copy()
    env["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
    env["CUDA_VISIBLE_DEVICES"] = config.cuda_visible_devices
    if extra_env:
        env.update(extra_env)

    command = build_vllm_command(config)
    working_dir = config.working_dir or os.getcwd()

    if config.activation_command:
        shell_command = f"{config.activation_command} && {' '.join(shlex.quote(part) for part in command)}"
        return subprocess.Popen(
            shell_command,
            shell=True,
            cwd=working_dir,
            executable="/bin/bash",
            env=env,
            stdout=stdout,
            stderr=stderr,
            text=True,
        )

    return subprocess.Popen(
        command,
        cwd=working_dir,
        env=env,
        stdout=stdout,
        stderr=stderr,
        text=True,
    )


def format_command_preview(command: Sequence[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)
