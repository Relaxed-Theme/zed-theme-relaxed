"""A calm little module to showcase the Relaxed theme."""

from __future__ import annotations

import asyncio
import re
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache

API_URL = "https://api.example.com/hammocks"
SLUG_PATTERN = re.compile(r"^[a-z0-9-]+$", re.IGNORECASE)


class Mood(Enum):
    CHILL = "chill"
    SLEEPY = "sleepy"
    FOCUSED = "focused"


@dataclass(frozen=True)
class Hammock:
    id: int
    label: str
    mood: Mood = Mood.CHILL
    tags: list[str] = field(default_factory=list)
    swinging: bool = False

    @property
    def is_valid(self) -> bool:
        return bool(SLUG_PATTERN.match(self.label))


@lru_cache(maxsize=128)
def describe(mood: Mood) -> str:
    match mood:
        case Mood.CHILL:
            return "Taking it easy"
        case Mood.SLEEPY:
            return "Almost asleep"
        case _:
            return "In the zone"


async def fetch_hammocks(limit: int = 10) -> list[Hammock]:
    await asyncio.sleep(0.5)  # pretend we are calling {API_URL}
    return [
        Hammock(id=i, label=f"hammock-{i}", swinging=i % 2 == 0)
        for i in range(limit)
    ]


async def main() -> None:
    hammocks = await fetch_hammocks(limit=5)
    swinging = [h for h in hammocks if h.swinging and h.is_valid]

    for hammock in swinging:
        print(f"{hammock.label:<12} {describe(hammock.mood)!r}")

    ratio = len(swinging) / len(hammocks)
    print(f"{len(swinging)}/{len(hammocks)} swinging ({ratio:.0%})")


if __name__ == "__main__":
    asyncio.run(main())
