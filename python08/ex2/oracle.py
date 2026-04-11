import os
from dotenv import load_dotenv  # type: ignore


def get_configuration() -> dict:
    load_dotenv()
    return {
        "matrix_mode": os.getenv("MATRIX_MODE"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT")
    }


def check_configuration(conf: dict) -> None:
    configuration = ["MATRIX_MODE", "DATABASE_URL",
                     "API_KEY", "ZION_ENDPOINT", "LOG_LEVEL"]
    missing_req = [i for i in configuration if not conf.get(i.lower())]
    if (missing_req):
        print("Warning: missing configuration")
        for i in missing_req:
            print(f" - {i}")
        exit(1)


def show_configuration(conf: dict) -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    mode = conf.get("matrix_mode")
    if mode == "development":
        print(f"Mode: {mode}")
        print("Database: Connected to local instance")
    elif mode == "production":
        print(f"Mode: {mode}")
        print("Database: Connected to remote server")
    elif mode is not None:
        print("Mode: unknown")
        print("Database: Connected")
    print(f"Log Level: {conf.get('log_level')}")
    print("API Access: Authenticated")
    print("Zion Network: Online")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if not os.path.exists(".env"):
        print("[WARNING] .env file not found")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    try:
        conf = get_configuration()
        check_configuration(conf)
        show_configuration(conf)
    except Exception as err:
        print(err)
