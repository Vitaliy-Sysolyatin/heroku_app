# Selenium Basic + Advanced

## Структура

- `tests/basic/` — ДЗ 14.
- `tests/advanced/` — ДЗ 16.
- `pages/` — Page Object'ы ДЗ 14.
- `conftest.py` — ДЗ 14.
- `tests/advanced/conftest.py` — фикстура ДЗ 16 с настройками Allure.
- `files/` — файлы проекта.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

Все тесты:

```bash
pytest -v
```

ДЗ 14:

```bash
pytest tests/basic -v
```

ДЗ 16:

```bash
pytest tests/advanced -v
```

Allure:

```bash
pytest tests/advanced -v --alluredir=allure-results
allure serve allure-results
```
