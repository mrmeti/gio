#cr Amir Reza
# @Nu_Tm
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.raw import functions
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from re import match
import random
from datetime import datetime
import os ; os.chdir(os.path.dirname(os.path.abspath(__file__)))
def if_not_exist_creat(filename):
    if not os.path.isfile(filename):
        with open(filename , "w") as f:
            f.write("")
            f.close() 
def write(filename , text):
    with open(filename , "w") as f:
        f.write(text)
        f.close() 
def read(filename):
    with open(filename , "r") as f:
        return f.read()

org = [":", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
fonts = [[":", "๐ถ", "๐ท", "๐ธ", "๐น", "๐บ", "๐ป", "๐ผ", "๐ฝ", "๐พ", "๐ฟโ"],
[":", "๐", "๐", "๐", "๐", "๐", "๐", " ๐", "๐", "๐ ", "๐ก"],
[":", "๐ฌ", "๐ญ", "๐ฎ", "๐ฏ", "๐ฐ", "๐ฑ", "๐ฒ", "๐ณ", "๐ด", "๐ต"],
[":", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐", "๐"],
[":", "๐ถ", "า1", "า2", "า3", "า4", "า5", "า6", "า7", "า8", "า9า"],
[":", "โช","โ ","โก","โข","โฃ","โค","โฅ","โฆ","โง","โจ"],
[":", "โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ","โฌ๐โญ"],
[":","๐ฌ","๐ญ","๐","โฌ๐โญ", "๐","โค","โฌ๐โญ","๐ฝ","๐ด","โฌ๐โญ"],
[":","โฐ","ยน","ยฒ","ยณ","โด","โต","โถ","โท","โธ","โน"]]

if_not_exist_creat("timeinname")
if_not_exist_creat("timeinbio")

api_id = 2591609
api_hash = 'dbe01607cc2d434e3b94dc0a85c8c9c7'
app = Client("meti", api_id, api_hash)

def create_time():
    a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
    ran = random.choice(fonts)
    for char in a :
        a = a.replace(char , ran[int(org.index(str(char)))])
    return a
time = ""
def job():
    global time
    if time != datetime.now(timezone("Asia/Tehran")).strftime("%H:%M"):
        if read("timeinname") == "on":
            try:
                app.send(functions.account.UpdateProfile(last_name=f'| {create_time()}'))
            except Exception as e:
                print(e)
        if read("timeinbio") == "on":
            try:
                app.send(functions.account.UpdateProfile(about=f'๐๐๐๐ ๐๐ โซ [--{create_time()}--] ๐๐๐  ๐'))
            except Exception as e:
                print(e)
        time = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")

@app.on_message(filters.me and filters.text)
def tool(app, m:Message):
    chat_id, message_id, text = m.chat.id, m.message_id, m.text
    if match(r"^[Hh][Ee][Ll][Pp]$", text):
          app.edit_message_text(m.chat.id , m.message_id , """
โโโโโโฐ**๐๏ธ๐๏ธ๐๏ธ๐๏ธ**โฑโโโฑโ 
โโญโโโโโโโโโโโโโโโโฃ  
โโฃโชผโ `Timebio` -> [ on - off ]
โโฃโชผโ `Timename` -> [ on - off ]
โโฃโชผโ  ๐๐ผ๐ฑ๐ฒ๐ฑ ๐๐ ๐ ๐ฒ๐๐ถ๐๐ ๐ง๐ฒ๐ฎ๐บ ๐ฅ๐ค
โโฐโโโโโโโโโโโโโโโโฃ 
โโโโโโโโโโโโโโโโโโโโโฑโ """)
    elif match(r"^[Tt][Ii][Mm][Ee][Nn][Aa][Mm][Ee]$", text.split()[0]):
        if match(r"^[Oo][Nn]$", text.split()[1]):
            write("timeinname", "on")
            app.edit_message_text(chat_id, message_id, "๐๐ข๐ฆ๐ ๐ข๐ง ๐ง๐๐ฆ๐ [ `๐จ๐ง` ]")
        else:
            write("timeinname", "off")
            app.edit_message_text(chat_id, mrssage_id, "๐๐ข๐ฆ๐ ๐ข๐ง ๐ง๐๐ฆ๐ [ `๐จ๐๐` ]")
    elif match(r"^[Tt][Ii][Mm][Ee][Bb][Ii][Oo]$", text.split()[0]):
        if match(r"^[Oo][Nn]$", text.split()[1]):
            write("timeinbio", "on")
            app.edit_message_text(chat_id, message_id, "๐๐ข๐ฆ๐ ๐ข๐ง ๐๐ข๐จ [ `๐จ๐ง` ]")
        else:
            write("timeinbio", "off")
            app.edit_message_text(chat_id, message_id, "๐๐ข๐ฆ๐ ๐ข๐ง ๐๐ข๐จ [ `๐จ๐๐` ]")
scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=5)
scheduler.start()
app.start(), idle(), app.stop()
