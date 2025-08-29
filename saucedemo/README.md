# SauceDemo Test Automation Project

## Project Objective
This project automates testing of the SauceDemo website using Selenium WebDriver and Pytest. It includes tests for login functionality and inventory page verification.

## Prerequisites
- Python 3.7 or higher must be installed on your system.
- Google Chrome browser installed.
- ChromeDriver matching your Chrome version (see warning below).

## Critical Warning: ChromeDriver Setup
**You must manually download ChromeDriver that matches your installed Chrome browser version and ensure it is available in your system's PATH.**

1. Check your Chrome version by navigating to `chrome://version/` in your browser.
2. Download the corresponding ChromeDriver from the official site: https://chromedriver.chromium.org/downloads
3. Extract the chromedriver executable and place it in a directory included in your system's PATH (e.g., `/usr/local/bin` on macOS/Linux or `C:\Windows\System32` on Windows).

Failure to set up ChromeDriver correctly will result in test execution errors.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd saucedemo
```

### 2. Create and Activate Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running Tests

### Run All Tests
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest tests/test_login.py -v
```

### Run a Single Test
```bash
pytest tests/test_login.py::test_login_success -v
```

## Project Structure
```
saucedemo/
├── tests/
│   ├── __init__.py
│   ├── login_page.py    # Page Object Model for Login page
│   └── test_login.py    # Test cases
├── .gitignore
├── requirements.txt
└── README.md
```

## Test Cases
- **test_login_success**: Verifies successful login redirects to inventory page
- **test_login_failure**: Verifies error message on invalid credentials
- **test_inventory_page**: Verifies inventory items are displayed after login
