# TOKEN: [redacted]
# INVITE LINK (Admin Perms): [redacted]
# HIKARI DOCS: https://www.hikari-py.dev/hikari/index.html

import lightbulb
import miru

# When testing: default_enabled_guilds = ([redacted]) should be added to improve command speeds
bot = lightbulb.BotApp(token = "[redacted]", ignore_bots = True)

miru.load(bot)


bot.load_extensions_from('./commands')

bot.run()
