import telebot

KEY_API = "5924480017:AAG-OaLC-656XeFxNwFf4JbpGRgji74uHuU"


bot = telebot.TeleBot(KEY_API)


@bot.message_handler(commands=["start"])
def responde(mensagem):

    bot.reply_to(mensagem, """
        Bem-vindo ao bot de ferramentas da estação climatológica do Seridó!\n
Escolha a hora da medição:
    /12utc
    /18utc
    /24utc\n
Ou ainda o synop:
    /synop12
    /synop18
    /synop24\n
Ou clique no botão Menu!
    """)

@bot.message_handler(commands=["12utc"])
def responde12(mensagem):
    bot.reply_to(mensagem,
"""
TEMP //
BAROM //
C. WILD //
DIR //
T. Nuv //
Quant //
BS //
BU //
TX //
TN //
TP //
VTot2m //
02 //
05 //
10 //
30 //
""")

@bot.message_handler(commands=["18utc"])
def responde18(mensagem):
    bot.reply_to(mensagem,
"""
TEMP //
BAROM //
C. WILD //
DIR //
T. Nuv //
Quant //
BS //
BU //
02 //
05 //
10 //
30 //
""")

@bot.message_handler(commands=["24utc"])
def responde24(mensagem):
    bot.reply_to(mensagem,
"""
TEMP //
BAROM //
C. WILD //
DIR //
T. Nuv //
Quant //
BS //
BU //
TX //
TN //
02 //
05 //
10 //
30 //
""")

@bot.message_handler(commands=["synop12"])
def syn12(mensagem):
    bot.reply_to(mensagem,
"""
Bom dia!
Synop — 12UTC — 82690
""")

@bot.message_handler(commands=["synop18"])
def syn18(mensagem):
    bot.reply_to(mensagem,
"""
Boa tarde!
Synop — 18UTC — 82690
""")

@bot.message_handler(commands=["synop24"])
def syn24(mensagem):
    bot.reply_to(mensagem,
"""
Boa noite!
Synop — 00UTC — 82690
""")

bot.polling()