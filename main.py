import asyncio
import aiosqlite
import aiosmtplib
from email.message import EmailMessage
from datetime import datetime


async def send_mail(address, name):
    message = EmailMessage()
    message["From"] = "root@localhost"
    message["To"] = address
    message["Subject"] = 'Рады, что вы с нами!'
    message.set_content(f"Многоуважаемый, {name}! Спасибо, что пользуетесь нашим сервисом объявлений.")

    await aiosmtplib.send(message, hostname="127.0.0.1", port=2525)

async def main():
    async with aiosqlite.connect('contacts.db') as connect:
        select = await connect.execute('SELECT * FROM contacts;')
        contacts = await select.fetchall()
        await asyncio.gather(*[send_mail(contact[3], contact[1]) for contact in contacts])


if __name__ == '__main__':
    start = datetime.now()
    asyncio.run(main())
    now = datetime.now() - start
    print(now)

