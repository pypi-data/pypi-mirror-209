import argparse
import logging

from .main import main


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task')
    parser.add_argument('--date', help='YYYYMMDD')

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info(args)

    main(args.task, args.date)
