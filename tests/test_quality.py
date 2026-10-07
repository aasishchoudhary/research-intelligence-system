from research_intelligence.models import Claim, ClaimType
from research_intelligence.quality import evidence_coverage, unsupported_claims, validate_provenance

def test_supported_claim_has_full_coverage():
    claim = Claim("C1", "supported", ClaimType.FACT, ("E1",))
    assert evidence_coverage([claim]) == 1.0
    assert unsupported_claims([claim]) == []

def test_unsupported_fact_is_flagged():
    claim = Claim("C1", "unsupported", ClaimType.FACT)
    assert evidence_coverage([claim]) == 0.0
    assert unsupported_claims([claim]) == [claim]

def test_missing_evidence_reference_is_detected():
    claim = Claim("C1", "broken", ClaimType.FACT, ("MISSING",))
    assert validate_provenance([claim], []) == ["Claim C1 references missing evidence MISSING"]
