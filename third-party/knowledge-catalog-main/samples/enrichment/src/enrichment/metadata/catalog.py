# Catalog service
#

import typing as t

import google.cloud.dataplex_v1 as dataplex
import google.protobuf.json_format as jsonpb


SCHEMA_ASPECT_RESOURCE = 'projects/dataplex-types/locations/global/aspectTypes/schema'
SCHEMA_ASPECT_KEY = '655216118709.global.schema'

DESCRIPTIONS_ASPECT_RESOURCE = 'projects/dataplex-types/locations/global/aspectTypes/descriptions'
DESCRIPTIONS_ASPECT_KEY = '655216118709.global.descriptions'

OVERVIEW_ASPECT_RESOURCE = 'projects/dataplex-types/locations/global/aspectTypes/overview'
OVERVIEW_ASPECT_KEY = '655216118709.global.overview'


def _format_description(source_desc, catalog_desc: str, blank_ok: bool=True) -> str:
  desc = source_desc + ';' + catalog_desc
  desc = desc.strip(';')

  if desc or blank_ok:
    return desc
  return 'no existing description'


def _format_schema(schema: t.Dict[str, t.Any], descriptions: t.Dict[str, t.Any]) -> str:
  all_fields = []
  field_stack = []

  def push_fields(prefix: str, fields: t.List[t.Any], descs: t.List[t.Any]):
    descs_map = {f['name']: f for _, f in enumerate(descs)}

    for f in reversed(fields):
      name = f['name']
      desc = f.get('description', '') + ';' + descs_map.get(name, {}).get('description', '')
      desc = desc.strip(';')

      field_stack.append({
        'p': prefix,
        'n': name,
        't': f['dataType'],
        'd': desc,
        'sf': f.get('fields', None),
        'sd': descs_map.get(name, {}).get('fields', [])
      })

  push_fields('', schema.get('fields', []), descriptions.get('fields', []))
  while (field_stack):
    f = field_stack.pop()
    all_fields.append(f'* {f["p"]}{f["n"]} ({f["t"]}) {f["d"]}')

    if (f['sf']):
      push_fields(f['p'] + f['n'] + '.', f['sf'], f['sd'])

  all_fields.append('')
  return '\n'.join(all_fields)


def lookup_table_info(table_name: str) -> t.Tuple[str, bool]:
  project_id, dataset_id, table_id = table_name.split('.')
  catalog = dataplex.CatalogServiceClient()

  search_entries_response = catalog.search_entries(
    request=dataplex.SearchEntriesRequest(
      name=f'projects/{project_id}/locations/global',
      scope=f'projects/{project_id}',
      query=f'type=table system=bigquery dataset={dataset_id} name={table_id}',
      page_size=1,
      semantic_search=True,
    )
  )

  table_entry = search_entries_response.results[0].dataplex_entry
  table_entry = catalog.get_entry(
    request=dataplex.GetEntryRequest(
      name=table_entry.name,
      view='CUSTOM',
      aspect_types=[
        SCHEMA_ASPECT_RESOURCE,
        DESCRIPTIONS_ASPECT_RESOURCE,
        OVERVIEW_ASPECT_RESOURCE,
      ],
    )
  )
  table_info = jsonpb.MessageToDict(table_entry._pb)
  aspects = table_info.get('aspects', {})
  schema = aspects.get(SCHEMA_ASPECT_KEY, {}).get('data', {})
  descriptions = aspects.get(DESCRIPTIONS_ASPECT_KEY, {}).get('data', {})
  overview = aspects.get(OVERVIEW_ASPECT_KEY, {}).get('data', {})

  documentation = overview.get('content', '')
  has_documentation = not not documentation

  context = [
    _format_description(
      table_info['entrySource'].get('description', ''),
      descriptions.get('description', ''),
      blank_ok=False),
    '',
    'Schema:',
    '',
    _format_schema(schema, descriptions),
    '',
    'Documentation:',
    documentation if has_documentation else 'mo existing documentation',
  ]
  return '\n'.join(context), has_documentation
