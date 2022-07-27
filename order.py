from discord.ext import commands

orders = {}
class order(commands.Cog):
    def init(self, bot):
        self.bot = bot
    #增加訂餐項目
    # 使用者輸入 $addorder 時會觸發
    @commands.command()
    async def addorder(self, ctx,num,dish):
        if dish not in orders :
            orders[dish] = 0
        orders[dish] += int(num)
        for order_dish in orders :
            send_order_dish = str(order_dish+ ':'+str(orders[order_dish]))
            await ctx.send(f'{send_order_dish}')
    #刪除訂餐項目
    #使用者輸入 $deleteorder 時會觸發
    @commands.command()
    async def deleteorder(self, ctx,num,dish):        
        orders[dish] -= int(num)
        if orders[order_dish] == 0 :
            del orders[order_dish]
        if orders=={}:
            await ctx.send('No order!')
        for order_dish in orders :
            send_order_dish = str(order_dish+ ':'+str(orders[order_dish]))
            await ctx.send(send_order_dish)
    #清空訂餐列表
    #使用者輸入$cleanorder 時會觸發
    @commands.command()
    async def cleanorder(self, ctx):
        list1=[]
        for i in orders.keys():
            list1.append(i)
        for j in list1:
            del orders[j]
        await ctx.send('No order!')
    #看訂餐列表
    #使用者輸入$showorder 時會觸發
    @commands.command()
    async def showorder(self, ctx):
        for order_dish in orders :
            send_order_dish = str(order_dish+ ':'+str(orders[order_dish]))
            await ctx.send(send_order_dish)
        if orders=={}:
            await ctx.send('No order!')
# 從主程式加入此功能需要用到的函數            
def setup(bot):
    bot.add_cog(order(bot))