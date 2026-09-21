import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user} | Slash commands synced")

@tree.command(name="ping", description="عرض سرعة البوت")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"🏓 Pong! {round(bot.latency * 1000)}ms")

@tree.command(name="server", description="معلومات السيرفر")
async def server(interaction: discord.Interaction):
    guild = interaction.guild
    if guild is None:
        return await interaction.response.send_message("❌ هذا الأمر داخل السيرفر فقط.")
    await interaction.response.send_message(
        f"🏠 **{guild.name}**\n"
        f"👥 الأعضاء: **{guild.member_count}**\n"
        f"🆔 ID: **{guild.id}**"
    )

@tree.command(name="user", description="معلومات عضو")
@app_commands.describe(member="العضو")
async def user(interaction: discord.Interaction, member: discord.Member | None = None):
    member = member or interaction.user
    await interaction.response.send_message(
        f"👤 **{member.display_name}**\n"
        f"🆔 ID: **{member.id}**\n"
        f"📅 انضم: **{discord.utils.format_dt(member.joined_at, 'D') if member.joined_at else 'غير معروف'}**"
    )

@tree.command(name="avatar", description="عرض صورة العضو")
@app_commands.describe(member="العضو")
async def avatar(interaction: discord.Interaction, member: discord.Member | None = None):
    member = member or interaction.user
    await interaction.response.send_message(member.display_avatar.url)

@tree.command(name="help", description="عرض أوامر البوت")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🤖 **أوامر البوت**\n"
        "`/ping` — سرعة البوت\n"
        "`/server` — معلومات السيرفر\n"
        "`/user` — معلومات عضو\n"
        "`/avatar` — صورة العضو\n"
        "`/help` — قائمة الأوامر"
    )


@tree.command(name="clear", description="حذف رسائل من القناة")
@app_commands.describe(amount="عدد الرسائل")
@app_commands.default_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: app_commands.Range[int, 1, 100]):
    if not interaction.channel or not hasattr(interaction.channel, "purge"):
        return await interaction.response.send_message("❌ لا يمكن استخدام الأمر هنا.", ephemeral=True)
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=amount)
    await interaction.followup.send(f"🧹 تم حذف **{len(deleted)}** رسالة.", ephemeral=True)

@tree.command(name="kick", description="طرد عضو")
@app_commands.describe(member="العضو", reason="السبب")
@app_commands.default_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = "بدون سبب"):
    try:
        await member.kick(reason=reason)
        await interaction.response.send_message(f"👢 تم طرد **{member}**.")
    except discord.Forbidden:
        await interaction.response.send_message("❌ البوت لا يملك صلاحية طرد هذا العضو.", ephemeral=True)

@tree.command(name="ban", description="حظر عضو")
@app_commands.describe(member="العضو", reason="السبب")
@app_commands.default_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = "بدون سبب"):
    try:
        await member.ban(reason=reason)
        await interaction.response.send_message(f"🔨 تم حظر **{member}**.")
    except discord.Forbidden:
        await interaction.response.send_message("❌ البوت لا يملك صلاحية حظر هذا العضو.", ephemeral=True)

@tree.command(name="unban", description="فك حظر عضو بواسطة ID")
@app_commands.describe(user_id="ID العضو")
@app_commands.default_permissions(ban_members=True)
async def unban(interaction: discord.Interaction, user_id: str):
    try:
        user = await bot.fetch_user(int(user_id))
        await interaction.guild.unban(user)
        await interaction.response.send_message(f"🔓 تم فك الحظر عن **{user}**.")
    except (ValueError, discord.NotFound, discord.Forbidden):
        await interaction.response.send_message("❌ تعذر فك الحظر. تأكد من الـ ID والصلاحيات.", ephemeral=True)

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN غير موجود في ملف .env")

bot.run(TOKEN)
