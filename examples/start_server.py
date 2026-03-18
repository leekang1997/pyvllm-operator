from pyvllm_operator import VLLMConfig, build_vllm_command


config = VLLMConfig(
    model_path="/path/to/model",
    served_model_name="my-model",
    port=8000,
    gpu_devices=["0"],
)

print("Preview command:")
print(" ".join(build_vllm_command(config)))
print("Call start_vllm_server(config) when you are ready to launch the server.")
