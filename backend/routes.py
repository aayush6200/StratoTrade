from flask import Blueprint
from bot import Bot

# Create a Blueprint named 'bot_blueprint'
bot_blueprint = Blueprint('bot_blueprint', __name__)

# Instantiate the bot here if it's meant to persist across requests
bot = Bot()


@bot_blueprint.route('/user/dummyRequest')
def dummyRequest():
    return "Hello world from stratotrade"


@bot_blueprint.route('/user/trade')
def get_trade():
    trade_object = bot.get_trade()
    # Serialize trade_object to JSON as needed
    return trade_object


@bot_blueprint.route('/user/portfolio')
def get_portfolio():
    user_portfolio = bot.get_portfolio()
    # Serialize user_portfolio to JSON as needed
    return user_portfolio


@bot_blueprint.route('/user/info')
def get_user_info():
    user_info = bot.get_user_info()
    # Serialize user_info to JSON as needed
    return user_info


@bot_blueprint.app_errorhandler(404)
def blueprint_page_not_found(e):
    # Only handles 404 errors from within the bot_blueprint routes
    return "This user route doesn't exist. Please check your URLs.", 404
