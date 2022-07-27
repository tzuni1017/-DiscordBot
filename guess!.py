import discord
from discord.ext import commands
import random

player={}
class guess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #幾A幾B
    # 使用者輸入 $guess 時會觸發
    @commands.command()
    async def guess(self, ctx):
        #判斷輸入者和頻道是否正確
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        await ctx.send("START!")
        pwd = random.sample(range(0, 10), 4)
        A = 0
        B = 0
        x = 0
        #判斷幾A幾B的主程式
        while A != 4:
            #取得輸入的數字
            response = await self.bot.wait_for('message', check=check)
            num = response.content
            while len(num) != 4 or len(set(num)) != 4 :
                if num =='end':
                    await ctx.send("結束!")#強制結束
                    break
                await ctx.send("請重新輸入四個不重複數字")
                response = await self.bot.wait_for('message', check=check)
                num = response.content
            if num =='end':
                break
            lista = list(map(int, list(num)))
            A = 0
            B = 0
            x += 1
            for i in lista:
                if i in pwd:
                    if lista.index(i) == pwd.index(i):
                        A += 1
                    else:
                        B += 1
            await ctx.send(f'{num}:{A}A{B}B')
            if A==4 and B==0 :
                player[ctx.author.name] = x
                await ctx.send("Congratulations~")
                a = sorted(player.items(), key=lambda d: d[1])
                #排名
                k = 1
                for j in a :
                    await ctx.send(f'第{k}名 {j[0]}:{j[1]}') 
                    k += 1
# 從主程式加入此功能需要用到的函數
def setup(bot):
    bot.add_cog(guess(bot))
