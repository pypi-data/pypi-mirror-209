@_bot.event
async def on_slash_command_error(ctx: disnake.ApplicationCommandInteraction, error: Exception) -> None:
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.response.send_message("I don't have permissions to run this command.")

@_bot.event
async def on_reaction_add(reaction, user):
    try:

        await log_reaction(reaction, user, type='Sent')
    except:
        pass

@_bot.event
async def on_reaction_remove(reaction, user):
    try:
        await log_reaction(reaction, user, type='Deleted')
    except:
        pass