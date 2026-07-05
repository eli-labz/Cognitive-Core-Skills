# Metadata download tool
#

import argparse
import pathlib

import enrichment.metadata.snapshot as snapshot


def main():
  parser = argparse.ArgumentParser(description='Download metadata from the Catalog')
  parser.add_argument(
    '--dataset',
    required=True,
    help='The dataset to download metadata for.',
  )
  parser.add_argument(
    '--dir',
    required=True,
    help='The directory to save the metadata into.',
  )
  args = parser.parse_args()

  dir = pathlib.Path(args.dir)
  dir.mkdir(parents=True, exist_ok=True)

  snapshot.download_entries(dir, args.dataset)


if __name__ == '__main__':
  main()
