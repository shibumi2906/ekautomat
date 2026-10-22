# AI Calculation Engine

A local system for extracting data from technical drawings and preparing cost calculation inputs.

The project is designed to automate the processing of manufacturing documentation: the system accepts a technical drawing, extracts technical parameters, checks data completeness, and prepares the result for further calculation and export to Excel.

## Problem

When technical drawings are processed manually, a specialist has to:

- find dimensions and technical parameters;
- transfer data into calculation spreadsheets;
- check for missing values;
- correct data formatting;
- repeat the same operations for every document.

The system reduces manual work and helps transform information from technical drawings into a consistent structured format.

## How the system works

1. Receives a technical drawing in PDF format.
2. Converts document pages into images.
3. Extracts text and numerical values.
4. Passes the extracted data to a local language model.
5. Groups the parameters according to a predefined structure.
6. Flags missing or uncertain values.
7. Prepares the data for cost calculation and export to Excel.

## Key features

- processing of PDF technical drawings;
- OCR text recognition;
- extraction of dimensions and technical parameters;
- structuring of unformatted data;
- detection of missing values;
- preparation of data for Excel;
- local processing without sending documents to external cloud services;
- configurable processing logic through settings and prompts.

## Architecture

The solution uses a hybrid approach:

- deterministic modules handle file loading, conversion, cleaning, and data transfer;
- OCR extracts textual information from technical drawings;
- a local LLM interprets the extracted data and transforms it into the required structure;
- the resulting values can be used by the calculation engine or exported to Excel.

The LLM does not perform arithmetic calculations instead of the programmatic calculation core. Its role is to interpret document content and help process unstructured data.

## Project structure

```text
ekautomat/
├── config/
│   └── settings.yaml       # processing settings
├── data/
│   └── input/
│       └── test_blueprint.pdf
├── prompts/
│   └── prompt.txt          # instructions for the local model
├── src/
│   ├── convert.py          # PDF conversion and file preparation
│   ├── ocr.py              # text recognition
│   └── utils.py            # helper functions
├── .gitignore
└── README.md
```

---

# Русская версия


# AI Calculation Engine

Локальная система для извлечения данных из технических чертежей и подготовки расчёта себестоимости.

Проект предназначен для автоматизации обработки производственной документации: система принимает чертёж, извлекает технические параметры, проверяет полноту данных и подготавливает результат для дальнейшего расчёта и переноса в Excel.

## Задача

При ручной обработке чертежей специалисту приходится:

- находить размеры и технические параметры;
- переносить данные в расчётные таблицы;
- проверять пропущенные значения;
- исправлять формат данных;
- повторять одни и те же действия для каждого документа.

Система сокращает объём ручной работы и помогает привести информацию из чертежей к единому структурированному виду.

## Как работает система

1. Получает технический чертёж в PDF.
2. Преобразует страницы документа в изображения.
3. Извлекает текст и числовые значения.
4. Передаёт данные локальной языковой модели.
5. Группирует параметры по заданной структуре.
6. Отмечает отсутствующие или сомнительные значения.
7. Подготавливает данные для расчёта себестоимости и выгрузки в Excel.

## Основные функции

- обработка PDF-чертежей;
- OCR-распознавание текста;
- извлечение размеров и технических параметров;
- структурирование неформатированных данных;
- проверка пропущенных значений;
- подготовка данных для Excel;
- локальная обработка без передачи документов во внешние облачные сервисы;
- настройка логики через конфигурационный файл и промт.

## Архитектура

В основе решения используется комбинированный подход:

- детерминированные модули отвечают за загрузку файлов, конвертацию, очистку и передачу данных;
- OCR извлекает текстовую информацию из чертежа;
- локальная LLM интерпретирует полученные данные и приводит их к заданной структуре;
- итоговые значения можно использовать в расчётном ядре или экспортировать в Excel.

LLM не выполняет арифметические расчёты вместо программного ядра. Её задача — интерпретировать содержание документа и помогать работать с неструктурированными данными.

## Структура проекта

```text
ekautomat/
├── config/
│   └── settings.yaml       # настройки обработки
├── data/
│   └── input/
│       └── test_blueprint.pdf
├── prompts/
│   └── prompt.txt          # инструкции для локальной модели
├── src/
│   ├── convert.py          # преобразование PDF и подготовка файлов
│   ├── ocr.py              # распознавание текста
│   └── utils.py            # вспомогательные функции
├── .gitignore
└── README.md
