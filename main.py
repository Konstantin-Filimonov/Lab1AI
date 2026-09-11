"""
Этап 1. Проверка подключения.

Выполняет один простой запрос к модели, заданной в .env,
выводит текст ответа и время выполнения.

Инструкция:
1. Запустите LM Studio, во вкладке "Developer" -> "Local Server" нажмите Start Server.
2. Загрузите первую модель в LM Studio.
3. В .env укажите LLM_MODEL = точное имя загруженной модели
   (см. curl http://localhost:1234/v1/models) и LLM_MODEL_LABEL для отчёта.
4. Запустите: python main.py
5. Зафиксируйте в отчёте фактический MODEL_NAME.
6. Смените модель в LM Studio, поменяйте LLM_MODEL / LLM_MODEL_LABEL в .env,
   повторите запуск для второй модели.
"""

from llm_client import ask_model, MODEL_NAME, MODEL_LABEL, list_available_models

if __name__ == "__main__":
    print(f"Проверка подключения к модели: {MODEL_NAME} ({MODEL_LABEL})")

    try:
        available = list_available_models()
        print(f"Модели, доступные на сервере сейчас: {available}")
        if MODEL_NAME not in available:
            print(
                "ВНИМАНИЕ: LLM_MODEL из .env не совпадает ни с одной из "
                "моделей, отданных сервером. Проверьте имя."
            )
    except Exception as exc:
        print(f"Не удалось получить список моделей: {exc}")

    print("-" * 60)

    answer, latency = ask_model(
        "Объясни разницу между хешированием и шифрованием."
    )
    print(answer)
    print(f"\nВремя ответа: {latency:.2f} c")
