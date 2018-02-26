#!/usr/bin/env python
import os
import argparse

from core import (
    logger,
    settings
)


class MainApp():
    def run(self):
        logger.info("main.test = %s" % settings.get('main', 'test'))


if __name__ == '__main__':
    def parse_args():
        def extant_file(x):
            if not os.path.exists(x):
                raise argparse.ArgumentTypeError(
                    "File {0} does not exist".format(x)
                )
            return x

        default_config = os.path.join(
            os.path.abspath(os.path.join(__file__, os.pardir, 'config.ini')))

        parser = argparse.ArgumentParser(
            formatter_class=lambda prog: argparse.HelpFormatter(
                prog, max_help_position=40))
        parser.add_argument(
            "-c", "--config", help="config file", required=False,
            type=extant_file, metavar="config.ini", default=default_config)
        return parser, parser.parse_args()

    parser, args = parse_args()
    settings.init(args.config)
    try:
        app = MainApp()
        app.run()
    except KeyboardInterrupt:
        pass
