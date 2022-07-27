import discord
from discord.ext import commands
import os

# Bot object、設定指令開頭
bot = commands.Bot(command_prefix='$')

# 從 token.txt 中讀取 token
# 使用 os.path.join() 在不同作業系統會以 / 或是 \ 連接路徑

with open(os.path.join("token.txt"), 'r') as f:
    token = f.read().strip("\n")

# 從 extensions.txt 中讀取現有功能，並加入那些功能
with open(os.path.join("extensions.txt"), 'r') as f:
    for extension in f:
        # 加入功能
        bot.load_extension(extension.strip('\n')) 

# 一開始準備就緒時會觸發
@bot.event
async def on_ready():
    ch = bot.get_channel(992297511932936266)
    await ch.send('online')
    print("Ready!")
    # 印出 bot 這個 user 的資訊
    print("User name:", bot.user.name)
    print("User ID:", bot.user.id)

# 監聽訊息，有訊息時會觸發
@bot.event
async def on_message(message):
    # 檢查訊息是否是 bot 自己傳的
    if message.author.id == bot.user.id:
        return

    # 回應有 hello 的訊息
    if "hello" in message.content.lower():
        await message.channel.send("Hello~ Nice to meet you.") # Bot 傳送訊息

    # 回應 help 開頭的訊息
    if message.content.lower().startswith("help"):
        await message.channel.send("Enter commands starting with $ or enter $help for more information:)")

    # 加這行才可以用 commands
    await bot.process_commands(message)

# load extension 加入功能
# 使用者輸入 $load 時會觸發
@bot.command(help = "Load extension.", brief = "Load extension.")
async def load(ctx, extension): # extension: 使用者輸入要加入的功能
    try:
        bot.load_extension(extension.lower()) # load extension, lower() 因為檔名是小寫
        await ctx.send(f"{extension} loaded.") # Bot 傳送訊息
    except Exception as e:
        await ctx.send(e) # 若加入失敗印出錯誤訊息

# unload extension 卸載功能
@bot.command(help = "Un-load extension.", brief = "Un-load extension.")
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension.lower()) # load extension, lower() 因為檔名是小寫
        await ctx.send(f"{extension} unloaded.") # Bot 傳送訊息
    except Exception as e:
        await ctx.send(e)
    pass
    
# reload extension 重新加入功能
@bot.command(help = "Re-load extension.", brief = "Re-load extension.")
async def reload(ctx, extension):
    try:
        bot.reload_extension(extension.lower()) # load extension, lower() 因為檔名是小寫
        await ctx.send(f"{extension} reloaded.") # Bot 傳送訊息
    except Exception as e:
        await ctx.send(e)
    pass
    
bot.run(token) # 執行