from flask import Flask, render_template, request
import yfinance as yf
import datetime

app = Flask(__name__)

def calculate_five_year_return(stock):
    try:
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=5 * 365)

        hist = stock.history(start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

        if not hist.empty:
            start_price = hist['Close'][0]
            end_price = hist['Close'][-1]
            return_rate = ((end_price - start_price) / start_price) * 100
            return round(return_rate, 2)
        else:
            return None
    except Exception as e:
        print(f"Error calculating 5-year return: {e}")
        return None

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)

        info = stock.info

        current_price = info.get('currentPrice')
        beta = info.get('beta')
        pe_ratio = info.get('trailingPE')
        volume = info.get('volume')
        five_year_avg_return = calculate_five_year_return(stock)

        company_name = info.get('shortName', 'N/A')

        stock_data = {
            'ticker': ticker.upper(),
            'company_name': company_name,
            'current_price': current_price,
            'beta': beta,
            'pe_ratio': pe_ratio,
            'volume': volume,
            'five_year_avg_return': five_year_avg_return
        }

        return stock_data

    except Exception as e:
        print(f"Error retrieving data for {ticker}: {e}")
        return None

def assess_investment(stock_data, time_horizon, risk_tolerance):
    beta = stock_data.get('beta')
    five_year_return = stock_data.get('five_year_avg_return')
    pe_ratio = stock_data.get('pe_ratio')

    assessment = 'Ok'
    reasons = []

    if beta is None or five_year_return is None or pe_ratio is None:
        assessment = 'Bad'
        explanation = "Insufficient data to make an assessment."
        return assessment, explanation

    if risk_tolerance == 'Low':
        if beta < 1:
            reasons.append("The stock has lower volatility suitable for low risk tolerance.")
        else:
            assessment = 'Bad'
            reasons.append("High volatility stock, not suitable for low risk tolerance.")

    elif risk_tolerance == 'High':
        if beta > 1:
            reasons.append("High volatility matches high risk tolerance.")
        else:
            reasons.append("Low volatility stock, might not meet high risk preferences.")

    if time_horizon == 'Long-term':
        if five_year_return > 0:
            reasons.append("Positive 5-year return indicates good long-term performance.")
        else:
            assessment = 'Bad'
            reasons.append("Negative 5-year return, not ideal for long-term investment.")

    elif time_horizon == 'Short-term':
        reasons.append("Short-term investment; consider recent performance indicators.")

    if pe_ratio is not None:
        if pe_ratio < 15:
            reasons.append("Low P/E ratio suggests the stock may be undervalued.")
        elif pe_ratio > 25:
            assessment = 'Bad'
            reasons.append("High P/E ratio suggests the stock may be overvalued.")

    explanation = ' '.join(reasons)

    return assessment, explanation

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        time_horizon = request.form['time_horizon']
        risk_tolerance = request.form['risk_tolerance']

        stock_data = get_stock_data(ticker)

        if stock_data:
            assessment, explanation = assess_investment(stock_data, time_horizon, risk_tolerance)
            return render_template('result.html', stock_data=stock_data, assessment=assessment, explanation=explanation)
        else:
            error_message = f"Could not retrieve data for ticker symbol '{ticker.upper()}'. Please try again."
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
