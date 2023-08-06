import sys
import argparse

from cloud9_cli.command import Command
from cloud9_cli import VERSION


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--profile', dest='profile', action='store', default='default',
                        help='use aws credential profile.')
    parser.add_argument('-v', '--version', action='version', version=f'c9-cli v{VERSION}')

    args = parser.parse_args()
    profile = args.profile

    return {'profile': profile}


def main():
    try:
        options = get_arguments()

        Command(options['profile'])

    except KeyboardInterrupt:
        print('Cancelled by user.')
        sys.exit()


if __name__ == '__main__':
    main()
