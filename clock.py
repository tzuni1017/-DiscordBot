import discord
from discord.ext import commands
import time
from datetime import datetime
import json
import asyncio

clocklist ={}

class clock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #設定時間傳訊息
    # 使用者輸入 $clock 時會觸發
    @commands.command()
    async def clock(self, ctx):
        #判斷輸入者和頻道是否正確
        def check(tim):
            return tim.author == ctx.author and tim.channel == ctx.message.channel
        time1=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())#現在時間
        await ctx.send(f'it is {time1} now.')
        await ctx.send("輸入時間+事件 ex:2022-01-01 23:59:59 read")
        #取得設定時間的主程式
        while True:
            response = await self.bot.wait_for('message', check=check)
            settime = response.content[:19]#輸入者輸入的時間
            event = response.content[20:]#輸入的事件
            time2 = datetime.strptime(settime,'%Y-%m-%d %H:%M:%S')
            #輸入時間已超過 重新輸入
            if datetime.now() >= time2:
                await ctx.send("請重新輸入時間")
            else:
                clocklist[str(time2)] = event
                await ctx.send("OK!")#輸入成功
                break   
        #異步執行
        async def cd():
            while str(time2) in clocklist:
                if time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) == str(time2):
                    await ctx.send(f'{event}')
                    del clocklist[str(time2)]
                    break
                await asyncio.sleep(0.1)
        self.task = self.bot.loop.create_task(cd())
    #看設定的時間清單
    # 使用者輸入 $show 時會觸發
    @commands.command()
    async def show(self, ctx):
        if clocklist == {}:
            await ctx.send('無')
        for i in clocklist:
            await ctx.send(f'{i,clocklist[i]}')
    #刪除指定時間(輸入時不須加事件)
    # 使用者輸入 $deleteclock 時會觸發
    @commands.command()
    async def deleteclock(self,ctx,ex,ex2):
        dtime = ex + ' ' + ex2
        del clocklist[dtime]
        if clocklist == {}:
            await ctx.send('無')
        for i in clocklist:
            await ctx.send(f'{i,clocklist[i]}') 
# 從主程式加入此功能需要用到的函數
def setup(bot): 
    bot.add_cog(clock(bot))