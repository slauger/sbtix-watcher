#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import hashlib
import os

# Telegram Config
BOT_TOKEN = '<user-id>:<token>'
CHAT_ID = '<chat-id>'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Ziel-URL und Cache-Datei
url = "https://www.sbtix.de/swp"
base_url = "https://www.sbtix.de"
cache_file = "link_hash.txt"

def fetch_links():
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
  }
  response = requests.get(url, headers=headers, timeout=10)
  response.raise_for_status()
  soup = BeautifulSoup(response.text, "html.parser")
  links = sorted({base_url + a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("/swp/for/")})
  return links

def hash_links(links):
  combined = "\n".join(links)
  return hashlib.sha256(combined.encode("utf-8")).hexdigest()

def send_telegram_message(message):
  payload = {
    "chat_id": CHAT_ID,
    "text": message
  }
  try:
    r = requests.post(TELEGRAM_API_URL, data=payload, timeout=5)
    r.raise_for_status()
  except Exception as e:
    print(f"❌ Fehler beim Senden an Telegram: {e}")

def main():
  try:
    current_links = fetch_links()
    current_hash = hash_links(current_links)

    if os.path.exists(cache_file):
      with open(cache_file, "r") as f:
        old_hash = f.read().strip()
    else:
      old_hash = ""

    if current_hash != old_hash:
      print("🟢 Änderungen gefunden. Telegram-Nachricht wird gesendet.")
      message = "🆕 Neue oder geänderte Links auf https://sbtix.de/swp:\n" + "\n".join(current_links[:5]) + "\n..."
      send_telegram_message(message)
      with open(cache_file, "w") as f:
        f.write(current_hash)
    else:
      print("✅ Keine Änderungen an den Links.")
  except Exception as e:
    print(f"❌ Fehler beim Ausführen des Skripts: {e}")

if __name__ == "__main__":
  main()

