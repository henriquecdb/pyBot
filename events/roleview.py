import discord
from discord.utils import get


async def add_or_remove_role(button: discord.ui.Button, interaction: discord.Interaction, role_name: str):
    role = get(interaction.guild.roles, name=role_name)
    if role in interaction.user.roles:
        await interaction.user.remove_roles(role)
        embed = discord.Embed(
            title="Cargo Removido",
            description=f"O cargo {role.name} foi removido de você!",
            color=0xff0000)
    else:
        await interaction.user.add_roles(role)
        embed = discord.Embed(
            title="Cargo Adicionado",
            description=f"O cargo {role.name} foi adicionado a você!",
            color=0x00ff00)
    await interaction.response.send_message(embed=embed, ephemeral=True)


class RoleView(discord.ui.View):

    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Núcleo Project Reality', style=discord.ButtonStyle.primary)
    async def role1_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await add_or_remove_role(button, interaction, "Núcleo Project Reality")

    @discord.ui.button(label='Núcleo de Squad', style=discord.ButtonStyle.primary)
    async def role2_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await add_or_remove_role(button, interaction, "Núcleo Squad")

    @discord.ui.button(label='Núcleo de Foxhole', style=discord.ButtonStyle.primary)
    async def role3_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await add_or_remove_role(button, interaction, "Foxhole: Público")

    @discord.ui.button(label='Núcleo de ArmA III', style=discord.ButtonStyle.primary)
    async def role4_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await add_or_remove_role(button, interaction, "Núcleo ArmA 3")

    @discord.ui.button(label='Central Estudantil', style=discord.ButtonStyle.primary)
    async def role5_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await add_or_remove_role(button, interaction, "Central Estudantil")

    @discord.ui.button(label='Arquivados', style=discord.ButtonStyle.primary)
    async def role6_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await add_or_remove_role(button, interaction, "Arquivados")
