# Metadata publishing tool
#

import argparse
import pathlib
import sys

import enrichment.metadata.snapshot as snapshot


def main():
  parser = argparse.ArgumentParser(description='Publish metadata to the Catalog')
  parser.add_argument(
    '--dir',
    required=True,
    help='The directory containing the metadata to publish.',
  )
  args = parser.parse_args()

  dir = pathlib.Path(args.dir).resolve()
  if not dir.exists() or not dir.is_dir():
    print(f'Directory {dir} does not exist.')
    sys.exit(1)

  snapshot.publish_entries(dir)


if __name__ == '__main__':
  main()
