"""LLM helper module for data ingesting

This module only serves to unify how LLMs are interfaced with while ingesting rules
automatically. AI is primarily used to clean up ingested data. Manual review should be
used even after ingesting data.
"""

from anthropic import Anthropic
from anthropic.types import ContentBlock
from dataclasses import dataclass
from typing import List
from dotenv import dotenv_values


@dataclass
class LLMResult:
    response: str | None
    thought: List[ContentBlock]


class LLMConnection:

    client: Anthropic
    model: str
    max_tokens: int

    def __init__(self) -> None:
        dotenv_config = dotenv_values(".env")
        if (
            dotenv_config["ANTHROPIC_API_KEY"]
            and dotenv_config["ANTHROPIC_BASE_URL"]
            and dotenv_config["ANTHROPIC_MODEL"]
        ):
            self.client = Anthropic(
                api_key=dotenv_config["ANTHROPIC_API_KEY"],
                base_url=dotenv_config["ANTHROPIC_BASE_URL"],
            )
            self.model = dotenv_config["ANTHROPIC_MODEL"]

            if (
                "ANTHROPIC_MAX_TOKENS" in dotenv_config.keys()
                and dotenv_config["ANTHROPIC_MAX_TOKENS"]
            ):
                self.max_tokens = int(dotenv_config["ANTHROPIC_MAX_TOKENS"])
            else:
                self.max_tokens = 1024

        else:
            raise KeyError(
                "Missing ANTHROPIC_ values from .env, cannot use LLM connection."
            )

    def send_message(self, system_prompt: str, user_prompt: str) -> LLMResult:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        output: str | None = None
        thoughts: List[ContentBlock] = []
        for block in message.content:
            if block.type == "text":
                output = block.text.strip()
            else:
                thoughts.append(block)

        return LLMResult(response=output, thought=thoughts)
