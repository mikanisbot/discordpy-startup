import re
import time
from discord.ext import commands
import os
import random
import traceback
import discord
import time
import datetime
import psutil
import string
import aiohttp

adminid = 704702259665043476
developer = [704702259665043476, 562308096538705930]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
token = "NzU5NDEwNDIyNTkxMzg5NzM2.X29GEQ.py4Dm0IZrVIWqIukZS2jJmy7KTA"

bot.remove_command('help')

@bot.command()
async def debug(ctx):
 await ctx.send(str(ctx.channel))

@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title="ヘルプコマンドです！", description=f"計算:計算ができます(使い方:計算 1+1)\nパスワード:指定した桁数のパスワードを生成します､詳しい使い方は'パスワード --help'を実行してください\nDM:指定した人に匿名でDMを送ります(使い方:DM @ユーザー メッセージ)\nbot人数：botの数を調べます\npin：ピン留めします\nping：確認します\nping2：確認します\nui：ユーザーを調べます(使い方：ui @ユーザー)\n uuser：ユーザー調査です！(使い方：uuser ユーザーID)\nサイコロをふる：サイコロをふります！(使い方：サイコロをふる 1d6)\nチャンネル：指定したチャンネルに書き込みます！(使い方：チャンネル #(チャンネル名) てすと)\nチャンネル確認：チャンネルを確認します！\nチャンネル2：その場のチャンネルに書き込みます！(使い方：チャンネル2 てすと)\nユーザー人数：ユーザー人数を調べます！\nリンク：短縮リンクを作ります！(使い方：リンク URL)\nフォロー：アナウンスチャンネルをフォローします\n全体人数：サーバー人数を調べます！\n役職持ち確認：役職所持者を確認します！(使い方：役職持ち確認 役職名)\n時間確認：時間を確認します！\n野生：ネタコマンドです！\n鯖知りたい：サーバーの情報を知ることができます！(使い方：鯖知りたい サーバーID)\nバグ報告 (バグ報告します"))


@bot.command()
async def help2(ctx):
     await ctx.send(embed=discord.Embed(title="運営用ヘルプコマンドです！", description=f"チャンネルトピック：チャンネルトピックをいじります！(使い方：チャンネルトピック てすと)\nkick：対象者を蹴ります！(使い方：kick ユーザーID)\nban：対象者をBANします！(使い方：ban ユーザーID)\n役職付与：役職を付与します！(使い方：役職付与 メンバーの名前 役職名)\n脱出：サーバーから退室します！(使い方：脱出 サーバーID)\n使用率：使用率を調べます！\nvcから切断VCから強制切断します！(使い方：vcから切断 めんばあ)\nend：BOTを終了させます！\nプレイ中変更：プレイ中を変更します！(使い方：プレイ中変更 てすと)"))

@bot.event
async def on_command_error(ctx, error):
 if ctx.message.author.id in developer:
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
 else:
  await ctx.send("何かしらのエラーが起きたようです､構文ミスでないことを確認してから開発者にご相談ください\nまた､DMでは使えないコマンドも存在します")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name="フォロー")
async def follow(ctx, channel_id=742443380344094752):
   i = dict(ctx.author.guild_permissions)
   if i['manage_webhooks'] == True:
    syutoku = bot.get_channel(channel_id)
    # print(syutoku.id)
    tyannneru = syutoku.is_news()
    # print(tyannneru)
    if tyannneru == False:
        await ctx.send("アナウンスチャンネルじゃないよ( ๑´•ω•`๑)")
    else:
        await syutoku.follow(destination=ctx.channel)
        await ctx.send("アナウンスチャンネルをフォローした。\nいらなくなったら運営に頼んで消して貰ってね。")    
   else:
    await ctx.send("何様のつもりですか･･････?	")

@bot.event
async def on_message(message):
 if message.author == bot.user:
  return
 if str(message.channel) == "mikan_global":
#  await message.delete()
  embed = discord.Embed(description=message.content)
  embed.set_author(name = message.author.name + "#" + message.author.discriminator + "@" + message.guild.name, icon_url=message.author.avatar_url)
  embed2 = discord.Embed()
  embed2.set_author(name = message.author.name + "#" + message.author.discriminator + "@" + message.guild.name, icon_url=message.author.avatar_url)
  j = 0
  for i in message.attachments:
   if j == 0:
    embed.set_image(url=i.proxy_url)
    for channels in bot.get_all_channels():
     if channels.name == "mikan_global":
      await channels.send(embed=embed)
    j = 1
   elif j == 1:
    embed2.set_image(url=i.proxy_url)
    for channels in bot.get_all_channels():
     if channels.name == "mikan_global":
      await channels.send(embed=embed2)
  if j == 0:
   for channels in bot.get_all_channels():
    if channels.name == "mikan_global":
     await channels.send(embed=embed)
  await message.delete()
 else:
  if "ypa" in message.content.lower():
   if "http" in message.content.lower():
    await bot.process_commands(message)
    return
   else:
    await message.channel.send("あなたスパイ•́ω•̀)?")
  await bot.process_commands(message)


@bot.command(pass_context=True)
async def ping2(ctx):  # 処理時間を返す
    startt = time.time()
    tmp = await ctx.send("計測中……!")
    await tmp.edit(content="pong！\n結果:**" + str(round(time.time()-startt, 3))+"**秒ですฅ✧！")

@bot.command(name='パスワード')
async def passwd(ctx, *args):
 opt = list(args)
 if opt[0] == "--help":
  await ctx.send("パスワード生成コマンドです\n基本的な使い方: パスワード 桁数\n桁数の前に入れるオプション:\n--no-spchar 記号を含まない\n--only-number 数字のみ")
 elif str(type(ctx.channel)) == "<class 'discord.channel.DMChannel'>":
  i = 0
  passwd = ""
  if opt[0] == "--no-spchar":
   if int(opt[1]) > 2000:
    await ctx.send("文字数は2000文字以下にしてね､BOTが壊れちゃうよ( ๑´•ω•`๑)")
    return
   else:
    while i < int(opt[1]) :
     passwd = passwd + random.choice(string.ascii_letters + string.digits)
     i = i + 1
  elif opt[0] == "--only-number":
   if int(opt[1]) > 2000:
    await ctx.send("文字数は2000文字以下にしてね､BOTが壊れちゃうよ( ๑´•ω•`๑)")
    return
   else:
    while i < int(opt[1]) :
     passwd = passwd + random.choice(string.digits)
     i = i + 1
  else:
   if int(opt[0]) > 1998:
    await ctx.send("文字数は1998文字以下にしてね､BOTが壊れちゃうよ( ๑´•ω•`๑)")
    return
   else:
    while i < int(opt[0]) :
     passwd = passwd + random.choice(string.ascii_letters + string.digits + "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~")
     i = i + 1
    await ctx.send("パスワードの生成が完了しました､生成されたパスワードは")
    await ctx.send("`" + passwd + "`")
    await ctx.send("です")
    return
  await ctx.send("パスワードの生成が完了しました､生成されたパスワードは")
  await ctx.send(passwd)
  await ctx.send("です")
 else:
  await ctx.send("このコマンドはDM以外で実行するべきではありません､このBOTとのDM上で実行してください")

@bot.command(name='計算')
async def keisan(ctx, *, arg):
  if re.fullmatch(r'[0-9\-+*/^\s()]+', arg):
   await ctx.send("答えは" + str(eval(arg.replace("^", "**"))) + "です")
  else:
   await ctx.send("計算式じゃないよぉ( ๑´•ω•`๑)")

@bot.command(name='野生')
async def _yasei(ctx):
    col = random.randint(0x000000, 0xffffff)
    nikkuname = ctx.author.nick
    if nikkuname == None:
        await ctx.send(embed=discord.Embed(title="あ！", description=f"野生の{ctx.author.name}が飛び出してきた！", color=col))
    else:
        await ctx.send(embed=discord.Embed(title="あ！", description=f"野生の{ctx.author.name}({nikkuname})が飛び出してきた！", color=col))


@bot.command(name='チャンネルトピック')
async def channeltopic(ctx, channel: discord.TextChannel, *, topic):
    i = dict(ctx.author.guild_permissions)
    if i['manage_channels'] == True:
       await channel.edit(topic=topic)
    else:
        await ctx.send('何様のつもりですか……？')


@bot.command(name="チャンネル")
async def _channel(ctx, channel: discord.TextChannel, *, arg):
    await channel.send(arg)
    if str(type(ctx.channel)) != "<class 'discord.channel.DMChannel'>":
     await ctx.message.delete()


@bot.command(name="チャンネル2")
async def _channelninini(ctx, *, arg):
    await ctx.send(arg)
    if str(type(ctx.channel)) != "<class 'discord.channel.DMChannel'>":
     await ctx.message.delete()

@bot.command(name="DM")
async def loveletter(ctx, member: discord.Member, *, arg):
 await member.send(arg)
 await ctx.send("あなたのメッセージ､届けましたよ(❁´ω`❁)")

@bot.command(name="kick")
async def _kick(ctx, arg: discord.Member, *, riyuu=None):
    i = dict(ctx.author.guild_permissions)
    if i['kick_members'] == True:
        await ctx.guild.kick(arg, reason=riyuu)
        await ctx.send(f'実行者：{ctx.author.name}\n<@{arg}> をキックした。\n理由：{riyuu}')
    else:
        await ctx.send('何様のつもりですか……？')


@bot.command(name="ban")
async def _ban2(ctx, arg: discord.Member, *, riyuu=None):
    i = dict(ctx.author.guild_permissions)
    if i['ban_members'] == True:
        await ctx.guild.ban(arg, reason=riyuu)
        await ctx.send(f'実行者：{ctx.author.name}\n<@{arg}> をえっついした。\n理由：{riyuu}')
    else:
        await ctx.send('何様のつもりですか……？')


@bot.command(name="サイコロをふる", aliases=["d"])
async def daisuno(ctx, dice: str):
#    rolls, limit = map(int, dice.split('d'))
#    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    list = dice.split("d")
    await ctx.send(random.randint(int(list[0]), int(list[1])))


@daisuno.error
async def daisuno_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("え？\n……お願いですが、数字d数字でお願いします。\nあと0以下はやめてください。")


@bot.command(name="役職付与")
async def _yakusyokunoyatu(ctx, member: discord.Member, role: discord.Role):
    i = dict(ctx.author.guild_permissions)
    if i['manage_roles'] == True:
        await member.add_roles(role)
        await ctx.send(f'{member.name}さんに{role}を付与しました。')
    else:
        await ctx.send('何様のつもりですか……？')


@bot.command(aliases=["ピン留め切替", "次のメッセージをピン留めして"])
async def pin(ctx, mid: int):
   i = dict(ctx.author.guild_permissions)
   if i['manage_channels'] == True:
    msg = await ctx.message.channel.fetch_message(mid)
    if msg.pinned:
        await msg.unpin()
        await ctx.send(f"ピンを外しました。：{ctx.author.name}")
    else:
        await msg.pin()
        await ctx.send(f"ピンをしました。：{ctx.author.name}")
   else:
    await ctx.send('何様のつもりですか……？')


@bot.command(name="時間確認")
async def _zikannnnnnn(ctx):
    # t = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    color = random.randint(0x000000, 0xffffff)
    await ctx.send(embed=discord.Embed(title="時間です。よく見ておいてくださいね。", description=f"{now}", color=color))


@bot.command()
async def ui(ctx, *, member: discord.Member):
        col = random.randint(0x000000, 0xffffff)
        user = member
        embed = discord.Embed(title=f"{user.name}の情報", color=col)
        embed.set_thumbnail(url=f'{user.avatar_url_as(static_format="png")}')
        embed.add_field(name="名前", value=f"{user.name}", inline=False)
        embed.add_field(name="ID", value=f"{user.id}", inline=False)
        embed.add_field(name="タグ", value=f"{user.discriminator}", inline=False)
        embed.add_field(name="BOT", value=f"{user.bot}", inline=False)
        if str(type(ctx.channel)) != "<class 'discord.channel.DMChannel'>":
         embed.add_field(name="サーバー上の名前",value=f"{member.nick}", inline=False)
         embed.add_field(name="権限", value=",".join([row[0] for row in list(member.guild_permissions) if row[1]]), inline=False)
        if member.activity != None:
         embed.add_field(name="アクティビティ", value=member.activity.name)
        embed.add_field(name="ステータス", value=f"{member.status}", inline=False)
        embed.add_field(name="アカウント作成日", value=f"{user.created_at}")
        if str(type(ctx.channel)) != "<class 'discord.channel.DMChannel'>":
         i = 0
         for temp in member.roles:
          if i == 0:
           i = 1
          elif i == 1:
           roles = temp.name
           i = 2
          else:
           roles = temp.name + "," + roles
         embed.add_field(name="役職", value=roles, inline=False)
        await ctx.send(embed=embed)


@bot.command(name="鯖知りたい")
async def _si(ctx, guild_id=None):
    if guild_id == None:
        guild_id = int(ctx.guild.id)
        guild = bot.get_guild(ctx.guild.id)
    else:
        guild_id = int(guild_id)
        guild = bot.get_guild(guild_id)
    ch_tcount = len(guild.text_channels)
    ch_vcount = len(guild.voice_channels)
    ch_count = len(guild.channels)
    kt_count = len(guild.categories)
    guild = discord.utils.get(bot.guilds, id=guild_id)
    embed = discord.Embed(title=f"{guild.name}の情報", color=ctx.author.color)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="名前", value=f"{guild.name}", inline=False)
    embed.add_field(name="ID", value=f"{guild.id}", inline=False)
    embed.add_field(name="言語", value=f"{guild.region}", inline=False)
    embed.add_field(name="作成日", value=f"{guild.created_at}", inline=False)
    embed.add_field(name="オーナー", value=f"{guild.owner.name}", inline=False)
    embed.add_field(name="テキストチャンネル数", value=f"{ch_tcount}")
    embed.add_field(name="ボイスチャンネル数", value=f"{ch_vcount}")
    embed.add_field(name="カテゴリー数", value=f"{kt_count}")
    embed.add_field(name="合計チャンネル数(カテゴリー含む)", value=f"{ch_count}")
    embed.add_field(name="サーバー承認レベル", value=f"{guild.mfa_level}")
    embed.add_field(name="サーバー検証レベル", value=f"{guild.verification_level}")
    embed.add_field(name="サーバーブーストレベル", value=f"{guild.premium_tier}")
    embed.add_field(name="サーバーをブーストしたユーザー数",
                    value=f"{guild.premium_subscription_count}")
    # embed.add_field(name="サーバーは大きい？", value=f"{guild.large}")
    await ctx.send(embed=embed)


@bot.command(name="脱出", pass_context=True)
async def huttobasu(ctx):
    i = dict(ctx.author.guild_permissions)
    if i['kick_members'] == True:
        server = ctx.guild
        await ctx.send(f"{server.name}から退室しました。")
        await server.leave()
    else:
        await ctx.send("不可能です……。")


@bot.command(name="リンク", aliases=["短縮リンク"])
# @commands.is_owner()
async def tansyukutyannnnnnnnn(ctx, long_url: str):
    col = random.randint(0x000000, 0xffffff)
    url = "https://is.gd/create.php?format=simple&url=" + long_url
    async with aiohttp.ClientSession() as session:
     async with session.get(url) as response:
      await ctx.send(embed=discord.Embed(title="短縮リンク", description=await response.text(), color=col))
    if str(type(ctx.channel)) != "<class 'discord.channel.DMChannel'>":
     await ctx.message.delete()


@bot.command(aliases=["ユーザー調査"])
# @commands.is_owner()
async def uuser(ctx, idi: int):
    colour = random.randint(0x000000, 0xffffff)
    guild_names = '\n'.join(
        g.name for g in bot.guilds if g.get_member(idi) in g.members)
    embed = discord.Embed(
        title="該当ユーザーが居る場所", description=guild_names[:2000] + '...' if guild_names[:2000] else '', colour=colour)
    await ctx.send(embed=embed)


@bot.command(name="使用率")
async def naganomeeeeeee(ctx):
   if ctx.message.author.id == adminid:
    mem = psutil.virtual_memory()
    allmem = str(mem.total/1000000000)[0:3]
    used = str(mem.used/1000000000)[0:3]
    ava = str(mem.available/1000000000)[0:3]
    memparcent = mem.percent
    await ctx.send(f"全てのメモリ容量:{allmem}GB\n使用量:{used}GB({memparcent}%)\n空き容量{ava}GB({100-memparcent}%)")
   else:
    await ctx.send("何様のつもりですか･･････?")


@bot.command(name="全体人数")
# @commands.has_permissions(administrator=True)
async def ninzuuzentai(ctx):
    guild = ctx.guild
    member_count = guild.member_count
    await ctx.send(f'メンバー数：{member_count}')


@bot.command(name="ユーザー人数")
# @commands.has_permissions(administrator=True)
async def yuzaninzuu(ctx):
    guild = ctx.guild
    user_count = sum(1 for member in guild.members if not member.bot)
    await ctx.send(f'ユーザ数：{user_count}')


@bot.command(name="bot人数")
# @commands.has_permissions(administrator=True)
async def botninzuu(ctx):
    guild = ctx.guild
    bot_count = sum(1 for member in guild.members if member.bot)
    # bot_count = sum(1 for member in guild.memers if member.bot) #間違い
    await ctx.send(f'BOT数：{bot_count}')


@bot.command(name="チャンネル確認")
async def channelchannel(ctx):
    girudo = ctx.guild.channels
    channelcount = len(girudo)
    await ctx.send(embed=discord.Embed(title=f"チャンネル数：{channelcount}", description="500になったら作れません。"))


@bot.command(name="役職持ち確認")
async def roleuserni(ctx, role: discord.Role):
    colour = random.randint(0x000000, 0xffffff)
    mario = role.id
    # guild_names = [member.name for member in ctx.guild.get_role(mario).members]
    guild_names = '\n'.join(
        member.name for member in ctx.guild.get_role(mario).members)
    guild_dayo = [member.name for member in ctx.guild.get_role(mario).members]
    rokerannni = sum(1 for member in guild_dayo)
    await ctx.send(embed=discord.Embed(title=f"{role}を持つメンバー一覧\n人数：{rokerannni}", description=guild_names[:2000] + '...' if guild_names[:2000] else '', colour=colour))


@bot.command(name="vcから切断")
async def _vckikku(ctx, member: discord.Member):
    i = dict(ctx.author.guild_permissions)
    if i['kick_members'] == True:
        await member.move_to(None)
    else:
        await ctx.send("できません！")


@bot.command()
async def end(ctx):
    if ctx.message.author.737320852617560120 == adminid:  # 
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="シャットダウン！", description="終了します！", color=color))
        await bot.close()
    else:
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="違います！", description="……。", color=color))


@bot.command(name="プレイ中変更")
# @commands.is_owner()
async def pureityuudadada(ctx, *, st):
    if ctx.message.author. 737320852617560120 in [adminid]:  # このidのとこは自身のIDに変更してね
        await bot.change_presence(activity=discord.Game(name=st))
        await ctx.send(embed=discord.Embed(title="変更しました！", description=f"{st}"))
    else:
        await ctx.send(embed=discord.Embed(title="あなたは違いますよ！？", description="何しているんですか！？"))


@bot.command(name='バグ報告')
async def bug(ctx, *, text):
    color = random.randint(0x000000, 0xffffff)
    for i in [756787546847051856]:
        ch = bot.get_channel(i)
        await ch.send(embed=discord.Embed(title="意見ありがとうございます。", description=f"報告内容：{text}\n報告者：{ctx.author.name}({ctx.author.id})\nサーバー：{ctx.guild.name}:{ctx.guild.id}", color=color))
    await ctx.send("参考にします。")
    await ctx.message.delete()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="夏海が起きてるよぉん(❁´ω`❁)"))
    print("logged in as " + bot.user.name)
    member = bot.get_user(adminid)
    await member.send("起動完了")

bot.run(token)
	



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="(Python)です"))
    evals.setup(bot)
    print("logged in as " + bot.user.name)
    for channel in bot.get_all_channels():
        if channel.name == '夏海起動時メッセージ':
            await channel.send('おはようございます！\n今日も頑張りましょう！')

bot.run(token)
