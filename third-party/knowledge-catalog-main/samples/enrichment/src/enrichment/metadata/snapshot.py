# Catalog metadata snapshot
#

import pathlib
import typing as t
import yaml

import google.cloud.dataplex_v1 as dataplex
import google.protobuf.field_mask_pb2 as field_mask_pb2
import google.protobuf.json_format as jsonpb

import enrichment.util.markdown as markdown


OVERVIEW_ASPECT_RESOURCE = 'projects/dataplex-types/locations/global/aspectTypes/overview'
OVERVIEW_ASPECT_KEY = '655216118709.global.overview'


def _entry_to_md(entry: t.Dict[str, t.Any]) -> t.Tuple[str, str]:
  table_name_parts = entry['entrySource']['resource'].split('/')
  table_name = f'{table_name_parts[1]}.{table_name_parts[3]}.{table_name_parts[5]}'

  aspects = entry.get('aspects', {})
  overview = aspects.get(OVERVIEW_ASPECT_KEY, {}).get('data', {})

  md = [
    f'---',
    f'name: {entry["name"]}',
    f'resource: {entry["entrySource"]["resource"]}',
    f'---',
    f'# {table_name}',
    f'## Overview\n',
    overview.get('content', '')
  ]

  return table_name, '\n'.join(md)


def _md_to_entry(md: str) -> t.Dict[str, t.Any]:
  frontmatter, body = markdown.parse(md)

  overview = ''
  if '## Overview' in body:
    overview = body.split('## Overview', 1)[1].strip()

  return {
    'name': frontmatter['name'],
    'aspects': {
      OVERVIEW_ASPECT_KEY: {
        'aspectType': OVERVIEW_ASPECT_RESOURCE,
        'data': {
          'content': overview,
          'contentType': 'MARKDOWN'
        }
      }
    },
    'entrySource': {
      'resource': frontmatter['resource']
    }
  }


def download_entries(dir: pathlib.Path, dataset: str):
  project_id, dataset_id = dataset.split('.')
  dataset_entry = None
  location_id = ''

  catalog = dataplex.CatalogServiceClient()

  search_entries_response = catalog.search_entries(
    request=dataplex.SearchEntriesRequest(
      name=f'projects/{project_id}/locations/global',
      scope=f'projects/{project_id}',
      query=f'type=dataset name={dataset_id}',
      page_size=1,
      semantic_search=True,
    )
  )
  for result in search_entries_response.results:
    dataset_entry = result.dataplex_entry
    location_id = dataset_entry.entry_source.location

  entry_filter = f'parent_entry="{dataset_entry.name}"'
  entry_group = f'projects/{project_id}/locations/{location_id}/entryGroups/@bigquery'

  list_entries_response = catalog.list_entries(
    request=dataplex.ListEntriesRequest(
      parent=entry_group,
      filter=entry_filter,
    )
  )

  for entry in list_entries_response.entries:
    entry = catalog.get_entry(
      request=dataplex.GetEntryRequest(
        name=entry.name,
        view='CUSTOM',
        aspect_types=[
          OVERVIEW_ASPECT_RESOURCE,
        ],
      )
    )

    table_name, markdown = _entry_to_md(jsonpb.MessageToDict(entry._pb))
    table_path = dir / f'{table_name}.md'
    table_path.write_text(markdown)
    print(f'Downloaded {table_name}')


def publish_entries(dir: pathlib.Path):
  catalog = dataplex.CatalogServiceClient()

  for table_path in dir.glob('*.md'):
    entry_data = _md_to_entry(table_path.read_text())

    updated_entry = dataplex.Entry()
    jsonpb.ParseDict(entry_data, updated_entry._pb, ignore_unknown_fields=True)

    catalog.update_entry(
      request=dataplex.UpdateEntryRequest(
        entry=updated_entry,
        update_mask=field_mask_pb2.FieldMask(paths=['aspects']),
        aspect_keys=[OVERVIEW_ASPECT_KEY],
      )
    )

    print(f'Published {table_path.stem}')


def list_entries(dir: pathlib.Path):
  return [table_path.stem for table_path in dir.glob('*.md')]

def update_entry(dir: pathlib.Path, out_dir: pathlib.Path, table_name: str, content: str):
  table_path = dir / f'{table_name}.md'
  out_table_path = out_dir / f'{table_name}.md'

  entry_data = _md_to_entry(table_path.read_text())
  entry_data['aspects'][OVERVIEW_ASPECT_KEY]['data']['content'] = content

  _, markdown = _entry_to_md(entry_data)
  out_table_path.write_text(markdown)


def show_entry(dir: pathlib.Path, table_name: str):
  table_path = dir / f'{table_name}.md'
  print(table_path.read_text())
