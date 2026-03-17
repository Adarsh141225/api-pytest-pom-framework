# API + UI Automation Framework (Pytest + POM)

## Overview
Production-grade automation framework for 
testing RESTful APIs and Web UI using 
Page Object Model (POM) pattern.

## Tech Stack
- Language: Python 3.13
- Testing Framework: Pytest
- API Client: Requests library
- UI Automation: Selenium WebDriver
- UI Automation: Playwright
- Pattern: Page Object Model (POM)
- Reporting: Pytest-HTML
- CI/CD: Docker + Jenkins

## Framework Structure
```
├── clients/          # API client (CRUD operations)
├── pages/            # UI Page Objects
│   ├── base_page.py  # Selenium base methods
│   ├── login_page.py # Selenium login page
│   └── pw_login_page.py # Playwright login page
├── tests/            # All test cases
├── utils/            # ConfigLoader + Schemas
├── config.ini        # Environment config
├── Dockerfile        # Container setup
└── Jenkinsfile       # CI/CD pipeline
```

## Key Features
- API Chaining: Dynamic data between requests!
- Contract Testing: JSON schema validation!
- Parallel Execution: pytest-xdist -n auto!
- UI Testing: Selenium + Playwright with POM!
- Parametrize: Multiple data sets in one test!
- Reporting: Automated HTML reports!

## Execution
```bash
# Run all tests
pytest --html=report.html

# Run API tests only
pytest tests/test_chained_api.py -v

# Run Selenium UI tests
pytest tests/test_login_ui.py -v

# Run Playwright tests
pytest tests/test_playwright_login.py -v

# Parallel execution
pytest -n auto --html=report.html