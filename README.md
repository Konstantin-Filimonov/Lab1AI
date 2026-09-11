# Лабораторная работа №1. Первое знакомство с LLM через API (LM Studio)

## 0. Подготовка

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Запустите LM Studio → вкладка **Developer** → **Local Server** → **Start Server**
(по умолчанию порт `1234`). Загрузите первую модель.

Узнайте точное имя модели:
```bash
curl http://localhost:1234/v1/models
```

Впишите это имя в `.env` как `LLM_MODEL`, а в `LLM_MODEL_LABEL` — короткое
человекочитаемое имя для таблиц (например `Model A`).

## 1. Этап 1 — проверка подключения

```bash
python main.py
```
Должен вывестись текст ответа и время выполнения. Повторите для второй модели:
загрузите её в LM Studio, обновите `LLM_MODEL` и `LLM_MODEL_LABEL` в `.env`,
запустите `python main.py` снова. Зафиксируйте оба фактических имени моделей в отчёте.

## 2. Этап 2 — тестовый набор

Уже готов в `prompts.py` — 10 запросов, по одному на каждый требуемый тип задачи.
При желании отредактируйте под свою предметную область (например, замените
часть запросов на задачи по ИБ вашего направления, как рекомендует Приложение А методички).

## 3. Этап 3 — автоматизация эксперимента

Для КАЖДОЙ модели (по очереди, меняя `.env` и модель в LM Studio):

```bash
python run_experiment.py
```

Результаты дописываются в `results/experiment_results.csv` (общий файл для всех моделей,
старые строки не удаляются).

## 4. Этап 4 — оценка результатов

```bash
python make_scoring_template.py
```

Откройте `results/scoring_template.csv` в Excel/LibreOffice/Google Sheets и вручную
проставьте баллы 0–2 по столбцам `correctness_0_2`, `completeness_0_2`,
`instruction_follow_0_2`, `usefulness_0_2`, сверяясь со столбцом `answer`.
Если корректность нельзя проверить — поставьте `True` в `score_uncertain` и не придумывайте оценку.

## 5. Сводная таблица (раздел 9 методички)

```bash
python summarize.py
```

Выведет и сохранит `results/summary.csv` (средние по моделям) и
`results/summary_by_type.csv` (средние по моделям и типам задач) — вставьте их в отчёт.

## 6. Дополнительное задание (по желанию, п. 10)

```bash
python bonus_stability.py
```

Повторяет 3 запроса по 5 раз для текущей модели из `.env`, считает длину ответов
(для оценки лаконичности) — запустите для каждой модели отдельно.

## Структура проекта

```
lab01_llm_api/
├── .env.example
├── .gitignore
├── requirements.txt
├── llm_client.py          # общий клиент к LM Studio
├── main.py                 # Этап 1: проверка подключения
├── prompts.py               # Этап 2: тестовый набор из 10 запросов
├── run_experiment.py        # Этап 3: автоматизация + сохранение в CSV
├── make_scoring_template.py # Этап 4: шаблон для ручной оценки
├── summarize.py              # Раздел 9: сводное сравнение моделей
├── bonus_stability.py        # Доп. задание: стабильность ответов
└── results/                  # CSV-результаты (создаётся автоматически)
```
