## **Дипломный проект "Яндекс Практикум". Часть 3: UI**

### Проект автоматизации тестирования сайта "Stellar burgers"

1. Ссылка на сайт: *https://stellarburgers.nomoreparties.site/*
2. Автотесты подключены в браузерах: *Google Chrome* и *Mozilla Firefox*
3. Основа для написания автотестов: *Selenium WebDriver* и *Pytest*
4. В автотестах используются: фикстуры и параметризация
5. Отчет о тестировании: *Allure*

**Установка Pytest:**
````
pip install pytest
````

**Установка Selenium:**
````
pip install selenium
````

**Установка Requests:**
````
pip install requests
````

**Запуск автотестов:**
````
pytest -v
````

**Отчет о тестировании Allure:**
````
pip install allure-pytest
````
````
pytest tests --alluredir=allure_results
````
````
allure serve allure_results
````