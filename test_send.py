
import os
from dotenv import load_dotenv
import telebot

# 加载环境变量
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(BOT_TOKEN)

try:
    bot.send_message(CHANNEL_ID, "📢 测试成功！Bot 已连接频道。")
    print("✅ 消息已发送到频道！")
except Exception as e:
    print("❌ 发送失败：", e)
