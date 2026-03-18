from pyvllm_operator import OpenAICompatClient, VLLMConfig


config = VLLMConfig(
    model_path="/path/to/model",
    served_model_name="my-model",
    port=8000,
    api_key="EMPTY",
)

client = OpenAICompatClient(config)
print(client.chat("Hello, introduce yourself in one sentence."))
