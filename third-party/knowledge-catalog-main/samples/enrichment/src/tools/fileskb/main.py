# MCP tools for a simple file-system based knowledge-base
#

import argparse
import os
import pathlib
import re
import sys
import typing as t
from mcp.server.fastmcp import FastMCP


mcp = FastMCP('fileskb')
KB_ROOT = pathlib.Path('.').resolve()


def _safe_path(path: str) -> pathlib.Path:
  '''Ensure the path is within the KB_ROOT to prevent directory traversal.
  '''
  clean_path = path.lstrip('/')
  full_path = (KB_ROOT / clean_path).resolve()
  if not str(full_path).startswith(str(KB_ROOT)):
    raise ValueError(f'Access denied: Path "{path}" is outside the knowledge base root.')
  return full_path


@mcp.tool(name='list')
def list_contents(path: str = '') -> str:
  '''List the contents of a directory in the knowledge base.
  
  Args:
    path: Optional relative path within the knowledge base to list.
  '''
  target_dir = _safe_path(path)
  if not target_dir or not target_dir.exists() or not target_dir.is_dir():
    return f'Path not found or is not a directory: {path}'

  lines = []
  for item in target_dir.iterdir():
    item_type = 'directory' if item.is_dir() else 'file'
    item_path = str(item.relative_to(KB_ROOT))
    lines.append(f'{item.name} | {item_path} | {item_type}')
  return '\n'.join(lines)


@mcp.tool(name='read')
def read_file(path: str) -> str:
  '''Read the contents of a file in the knowledge base.
  
  Args:
    path: Relative path to the file.
  '''
  target_file = _safe_path(path)
  if not target_file or not target_file.exists() or not target_file.is_file():
    return f'Path not found or is not a file: {path}'

  with open(target_file, 'r', encoding='utf-8') as f:
    return f.read()


@mcp.tool(name='search')
def search_content(query: str, path: str = '') -> t.List[t.Dict[str, t.Any]]:
  '''Search for a text query (regex supported) within markdown files.
  
  Args:
    query: The search string or regular expression.
    path: Optional relative path to restrict the search to a subdirectory or file.
  '''
  target_path = _safe_path(path)
  if not target_path or not target_path.exists():
    return f'Path not found: {path}'

  results = []
  try:
    pattern = re.compile(query, re.IGNORECASE)
  except re.error as e:
    return f'Invalid query: {e}'

  files_to_search = []
  if target_path.is_file():
    if target_path.suffix == '.md':
      files_to_search = [target_path]
  else:
    for root, _, files in os.walk(target_path):
      for file in files:
        if file.endswith('.md'):
          files_to_search.append(pathlib.Path(root) / file)

  for file_path in files_to_search:
    try:
      with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
          if pattern.search(line):
            results.append({
              'file': str(file_path.relative_to(KB_ROOT)),
              'line': line_num,
              'content': line.strip()
            })
    except Exception:
      continue

  return results


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='FileKB MCP Server')
  parser.add_argument(
    '--dir',
    required=True,
    help='Root directory for the knowledge base')
  args, unknown = parser.parse_known_args()

  KB_ROOT = pathlib.Path(args.dir).resolve()
  if not KB_ROOT.exists() or not KB_ROOT.is_dir():
    print(
      f'Error: Root directory "{KB_ROOT}" does not exist or is not a directory.',
      file=sys.stderr
    )
    sys.exit(1)

  mcp.run()
