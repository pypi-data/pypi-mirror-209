import argparse
import os

from zoterotex._sync import sync


def main():
    args = get_args()
    sync(**vars(args))


def get_args():
    parser = argparse.ArgumentParser("zoterotex")
    parser.add_argument("action", choices=("sync",),
                        help="The action to take (e.g. sync).")
    parser.add_argument("library_type", choices=("user", "group"),
                        help="Whether you're syncing with your user library or a group library.")
    parser.add_argument("library_id",
                        help="The ID of the library you're syncing with.")
    parser.add_argument("out_file",
                        help="A file to write the results.")
    parser.add_argument("--api-key", default=os.environ.get("ZOTERO_API_KEY", None),
                        help="The API key ()")
    parser.add_argument("--log-level", choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"), default="INFO")
    return parser.parse_args()


if __name__ == '__main__':
    main()
