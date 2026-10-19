# 公司 AI 助手 开发常用命令
# 用法:make <target>   (直接 make 即启动服务)

VENV     := .venv
PYTHON   := $(VENV)/bin/python
UVICORN  := $(VENV)/bin/uvicorn

HOST     := 127.0.0.1
PORT     := 8000

.DEFAULT_GOAL := run
.PHONY: run cli install test clean help

run: ## 启动 FastAPI 开发服务(热重载)
	$(UVICORN) app.main:app --reload --host $(HOST) --port $(PORT)

cli: ## 启动 DeepSeek 命令行对话
	$(PYTHON) scripts/deepseek_cli.py

install: ## 安装 requirements.txt 依赖
	$(VENV)/bin/pip install -r requirements.txt

test: ## 跑测试(需先安装 pytest)
	$(PYTHON) -m pytest tests/ -v

clean: ## 清理 __pycache__ 缓存
	find . -type d -name "__pycache__" -not -path "./.venv/*" -not -path "./venv/*" | xargs rm -rf

help: ## 显示本帮助
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'
