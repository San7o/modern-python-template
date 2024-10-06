from lib.fibonacci import compute_fibonacci
import logging  # note: not thread-safe
import argparse

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Compute fibonacci numbers.')
parser.add_argument('n', metavar='N', type=int, nargs='+',
                    help='number of fibonacci numbers to compute')


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logger.info('Started')

    args = parser.parse_args()

    logger.info(f"Computing fibonacci numbers for {args.n}")
    print(f"fibonacci numbers: {compute_fibonacci(args.n[0])}")

    logger.info('Finished')


if __name__ == "__main__":
    main()
