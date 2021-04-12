import os
import sys
from pathlib import Path

from dotenv import load_dotenv

env_path = Path() / '.env'
load_dotenv(dotenv_path=env_path)


def get_env_value(env_variable, def_value):
    try:
        print(env_variable, os.environ[env_variable])
        return os.environ[env_variable]
    except KeyError as e:
        print(e)
        return def_value


APP_DB_NAME = get_env_value('APP_DB_NAME', "")
APP_DB_USER = get_env_value('APP_DB_USER', "")
APP_DB_PASS = get_env_value('APP_DB_PASS', "")
APP_DB_HOST = get_env_value('APP_DB_HOST', "")
APP_DB_PORT = get_env_value('APP_DB_PORT', "")
APP_VK_TOKEN = get_env_value('APP_VK_TOKEN', "")
