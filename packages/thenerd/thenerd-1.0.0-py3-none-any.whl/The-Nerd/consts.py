dictionary_check = True
timer_check = True 
content_check = True 
history_check = True
lev = ["Level-5+", "Level-10+", "Level-15+"]
level_num = [5, 10, 15]
intents = disnake.Intents.default()
intents.members = True
_bot = commands.Bot(command_prefix="nerd", intents=intents)
_bot.remove_command('help')
amount_del = 0
rand = 0
chvc=[]
time_window_milliseconds = 5000
max_msg_per_window = 5
author_msg_times = {}
sent_color = 0xE3E5E8
changed_color = 0xFAA61A
deleted_color = 0xF04747
colors = [1752220, 1146986, 3066993, 2067276, 3447003, 2123412, 10181046, 7419530, 15277667, 15844367, 11342935, 12745742, 15105570, 11027200, 15158332, 10038562, 9807270, 9936031, 8359053, 12370112, 3426654, 2899536, 16776960]

@_bot.slash_command()
async def economy(ctx):
    pass

@_bot.slash_command()
async def cybersec(ctx):
    pass

@_bot.slash_command()
async def fun(ctx):
    pass

@_bot.slash_command()
async def mod(ctx):
    pass

@_bot.slash_command()
async def util(ctx):
    pass

@_bot.slash_command()
async def engineering(ctx):
    pass

@_bot.slash_command()
async def shopping(ctx):
    pass

@_bot.slash_command()
async def working(ctx):
    pass

@_bot.slash_command()
async def geek(ctx):
    pass

@_bot.slash_command()
async def computing(ctx):
    pass

@_bot.slash_command()
async def taxing(ctx):
    pass

@_bot.slash_command()
async def loaning(ctx):
    pass

@_bot.slash_command()
async def learning(ctx):
    pass

@_bot.slash_command()
async def miner(ctx):
    pass

@_bot.slash_command()
async def leaderboard(ctx):
    pass

@_bot.slash_command()
async def marketing(ctx):
    pass

@_bot.slash_command()
async def crypto(ctx):
    pass