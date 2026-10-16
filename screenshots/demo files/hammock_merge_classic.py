"""A calm little module to showcase the Relaxed theme."""

import asyncio
import re

<<<<<<< HEAD
API_URL = "https://api.example.com/v2/hammocks"
DEFAULT_LIMIT = 10
=======
API_URL = "https://hammocks.example.org/api"
DEFAULT_LIMIT = 25
TIMEOUT_SECONDS = 3.5
>>>>>>> feature/gentle-swing
SLUG_PATTERN = re.compile(r"^[a-z0-9-]+$", re.IGNORECASE)


class Hammock:
    def __init__(self, id: int, label: str, swinging: bool = False) -> None:
        self.id = id
        self.label = label
        self.swinging = swinging

    def __repr__(self) -> str:
<<<<<<< HEAD
        return f"Hammock(id={self.id}, label={self.label!r})"
=======
        state = "swinging" if self.swinging else "resting"
        return f"<Hammock #{self.id:03} {self.label} ({state})>"
>>>>>>> feature/gentle-swing


async def fetch_hammocks(limit: int = DEFAULT_LIMIT) -> list[Hammock]:
    """Fetch hammocks, gently."""
    if limit <= 0:
        raise ValueError(f"limit must be positive, got {limit}")
    await asyncio.sleep(0.5)
    return [Hammock(i, f"hammock-{i}", swinging=i % 2 == 0) for i in range(limit)]


if __name__ == "__main__":
    print(asyncio.run(fetch_hammocks()))
