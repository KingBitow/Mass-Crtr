import os

ASSET_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Assets")

Config = {
    "bot_type": 2,                  # 1 = Selenium (needs Chrome + ChromeDriver), 2 = Requests (faster, no browser)
    "use_local_ip_address": True,
    "use_custom_proxy": False,
    "proxy_file_path": os.path.join(ASSET_DIR, "proxies.txt"),
    "amount_per_proxy": 1,
    "amount_of_account": 5,         # how many accounts to create
    "email_domain": "gmail.com",
    "country": "us",                # "us", "it", "de", etc.
    
    # Optional — for auto email verification (IMAP)
    "activation_email_addr": "",    # your_imap_email@gmail.com
    "activation_email_pass": "",    
    "activation_email_serv": "imap.gmail.com",
    "activation_email_spor": 993,
}
