import os
import requests
import datetime
import telebot
from dotenv import load_dotenv  # ✅ 加载 .env

load_dotenv()  # ✅ 加载本地环境变量

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHANNEL_NAME = os.environ.get("TELEGRAM_CHANNEL")
API_URL = "https://www.thesportsdb.com/api/v1/json/3/eventday.php?d={}&s=Soccer"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')

def fetch_matches():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    url = API_URL.format(today)
    res = requests.get(url)
    data = res.json()
    events = data.get("events")
    if not events:
        return ["⚽ 今天没有足球比赛"]

    messages = []
    for event in events:
        league = event.get("strLeague")
        home = event.get("strHomeTeam")
        away = event.get("strAwayTeam")
        time = event.get("strTime")
        idEvent = event.get("idEvent")
        url = f"https://www.thesportsdb.com/event/{idEvent}"

        messages.append(f"🏆 {league}
{home} vs {away} ⏰ {time}
👉 [详情]({url})")

    return messages

def send_daily_matches():
    messages = fetch_matches()
    for msg in messages:
        bot.send_message(CHANNEL_NAME, msg)

if __name__ == "__main__":
    send_daily_matches()