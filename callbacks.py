from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext

from settings import WEB_APP_URL


def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    first_name = update.message.from_user.first_name

    bot.send_message(
        chat_id=update.message.chat.id,
        text=(
            f"Assalomu Alaykum, {first_name}!\n"
            "\n"
            "Ijodimizga qiziqish bildirganingiz uchun tashakkur!\n"
            "\n"
            "Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar "
            "mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan "
            "turdagi kiyim buyurtma berganlarga qo'shimcha ravishda "
            "stikerpak sovg'a qilinadi :)\n"
            "\n"
            "Toshkent bo'yicha yetkazib berish: 1–3 ish kuni\n"
            "O'zbekiston bo'yicha yetkazib berish: 3–7 ish kuni\n"
            "O'zbekiston bo'yicha jo'natmalar seshanba va juma kunlari amalga "
            "oshiriladi\n"
            "\n"
            "450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!\n"
            "\n"
            "Agar bu shartlar sizni qoniqtirsa, \"🔥 Mahsulotlar\" bo'limiga "
            "o'tish orqali buyurtma berishni boshlashingiz mumkin."
        ),
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="🔥 Mahsulotlar",
                        web_app=WebAppInfo(url=WEB_APP_URL),
                    ),
                    KeyboardButton(text="📥 Savat"),
                ],
                [
                    KeyboardButton(text="💼 Hamkorlik"),
                    KeyboardButton(text="ℹ️ Ma'lumot"),
                ],
                [
                    KeyboardButton(text="🌐 Tilni tanlash"),
                ],
            ],
            resize_keyboard=True,
        ),
    )


def help(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Qanday yordam bera olaman?",
    )


def send_cart(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Sizning savatingiz bo'sh",
    )