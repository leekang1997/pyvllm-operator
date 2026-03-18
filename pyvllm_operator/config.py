from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class VLLMConfig:
    model_path: str
    served_model_name: str
    host: str = "127.0.0.1"
    port: int = 8000
    api_key: str = "EMPTY"
    gpu_devices: list[str] = field(default_factory=lambda: ["0"])
    gpu_memory_utilization: float = 0.8
    max_model_len: int = 8192
    tensor_parallel_size: Optional[int] = None
    trust_remote_code: bool = True
    python_executable: str = "python3"
    working_dir: Optional[str] = None
    activation_command: Optional[str] = None

    @property
    def base_url(self) -> str:
        return f"http://{self.host}:{self.port}/v1"

    @property
    def cuda_visible_devices(self) -> str:
        return ",".join(self.gpu_devices)
