# LocalChatBot

## 사용방법

1. 모델 다운로드

``` bash
# hugginface transformers, pytorch required
cd ./models && python3 down_model.py --model-name deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
```

2. 환경설정

사용 환경에 맞게 변경

```bash
# .env

export MODEL_NAME=Qwen2.5-0.5B-Instruct
export SERVED_MODEL_NAME=ChatBot
export GPU_MEMORY_UTILIZATION=0.8

export WEBUI_PORT=3000
```

3. 실행

```bash
bash launch.sh
```