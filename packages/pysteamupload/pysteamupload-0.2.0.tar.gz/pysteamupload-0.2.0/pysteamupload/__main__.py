import os
import sys
import argparse
import platform
from loguru import logger
from dotenv import load_dotenv
from pysteamupload.linux_pysteamupload import LinuxPySteamUpload
from pysteamupload.windows_pysteamupload import WindowsPySteamUpload


def parse_argv() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PySteamUpload")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("initialize_only", help="Initialize only")
    upload_parser = subparsers.add_parser("upload", help="Upload")

    upload_parser.add_argument("--app_id", help="specify which APPLICATION is being targeted", type=int, required=True)
    upload_parser.add_argument("--depot_id", help="specify which DEPOT is being targeted", type=int, required=True)
    upload_parser.add_argument("--build_description", help="specify a build DESCRIPTION", required=True)
    upload_parser.add_argument("--content_path", help="specify which CONTENT local directory should be uploaded", required=True)
    return parser.parse_args()


def check_required_variables() -> None:
    required_env_vars = (
        "STEAM_USERNAME",
        "STEAM_PASSWORD",
    )
    missing_keys = []
    for key in required_env_vars:
        if key not in os.environ:
            missing_keys.append(key)
    if missing_keys:
        raise KeyError(f"Missing environment variables {missing_keys}")


def main() -> None:
    load_dotenv()
    check_required_variables()

    operating_system: str = platform.system().lower()
    if operating_system == "windows":
        ps = WindowsPySteamUpload()
    elif operating_system == "linux":
        ps = LinuxPySteamUpload()
    else:
        raise RuntimeError(f"Unsupported operating system [{operating_system}]")

    args: argparse.Namespace = parse_argv()
    exit_code = 1
    if args.command == "initialize_only":
        exit_code: int = ps.initialize_only()
    elif args.command == "upload":
        exit_code: int = ps.upload(
            app_id=args.app_id,
            depot_id=args.depot_id,
            build_description=args.build_description,
            content_path=args.content_path,
        )
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
