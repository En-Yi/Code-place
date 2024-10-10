https://hub.docker.com/r/amperecomputingai/llama.cpp

https://hub.docker.com/r/3x3cut0r/llama-cpp-python#docker-compose
docker run -d  --name llama-cpp-python --cap-add SYS_RESOURCE -e MODEL_DOWNLOAD="False" -e MODEL_REPO="local" -e MODEL="mistral-7b-instruct-v0.2.Q4_K_M.gguf"
