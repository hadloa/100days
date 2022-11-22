import requests
import os
from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_request_data(url, params):
    r = requests.get(url=url, params=params)
    r.raise_for_status()
    return r.json()


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

av_auth_token = os.environ.get("AV_API_KEY")


def get_daily_stock_data(stock, key=av_auth_token):
    url = 'https://www.alphavantage.co/query'
    params = {
        "function": 'TIME_SERIES_DAILY_ADJUSTED',
        "symbol": stock,
        "apikey": key
    }
    return get_request_data(url=url, params=params)


def get_stock_delta(stock):
    daily_data = get_daily_stock_data(stock)
    x1 = float(list(daily_data['Time Series (Daily)'].values())[1]['4. close'])
    x2 = float(list(daily_data['Time Series (Daily)'].values())[0]['4. close'])
    delta = round((x2 - x1) / x1 * 100)
    return delta


#STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_auth_token = auth_token = os.environ.get("NEWS_API_KEY")


def get_news_data(search, key=news_auth_token):
    url = 'https://newsapi.org/v2/everything'
    date = datetime.now().date()
    params = {'q': search,
              'from': date,
              'sortBy': 'popularity',
              'apiKey': key
              }
    return get_request_data(url=url, params=params)


def get_news_headline_url(search):
    news_data = get_news_data(search)
    headline = list(news_data['articles'])[0]['title']
    url = list(news_data['articles'])[0]['url']
    return headline, url


#STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
twilio_sid = 'AC91d68a7586b73e0b2dad10287c34d8ad'
twilio_auth_token = os.environ.get("TWILIO_API_KEY")


def text_me(text, sid=twilio_sid, key=twilio_auth_token, to='+13522267999'):
    client = Client(sid, key)
    message = client.messages \
        .create(
        body=text,
        from_='+18595358396',
        to=to
                )

    print(message.status)


def stock_message_parser(stock=STOCK, company=COMPANY_NAME):
    delta = get_stock_delta(stock)
    message = None
    if abs(delta) >= 5:
        message_tuple = get_news_headline_url(company)
        if delta > 0:
            message = f"{stock}: 🔺"
        elif delta < 0:
            message = f"{stock}: 🔻"
        message += f"{abs(delta)}%\n" \
                   f"Headline: {message_tuple[0]}\n\n" \
                   f"Link: {message_tuple[1]}"
    else:
        message = f"No Major Movements in {stock} yesterday."
    return message


def main():
    stock_news = stock_message_parser()
    text_me(stock_news)


main()
