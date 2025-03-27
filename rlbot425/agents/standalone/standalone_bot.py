from typing import TypeAlias

from rlbot425.agents.base_agent import BaseAgent
from rlbot425.utils.bot_runner import BotRunner

StandaloneBot: TypeAlias = BaseAgent


def run_bot(bot_class: type[BaseAgent], default_agent_id: str | None = None):
    """
    Run the bot with the given class.
    """

    runner = BotRunner(bot_class)
    runner.run()
