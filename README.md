# Stock Analyzer

Stock Analyzer is a Python-based web application that allows users to evaluate whether a specific stock aligns with their risk tolerance and investment preferences. **Note: This tool is for informational purposes only and is not sound investment advice.**

## Features

- Accepts user input for:
  - Risk tolerance level (e.g., conservative, moderate, aggressive).
  - Stock ticker symbol.
- Retrieves real-time stock data using `yfinance`.
- Performs analysis using financial data and user-provided risk tolerance.
- Outputs results indicating whether the stock aligns with the user's portfolio preferences.

## Tech Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Data Handling**: Pandas, Numpy
- **Data Retrieval**: yfinance, BeautifulSoup
- **Database (if applicable)**: Peewee

## Requirements

The project uses the following dependencies:

- Flask: Web framework for serving the application.
- yfinance: For fetching stock data.
- Pandas & Numpy: For data analysis and manipulation.
- BeautifulSoup: For web scraping (if needed for supplementary data).
- Jinja2: For rendering HTML templates.
- Additional dependencies are listed in `requirements.txt`.

## Install them using:

### BASH
pip install -r requirements.txt
Installation
Clone the repository:


git clone https://github.com/your-username/stock-analyzer.git
cd stock-analyzer
Create a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

### Install dependencies:

pip install -r requirements.txt
Run the Flask application:

python app.py
Open your browser and navigate to:


http://127.0.0.1:5000

## Usage
Launch the web app by running the Flask server.
Enter the following:
Your risk tolerance level (conservative, moderate, or aggressive).
The stock ticker symbol of the stock you want to analyze.
Submit the form to analyze the stock.
View the result, which indicates whether the stock fits your risk profile based on financial metrics and risk assessment.

### Example Output
Input:
Risk Tolerance: Moderate
Stock Ticker: AAPL
Output:
"AAPL is a suitable stock for your portfolio given your moderate risk tolerance."
OR
"AAPL may be too volatile for your portfolio based on your risk preferences."
Disclaimer
This application is for informational purposes only and is not sound investment advice. Always consult with a financial professional before making investment decisions.

## Project Structure
stock-analyzer/
│
├── app.py                # Main application script
├── templates/            # HTML templates for web UI
├── static/               # CSS and other static assets
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation

## Dependencies
The following dependencies are used in this project:

Flask: Web framework.
Pandas and Numpy: Data analysis and processing.
yfinance: Stock data API.
BeautifulSoup: For potential scraping tasks.
Peewee: Lightweight database ORM.
Other dependencies listed in requirements.txt.