"""A collection of tools used by the Knowledge Catalog Search Agent."""

import logging
import os

from google.api_core.exceptions import PermissionDenied
from google.cloud import dataplex_v1

from .utils import get_consumer_project


def knowledge_catalog_search(
    query: str,
) -> dict[str, list[str] | str]:
  """Searches Knowledge Catalog using Semantic Search capabilities.

  Args:
      query: The natural language search query.

  Returns:
      A dictionary containing a list of entries along with their metadata
      or an error message. For example, {'results': [{'entry_name': 'entry1',
      'system': 'BIGQUERY', ...}]}.
  """
  try:
    consumer_project_id = get_consumer_project()
  except ValueError as e:
    return {"Error obtaining consumer project": str(e)}

  try:
    endpoint = "dataplex.googleapis.com"

    client = dataplex_v1.CatalogServiceClient(
        client_options={"api_endpoint": endpoint}
    )

    parent_name = f"projects/{consumer_project_id}/locations/global"
    response = client.search_entries(
        request={
            "name": parent_name,
            "query": query,
            "page_size": 50,
            "semantic_search": True,
        }
    )

    entries = [
        {
            "entry_name": result.dataplex_entry.name,
            "system": result.dataplex_entry.entry_source.system,
            "resource_id": result.dataplex_entry.entry_source.resource,
            "display_name": result.dataplex_entry.entry_source.display_name,
        }
        for result in response.results
    ]

    return {"results": entries}

  except PermissionDenied:
    logging.warning("Knowledge Catalog search failed due to permission error")
    return {
        "error": (
            "Permission denied: The user does not have permission to call"
            " Knowledge Catalog Search."
        )
    }
  except Exception as e:  # pylint: disable=broad-except
    logging.exception(
        "An unexpected error occurred during Knowledge Catalog search"
    )
    return {"error": f"An unexpected error occurred: {e}"}
