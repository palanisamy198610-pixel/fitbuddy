import os


class Config:
    # Flask secret key
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "skillwallet-secret-key"
    )

    # MySQL Database Configuration
    MYSQL_HOST = os.environ.get(
        "MYSQL_HOST",
        "localhost"
    )

    MYSQL_USER = os.environ.get(
        "MYSQL_USER",
        "root"
    )

    MYSQL_PASSWORD = os.environ.get(
        "MYSQL_PASSWORD",
        ""
    )

    MYSQL_DATABASE = os.environ.get(
        "MYSQL_DATABASE",
        "skillwallet"
    )

    MYSQL_PORT = int(
        os.environ.get(
            "MYSQL_PORT",
            3306
        )
    )

    # Application settings
    APP_NAME = "SkillWallet"
    FIDBUDDY_NAME = "FidBuddy"
    DEBUG = True
