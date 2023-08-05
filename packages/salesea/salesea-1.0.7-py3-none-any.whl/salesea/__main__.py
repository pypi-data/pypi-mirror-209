import sys

from .config import load_config
from .log import logger
from .utils import out_print


def script_main():
    def print_version():
        import pkg_resources
        out_print(f'salesea {pkg_resources.get_distribution("salesea").version}')

    # 命令行解析
    import argparse
    parser = argparse.ArgumentParser(
        prog='salesea',
        usage='%(prog)s [command] [options]',
        description='This is an Nginx log collection tool.',
        add_help=False
    )
    parser.add_argument(
        '-V', '--version', action='store_true',
        help='Print version and exit'
    )
    parser.add_argument(
        '-h', '--help', action='store_true',
        help='Print this help message and exit'
    )
    parser.add_argument(
        '-g', '--generate', action='store_true',
        help='Generate the configuration file'
    )
    parser.add_argument(
        '-s', '--start', action='store_true',
        help='Start the service'
    )
    parser.add_argument(
        '-c', '--config', type=str, default='salesea.ini',
        help='Specify the configuration file'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Debug mode'
    )

    args = parser.parse_args()

    if args.help:
        print_version()
        parser.print_help()
        sys.exit()

    if args.version:
        print_version()
        sys.exit()

    if args.generate:
        from .config import generate_config
        generate_config()
        sys.exit()

    if args.debug:
        logger.setLevel('DEBUG')

    if args.start:
        load_config(args.config or None)
        from . import launch
        launch()
        sys.exit()

    parser.print_help()
    sys.exit()


def main():
    try:
        script_main()
    except KeyboardInterrupt:
        out_print("\n\nCtrl+C")
