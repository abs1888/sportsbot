
import os
import requests
import telebot
from dotenv import load_dotenv
import schedule
import time
from datetime import datetime, timedelta

# 加载 .env 环境变量
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
THESPORTSDB_API_KEY = os.getenv("THESPORTSDB_API_KEY")  # 可选
bot = telebot.TeleBot(BOT_TOKEN)

# 中文联赛映射（示例）
LEAGUE_NAMES = {
    "English Premier League": "英格兰超级联赛",
    "Spanish La Liga": "西班牙足球甲级联赛",
    "Italian Serie A": "意大利足球甲级联赛",
}

def get_matches(day_offset=0):
    target_date = datetime.now() + timedelta(days=day_offset)
    date_str = target_date.strftime('%Y-%m-%d')
    url = f"https://www.thesportsdb.com/api/v1/json/1/eventsday.php?d={date_str}&s=Soccer"

    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()
    return data.get("events", []) or []

def get_team_badge(team_name):
    url = f"https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t={team_name}"
    resp = requests.get(url)
    if resp.status_code == 200:
        teams = resp.json().get("teams")
        if teams:
            return teams[0].get("strTeamBadge")
    return None

def send_matches_with_images(chat_id=None, day_offset=0):
    matches = get_matches(day_offset)
    if not matches:
        return

    for match in matches:
        league_en = match.get("strLeague", "未知联赛")
        league_cn = LEAGUE_NAMES.get(league_en, league_en)

        home_team = match.get("strHomeTeam", "主队")
        away_team = match.get("strAwayTeam", "客队")
        time_str = match.get("strTime", "时间未知")
        event_id = match.get("idEvent")

        detail_url = f"https://www.thesportsdb.com/event/{event_id}" if event_id else ""

        caption = f"🏟 {league_cn}\n⚽ {home_team} vs {away_team}\n🕘 时间: {time_str}"
        if detail_url:
            caption += f"\n🔗 [比赛详情]({detail_url})"

        home_badge = get_team_badge(home_team)
        away_badge = get_team_badge(away_team)

        media = []
        if home_badge:
            media.append({'type': 'photo', 'media': home_badge, 'caption': f"{home_team} 队徽"})
        if away_badge:
            media.append({'type': 'photo', 'media': away_badge, 'caption': f"{away_team} 队徽"})

        if media:
            for item in media:
                bot.send_photo(chat_id or CHANNEL_ID, item['media'], caption=item['caption'])
        bot.send_message(chat_id or CHANNEL_ID, caption, parse_mode="Markdown")

# 设置每天北京时间 9 点运行（UTC 为 1 点）
schedule.every().day.at("01:00").do(send_matches_with_images)

if __name__ == "__main__":
    print("🏃 Bot started...")
    while True:
        schedule.run_pending()
        time.sleep(1)
