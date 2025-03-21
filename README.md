# LocalChatBot

## 사용방법

### 1. 모델 다운로드

``` bash
# hugginface transformers, pytorch required
cd ./models && python3 down_models.py --model-name deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
```

### 2. 환경설정

사용 환경에 맞게 변경

```bash
# .env

export MODEL_NAME=Qwen2.5-0.5B-Instruct
export SERVED_MODEL_NAME=ChatBot
export GPU_MEMORY_UTILIZATION=0.8

export WEBUI_PORT=3000
```

### 3. 실행

```bash
bash launch.sh
```

## Advanced

### 사용중인 GPU의 compute capability가 80 이상이면 👉 Flash Attention, V1 engine, bf16 사용

아래처럼 VLLM_USE_V1, VLLM_ATTENTION_BACKEND bfloat16 옵션 추가하여 사용

```yaml
services:
  vllm:
    ...
    entrypoint: python3 -m vllm.entrypoints.openai.api_server
    ...
    --dtype bfloat16 # 👈
    ...
    environment:
      - VLLM_USE_V1 1  # 👈
      - VLLM_ATTENTION_BACKEND: "FLASH_ATTN"  # 👈
```

### GPU 2개 이상 쓸 수 있다 👉 Tensor Parallel 사용 (방법은 따로 연락)



