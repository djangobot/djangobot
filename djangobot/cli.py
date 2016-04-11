import argparse
import importlib
import os
import sys

from .client import Client


class CLI(object):
    """
    Main command-line interface
    """

    def __init__(self):
        description = 'Slack bridge to a channels-based Django app'
        self.parser = argparse.ArgumentParser(
            description=description
        )
        self.parser.add_argument(
            '-t',
            '--token',
            dest='token',
            help='Slack API token',
            default=os.environ.get('DJANGOBOT_TOKEN', None),
        )
        self.parser.add_argument(
            'channel_layer',
            help='ASGI channel layer instance to listen on given as path.to.module:layer',
        )

    @classmethod
    def entry(cls):
        """
        External starting point
        """
        cls().run(sys.argv[1:])

    def run(self, args):
        """
        Pass in raw arguments, instantiate Slack API and begin client.
        """
        args = self.parser.parse_args(args)
        if not args.token:
            raise ValueError('Supply the slack token through --token or setting DJANGOBOT_TOKEN')

        # Import the channel layer
        sys.path.insert(0, ".")
        module_path, object_path = args.channel_layer.split(':', 1)
        channel_layer = importlib.import_module(module_path)
        for part in object_path.split('.'):
            channel_layer = getattr(channel_layer, part)

        # Boot up the client
        Client(
            channel_layer=channel_layer,
            token=args.token,
        ).run()

