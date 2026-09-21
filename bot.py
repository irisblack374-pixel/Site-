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
    print(f"Logged in as {bot.user}")

@bot.event
async def on_connect():
    if not getattr(bot, "_commands_synced", False):
        await tree.sync()
        bot._commands_synced = True
        print("Slash commands synced")

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
        "`/help` — قائمة الأوامر\n"
        "`/clear` — حذف رسائل\n"
        "`/kick` — طرد عضو\n"
        "`/ban` — حظر عضو\n"
        "`/unban` — فك حظر بواسطة ID"
    )


@tree.command(name="clear", description="حذف رسائل من القناة")
@app_commands.describe(amount="عدد الرسائل")
@app_commands.default_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: app_commands.Range[int, 1, 100]):
    if interaction.guild is None:
        return await interaction.response.send_message(
            "❌ هذا الأمر داخل السيرفر فقط.", ephemeral=True
        )
    if not interaction.channel or not hasattr(interaction.channel, "purge"):
        return await interaction.response.send_message(
            "❌ لا يمكن استخدام الأمر هنا.", ephemeral=True
        )

    me = interaction.guild.me
    if me is None or not me.guild_permissions.manage_messages:
        return await interaction.response.send_message(
            "❌ البوت لا يملك صلاحية **Manage Messages**.", ephemeral=True
        )

    await interaction.response.defer(ephemeral=True)
    try:
        deleted = await interaction.channel.purge(limit=amount)
    except discord.Forbidden:
        return await interaction.followup.send(
            "❌ تعذر حذف الرسائل. تحقق من صلاحيات البوت.", ephemeral=True
        )
    except discord.HTTPException:
        return await interaction.followup.send(
            "❌ حدث خطأ من Discord أثناء حذف الرسائل.", ephemeral=True
        )

    await interaction.followup.send(
        f"🧹 تم حذف **{len(deleted)}** رسالة.", ephemeral=True
    )

@tree.command(name="kick", description="طرد عضو")
@app_commands.describe(member="العضو", reason="السبب")
@app_commands.default_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = "بدون سبب"):
    if interaction.guild is None:
        return await interaction.response.send_message(
            "❌ هذا الأمر داخل السيرفر فقط.", ephemeral=True
        )

    me = interaction.guild.me
    if member == interaction.guild.owner:
        return await interaction.response.send_message(
            "❌ لا يمكن طرد مالك السيرفر.", ephemeral=True
        )
    if me is None or not me.guild_permissions.kick_members:
        return await interaction.response.send_message(
            "❌ البوت لا يملك صلاحية **Kick Members**.", ephemeral=True
        )
    if member >= me:
        return await interaction.response.send_message(
            "❌ لا يمكن للبوت طرد عضو رتبته أعلى من رتبته أو مساوية لها.",
            ephemeral=True,
        )

    try:
        await member.kick(reason=reason)
        await interaction.response.send_message(f"👢 تم طرد **{member}**.")
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ تعذر طرد العضو. تحقق من الصلاحيات وترتيب الرتب.",
            ephemeral=True,
        )
    except discord.HTTPException:
        await interaction.response.send_message(
            "❌ حدث خطأ من Discord أثناء تنفيذ الطرد.", ephemeral=True
        )

@tree.command(name="ban", description="حظر عضو")
@app_commands.describe(member="العضو", reason="السبب")
@app_commands.default_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = "بدون سبب"):
    if interaction.guild is None:
        return await interaction.response.send_message(
            "❌ هذا الأمر داخل السيرفر فقط.", ephemeral=True
        )

    me = interaction.guild.me
    if member == interaction.guild.owner:
        return await interaction.response.send_message(
            "❌ لا يمكن حظر مالك السيرفر.", ephemeral=True
        )
    if me is None or not me.guild_permissions.ban_members:
        return await interaction.response.send_message(
            "❌ البوت لا يملك صلاحية **Ban Members**.", ephemeral=True
        )
    if member >= me:
        return await interaction.response.send_message(
            "❌ لا يمكن للبوت حظر عضو رتبته أعلى من رتبته أو مساوية لها.",
            ephemeral=True,
        )

    try:
        await member.ban(reason=reason)
        await interaction.response.send_message(f"🔨 تم حظر **{member}**.")
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ تعذر حظر العضو. تحقق من الصلاحيات وترتيب الرتب.",
            ephemeral=True,
        )
    except discord.HTTPException:
        await interaction.response.send_message(
            "❌ حدث خطأ من Discord أثناء تنفيذ الحظر.", ephemeral=True
        )

@tree.command(name="unban", description="فك حظر عضو بواسطة ID")
@app_commands.describe(user_id="ID العضو")
@app_commands.default_permissions(ban_members=True)
async def unban(interaction: discord.Interaction, user_id: str):
    if interaction.guild is None:
        return await interaction.response.send_message(
            "❌ هذا الأمر داخل السيرفر فقط.", ephemeral=True
        )

    me = interaction.guild.me
    if me is None or not me.guild_permissions.ban_members:
        return await interaction.response.send_message(
            "❌ البوت لا يملك صلاحية **Ban Members**.", ephemeral=True
        )

    try:
        user = await bot.fetch_user(int(user_id))
    except (ValueError, discord.NotFound):
        return await interaction.response.send_message(
            "❌ الـ ID غير صحيح أو المستخدم غير موجود.", ephemeral=True
        )
    except discord.HTTPException:
        return await interaction.response.send_message(
            "❌ تعذر الوصول إلى بيانات المستخدم من Discord.", ephemeral=True
        )

    try:
        await interaction.guild.unban(user, reason=f"Unbanned by {interaction.user}")
        await interaction.response.send_message(f"🔓 تم فك الحظر عن **{user}**.")
    except discord.NotFound:
        await interaction.response.send_message(
            "❌ هذا المستخدم غير محظور في السيرفر.", ephemeral=True
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ البوت لا يملك صلاحية فك الحظر.", ephemeral=True
        )
    except discord.HTTPException:
        await interaction.response.send_message(
            "❌ حدث خطأ من Discord أثناء فك الحظر.", ephemeral=True
        )

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN غير موجود في ملف .env")

bot.run(TOKEN)
