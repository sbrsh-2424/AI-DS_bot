import logging
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters

import os

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' , level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = '5069245007:AAHt8ocv6v-kupA6so4GEwLinRe9et6otos'

def start(update, context):
    update.message.reply_text("Welcome!")
    update.message.reply_text("Initiating Services!") 
    update.message.reply_text('''By using the following commands
You can get these things from me
    
/first_unit -> First Unit Handwritten Notes
/second_unit -> Second Unit Handwritten Notes
/third_unit -> Third Unit Handwritten Notes
/maths_notes -> Maths Online Class Notes
''')

def first_unit(update, context):
    update.message.reply_text("The following commands will give you the link for the Unit-1 notes!")
    update.message.reply_text('''
/U1_CH3151 -> Engineering Chemistry
/U1_PH3151 -> Engineering Physics
/U1_MA3151 -> Matrices and Calculus
/U1_GE3151 -> Problem Solving & Python Programming
/U1_HS3151 -> Professional English
''')

def U1_CH3151(update, context):
    update.message.reply_text("Unit-1 Engineering chemistry")
    update.message.reply_text("https://drive.google.com/file/d/1-TOeCWEMLDCspmgRV6WvhuNvKaJTsVsP/view?usp=drivesdk")

def U1_PH3151(update, context):
    update.message.reply_text("Unit-1 Engineering physics")
    update.message.reply_text("https://drive.google.com/file/d/1-dDFV-TmzrcuiE2YdCLz2gVC4pYMqF5M/view?usp=drivesdk")

def U1_MA3151(update, context):
    update.message.reply_text("Unit-1 Matrices and calculus")
    update.message.reply_text("https://drive.google.com/file/d/1-Te48YPYHIwuDiX_WX8eaNOW8UVWo12K/view?usp=drivesdk")

def U1_GE3151(update, context):    
    update.message.reply_text("Unit-1 Problem solving & Python programming")
    update.message.reply_text("https://drive.google.com/file/d/10GOBtALossj-MmynzfcsfoJQboykyUBz/view?usp=drivesdk")

def U1_HS3151(update, context):
    update.message.reply_text("Unit-1 Professional English")
    update.message.reply_text("https://drive.google.com/file/d/1-Xu2AOHAHYgmcXSxXl8EDWJI4aG8Sofb/view?usp=drivesdk")
                              

def second_unit(update, context):
    update.message.reply_text("The following commands will give you the link for the Unit-2 notes!")
    update.message.reply_text('''
/U2_CH3151 -> Engineering Chemistry
/U2_PH3151 -> Engineering Physics
/U2_MA3151 -> Matrices and Calculus
/U2_GE3151 -> Problem Solving & Python Programming
/U2_HS3151 -> Professional English
''')

def U2_CH3151(update, context):
    update.message.reply_text("Unit-2 Engineering chemistry")
    update.message.reply_text("https://drive.google.com/file/d/108qYCzhycsP0BFVr7NdI7tQg0qEaacMe/view?usp=drivesdk")

def U2_PH3151(update, context):
    update.message.reply_text("Unit-2 Engineering physics")
    update.message.reply_text("https://drive.google.com/file/d/1027MHXhJjsw0tLZn9VdEgSENMbHje0Cr/view?usp=drivesdk")

def U2_MA3151(update, context):
    update.message.reply_text("Unit-2 Matrices and calculus")
    update.message.reply_text("https://drive.google.com/file/d/10CzlArbfQ64S9Pa2_Vu5IVAbeHxAGSJe/view?usp=drivesdk")

def U2_GE3151(update, context):    
    update.message.reply_text("Unit-2 Problem solving & Python programming")
    update.message.reply_text("https://drive.google.com/file/d/10CMoSss7hkOhwgGUx90wf_nEeNuqgEJo/view?usp=drivesdk")

def U2_HS3151(update, context):
    update.message.reply_text("Unit-2 Professional English")
    update.message.reply_text("https://drive.google.com/file/d/1K4LiRIzEPlNvH1FYfOxyFCsysHrZYb6i/view?usp=drivesdk")
                              

def third_unit(update, context):
    update.message.reply_text("The following commands will give you the link for the Unit-3 notes!")
    update.message.reply_text('''
/U3_CH3151 -> Engineering Chemistry
/U3_PH3151 -> Engineering Physics
/U3_MA3151 -> Matrices and Calculus
/U3_GE3151 -> Problem Solving & Python Programming
/U3_HS3151 -> Professional English
''')

def U3_CH3151(update, context):
    update.message.reply_text("Unit-3 Engineering chemistry")
    update.message.reply_text("https://drive.google.com/file/d/1-iAzW27Ed2OoJtqw37NnpeCytG5MgNNB/view?usp=drivesdk")
                              
def U3_PH3151(update, context):
    update.message.reply_text("Unit-3 Engineering physics")
    update.message.reply_text("https://drive.google.com/file/d/10FDPYXSR0rPKXdOYJlYqQJOK3xcSE3JC/view?usp=drivesdk")
                              
def U3_MA3151(update, context):
    update.message.reply_text("Unit-3 Matrices and calculus")
    update.message.reply_text("https://drive.google.com/file/d/1-mQtfKu1HSxwtz4Jb1cLJpDNr4213fGl/view?usp=drivesdk")
                              
def U3_GE3151(update, context):    
    update.message.reply_text("Unit-3 Problem solving & Python programming")
    update.message.reply_text("https://drive.google.com/file/d/1-dYtd-b_uqwkZdEfgGbFSCdVVspRDGX2/view?usp=drivesdk")
                              
def U3_HS3151(update, context):
    update.message.reply_text("Unit-3 Professional English")
    update.message.reply_text("https://drive.google.com/file/d/1-vjRKqmhsf2bXc6Fdqre9JDC8EaBvEon/view?usp=drivesdk")

def maths_notes(update, context):
    update.message.reply_text('''
    Maths Online Class Notes:
    
    /eulers_theorem -> Euler's Theorem On Homogeneous Function
    
    /lagranges_problems -> Lagranges Method Of Undertermined Multipliers
    
    /min_max -> Min And Max Problems
    
    /taylors_series -> Problems On Taylor's Series
    
    /unit_3 -> Functions Of Several Variables - PPT
    ''')
    
def eulers_theorem(update, context):
    update.message.reply_text("Euler's Theorem")
    update.message.reply_text("https://drive.google.com/file/d/1A0AAmTq4JDJDONKKQHhAPdXzfZfTu7Ga/view?usp=drivesdk")
    
def lagranges_problems(update, context):
    update.message.reply_text("Langranges Problems")
    update.message.reply_text("https://drive.google.com/file/d/19rEtx6Rehi0emdBXySlf7WKQ7_2xriZT/view?usp=drivesdk")
    
def min_max(update, context):
    update.message.reply_text("Min and Max Problems")
    update.message.reply_text("https://drive.google.com/file/d/19rkWEjCsnz9Hwc_5l0rU4Z3P-hD27S2N/view?usp=drivesdk")
    
def taylors_series(update, context):
    update.message.reply_text("Taylor's Series Problems")
    update.message.reply_text("https://drive.google.com/file/d/19r7P9XbhjRuInzGQhIcngQjz1AWV_sVd/view?usp=drivesdk")
    
def unit_3(update, context):
    update.message.reply_text("Unit-3 Functions of Several Variables PPT")
    update.message.reply_text("https://docs.google.com/presentation/d/1AE1sXOgW1dEwR2J59ubu4AZNVkeXYdJ4/edit?usp=drivesdk&ouid=101946115121402932191&rtpof=true&sd=true")

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
    disp.add_handler(CommandHandler("first_unit", first_unit))
    disp.add_handler(CommandHandler("U1_CH3151", U1_CH3151))
    disp.add_handler(CommandHandler("U1_PH3151", U1_PH3151))
    disp.add_handler(CommandHandler("U1_MA3151", U1_MA3151))
    disp.add_handler(CommandHandler("U1_GE3151", U1_GE3151))
    disp.add_handler(CommandHandler("U1_HS3151", U1_HS3151))

    disp.add_handler(CommandHandler("second_unit", second_unit))
    disp.add_handler(CommandHandler("U2_CH3151", U2_CH3151))
    disp.add_handler(CommandHandler("U2_PH3151", U2_PH3151))
    disp.add_handler(CommandHandler("U2_MA3151", U2_MA3151))
    disp.add_handler(CommandHandler("U2_GE3151", U2_GE3151))
    disp.add_handler(CommandHandler("U2_HS3151", U2_HS3151))

    disp.add_handler(CommandHandler("third_unit", third_unit))
    disp.add_handler(CommandHandler("U3_CH3151", U3_CH3151))
    disp.add_handler(CommandHandler("U3_PH3151", U3_PH3151))
    disp.add_handler(CommandHandler("U3_MA3151", U3_MA3151))
    disp.add_handler(CommandHandler("U3_GE3151", U3_GE3151))
    disp.add_handler(CommandHandler("U3_HS3151", U3_HS3151))
    
    disp.add_handler(CommandHandler("maths_notes", maths_notes))
    disp.add_handler(CommandHandler("eulers_theorem", eulers_theorem))
    disp.add_handler(CommandHandler("lagranges_problems", lagranges_problems))
    disp.add_handler(CommandHandler("min_max", min_max))
    disp.add_handler(CommandHandler("taylors_series", taylors_series))
    disp.add_handler(CommandHandler("unit_3", unit_3))
    
    disp.add_handler(MessageHandler(Filters.text, echo))
    disp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    
    updater.bot.setWebhook('https://frozen-dusk-17212.herokuapp.com/' + TOKEN)
                           
    updater.idle()

if __name__ == '__main__':
    main()

