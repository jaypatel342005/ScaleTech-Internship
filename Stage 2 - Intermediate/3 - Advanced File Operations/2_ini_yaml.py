import configparser
import yaml
import os

DIR = os.path.dirname(os.path.abspath(__file__))

# ---- INI (configparser) ----

# create ini file
config = configparser.ConfigParser()

config["database"] = {
    "host": "localhost",
    "port": "5432",
    "username": "admin"
}

config["application"] = {
    "name": "StudentApp",
    "debug": "true"
}

with open(os.path.join(DIR, "config.ini"), "w") as f:
    config.write(f)


# read ini file
config = configparser.ConfigParser()
config.read(os.path.join(DIR, "config.ini"))

# access values
print(config["database"]["host"])
print(config["database"]["port"])
print(config["application"]["name"])

# ini values are strings by default, use getint/getboolean
port = config["database"].getint("port")
debug = config["application"].getboolean("debug")
print(port, type(port))
print(debug, type(debug))

# list sections
print(config.sections())


# ---- YAML ----

# create yaml file
app_config = {
    "app": {
        "name": "StudentApp",
        "version": 1.0,
        "debug": True
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "developers": ["Jay", "Rahul", "Amit"],
    "features": {
        "authentication": True,
        "logging": True
    }
}

with open(os.path.join(DIR, "config.yaml"), "w") as f:
    yaml.safe_dump(app_config, f, sort_keys=False)


# read yaml file
with open(os.path.join(DIR, "config.yaml"), "r") as f:
    config = yaml.safe_load(f)

print(config)

# access values
print(config["app"]["name"])
print(config["database"]["host"])
print(config["database"]["port"])
print(config["database"]["credentials"]["username"])
print(config["features"]["authentication"])

# yaml list
for dev in config["developers"]:
    print(dev)


# real internship example - config-driven setup
with open(os.path.join(DIR, "config.yaml"), "r") as f:
    cfg = yaml.safe_load(f)

APP_NAME = cfg["app"]["name"]
DEBUG = cfg["app"]["debug"]
DB_HOST = cfg["database"]["host"]
DB_PORT = cfg["database"]["port"]

print(f"starting {APP_NAME} | debug={DEBUG}")
print(f"db: {DB_HOST}:{DB_PORT}")


# environment variables for secrets (never hardcode secrets)
# os.environ["DB_PASSWORD"] = "secret"  # set by OS/deployment
db_password = os.getenv("DB_PASSWORD", "not_set")
print(f"db password: {db_password}")
