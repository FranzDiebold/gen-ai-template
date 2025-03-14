"""State module for managing agent state."""

from typing import Dict, List

from pydantic import BaseModel


class State(BaseModel):
    """Class representing the state of the agent interaction."""

    messages: List[Dict]
    interrupt_response: str = "example"
