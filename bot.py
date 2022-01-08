import logging
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters

import os

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' , level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = '5069245007:AAHt8ocv6v-kupA6so4GEwLinRe9et6otos'

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hello! Welcome To DACE_Bot!")
    update.message.reply_text("""
    I can recognize the following commands:

    /start -> Welcome Message
    /about -> Information About DACE
    /contact -> Information About Contact
    /social_media -> Social Media Links
    /courses -> Courses Offered
    /creator -> Information About Creator
    /science_expo -> Date To Be Conducted
    /team -> About Team
    """)

def about(update, context):
    """Send a message when the command /about is issued."""
    update.message.reply_text("DACE Cultivating Technology")
    update.message.reply_text("Dhaanish Ahmed College of Engineering (DACE) is under the aegis of the Ayyanavaram Educational Trust (AET), which was established in the year 1980 by the founder and esteemed Chairman Alhaj.K.Moosa, with a noble aim of promoting ‘Technical Higher Education’. The founder Chairman Alhaj.K.Moosa he himself is an Educationalist and philanthropist with very rich experience in the field of education, whose focus is to provide quality technical education to the socially and economically backward segment. Presently, AET is managing several schools and Engineering colleges, educating around 5000 aspirants.")
    update.message.reply_text('''
DACE is an NAAC Accredited with B++
We have approval from AICTE for the following

We have PIO (persons of Indian Origin)
OCI- (Overseas Citizenship)
FN (Overseas Citizenship)
NRI (Non-Resident Indian)
''')
    update.message.reply_text('''
Recognition on our Institution by
University Grand Commission (UGC) - 
Ministry of Human Resource Development(MHRD)

Approval under section 2(f) of UGC Aact,1956

Approval under 12(B) of UGC Aact,1956

DACE is approved by AICTE, New Delhi and affiliated to Anna University, Chennai,India.

DACE is an ISO 9001:2015 certified institution. DACE was started in the year 2002 and is currently offering
''')
    
def website(update, context):
    """Send a message when the command /website is issued."""
    update.message.reply_text("Our website www.dhaanish.in")

def social_media(update, context):
    """Send a message when the command /social_media is issued."""
    update.message.reply_text("Face Book DhaanishAhmedCE https://www.facebook.com/DhaanishAhmedCE/")
    update.message.reply_text("Instagram dace_engineering https://www.instagram.com/dace_engineering/")
    update.message.reply_text("In Youtube DACE Offical https://www.youtube.com/c/DACEOfficial/featured")

def courses(update, context):
    """Send a message when the command /courses is issued."""
    update.message.reply_text('''
    Courses Offered
UG
B.E - Electronics & Communication Engineering
B.E - Electrical & Electronics Engineering
B.E - Computer Science Engineering
B.E - Civil Engineering
B.E - Mechanical Engineering
B.E - Robotics & Automation
B.Tech - Artificial Intelligence & Data Science
B.Tech - Petroleum Engineering

PG
MBA - Master of Business Administration
M.E – Applied Electronics
M.E – Computer Science and Engineering
''')
    
def creator(update, context):
    """Send a message when the command /creator is issued."""
    update.message.reply_text("A Team of students of DACE created me!")
    update.message.reply_text("For Dhaanish Tech Hunt!")

def tech_hunt(update, context):
    """Send a message when the command /tech_hunt is issued."""
    update.message.reply_text("Tech Hunt is conducted on 28.12.2021")

def team(update, context):
    """Send a message when the command /team is issued."""
    update.message.reply_text("The Team has four members...")
    update.message.reply_text('''
    Sabarish.T.K - Team Leader
Team Members:
    Sabith Ahmed.S
    Suresh.L
    Mohammed Ahsen.p
    Wasiq Mohideen.M
    ''')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
   
def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("about", about))
    disp.add_handler(CommandHandler("website", website))
    disp.add_handler(CommandHandler("social_media", social_media))
    disp.add_handler(CommandHandler("courses", courses))
    disp.add_handler(CommandHandler("creator", creator))
    disp.add_handler(CommandHandler("tech_hunt", tech_hunt))
    disp.add_handler(CommandHandler("team", team))
    disp.add_handler(MessageHandler(Filters.text, echo))
    disp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    
    updater.bot.setWebhook('https://secure-dusk-63119.herokuapp.com/' + TOKEN)
                           
    updater.idle()

if __name__ == '__main__':
    main()

