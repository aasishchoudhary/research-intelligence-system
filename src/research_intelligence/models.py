from dataclasses import dataclass, field
from enum import Enum
from typing import Tuple

class ClaimType(str, Enum):
    FACT = "FACT"
    CALCULATION = "CALCULATION"
    INTERPRETATION = "INTERPRETATION"
    ASSUMPTION = "ASSUMPTION"
    UNKNOWN = "UNKNOWN"

@dataclass(frozen=True)
class Source:
    source_id: str
    title: str
    publisher: str
    url: str
    published_at: str | None = None

@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    source_id: str
    quote: str
    locator: str

@dataclass(frozen=True)
class Claim:
    claim_id: str
    text: str
    claim_type: ClaimType
    evidence_ids: Tuple[str, ...] = field(default_factory=tuple)
    confidence: float = 0.0

@dataclass(frozen=True)
class ResearchReport:
    title: str
    question: str
    claims: Tuple[Claim, ...]
    sources: Tuple[Source, ...]
    evidence: Tuple[Evidence, ...]
