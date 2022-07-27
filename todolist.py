import discord
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime
from discord.ext import commands

ToDoList={}

class todolist(commands.Cog):
    def init(self, bot):
        self.bot = bot
    date = datetime.date.today()
    #看todolist
    # 使用者輸入$showtodolist 時會觸發
    @commands.command()
    async def showtodolist(self, ctx):
        
        if ToDoList == {} :
            await ctx.send('To Do List: all done!')
        else :
            await ctx.send('To Do List:')
            for show_date in ToDoList :
                await ctx.send(show_date)
                for show_task in ToDoList[show_date] :
                    await ctx.send(show_task)
    #清空todolist
    #使用者輸入 $cleantodolist 時會觸發
    @commands.command()
    async def cleantodolist(self, ctx):
        list1=[]
        for i in ToDoList.keys():
            list1.append(i)
        for j in list1:
            del ToDoList[j]
        await ctx.send('To Do List: all done!')
    #增加todolist項目
    #使用者輸入$add 時會觸發
    @commands.command()
    async def add(self, ctx,extension):
        date = datetime.date.today()    
        if date not in ToDoList :
            ToDoList[date] = []
        ToDoList[date].append(extension)
        await ctx.send('To Do List:')
        for show_date in ToDoList :
                await ctx.send(show_date)
                for show_task in ToDoList[show_date] :
                    await ctx.send(show_task)
    #刪除todolist項目
    #使用者輸入$delete 時會觸發
    @commands.command()
    async def delete(self, ctx,extension):
        date = datetime.date.today()
        ToDoList[date].remove(extension)
        await ctx.send('To Do List:')
        for show_date in ToDoList :
                await ctx.send(show_date)
                for show_task in ToDoList[show_date] :
                    await ctx.send(show_task)
# 從主程式加入此功能需要用到的函數
def setup(bot):
    bot.add_cog(todolist(bot))