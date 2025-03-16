# AITestAutomation

AI Test Automation using browser use and Playwright.

## Overview

This project automates browser interactions and validations using AI and Playwright. It includes tasks such as opening a webpage, extracting information, and performing actions on the webpage.

## Features

- Open and maximize browser windows
- Extract and enter credentials
- Click buttons and extract search results
- Extract attributes and URLs
- Retrieve product descriptions

## Setup

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/AITestAutomation.git
    cd AITestAutomation
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the project root with the following content:
    ```dotenv
    GEMINI_API_KEY=your_gemini_api_key
    LOGIN_USERNAME=your_username
    LOGIN_PASSWORD=your_password
    ```

## Usage

Run the main script to start the automation:
```sh
python main.py