# User provided information sources
#

import json
import os
import pathlib
import typing as t

from google.adk.code_executors.unsafe_local_code_executor import UnsafeLocalCodeExecutor
from google.adk.skills import load_skill_from_dir
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.skill_toolset import SkillToolset
from mcp import StdioServerParameters


def _load_mcp_toolsets(mcp_config: pathlib.Path) -> list[McpToolset]:
  try:
    with open(mcp_config, 'r') as f:
      config = json.load(f)
  except json.JSONDecodeError:
    return []

  toolsets = []
  mcp_servers = config.get('mcpServers', {})
  for name, server_config in mcp_servers.items():
    if 'command' in server_config:
      command = os.path.expandvars(server_config['command'])
      args = [os.path.expandvars(a) for a in server_config.get('args', [])]
      env = server_config.get('env')
      timeout = server_config.get('timeout', 30.0)

      toolsets.append(McpToolset(
          connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
              command=command, args=args, env=env
            ),
            timeout=timeout,
          )
        )
      )
    elif 'httpUrl' in server_config:
      url = server_config['httpUrl']
      timeout = server_config.get('timeout', 30.0)

      toolsets.append(McpToolset(
          connection_params=StreamableHTTPConnectionParams(
            url=url,
            timeout=timeout,
          )
        )
      )
  return toolsets


def _load_skills(skills_dir: pathlib.Path) -> SkillToolset | None:
  skills = []
  for skill_path in skills_dir.iterdir():
    if skill_path.is_dir():
      try:
        skills.append(load_skill_from_dir(skill_path))
      except Exception as e:
        pass

  if not skills:
    return []

  # WARNING: UnsafeLocalCodeExecutor has security concerns and should NOT
  # be used in production environments.
  return SkillToolset(skills=skills, code_executor=UnsafeLocalCodeExecutor())


def load_sources_config(dir: pathlib.Path, instruction: str, tools: t.List[t.Any]) -> t.Tuple[str, t.List[t.Any]]:
  custom_instructions = dir / 'instructions.md'
  if custom_instructions.exists():
    instruction = instruction.format(
      user_instruction=custom_instructions.read_text(encoding='utf-8'))

  tools = tools.copy()

  mcp_config = dir / 'mcp.json'
  if mcp_config.exists() and mcp_config.is_file():
    mcp_toolsets = _load_mcp_toolsets(mcp_config)
    if mcp_toolsets:
      tools.extend(mcp_toolsets)

  skills_dir = dir / 'skills'
  if skills_dir.exists() and skills_dir.is_dir():
    skills_toolset = _load_skills(skills_dir)
    if skills_toolset:
      tools.append(skills_toolset)

  return instruction, tools
