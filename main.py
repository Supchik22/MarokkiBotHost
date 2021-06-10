import asyncio # needed for sleep that won't block the bot, only for this example
import discord
from discord.ext import commands
import aiohttp
import random
from PIL import Image, ImageDraw, ImageFont
from discord.utils import get
from bs4 import BeautifulSoup
import requests
import time
import os, os.path
import json



toke="NzY5MTIyMjcyOTEyODY3MzU4.X5Ka7w"
TOKEN = ".OPwyhbHigA6q6OaaP7gIog8LfXY"
bot = commands.Bot(command_prefix='m.')

bot.remove_command('help')


@bot.command(name='ошибка')
async def error(ctx):
  embed=discord.Embed(description="Ошибки делают все!", color=0x00ff08)
  embed.set_author(name="Клик сюда что бы описать её!", url="https://docs.google.com/forms/d/e/1FAIpQLSeAAHBcIYQ80iU9NnNcaPp8NEj06eaGSokAXyie0imFQfBDXQ/viewform?usp=sf_link")
  await ctx.send(embed=embed)

@bot.event
async def on_ready():
    activity = discord.Game(name=f"|||У меня вопрос а что написать в статус?||| ", type=2)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


@bot.command(name='Марокки')
async def Marokki(ctx):
	embed=discord.Embed(title="Здрасте")
	embed.add_field(name="Туториал по боте", value="префикс команд m.", inline=True)
	embed.add_field(name="m.хелп", value="список команд", inline=True)
	embed.add_field(name="m.карточку_дай", value="выдача карточки", inline=True)
	embed.set_footer(text="все я думаю хватит")
	await ctx.send(embed=embed)

@bot.command(name='скин')
async def skin(ctx, name):
    
	username = name

	resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
	uuid = resp.json()["id"]

	embed=discord.Embed(title='Скин', color=0xe30dd1)
	embed.set_thumbnail(url=f'https://crafatar.com/renders/body/{uuid}')
	embed.set_footer(text='хиххихих')
	await ctx.send(embed=embed)

    
@bot.command(name='imposter')
async def imposter(ctx, color, name):
  await ctx.send(f'https://vacefron.nl/api/ejected?name={name}&impostor=true&crewmate={color}')

    
    
    

fishs = [
  'Рогалик АААА',
  'Палка что она там делает?',
  'Аниме тян ой',
  'Чашка чая',
  'Даша',
  'Леон',
  'Геометрия 8класс',
  'мотематичка',
  'Рыба фуга с морковкой :)'
]

def card(authorid):
  file_1 = open(f"{authorid}.json", "r")
  file_1.close()
  return True



def money(authorid):
  file_1 = open(f"{authorid}.json", "r")
  money = file_1.read()
    #МАНИ НА КАРМАНЕЕ
  file_1.close()
  denyagi = json.loads(money)
  mani = denyagi['money']

  return mani

def addmoney(authorid, c):
  mani = money(authorid)
  mani = int(mani)
  mani += c
  manimani = {
  "money": mani
  }
  
  #denyagi['money']
  file_1 = open(f"{authorid}.json", "w")
  file_1.write(f'{json.dumps(manimani)}')
  file_1.close()


def deletemoney(authorid, c):
  if money(authorid) == 0:
    print('Я не могу предоставить ему кредит!!!!')
  else:
    mani = money(authorid)
    mani = int(mani)
    mani -= c
    if mani < 0:
      print('ну ты точно не пройдешь!Я не могу предоставить ему кредит!!!! ')
    else:
      manimani = {
      "money": mani
      }
  
    #denyagi['money']
      file_1 = open(f"{authorid}.json", "w")
      file_1.write(f'{json.dumps(manimani)}')
      file_1.close()
      return True
    


@bot.command()  # просто для бота
async def youtube(ctx):  # Команда
    await ctx.message.add_reaction("✅")
    await ctx.send("кнопка ютуба , \n🟥🟥🟥🟥🟥\n🟥🟥⬜🟥🟥\n🟥🟥⬜⬜🟥\n🟥🟥⬜🟥🟥\n🟥🟥🟥🟥🟥")



@bot.command()  # просто для бода
async def chpock(ctx):  # Команда
    await ctx.message.add_reaction("✅")
    await ctx.send("👄👄👄👄💋💋💋💋")


@bot.command()  # просто для бота
async def russian(ctx):  # Команда
    await ctx.message.add_reaction("✅")
    await ctx.send("⬜⬜⬜\n🟦🟦🟦\n🟥🟥🟥\n")


                   
                   
                   
                   
                   
@bot.command()  # просто для бота
async def ukrain(ctx):  # Команда
    await ctx.message.add_reaction("✅")
    await ctx.send("🟦🟦🟦\n🟨🟨🟨\n🟨🟨🟨\n")


@bot.command()
async def fish(ctx):
  await ctx.send(random.choice(fishs))


embed43=discord.Embed(title="предметы ахмеда", color=0x61ff6b)
embed43.add_field(name="букет-роз <:unnamed:813795732954939483> за 40крышек", value="ММ а пахнэ як!", inline=True)
embed43.add_field(name="носки - 15крышек 🧦", value="а че нормально ", inline=True)
embed43.add_field(name=" мороженое - 14🍧", value="много не кушать!", inline=True)
embed43.add_field(name=" тортик - 17 крышек 🍰", value="ммм сладка", inline=True)
embed43.add_field(name=" тв-лимон за 30крышек <:tv_limon:816555500547866634>", value="он эмм зачем?", inline=True)
embed43.add_field(name="бикини - 40 крышек 👙", value="вам много знать не нада", inline=True)
embed43.add_field(name="ваз - 100 крышек🚗 ", value="машина мая ваз 2101", inline=True)
embed43.add_field(name="ананас - 7🍍", value="что ананасак на англиском пайн эпл кста", inline=True)
embed43.add_field(name=" суши-ролы - 40🍙 ", value="Ета суши а да ", inline=True)
embed43.add_field(name="звезды - 100✨", value="звезда ", inline=True)
embed43.add_field(name="леон - 999999крышек<:leon:818182964147781702>", value="тоже звезда ", inline=True)
embed43.add_field(name="хлеб - 16крышек🍞", value="Он не ютубер ........ ", inline=True)
embed43.add_field(name="сало - 19крышек<:calo:818889331007553577>", value="Україньське сало! ", inline=True)
embed43.add_field(name="клубника - 5крышек🍓", value="крутая", inline=True)
embed43.add_field(name="дынька - 20крышек🍈", value="Ля", inline=True)
embed43.add_field(name="вишня - 20крышек🍒", value="красный", inline=True)
embed43.add_field(name="Манго - 30крышек🥭", value="Не манга", inline=True)
embed43.add_field(name="кокос - 30крышек🥥", value="Крепкий орешек!", inline=True)



@bot.command(name='генератор-вещей')
async def generatoritems(ctx, name, buy, mesage, iops, emoji=' '):
    buy = int(buy)
    lof = f"{name} - {buy}крышек{emoji}"
    await ctx.send(f"""```py \n embed43.add_field(name="{lof}", value="{iops}", inline=True)```""")
    codel = f"""```py \n if item == "{name}":\n  if deletemoney(authorid=ctx.author.id, c={buy})\n  pitem(id=user.id, name="{name}")  \n  await ctx.send(f"{mesage}")```"""

    await ctx.send(codel)


def pitem(id, name):
    file_1 = open(f"{id}i.json", "a")
    file_1.write(f'{name} &\n')
      
    # Записываем сюда что-то, предварительно преобразовав в строку командой str(x)

    file_1.close()



@bot.command(name='быро_скажи')
async def say(ctx, arg):
  await ctx.send(arg)

@bot.command(name='перевести')
async def test12(ctx, user: discord.Member, c: int):
  #deletemoney(authorid=ctx.author.id, c=c)
  if deletemoney(authorid=ctx.author.id, c=c):
    addmoney(user.id, c)
    await ctx.send('а оно все перевелось на картучку пользователя')

@bot.command(name='подарить')
async def test14(ctx, user: discord.Member=None ,item=None):
  if user ==None:
    await ctx.send(embed=embed43)
    
  if item == 'букет-роз':
    if deletemoney(authorid=ctx.author.id, c=40):
      await ctx.send(f'Ты подарил букет роз {user}')
      pitem(user.id, item)
  if item == 'носки':
    if deletemoney(authorid=ctx.author.id, c=15):
      await ctx.send(f'Ты подарил НОСКИ🧦 {user}')
      pitem(user.id, item)
  if item == 'мороженое':
    if deletemoney(authorid=ctx.author.id, c=14):
      await ctx.send(f'Ты подарил МОРОЖЕНОЕ🍨 весной {user}')
      pitem(user.id, item)
  if item == 'тортик':
    if deletemoney(authorid=ctx.author.id, c=17):
      await ctx.send(f'Ты подарил ТОРТИК🍰 {user}')
      pitem(user.id, item)
  if item == 'тв-лимон':
    if deletemoney(authorid=ctx.author.id, c=30):
      await ctx.send(f'Ты подарил тв-лимон <:tv_limon:816555500547866634> {user}')
      pitem(user.id, item)
  if item == 'бикини':
    if deletemoney(authorid=ctx.author.id, c=40):
      await ctx.send(f'ты подарил бикини👙 {user} ')
      pitem(user.id, item)
  if item == 'ваз':
    if deletemoney(authorid=ctx.author.id, c=100):
      await ctx.send(f'ты подарил ваз🏎{user} ')
      pitem(user.id, item)
  if item == 'ананас':
    if deletemoney(authorid=ctx.author.id, c=7):
      await ctx.send(f'ты подарил ананас🍍{user} ')
      pitem(id=user.id, name=f'{item}')
  if item == 'суши-ролы':
    if deletemoney(authorid=ctx.author.id, c=40):
      await ctx.send(f'ты подарил  суши-ролы🍥{user} ')
      pitem(user.id, item)
  if item == 'звезды':
    if deletemoney(authorid=ctx.author.id, c=100):
      await ctx.send(f'ты подарил  звезды✨{user} ')
      pitem(user.id, item)
  if item == 'Леон':
    if deletemoney(authorid=ctx.author.id, c=999999):
      await ctx.send(f'ты подарил  ЛЕОНА?{user} ')
      pitem(id=user.id, name=f'{item}')
  if item == 'хлеб':
    if deletemoney(authorid=ctx.author.id, c=16):
      await ctx.send(f'ты подарил  ХЛЕБ{user} ')
      pitem(id=user.id, name=f'{item}')
  if item == 'сало':
   if deletemoney(authorid=ctx.author.id, c=19):
     await ctx.send(f'ты подарил  САЛО?{user} ')
     pitem(id=user.id, name=f'{item}')
  if item == "клубника":
    if deletemoney(authorid=ctx.author.id, c=5):
      pitem(id=user.id, name="клубника")  
      await ctx.send(f"ты подарил клубнику🍓! {user}")
  if item == "дынька":
    if deletemoney(authorid=ctx.author.id, c=20):
      pitem(id=user.id, name="дынька")  
      await ctx.send(f"ты подарил дыньку🍈! {user}")
  if item == "вишня":
    if deletemoney(authorid=ctx.author.id, c=20):
      pitem(id=user.id, name="вишня")  
      await ctx.send(f"ты подарил вишню🍒 ! {user}")
  if item == "кокос":
      if deletemoney(authorid=ctx.author.id, c=30):
        pitem(id=user.id, name="кокос")  
        await ctx.send(f"ты подарил кокос🥥! {user}")
  if item == "Манго":
    if deletemoney(authorid=ctx.author.id, c=30):
      pitem(id=user.id, name="Манго")  
      await ctx.send(f"ты подарил манго🥭 ! {user}")
    


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, reason):
    await user.send(f'Вас забанили ;(.Вас забанил:{ctx.author}На: {ctx.guild.name}Причина:{reason}') 
    await user.ban()
    await ctx.send(f"<:BAN:799721976754733066> Короче рип :3")


@bot.command()
async def emoivb(ctx, channel: discord.VoiceChannel, *, new_name):
    await bot.edit(name=new_name)


  
@bot.command()
@commands.has_permissions(administrator=True)
async def crash(ctx, j):
  while j:
    edibles = ["отбивные", "пельмени","яйца","орехи"]
    for food in edibles:
      if food == "пельмени":
          await ctx.send("Я не ем пельмени!")
          break
      await ctx.send("Отлично, вкусные " + food)
    else:
      ctx.send("Хорошо, что не было пельменей!")
    await ctx.send("Ужин окончен.")


kicke = [
  'ИЗЫДИ! НЕЧЕСТЬ ПРОКЛЯТАЯ',
  'о кик :)',
  'О бросок сквозь стену',
  '`Кик` аче'
  'С любовью МАРОККИ БОТ'
]





@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member,* ,prichin):
    await user.kick(reason=prichin)
    await ctx.send(f"<:Kick:799723046607781950> {random.choice(kicke)} ")


@bot.command(name='новости')
async def news(ctx):
  url = 'http://mignews.com/mobile'
  b = 0
  page = requests.get(url)
  new_news = []
  news = []
  soup = BeautifulSoup(page.text, "html.parser")
  news = soup.findAll('a', class_='lenta')
  for i in range(len(news)):
    if news[i].find('span', class_='time2 time3') is not None:
        new_news.append(news[i].text)
  for i in range(len(new_news)):
    await ctx.send(new_news[i])
    b += 1
    if b > 5:
        break









@bot.command(name='карточку_дай')
async def cart_give(ctx):

    # Открываем файл "file.txt" для записи. "w" - переписать, "a" - дописать в конец.
    # Всегда используем слеши вперед, даже на виндовсе
    # Если такого файла нет и прав достаточно, то он создастся. Если нет - будет ошибка.
    # Проверить наличие файла можно функцией exists(path) из os.path
    try:
          file_1 = open(f"{ctx.author.id}.json", "r")
          

          file_1.close()
    # Закрываем файл
          await ctx.send('<:krishka_tebe_ponel:800075730050482216>ТЫ УЖЕ тут был :o')
          await ctx.send("https://media.discordapp.net/attachments/824636040651866163/824636063397838868/ed5411302dfb53e4e758d61dc02fa80f.png")

      
    except Exception:
      await ctx.send('текс ага создали<:krishka_tebe_ponel:800075730050482216>')
      await ctx.send("https://media.discordapp.net/attachments/824636040651866163/824636063397838868/ed5411302dfb53e4e758d61dc02fa80f.png")
      
      file_1 = open(f"{ctx.author.id}.json", "w")
      file_1.write('{"money": 0 }')
      
    # Записываем сюда что-то, предварительно преобразовав в строку командой str(x)

      file_1.close()
      file_1 = open(f"{ctx.author.id}i.json", "w")
      file_1.write('')
      
    # Записываем сюда что-то, предварительно преобразовав в строку командой str(x)

      file_1.close()

        
@bot.command(name='предметы')
async def items(ctx):
    file = open(f"{ctx.author.id}i.json", 'r')
    ms = file.readlines()
    file.close()
    invent = f"{ms} "
    invent = invent.replace('&', ' ' )
    await ctx.send(invent)


#@bot.command(name='топ_богачей')
#async def top_money(ctx):
#    members_c = let(ctx.guild.members)
#    embed=discord.Embed(title="✨ТОП✨БОГАЧЕЙ✨", description="ТОП 10", color=0x3de70d)
#    vikl = True
#    while vikl:
#    	member_k = ctx.guild.members[members_c]
#		if card(member_k.id):
#        	#Че ЗА!
#			embed.add_field(name=member_k.name, value=money(member_k.id), inline=False)
#			
#        members_c =+ 1
#        if members_c == 0 :
#            await ctx.send(embed=embed)
#            vikl = False
#            
        
        
        
        

    
    
@bot.command(name='газеты')
async def gazeti(ctx):
  file_1 = open(f"{ctx.author.id}.json", "r")
  money = file_1.read()
    #МАНИ НА КАРМАНЕЕ
  file_1.close()
  denyagi = json.loads(money)
  mani = denyagi['money']
  mani = int(mani)
  mani += 1
  manimani = {
  "money": mani
  }
  
  #denyagi['money']
  file_1 = open(f"{ctx.author.id}.json", "w")
  file_1.write(f'{json.dumps(manimani)}')
  file_1.close()
  await ctx.send('Ты розносил газеты и тебе дали 1крышку :)')



    
@bot.command(name='казино')
async def casino(ctx, co):
  co = int(co)
  if money(ctx.author.id) > co:
    chiuc= [
      "da",
      "net"
    ]
    
    if random.choice(chiuc) == "da":
    
      addmoney(ctx.author.id, co)
      await ctx.send('Удача на твоей стороне!')
    else:
      deletemoney(ctx.author.id, co)
      await ctx.send('А все иди денег нету')


  
    

@bot.command(name='карточка')
async def cartochka(ctx, user: discord.Member=None):
  if user == None:
    file_1 = open(f"{ctx.author.id}.json", "r")
    name = ctx.author.name
  else:
    file_1 = open(f"{user.id}.json", "r")
    name = user.name
  
  money = file_1.read()
    #МАНИ НА КАРМАНЕЕ
  file_1.close()
  denyagi = json.loads(money)
  out = Image.open("card.png")

  # ШРЫФТ
  fnt = ImageFont.truetype("Jura-Bold.ttf", 60)
  # get a drawing context
  d = ImageDraw.Draw(out)
  fnt2 = ImageFont.truetype("Jura-Bold.ttf", 30)
  # draw multiline text
  d.multiline_text((90,90), name, font=fnt, fill=(0, 0, 0))

  # draw multiline text
  d.multiline_text((40,150), f"{denyagi['money']} крышек", font=fnt, fill=(0, 0, 0))

  d.multiline_text((40,320), "Можешь потратить \nих командой m.подарить :)", font=fnt2, fill=(0, 0, 0))

  out.save("what.png", "PNG")
  
  
  file = discord.File("what.png", filename="what.png")
  await ctx.channel.send("Ну красиво.", file=file)

last_message = None
last_messagea = None
last_messageb = None

messagesg = [
  'разбор ваз 2104',
  'Влад где гроші',
  'Хто я?',
  'Джокер',
  'вы любите ягоды?',
  'Где пельмени?',
  '<:flushed5:801782380268355584>',
  'рыба',
  'не то',
  'домашний самогон',
  "Тупой авто редактор",
  "вот он! настоящий пельмень!",
  "Чея",
  "Влад лошок кресломешок на голове горшок",
  "крутое слово",
  "и это",
  "хватит?",
  "Не пускайте бота в мой кошелек",
  " А МНЕ СТОКА ДЕНЕГ??",
  "У меня удача",
  "и \n что є\nаєа\n",
  "Марокки ломик",
  "Кароче бан",
  "вы готовы дети?ъ",
  "все закрываю канал"
  "Миша лошок кресломешок на голове горшок",
  "Плохое слово",
  "Верь в меня Ёжик",
]

@bot.event
async def on_message(message):
  channel = message.channel
  global last_message
  global last_messagea
  global last_messageb
  
  if message.content == "m.персиковая_атака":
    print('ШО ЦЕ ТАКЕ')
  if message.content == "m.копировать":
    print('ШО ЦЕ ТАКЕ')
  else:
    last_messageb = last_messagea
    last_messagea = last_message
    last_message = message
  otvet = random.randint(7, 18)
  if otvet == 17:
    await channel.send(random.choice(messagesg))
  
  
  
  await bot.process_commands(message)


@bot.command(name="персиковая_атака")
@commands.has_role('🍑день персика 18.02.2021')
async def puk(ctx):
  await last_message.add_reaction('🍑')
  await last_messagea.add_reaction('🍑')
  await last_messageb.add_reaction('🍑')
  

@bot.command(name="копировать")
async def copy(ctx):
  await ctx.send(last_message.content)

 # await ctx.send(last_message.content)
@bot.event
async def on_raw_reaction_add(payload):
    addmoney(authorid=payload.user_id, c=1)
    




@bot.command(name='команды')
async def commandsbot(ctx):
  await ctx.send(bot.all_commands)


@bot.command(name='хелп')
async def helpcommands(ctx):
  embed=discord.Embed(title="Помощь", description="Тут ты можешь узнать о БАНКЕ КРЫШКА И другим плюшкам ;0", color=0xff42e0)
  embed.add_field(name="карточка", value=" выдает количиство КРЫШЕК", inline=True)
  embed.add_field(name="карточку_дай", value="начало всего !!!!", inline=False)
  embed.add_field(name="перевести [@PING] [количество]", value=" - переводит крышки ", inline=True)
  embed.add_field(name="подарить @человек вещь", value=" - дарит просто так  список предметов m.подарить ))))) ", inline=False)
  embed.add_field(name="скин (ник майнкрафт лицуха)", value=" - скин человека  ))))) ", inline=False)
  embed.add_field(name="youtube", value=" - арт  )9))) ", inline=False)
  embed.add_field(name="ukrain", value=" - арт слава украини ))9)) ", inline=False)
  embed.add_field(name="russian", value=" - арт rasssia )9))) ", inline=False)
  embed.add_field(name="персиковая_атака", value=" - для персиков там бум будет ))))) ", inline=False)
  embed.add_field(name="fish", value=" - посмотри сам что будет! )0)) ", inline=False)
  embed.add_field(name="kick", value=" - ета для админов ))9) ", inline=False)
  embed.add_field(name="ban", value=" - и ета для админов! ))0)) ", inline=False)
  embed.add_field(name="новости", value=" - и ета новости)0) ", inline=False)
  embed.add_field(name="предметы", value=" - твои инвентарь!)0) ", inline=False)
  embed.add_field(name="действие <действие>", value=" - действие ", inline=False) #
  embed.add_field(name="казино", value=" - кизино скока? ", inline=False) #топ_богачей
  embed.add_field(name="ошибка", value=" - ошибка???? ", inline=False) #топ_богачей
  # персиковая_атака
  await ctx.send(embed=embed)




@bot.command(name='действие')
async def me(ctx , me):
  await ctx.message.delete()
  embed = discord.Embed(title="Сообщение", description=f"{ctx.author.name} {me}", color=0x58f410)
  await ctx.channel.send(embed = embed)



#@bot.command(name='лобстер')







#youtube 
bot.run(f'{toke}{TOKEN}')