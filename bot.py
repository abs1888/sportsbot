
import requests
import datetime
import telebot

BOT_TOKEN = "8255780777:AAFbPiKHtWEOuclUZZXrp7oho0NEWMBw1Nk"
CHANNEL_NAME = "@tiyu_18888"
API_URL = "https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d={}&s=Soccer"

bot = telebot.TeleBot(BOT_TOKEN)

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

def send_to_channel():
    matches = fetch_matches()
    for match in matches:
        bot.send_message(CHANNEL_NAME, match, parse_mode="Markdown")

if __name__ == "__main__":
    send_to_channel()
