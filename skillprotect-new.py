"""
я тут зашел и кое-что подкоретировал, теперь бот видит добавившего краш бота и я сделал импорты нормально
"""
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

import datetime, os, discord, sys, asyncio, requests, json, time, random, pymongo
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from PIL import Image
from psutil import virtual_memory
import os
from reactionmenu import ButtonsMenu, ComponentsButton

os.system("clear")

blacknegr = []
guild_list = []
user_list = []
antiraidv = False
developerid = 0
guildID = 0
StaffRoleID = 0

start_time = datetime.datetime.now()

SystemLogsChannelID = 0000000000000000000
embedcolor = 0x055dff
customfooter = True
customfootvalue = ''
#Anti-Raid:
GracePeriodForKicks = 600
IncludeInviteLink = True
DiscordServerInviteLink = ''
CommandPrefix = 'sp!'
dev_ids = [922809610954477579]
token = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix=CommandPrefix,
                      help_command=None,
                      intents=discord.Intents.all())

#----------------------------event-------------------------------


@client.event
async def on_guild_join(guild):
    async for entry in guild.audit_logs(limit=2,action=discord.AuditLogAction.bot_add):
        user = entry.user
        try:
            embed = discord.Embed(
        title=f'привет!',
        description=
        'поставь мою роль какможно выше{entry.user}!!',
        color=0x0059ff)
        except: pass

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      error_embed = discord.Embed(
                    title="Ошибка :x", 
                    description ="Возникла ошибка - кманды не существует"
                    )    
    await ctx.send(embed = error_embed)


@client.event
async def on_ready():
    logo = open('logo.txt', 'r').read()
    print(f"{logo}")
    while True:
        await client.wait_until_ready()
        await client.change_presence(status=discord.Status.idle,
                                     activity=discord.Activity(
                                         name='version 2.0',
                                         type=discord.ActivityType.watching))


@client.event
async def on_guild_channel_create(ctx, channel):
    async for entry in channel.ctx.audit_logs(
            limit=1, action=discord.AuditLogAction.channel_create):
            embed = discord.Embed(title=f'внимание!',description='был добавлен краш бот!!!!',color=0x0059ff)
    await ctx.text_channels[0].send(embed=embed)
  
        
              
    


@client.event
async def on_webhook_update(webhook):
    async for entry in webhook.guild.audit_logs(
            limit=1, action=discord.AuditLogAction.webhook_create):
        embed = discord.Embed(
        title=f'ВНИМАНИЕ ПОПЫТКА КРАША СЕРВЕРА!',
        description=
        f'КРАШЕР {entry.user} МАССОВОЕ СОЗДАНИЕ ВЕБХУКОВ!!',
        color=0x0059ff)
    if not entry.user.id == client.user.id:
        await webhook.guild.ban(entry.user)


@client.event
async def on_member_join(member):
    if member.id in blacknegr:
        await member.ban(reason="краш бот")
        async for entry in member.guild.audit_logs(
                action=discord.AuditLogAction.bot_add):
            adder = entry.user
            break
        try:
            await member.guild.ban(adder,
                                   reason="Добавил краш бота",
                                   delete_message_days=0)
        except:
            await member.guild.text_channels[0].send(
                f"@everyone <@{member.guild.owner_id}>",
                embed=discord.Embed(
                    title="Добавили краш-бота",
                    description=f"Советую забанить {adder}, я сам не смог",
                    color=0xff0000))
            



@client.event
async def on_guild_join(guild):
    embed = discord.Embed(
        title=f'Привет!',
        description=
        '**@everyone ПРИВЕТ!** :point_up: \n\n**Спасибо что добавили меня на этот сервер**:ringed_planet: \n\n**Если вы нашли баг то пишите команду** ||!idea текст||  **и сразу в лс разработчику придёт сообщение** :briefcase: \n\n**Теперь вы защищены от краш ботов !** :shield:\n\n**Для полноценной защиты, у меня должны быть** ||Права Администратора.|| :robot:!! **аа и пж зайди на офф сервер бота discord.gg/lavanbot**',
        color=0x0059ff)
    await guild.text_channels[0].send(embed=embed)


@client.command()
async def delspamchannels(ctx, channame):
    count = 0
    for channel in ctx.guild.channels:
       if not entry.user.id == client.user.id:
            try:
                await channel.delete()
                count += 1
            except:
                try:
                    await channel.delete()
                    count += 1
                except:
                    pass
            else:
                pass
    embed = discord.Embed(
        title=f'ГОТОВО!',
        description=
        'ВСЕ СПАМ КАНАЛЫ УДАЛЕНЫ!',
        color=0x0059ff)

@client.event
async def on_message(message):
    try:
        await client.process_commands(message)
        if message.content.startswith("пинг") or message.content.startswith(
                "пинг"):
            embed = discord.Embed(description=f'понг!', color=embedcolor)
            if customfooter == True:
                embed.set_footer(text=f'{customfootvalue}',
                                 icon_url=f'{client.user.avatar_url}')
            else:
                embed.set_footer(text=f'{client.user.name} | {client.user.id}',
                                 icon_url=f'{client.user.avatar_url}')
            try:
                try:
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                    await message.reply(embed=embed, mention_author=False)
                except discord.HTTPException:
                    await message.reply(f'понг!', mention_author=False)
            except Exception:
                pass
        elif client.user in message.mentions:
            embed = discord.Embed(
                description=
                f'Всем привет! Я вижу, что вы упомянули меня! Мой префикс команды бота `{CommandPrefix}`.',
                color=embedcolor)
            if customfooter == True:
                embed.set_footer(text=f'{customfootvalue}',
                                 icon_url=f'{client.user.avatar_url}')
            else:
                embed.set_footer(text=f'{client.user.name} | {client.user.id}',
                                 icon_url=f'{client.user.avatar_url}')
            try:
                try:
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                    await message.reply(embed=embed, mention_author=True)
                except discord.HTTPException:
                    await message.reply(
                        f'Всем привет! Я вижу, что вы упомянули меня! Мой префикс команды бота `{CommandPrefix}``.',
                        mention_author=True)
            except Exception:
                pass
    except Exception as e:
        developer = client.get_user(developerid)
        text = str('''Ошибка на линии {}'''.format(
            sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='ошибка события on_message',
                              description=f'{text}, {str(e)}',
                              color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("ошибка события on_message" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) +
              f'{str(e)}')
        print("----------------------------------------")


#----------------------------command PPPPPPPPP-------------------------------


@client.command(aliases=['Ping', 'пинг', 'Пинг'])
async def ping(ctx):
    if not ctx.author.id in dev_ids:
        return await ctx.send("**ОШИБКА**",
                              embed=discord.Embed(title='НЕТ ПРАВ',
                                                  description=f'ТЫ НЕ ОВНЕР',
                                                  colour=0xf00a0a))
    ping = client.ws.latency
    message = await ctx.send(
        'подождите...')  # Переменная message с первоначальным сообщением
    await message.edit(
        embed=discord.Embed(title='Понг',
                            description=f'`{ping * 1000:.0f}ms` :ping_pong:',
                            colour=0x055dff))


@client.command()
@cooldown(1, 30, BucketType.user)
async def timeup(ctx):
    timeUp = time.time()
    hoursUp = round(timeUp) // 3600
    timeUp %= 3600
    minutesUp = round(timeUp) // 60
    timeUp = round(timeUp % 60)
    msg = "Бот запустился: **{0}** час. **{1}** мин. **{2}** сек. назад".format(
        hoursUp, minutesUp, timeUp)
    await ctx.send(f"{msg}")


@client.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def image(ctx):
    files = []
    for file in ctx.message.attachments:
        fp = io.BytesIO()
        await file.save(fp)
        files.append(
            discord.File(fp, filename=file.filename,
                         spoiler=file.is_spoiler()))
    await ctx.send(files=files)


@client.command(aliases=["инфа"])
async def info(ctx):
    # Переменная с количеством шардов в боте
    available_shards = client.shard_count

    # Переменная с пингом бота до текущего шарда
    shard_ping = client.latency

    # Переменная с пингами ВСЕХ шардов бота
    shards_pings = client.latencies
    await ctx.send(
        f"Сейчас {available_shards} шардов, пинг текущего шарда: {shard_ping} мс, пинг всех шардов: {shards_pings}"
    )


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def servers(ctx):
    total = 0
    for guild in client.guilds:
        if ctx.author in guild.members:
            total += 1
    await ctx.send(f"Общих серверов: {total}")


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def ram(ctx):
    ram = virtual_memory().total
    used = virtual_memory().used

    field = []
    while len(field) != 5:

        if round(used, 1) >= ram / 5:
            used -= ram / 5
            field.append("🟥 ")

        elif round(used, 1) >= ram / 10:
            used -= ram / 10
            field.append("🟨 ")

        elif used <= ram / 10:
            used = 0
            field.append("🟦 ")

        print(used)

    msg = ''
    for i in range(len(field)):
        msg += field[i]

    embed = discord.Embed(title="Используемая оперативная память",
                          description=msg)
    embed.set_footer(
        text=
        f"{round(virtual_memory().used /1024/1024/1024, 2)} ГБ из {round(ram /1024/1024/1024, 2)} гб"
    )
    colour = 0x055dff
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def idea(ctx, *, idea=None):
    if idea is None:
        embed = discord.Embed(title="Ошибка",
                              description="Укажите идею `>idea <idea>`",
                              color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        member = await client.fetch_user(931344723925418004)
        embed = discord.Embed(
            title="Новая Идея!",
            description=
            f"**Отправитель:\n**{ctx.author}\n**Айди:**\n{ctx.author.id}\n**Идея:**\n{idea}",
            color=discord.Color.green())
        await member.send(embed=embed)
        embed2 = discord.Embed(
            title="Успешно!",
            description=
            f"Идея была успешно отправлена создатаелю\n**Содержимое:**\n{idea}",
            color=discord.Color.green())
        await ctx.send(embed=embed2)


@client.command()
async def owner(ctx):
    embed = discord.Embed(title='ПОМОЩЬ', description=f'', colour=0x0059ff)
    embed.set_footer(
        text='Все права защищены',
        icon_url=
        'https://cdn.discordapp.com/avatars/483558478565343232/5c5a8740803b62d842d5a0b64ade2612.webp?size=1024'
    )
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/avatars/704967695036317777/961384e7fde6d107a479c8ee66b6ac42.webp?size=128'
    )
    await ctx.message.add_reaction('✅')
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='ХЕЛП',
        description=
        f'''**:closed_book: | Список команд.**\n\n**{CommandPrefix}`timeup` - показывает когда бот запущен.**\n\n**{CommandPrefix}`info` - показывает сколько шардов.**\n\n**{CommandPrefix}`servers` - показывает сколько общих серверов с ботом.**\n\n**{CommandPrefix}`ram` - посмотреть нагрузку бота.**\n\n**{CommandPrefix}`pixel` - делает пиксельную аватарку.**\n\n**{CommandPrefix}`idea` <идея> - отправит идею разработчику.**\n\n**{CommandPrefix}`link` - Полезные сслыки.**\n\n**{CommandPrefix}`popit` - поп-ит.**\n\n**{CommandPrefix}`ball` <Вопрос> - Задайте вопрос шару.**\n\n**{CommandPrefix}`clear` <Количество> - очистить определённое количество сообщений.**\n\n**{CommandPrefix}`ban` <@Ping> - забанить участника.**\n\n**{CommandPrefix}`kick` <@Ping> - выгнать участника.**\n\n**{CommandPrefix}`mute` <@Ping> - выдать заглушение. **\n\n**{CommandPrefix}`unmute` <@Ping> - снять заглушение.**''',
        colour=0x055dff)
    embed.set_footer(
        text='MSC team | discord.gg/lavanbot',
        icon_url=
        'https://cdn.discordapp.com/avatars/483558478565343232/5c5a8740803b62d842d5a0b64ade2612.webp?size=1024'
    )
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/avatars/704967695036317777/961384e7fde6d107a479c8ee66b6ac42.webp?size=128'
    )
    await ctx.message.add_reaction('✅')
    await ctx.send(embed=embed)  # Вывод пинга в консоль


@client.command(brief="private",
                description="Создаёт приглашение, и отправляет его")
async def invite(ctx=None, id=None):
    g = client.get_guild(int(id))
    if not g: return await ctx.send('Сервер не найден')
    for x in g.text_channels:
        link = await x.create_invite(max_age=1, max_uses=10)
        link = str(link)
        await ctx.send(link)
        return link
        await ctx.send(f'Нет прав для создания инвайта ')


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def link(ctx):
    embed = discord.Embed(
        title='Ссылки',
        description=
        '**Наш дискорд-сервер: https://discord.gg/lavanbot**\n\n**Наш телеграм: https://t.me/kracher223 **\n\n**Ссылка на бота: https://discord.com/api/oauth2/authorize?client_id=941129586190725183&permissions=8&scope=bot**',
        colour=discord.Colour.blue())
    await ctx.send(embed=embed)


async def user_fetch(ctx):
    global victim
    victim = await client.fetch_user(922809610954477579)


@client.command()
async def popit(ctx):
    embed = discord.Embed(
        title='Поп-ит',
        description=
        '||:white_large_square:|| ||:blue_square:|| ||:green_square:|| ||:red_square:|| ||:yellow_square:||\n'
        * 5,
        colour=discord.Colour.from_rgb(228, 100, 16))
    embed.set_footer(text=f'По запросу {ctx.author}')
    await ctx.send(embed=embed)


@client.command()
async def ball(ctx, *, question):
    answers = [
        '`НИТ`', '`ДЯ`', '`ФЫРК`', '`ДА ЛАДНО`', '`ЧЕЛ..ТЫЫ...`',
        '`СТРАШНО! ОЧЕНЬ СТРАШНО! Я НЕ ЗНАЮ ЧТО ЭТО ТАКОЕ! ЕСЛИ БЫ Я ЗНАЛ ЧТО ЭТО ТАКОЕ! Я НЕ ЗНАЮ ЧТО ЭТО ТАКОЕ!!`',
        "`А КАК КАКАТЬ?`",
        "`СЛУУУУШАЙ НУУУ СМОТРИИИ! ЕСЛИ ЭТО ТАК ТО ТЫ ПОЛНЫЙ ИДИОТ!`", "`ХЗ`",
        "`ЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁПРСТ! ТЫ ШО ТАКОЙ СТРАШНЫЙ? ТА ЛАДНО ШУТКА!)`",
        "`ХЗ ЧТО НА ЭТО ОТВЕТИТЬ!`", "`КОНЕЧНО!`", "`НЕТ КОНЕЧНО`"
    ]
    answer = random.choice(answers)
    embed = discord.Embed(title='Шар думает... :timer:',
                          description=f'ЧТО БЫ ОТВЕТИТЬ НА `{question}`...',
                          colour=discord.Colour.from_rgb(0, 228, 66))
    msg = await ctx.send(embed=embed)
    time.sleep(1.5)
    embed = discord.Embed(title='ВОТ ЭТО ТОП ОТВЕТ!',
                          description=f'ОТВЕТ: {answer}',
                          colour=discord.Colour.from_rgb(0, 228, 66))
    await msg.edit(embed=embed)


@client.command()
async def logout(ctx):
    try:
        message1 = ctx.message
        author = ctx.message.author
        if author.id == developerid:
            await message1.add_reaction('✅')
            await client.logout()
        else:
            await message1.delete()
            message5 = await ctx.send(f'{author.mention}')
            await message5.delete()
            embed5 = discord.Embed(
                description=
                f'''{author.mention}, вы не можете использовать эту команду!''',
                color=embedcolor)
            if customfooter == True:
                embed5.set_footer(text=f'{customfootvalue}',
                                  icon_url=f'{client.user.avatar_url}')
            else:
                embed5.set_footer(
                    text=f'{client.user.name} | {client.user.id}',
                    icon_url=f'{client.user.avatar_url}')
            try:
                message6 = await ctx.send(embed=embed5)
            except discord.HTTPException:
                message6 = await ctx.send(
                    f'''{author.mention}, **вы не можете использовать эту команду!**'''
                )
            await asyncio.sleep(20)
            await message6.delete()
    except Exception as e:
        developer = client.get_user(developerid)
        text = str('''Ошибка на линии {}'''.format(
            sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='Ошибка функции commands.logout',
                              description=f'{text}, {str(e)}',
                              color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("Ошибка функции commands.logout" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) +
              f'{str(e)}')
        print("----------------------------------------")
        await asyncio.sleep(10)


@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
        messages.append(message)
    await channel.delete_messages(messages)
    govno = discord.Embed(title=f"Очищено {amount} сообщений",
                          description=f"**Модератор:** {ctx.author.mention}\n",
                          colour=discord.Colour.blue())
    await ctx.send(embed=govno)


@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.guild.ban(member)
    emb = discord.Embed(title='Бан',
                        timestamp=ctx.message.created_at,
                        colour=discord.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Выдал бан**',
                  value=ctx.message.author.mention,
                  inline=True)
    emb.add_field(name='**Причина**', value=reason, inline=False)
    emb.set_footer(text=f'Запросил: {ctx.author.name}',
                   icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)


# p-kick
@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await ctx.guild.kick(user)
    emb = discord.Embed(title='Кик',
                        timestamp=ctx.message.created_at,
                        colour=discord.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Выгнал**',
                  value=ctx.message.author.mention,
                  inline=True)
    emb.add_field(name='**Причина**', value=reason, inline=False)
    emb.set_footer(text=f'Запросил: {ctx.author.name}',
                   icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)


@client.command(aliases=["sb"])
@commands.cooldown(1, 40, commands.BucketType.user)
async def serverbanner(ctx):
    try:
        embed = discord.Embed()
        embed.set_image(url=ctx.guild.banner_url)
        await ctx.message.reply(embed=embed, mention_author=False)
    except:
        await ctx.send(f"{ctx.guild.banner_url}")


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def fox(ctx):
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)
    fox = response.json()

    embed = discord.Embed(color=0x36393F)
    embed.set_image(url=fox['image'])
    await ctx.message.reply(embed=embed, mention_author=False)


@client.command(usage="<member> [reason]")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Вы не указали причину"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Замучен")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Замучен")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=True,
                                          read_messages=False)
    mute = discord.Embed(description=f"**Участник отправился в мут.**\n\n"
                         f"**Модератор:**: {ctx.author.mention}\n"
                         f"**Участник:**: {member.mention}",
                         colour=discord.Colour.blue())
    mute.add_field(name="Причина", value=reason)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed=mute)


@client.command(usage="<member>")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Замучен")

    await member.remove_roles(mutedRole)
    unmute = discord.Embed(description=f"**Участник размучен.**\n\n"
                           f"**Модератор:** {ctx.message.author}\n"
                           f"**Участник:** {member.mention}",
                           colour=discord.Colour.blue())
    await ctx.send(embed=unmute)


@client.event
async def on_command_error(ctx, error):
    msg = 'Подождите для использования команды, она перезаряжается'
    embed = discord.Embed(title='⏳ Перезарядка команды',
                          description=msg,
                          color=0xff0000)
    lol2 = discord.Embed(
        title='💻 Недостаток прав',
        description="У вас недостаточно прав для выполнения данной команды",
        color=0xff0000)
    lol = discord.Embed(title='⛔ Неверный аргумент',
                        description="Укажите правильный аргумент",
                        color=0xff0000)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.author.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.author.send(embed=lol2)

keep_alive()
client.run(os.getenv("DISCORD_TOKEN"))

# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2
