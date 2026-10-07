from dataclasses import dataclass

@dataclass(frozen=True)
class Contradiction:
    left_claim_id: str
    right_claim_id: str
    reason: str

def detect_explicit_contradictions(claims: list[tuple[str, str, str]]) -> list[Contradiction]:
    grouped: dict[str, dict[str, str]] = {}
    for claim_id, topic, polarity in claims:
        grouped.setdefault(topic, {})[polarity] = claim_id
    results = []
    for topic, polarities in grouped.items():
        if "POSITIVE" in polarities and "NEGATIVE" in polarities:
            results.append(Contradiction(polarities["POSITIVE"], polarities["NEGATIVE"], "Opposed supplied polarity"))
    return results
