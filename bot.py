from config_data.config import config


def main():
    bot_token = config.tg_bot.token          
    superadmin = config.tg_bot.admin_ids[0]
    return (bot_token, superadmin)



if __name__ == "__main__":
    print(main())
