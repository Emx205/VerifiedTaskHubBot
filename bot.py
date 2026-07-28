from telebot import TeleBot, types
from config import *
from database import *

# Create database tables
create_tables()

# Create bot
bot = TeleBot(TOKEN)

# ==========================
# MAIN MENU
# ==========================

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("📋 Tasks", "💰 Balance")
    markup.row("📤 Submit Proof", "🏦 Withdraw")
    markup.row("👥 Referral", "ℹ️ Help")

    return markup

# ==========================
# /START
# ==========================

@bot.message_handler(commands=["start"])
def start(message):

    add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    )

    bot.send_message(
        message.chat.id,
        f"""
👋 Welcome to {BOT_NAME}

Complete tasks and earn money.

Choose an option below.
        """,
        reply_markup=main_menu()
    )

# ==========================
# TASKS
# ==========================

@bot.message_handler(func=lambda m: m.text == "📋 Tasks")
def tasks(message):

    bot.send_message(
        message.chat.id,
        f"""
📋 {TASK_NAME}

🎯 FOR NEW USERS ONLY

1️⃣ Register using my referral link

{REFERRAL_LINK}

2️⃣ Reach Level 20

3️⃣ Withdraw your first ₦150

4️⃣ Tap 📤 Submit Proof

🎁 Reward: ₦{TASK_REWARD}
        """
    )

# ==========================
# BALANCE
# ==========================

@bot.message_handler(func=lambda m: m.text == "💰 Balance")
def balance(message):

    bal = get_balance(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"💰 Your Balance: ₦{bal}"
    )

# ==========================
# REFERRAL
# ==========================

@bot.message_handler(func=lambda m: m.text == "👥 Referral")
def referral(message):

    bot.send_message(
        message.chat.id,
        """
👥 Referral Program

Invite your friends to join Verified Task Hub.

Referral tracking will be enabled soon.
        """
    )

# ==========================
# HELP
# ==========================

@bot.message_handler(func=lambda m: m.text == "ℹ️ Help")
def help_button(message):

    bot.send_message(
        message.chat.id,
        f"""
Need help?

Contact:

{SUPPORT}
        """
    )
