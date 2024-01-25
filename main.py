import datetime
import json
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import *
from discord.commands import Option
from dotenv import load_dotenv

from events.roleview import *

load_dotenv()
bot = discord.Bot()
guildID = '407878248480112642'
channelID = '1055539833407295579'


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    scheduler = AsyncIOScheduler()

    async def scheduled_task1():
        guild = bot.get_guild(int(guildID))
        channel = guild.get_channel(int(channelID))
        monthNames = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                      'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        month = monthNames[datetime.datetime.now().month - 1]
        msg = await channel.send(
            f"📢 Esta é a Chamada Obrigatória do mês de **{month}**. Todos os <@&1020194745722609684> tem 7 dias para confirmar na reação abaixo que estão ativos. Caso contrário, podem receber 2 pontos de infração.\n\n⚠️ Atenção a quem está em <@&1020234436236816394>, teremos uma chamada **especifica** para vocês.")
        await msg.add_reaction('<:spts:863119583275384864>')

    async def scheduled_task2():
        guild = bot.get_guild(int(guildID))
        channel = guild.get_channel(int(channelID))
        msg = await channel.send(
            "⚠️ Atenção membros em <@&1020234436236816394> marcados nessa mensagem.\n\nVocê tem 5 dias para reagir no ✅ abaixo. Caso contrário, será considerado inativo e perderá o cargo de membro.")
        await msg.add_reaction('\U00002705')

    scheduler.add_job(scheduled_task1, 'cron', day='25', hour='3', minute='0', id="task1", replace_existing=True)
    scheduler.add_job(scheduled_task2, 'cron', day='27', hour='3', minute='0', id="task2", replace_existing=True)

    # scheduler.print_jobs()

    scheduler.start()


@bot.slash_command()
async def roles(ctx):
    embed = discord.Embed(
        title="Núcleos",
        description="Atualmente o grupo Spartacus possui 4 núcleos ativos.\nClique no botão referente ao núcleo que deseja ter acesso.\n",
        color=0xFF0000)
    embed.set_image(url="https://i.imgur.com/Ml56dgF.png")
    await ctx.respond(embed=embed, view=RoleView())


@bot.slash_command()
async def list_members(ctx):
    with open('MembrosDate.json', 'r') as f:
        data = json.load(f)
    membros = data['membros']
    bloco_texto = ""
    for membro in membros:
        user_id = int(membro['id'])
        member = await ctx.guild.fetch_member(user_id)
        if member is not None:
            bloco_texto += f"<@{member.id}> {membro['data_entrada']}\n"
    bloco_texto += f"\n👥 Total: {len(membros)}"
    embed = discord.Embed(title="Nossos Membros", description=bloco_texto, color=7340032)
    embed.set_image(url="https://i.imgur.com/Ml56dgF.png")
    await ctx.send(embed=embed)


@bot.slash_command()
async def add_member(ctx, member_id: Option(str, required=True), entry_date: Option(str, required=True)):
    with open('MembrosDate.json', 'r') as f:
        data = json.load(f)

    new_member = {"id": member_id, "data_entrada": entry_date}
    data['membros'].append(new_member)

    with open('MembrosDate.json', 'w') as f:
        json.dump(data, f, indent=4)

    await ctx.respond(f"Member {member_id} added with entry date {entry_date}", ephemeral=True)


@bot.slash_command()
async def remove_member(ctx, member_id: Option(str, required=True)):
    with open('MembrosDate.json', 'r') as f:
        data = json.load(f)

    # Encontre o membro na lista e remova
    for i, member in enumerate(data['membros']):
        if member['id'] == member_id:
            del data['membros'][i]
            break

    with open('MembrosDate.json', 'w') as f:
        json.dump(data, f, indent=4)

    await ctx.respond(f"Member {member_id} removed", ephemeral=True)


channels = [856178528285360189, 856185518684504074, 1018270570456035418, 1189596088584376340, 1194292103778406511,
            1195761430478205050, 1195766388606898308, 1195765733712474274]


@bot.event
async def on_message(message):
    if message.channel.id in channels:
        await message.add_reaction('\U00002705')
        await message.add_reaction('\U0000274C')
        post_date = message.created_at.strftime("%d/%m/%Y")
        thread_name = f"{message.author.display_name} ({post_date})"
        thread = await message.create_thread(name=thread_name)
    # await bot.process_commands(message)


bot.run(os.getenv('TOKEN'))
