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

## 使用前提

这个仓库不是替代 `vLLM` 本身的推理框架，而是构建在 `vLLM` 之上的 Python 调用与启动封装层。

在使用之前，你至少需要：

1. 先安装好 `vLLM`
2. 确保本地有可用的模型权重
3. 确保显卡环境和 CUDA 环境可正常运行
4. 明确你要使用的模型路径、端口和 GPU 设备

如果没有先准备好 `vLLM` 运行环境，这个仓库只能帮你组织调用方式，不能真正完成推理服务启动。

## 这个项目是为了解决什么

很多人第一次用 vLLM 时，真正卡住的不是模型推理本身，而是“怎么把它顺手接进自己的实验或业务代码里”。

- 服务要先手动启动
- 端口、模型名、显卡设备要自己记
- 调试时常常要在 Shell、HTTP 请求和 Python 脚本之间来回切换
- 一旦项目里有多个模型或多个实验，调用方式很容易散掉

这个项目就是想把这些重复而零碎的启动与调用动作，整理成一个更干净的 Python 运行时封装。

## 如何使用这个项目

一个最常见的使用方式是：

1. 先安装并验证 `vLLM`。
2. 准备好本地模型权重目录。
3. 用 `VLLMConfig` 配好模型路径、模型名、端口和 GPU 设备。
4. 用 `build_vllm_command` 或 `start_vllm_server` 启动本地服务。
5. 确认服务已经可以通过 OpenAI 兼容接口访问。
6. 用 `OpenAICompatClient` 发起对话请求。
7. 把它嵌进你自己的实验脚本、评测脚本或者服务端代码里。

它特别适合：

- 本地单机实验
- 多轮 Prompt / 推理评测
- 小型研究项目的推理封装
- 想快速把 vLLM 接进现有 Python 工程的人

## 这个项目大概是怎么工作的

当前仓库的设计很轻，核心就是三个层次：

- `config.py`
  - 定义模型路径、端口、设备、API 地址等运行参数
- `launcher.py`
  - 负责把这些配置拼成 vLLM 启动命令，并拉起服务进程
- `client.py`
  - 负责通过 OpenAI 兼容接口发起请求，减少上层业务直接碰底层细节

这样做好处是，你的实验代码只需要关心“我要调用什么模型”，而不用每次重新处理服务启动和接口细节。

## 你需要配置哪些内容

至少需要明确下面这些信息：

- `model_path`
  - 你的本地模型权重目录
- `served_model_name`
  - 你希望对外暴露的模型名
- `port`
  - 本地推理服务端口
- `gpu_devices`
  - 允许使用的 GPU 编号
- `api_key`
  - OpenAI 兼容接口使用的 API key，占位值也可以
- `activation_command`
  - 如果你依赖特定 conda 环境，可以在这里接入环境激活命令

最关键的一点是：

- 这个项目负责“更方便地启动和调用 vLLM”
- `vLLM` 仍然负责“真正执行推理”

所以如果模型路径、显卡环境或 vLLM 安装本身有问题，这个封装层也无法替你绕过去。

## 它能给大家带来什么帮助

- 帮研究者快速把 vLLM 接进实验流程，而不是卡在启动细节上
- 帮工程同学统一模型调用方式，减少脚本风格混乱
- 帮团队把“推理服务层”和“业务逻辑层”分开，后续更容易维护
- 帮新手以更低成本理解 vLLM 的使用路径

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
pip install vllm openai

# 准备好本地模型路径后，再运行示例
pip install -r requirements.txt
python examples/start_server.py
```

## 一个更准确的上手思路

你可以把这个项目理解成：

- 先装好 `vLLM`
- 再用本仓库把 `vLLM` 的启动和调用方式整理得更适合 Python 工程

也就是说，它更像：

- `vLLM` 的 Python 运行时封装层
- 而不是一个独立的新推理引擎
