"""
Общий модуль для обращения к LLM через OpenAI-совместимый API (LM Studio).

Используется во всех этапах лабораторной работы (main.py, run_experiment.py).
"""

import os
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY", "lm-studio")
BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:1234/v1")
MODEL_NAME = os.getenv("LLM_MODEL")
MODEL_LABEL = os.getenv("LLM_MODEL_LABEL", MODEL_NAME or "unknown-model")

if not MODEL_NAME:
    raise RuntimeError(
        "LLM_MODEL не задан в .env. Узнайте точное имя модели командой:\n"
        "  curl http://localhost:1234/v1/models\n"
        "и загрузите нужную модель в LM Studio перед запуском."
    )

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

SYSTEM_PROMPT = "Отвечай точно и по существу."


def ask_model(prompt: str, system_prompt: str = SYSTEM_PROMPT) -> tuple[str, float]:
    """
    Отправляет один запрос модели и возвращает (текст_ответа, время_в_секундах).
    Бросает исключение наверх — обработка ошибок делается в вызывающем коде,
    чтобы можно было зафиксировать факт ошибки в результатах эксперимента.
    """
    started = time.perf_counter()

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )

    elapsed = time.perf_counter() - started
    text = response.choices[0].message.content
    return text, elapsed


def list_available_models() -> list[str]:
    """Возвращает список моделей, которые сервер LM Studio отдаёт сейчас."""
    models = client.models.list()
    return [m.id for m in models.data]
