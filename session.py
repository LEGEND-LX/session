
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
LEGENDBOT = """
"""
print(LEGENDBOT)
print("""String Generator. ==> LEGENDBot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.
╭╮╱╱╭━━━┳━━━┳━━━┳━╮╱╭┳━━━┳━━╮╭━━━┳━━━━╮
┃┃╱╱┃╭━━┫╭━╮┃╭━━┫┃╰╮┃┣╮╭╮┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃┃╱╱┃╰━━┫┃╱╰┫╰━━┫╭╮╰╯┃┃┃┃┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃┃╱╭┫╭━━┫┃╭━┫╭━━┫┃╰╮┃┃┃┃┃┃╭━╮┃┃╱┃┃╱┃┃
┃╰━╯┃╰━━┫╰┻━┃╰━━┫╱┃┃┣╯╰╯┃╰━╯┃╰━╯┃╱┃┃
╰━━━┻━━━┻━━━┻━━━┻╯╱╰━┻━━━┻━━━┻━━━╯╱╰╯"""
      )
APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as LEGENDBOT:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(LEGENDBOT.session.save())
    print("")
    print("You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions.")
    omk =LEGENDBOT.send_message("me", f"`{LEGENDBOT.session.save()}`")
    omk.reply("The above is the `LEGEND_STRING` #POWERFUL [LEGENDBOT](https://t.me/Legend_Userbot)"
		)
