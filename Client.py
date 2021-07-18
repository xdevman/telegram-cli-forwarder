from telethon import TelegramClient

# Get api ID/Hash From:
# https://my.telegram.org                
api_id = "HERE"                       
api_hash = "HERE"                
# Message ID
from_msgid = 0
to_msgid = "here"
# Public Channel
from_c = ""   
to_c = ""              

async def main():
     for xx in range(from_msgid, to_msgid+1):
         try :
             await client.forward_messages(to_c,xx,from_c)
             print(xx)
         except Exception as e:
             print(e)

with TelegramClient('session', api_id, api_hash) as client:
    client.loop.run_until_complete(main())
