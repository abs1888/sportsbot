
# ⚽ SportsBot - 体育赛事推荐机器人

一个通过 [TheSportsDB API](https://www.thesportsdb.com/) 获取体育赛事信息的 Telegram Bot，支持每日定时推送多联赛赛事推荐，可自动部署在 Render 上并连接 Telegram 频道。

---

## 🚀 功能特性

- ✅ 定时每日推送赛事推荐（支持多联赛）
- ✅ 接入 Telegram 频道自动推送
- ✅ 可扩展添加 logo、赛事图片、评分等信息
- ✅ 使用 Render 免费云部署，稳定托管

---

## 📦 技术栈

- Python 3.x
- requests / schedule
- Telegram Bot API
- TheSportsDB API
- Render（部署平台）

---

## 📸 使用效果（Telegram 频道中）

```
🏟️ 比赛推荐（今日）
- ⚽ 曼联 vs 曼城
- ⏰ 时间：2025-07-24 20:00
- 🏆 联赛：英超联赛
```

---

## 🛠️ 本地运行

```bash
git clone https://github.com/YOUR_tiyu_18888/sportsbot.git
cd sportsbot
pip install -r requirements.txt

# 设置环境变量
export BOT_TOKEN=your_8255780777:AAFbPiKHtWEOuclUZZXrp7oho0NEWMBw1Nk
export CHANNEL_ID=@your_tiyu_18888
export SPORTSDB_API_KEY=your_sportsdb_key

python main.py
```

---

## ☁️ Render 自动部署指南

1. 新建 Render Web Service
2. 构建命令：

   ```bash
   pip install -r requirements.txt
   ```

3. 启动命令：

   ```bash
   python main.py
   ```

4. 添加环境变量：

| Key                | Value                  |
|--------------------|------------------------|
| BOT_TOKEN          |8255780777:AAFbPiKHtWEOuclUZZXrp7oho0NEWMBw1Nk |
| CHANNEL_ID         | `@tiyu_1888bot`   |
| SPORTSDB_API_KEY   | `1` 或申请的 API key   |

---

## 📌 环境变量说明

- `BOT_TOKEN`: 8255780777:AAFbPiKHtWEOuclUZZXrp7oho0NEWMBw1Nk
- `CHANNEL_ID`: 目标推送的频道名（ `@tiyu_18888`）
- `SPORTSDB_API_KEY`: v1 Base URL = https://www.thesportsdb.com/api/v1/json
v2 Base URL = https://www.thesportsdb.com/api/v2/json API Key（https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Arsenal
)）

---

## 📬 联系 & 反馈

欢迎提出 issue 或 pull request。  
如需定制化功能（例如推送图片、比分分析、赛程订阅）欢迎联系开发者。

---

## ⭐ License

MIT License.
