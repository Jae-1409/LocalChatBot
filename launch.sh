source .env
COMPOSE_PROJECT_NAME=chatbot docker compose --file docker-compose.yaml up -d --remove-orphans --no-build vllm webui