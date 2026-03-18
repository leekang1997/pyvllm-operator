# PyVLLM-Operator

[中文](./README.md) | [English](./README_EN.md)

`PyVLLM-Operator` 是一个面向研究与业务场景的 vLLM Python 封装工具，目标是降低 vLLM 在本地实验、服务拉起与脚本调用中的接入成本。

## 项目定位

vLLM 本身擅长高性能推理，但在很多实际场景里，开发者仍然需要手动处理：

- 服务启动命令
- 模型路径和端口管理
- GPU 设备配置
- OpenAI 兼容请求封装
- 上层业务代码与推理服务之间的解耦

这个项目的目标，就是把这些重复动作封装为更轻的 Python 调用接口。

## 当前能力

- 自动拉起本地 vLLM OpenAI 兼容服务
- 封装基于 `OpenAI` SDK 的模型调用函数
- 统一管理模型路径、端口与 GPU 设备
- 支持把推理服务以 Python 脚本方式嵌入实验流程

## 当前仓库已包含

- `pyvllm_operator/config.py`
  - 统一配置模型路径、端口、GPU 和 API 信息
- `pyvllm_operator/launcher.py`
  - 构造并启动 vLLM 服务进程
- `pyvllm_operator/client.py`
  - 基于 OpenAI 兼容接口的轻量调用封装
- `examples/start_server.py`
  - 演示如何预览启动命令
- `examples/quick_chat.py`
  - 演示如何发起一次最小对话请求

## 对应源码原型

- vLLM 自动调用与本地服务拉起脚本原型
- 关键脚本：
  - `talk_big_model.py`
  - `vllm_use_rp1.py`

## 适合展示的技术点

- vLLM 推理服务自动拉起
- OpenAI 兼容接口封装
- 大模型推理服务与上层代码解耦
- 实验脚本级推理调用能力

## 适合写进简历的一句话

面向 vLLM 构建 Python 原生运行时封装，支持本地服务自动拉起、OpenAI 兼容接口调用及 GPU/端口统一管理，降低复杂推理实验与业务接入门槛。

## 当前需要清洗的内容

- 去掉写死的模型绝对路径
- 去掉本地 conda 环境名
- 提供可配置的端口和设备参数
- 添加最小可运行示例
- 补充依赖文件与许可证

## 推荐的仓库初始结构

```text
pyvllm-operator/
├── README.md
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

## 快速开始

```bash
pip install -r requirements.txt
python examples/start_server.py
```
