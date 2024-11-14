import enum
from typing import Annotated
from livekit.agents import llm
import logging

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)


class Zone(enum.Enum):
  LIVING_ROOM = "living_room"
  BEDROOM = "bedroom"
  KITCHEN = "kitchen"
  BATHROOM = "bathroom"
  OFFICE = "office"


class AssistantFnc(llm.FunctionContext):
  def __init__(self) -> None:
    super().__init__()

    self._temperature = {
      Zone.LIVING_ROOM: 22,
