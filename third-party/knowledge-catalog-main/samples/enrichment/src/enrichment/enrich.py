# Metadata enrichment agent
#

import argparse
import asyncio
import pathlib
import sys
import typing as t

import enrichment.documentation.agent as agent
import enrichment.metadata.catalog as catalog
import enrichment.metadata.snapshot as snapshot


def _create_enrichment_task(table_name: str) -> str:
  info, has_documentation = catalog.lookup_table_info(table_name)

  prompt = [
    f'Table: {table_name}',
    info,
    '',
  ]

  if has_documentation:
    prompt.append('Improve the document using the provided sources.')
  else:
    prompt.append('Generate documnentation using the provided sources.')

  print(prompt)
  return '\n'.join(prompt)


async def main():
  parser = argparse.ArgumentParser(description='Metadata enrichment agent')
  parser.add_argument(
    '--dir',
    required=True,
    help='Directory containing the metadata entries',
  )
  parser.add_argument(
    '--output-dir',
    required=False,
    help='Optional output directory to write updated metadata entries',
  )
  parser.add_argument(
    '--config-dir',
    required=True,
    help='Directory containing instructions.md, mcp.json, skills/',
  )
  args = parser.parse_args()

  metadata_dir = pathlib.Path(args.dir).resolve()
  if not metadata_dir.exists() or not metadata_dir.is_dir():
    print(f'Error: {args.dir} does not exist or is not a directory.')
    sys.exit(1)

  if args.output_dir:
    output_dir = pathlib.Path(args.output_dir).resolve()
    output_dir.mkdir(exist_ok=True, parents=False)
  else:
    output_dir = metadata_dir

  config_dir = pathlib.Path(args.config_dir).resolve()
  if not config_dir.exists() or not config_dir.is_dir():
    print(f'Error: {args.config_dir} does not exist or is not a directory.')
    sys.exit(1)


  def update_table(table_name: str, content: str) -> str:
    '''Updates the documentation content for a table.

    Args:
      table_name: The BigQuery table name in the format 'project_id.dataset_id.table_id'.
      content: The generated documentation content.

    Returns:
      A success message or an error message.
    '''
    try:
      snapshot.update_entry(metadata_dir, output_dir, table_name, content)
      return f'Successfully updated {table_name}'
    except Exception as e:
      return f'Failed to update {table_name}: {e}'


  runner = agent.create_runner('agent', [update_table], config_dir)

  tables = snapshot.list_entries(metadata_dir)
  for table in tables:
    task = _create_enrichment_task(table)
    await agent.run_task(runner, task)


if __name__ == '__main__':
  asyncio.run(main())
