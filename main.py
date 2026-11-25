from telegram.ext import ( Updater, CommandHandler, MessageHandler, Filters, )

from settings import TOKEN
from callbacks import start, help, send_cart, send_partnership


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(
        handler=CommandHandler(command=["start", "boshlash"], callback=start)
    )
    dispatcher.add_handler(
        handler=CommandHandler(command=["help", "yordam"], callback=help)
    )

    # message handlers
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("📥 Savat"),
            callback=send_cart,
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("💼 Hamkorlik"),
            callback=send_partnership,
        )
    )

    updater.start_polling()
    updater.idle()


main()