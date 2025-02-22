"""State module for managing agent state."""

from pydantic import BaseModel


class State(BaseModel):
    """Class representing the state of the agent interaction."""

    interrupt_response: str = "example"
