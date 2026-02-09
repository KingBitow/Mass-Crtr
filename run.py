from modules.config import Config
from modules.generateaccountinformation import generate_account_info
from modules.storeusername import store_account
from modules.activate_account import get_activation_url  # optional

if Config["bot_type"] == 1:
    from modules.seleniumbot import runbot
elif Config["bot_type"] == 2:
    from modules.requestbot import runBot
else:
    print("Invalid bot_type in config")
    exit()

for i in range(Config["amount_of_account"]):
    account_info = generate_account_info(
        Config["email_domain"],
        Config["country"]
    )
    
    username = account_info["username"]
    password = account_info["password"]
    email = account_info["email"]
    identity = account_info["identity"]
    
    print(f"[{i+1}] Creating: {username} | {email}")
    
    success = False
    if Config["bot_type"] == 1:
        success = runbot(username, password, email, identity)
    else:
        success = runBot(username, password, email, identity)
    
    if success:
        store_account(username, password, email)
        print(f"Success → saved to Assets/usernames.txt")
        
        # Optional auto-activation (if IMAP configured)
        if Config.get("activation_email_addr"):
            activation_link = get_activation_url(email)
            if activation_link:
                print(f"Activation link used: {activation_link}")
    else:
        print("Failed")
