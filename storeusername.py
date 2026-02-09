import os
from modules.config import Config, ASSET_DIR

def store_account(username, password, email):
    path = os.path.join(ASSET_DIR, "usernames.txt")
    line = f"{username}:{password}:{email}\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(line)
