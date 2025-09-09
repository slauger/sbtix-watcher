# Summer Breeze Ticket Watcher 🎫

Ein einfaches Python-Script, das automatisch die [Summer Breeze Ticketbörse](https://www.sbtix.de/swp) überwacht – speziell die Angebote für **Reserved Camping** (z. B. Blue Area) – und dich über **Telegram benachrichtigt**, sobald sich neue Angebote zeigen.

## 💡 Ziel

Automatisch benachrichtigt werden, wenn sich verfügbare Links auf der Ticketseite ändern – ideal, um z. B. **Tickets für Reserved Camping oder bestimmte Anreiseslots zu ergattern**.

## 🔧 Voraussetzungen

- Python 3.7+
- Telegram Bot + eigene Chat-ID
- `requests` und `beautifulsoup4`

## 🐍 Installation

```bash
git clone https://github.com/dein-nutzername/summerbreeze-watcher.git
cd summerbreeze-watcher
pip install -r requirements.txt
```

### 🧪 Testlauf

```bash
python sbtix_watcher.py
```

Du bekommst dann eine Ausgabe auf der Konsole, z. B.:

```
✅ Keine Änderungen an den Links.
```

Oder – wenn sich was getan hat:

```
🟢 Änderungen gefunden. Telegram-Nachricht wird gesendet.
```

## 📲 Telegram einrichten

### 1. Bot erstellen

- Gehe zu [@BotFather](https://t.me/botfather)
- Sende `/newbot` und folge den Anweisungen
- Notiere dir den **Bot Token**

### 2. Chat-ID ermitteln

- Starte den neuen Bot (z. B. mit `/start`)
- Öffne diese URL (Token ersetzen):

  ```
  https://api.telegram.org/bot<DEIN-TOKEN>/getUpdates
  ```

- Die Antwort enthält deine `chat.id`, z. B.:

  ```json
  "chat": { "id": 123456789, ... }
  ```

- Trage `BOT_TOKEN` und `CHAT_ID` in `sbtix_watcher.py` ein

## ⚙️ Automatisierung per cron

Füge das Skript z. B. alle 30 Minuten in deinen Cronjob ein:

```bash
crontab -e
```

```cron
*/30 * * * * /usr/bin/python3 /pfad/zu/sbtix_watcher.py >> /tmp/sbtix.log 2>&1
```

## 📂 Dateien

- `sbtix_watcher.py` – Hauptscript
- `link_hash.txt` – wird automatisch erzeugt, um die vorherigen Links zu speichern
- `requirements.txt` – Abhängigkeiten

## ✅ Beispielausgabe (Telegram)

> 🆕 Neue oder geänderte Links auf sbtix.de:  
> https://www.sbtix.de/swp/for/77832-tickets-blue-area-reserved-camping-2025-dinkelsbuehl-sinbronn-am-12-08-2025  
> ...

## 🛟 Hinweis

Dies ist kein offizielles Tool von Summer Breeze oder sbtix.de. Bitte nur für den persönlichen, fairen Gebrauch verwenden.

## 📘 Lizenz

MIT License – feel free to use, fork, improve.
