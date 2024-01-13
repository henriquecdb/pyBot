import discord
from discord.utils import get


class RoleView(discord.ui.View):

    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Núcleo de Project Reality',
                       style=discord.ButtonStyle.primary)
    async def role1_button(self, button: discord.ui.Button,
                           interaction: discord.Interaction):
        role = get(interaction.guild.roles, name="Núcleo Project Reality")
        await interaction.user.add_roles(role)
        embed = discord.Embed(
            title="Cargo Adicionado",
            description=f"O cargo {role.name} foi adicionado a você!",
            color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label='Núcleo de Squad',
                       style=discord.ButtonStyle.primary)
    async def role2_button(self, button: discord.ui.Button,
                           interaction: discord.Interaction):
        role = get(interaction.guild.roles, name="Núcleo Squad")
        await interaction.user.add_roles(role)
        embed = discord.Embed(
            title="Cargo Adicionado",
            description=f"O cargo {role.name} foi adicionado a você!",
            color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label='Núcleo de Foxhole',
                       style=discord.ButtonStyle.primary)
    async def role3_button(self, button: discord.ui.Button,
                           interaction: discord.Interaction):
        role = get(interaction.guild.roles, name="Foxhole: Ver Núcleo")
        await interaction.user.add_roles(role)
        embed = discord.Embed(
            title="Cargo Adicionado",
            description=f"O cargo {role.name} foi adicionado a você!",
            color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label='Núcleo de ArmA III',
                       style=discord.ButtonStyle.primary)
    async def role4_button(self, button: discord.ui.Button,
                           interaction: discord.Interaction):
        role = get(interaction.guild.roles, name="Núcleo ArmA 3")
        await interaction.user.add_roles(role)
        embed = discord.Embed(
            title="Cargo Adicionado",
            description=f"O cargo {role.name} foi adicionado a você!",
            color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label='Central Estudantil',
                       style=discord.ButtonStyle.primary)
    async def role5_button(self, button: discord.ui.Button,
                           interaction: discord.Interaction):
        role = get(interaction.guild.roles, name="Central Estudantil")
        await interaction.user.add_roles(role)
        embed = discord.Embed(
            title="Cargo Adicionado",
            description=f"O cargo {role.name} foi adicionado a você!",
            color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label='Arquivados',
                       style=discord.ButtonStyle.primary)
    async def role6_button(self, button: discord.ui.Button,
                           interaction: discord.Interaction):
        role = get(interaction.guild.roles, name="Arquivados")
        await interaction.user.add_roles(role)
        embed = discord.Embed(
            title="Cargo Adicionado",
            description=f"O cargo {role.name} foi adicionado a você!",
            color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)
