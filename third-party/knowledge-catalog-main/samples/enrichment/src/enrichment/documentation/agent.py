# Documentation generation agent
#

import pathlib
import textwrap
import typing as t
import uuid

from google.adk.agents.llm_agent import LlmAgent
from google.adk.cli.utils import logs
from google.adk.planners import BuiltInPlanner
from google.adk.runners import InMemoryRunner
from google.genai import types

import enrichment.util.markdown as markdown
from .sources import load_sources_config


def create_runner(name: str, tools: list[t.Any], config_dir: pathlib.Path) -> InMemoryRunner:
  agent_definition = pathlib.Path(__file__).parent / 'agent.md'
  params, instruction = markdown.parse(agent_definition.read_text(encoding='utf-8'))

  planner = None
  if params.get('thinking', False):
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=1024
        )
    )

  instruction, tools = load_sources_config(config_dir, instruction, tools)
  agent = LlmAgent(
      name=name,
      model=params['model'],
      description=params['description'],
      instruction=instruction,
      planner=planner,
      tools=tools,
  )

  return InMemoryRunner(agent=agent, app_name=name)


async def run_task(runner: InMemoryRunner, prompt: str):
  user = str(uuid.uuid4())
  session = await runner.session_service.create_session(
    app_name=runner.app_name, user_id=user
  )

  print('prompt > (text)')
  print(textwrap.shorten(prompt, width=240, placeholder='...'))

  async for event in runner.run_async(
      user_id=user,
      session_id=session.id,
      new_message=types.Content(
        role='user', 
        parts=[types.Part.from_text(text=prompt)]
      )
  ):
    if event.content and event.content.parts:
      for part in event.content.parts:
        if part.thought:
            print(f'{event.author} > (thought)\n' +
                  textwrap.shorten(part.text, width=180, placeholder='...'))
        elif part.text:
          print(f'{event.author} > (text)\n' +
                textwrap.shorten(part.text, width=180, placeholder='...'))
        elif part.function_call:
          args = ', '.join(f'{k}: {v}' for k, v in part.function_call.args.items())
          print(f'{event.author} > (tool {part.function_call.name})\n'
                + textwrap.shorten(args, width=240, placeholder='...'))
        elif part.function_response:
          response = part.function_response.response.get('content')
          if response:
            text = response[0].get('text')
            print(f'tool > {part.function_response.name}\n' +
                  textwrap.shorten(str(text), width=160, placeholder='...'))
