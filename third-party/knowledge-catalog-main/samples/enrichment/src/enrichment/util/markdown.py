# Markdown Helpers
#

import typing as t
import yaml


def parse(md: str) -> t.Tuple[t.Dict[str, t.Any], str]:
  frontmatter = {}
  body = md

  if md.startswith('---\n'):
    parts = md.split('---\n', 2)
    if len(parts) >= 3:
      frontmatter = yaml.safe_load(parts[1]) or {}
      body = parts[2]

  return frontmatter, body
