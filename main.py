from typing import Optional

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from telegram.ext import Updater
from pydantic import BaseModel

app = FastAPI()
updater = Updater("5335002137:AAE4xLCtIeean8hVOSsR32l3DGlZjaRKaOo", arbitrary_callback_data=True)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    name: str
    email: Optional[str] = 'nu a trimis numarul'
    phone: str
    message: str


def make_text(data: Data):
    return f"""
        \n<strong><b><i><u>Numele si prenumele</u></i></b></strong>:  {data.name}\n\n<strong><b><i><u>Email-ul</u></i></b></strong>:  {data.email}\n\n<strong><b><i><u>Numarul de telefon</u></i></b></strong>:  {data.phone}\n\n<strong><b><i><u>Mesajul</u></i></b></strong>:  {data.message}\n
    """


@app.post("/send_email")
async def send_email(data: Data):
    updater.bot.sendMessage(chat_id='499675458', text=make_text(data), parse_mode='HTML')
    return {"message": "success"}
