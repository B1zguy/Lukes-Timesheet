import discord
from the_logic import *

bot = discord.Client()
token = 'NDgyMjQyMzA5MzE2OTM1Njky.DmCD2g.d0RZLcCjQaAeSl7y1M8YD8ifzEQ'

@bot.event
async def on_ready():
    print('Nathans test as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    '''if message.content.startswith('Shifts'):
        info = get_Shift()
        tmp = []
        await message.channel.send('Melbourne times displayed:')
        for i in info:
            for j in i:
                tmp.append(i[j][0])
            # await message.channel.send(tmp[0], tmp[1])
            await message.channel.send('%s  -->  %s' % (tmp[0], tmp[1]))
            tmp.clear()
        await message.channel.send('Complete!')'''


    if message.content.startswith(('Shifts', 'shifts')):
        info = get_Shift()
        tmp = []
        tmpSend = str()
        await message.channel.send('Fetching next 7 days! Melbourne times displayed:')
        # i = list item, being a dict
        # j = key item, being begin/end's values
        for i in info:
            for j in i:
                tmp.append(i[j][0])
            # Concatenates results into a single message
            tmpSend = tmpSend + '\n' + tmp[0] + '    -->    ' + tmp[1]
            tmp.clear()
        await message.channel.send(tmpSend)
        await message.channel.send('Voilà!')


bot.run(token)

