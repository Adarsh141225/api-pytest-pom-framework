# API Automation Framework (Pytest + POM)

## Overview
This is a production-grade API automation framework built to test RESTful services. It uses the **Page Object Model (POM)** pattern to ensure the code is scalable and easy to maintain.

## Tech Stack
* **Language:** Python 3.13
* **Testing Framework:** Pytest
* **Pattern:** Page Object Model (POM)
* **Reporting:** Pytest-HTML

## Key Features
* **API Chaining:** Demonstrates passing dynamic data between different API requests.
* **Modular Design:** Clear separation between API client logic and test scenarios.
* **Environment Handling:** Built-in logic to handle non-persistent mock servers.
* **Clean Reporting:** Automated HTML reports for test execution summaries.

## 🚦 Execution
Run all tests and generate a report:
`pytest --html=report.html`
