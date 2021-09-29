from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

# Config для базы данных
host = env.str("host")
database = env.str("database")
user = env.str("user")
password = env.str("password")

# Config для middleware
ban_time = 60
exceeded_count = 3
