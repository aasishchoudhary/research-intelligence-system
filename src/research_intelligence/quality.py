from .models import Claim, ClaimType, Evidence

def unsupported_claims(claims: list[Claim]) -> list[Claim]:
    return [c for c in claims if c.claim_type not in {ClaimType.UNKNOWN, ClaimType.ASSUMPTION} and not c.evidence_ids]

def evidence_coverage(claims: list[Claim]) -> float:
    if not claims:
        return 1.0
    return (len(claims) - len(unsupported_claims(claims))) / len(claims)

def validate_provenance(claims: list[Claim], evidence: list[Evidence]) -> list[str]:
    known = {e.evidence_id for e in evidence}
    errors = []
    for claim in claims:
        for evidence_id in claim.evidence_ids:
            if evidence_id not in known:
                errors.append(f"Claim {claim.claim_id} references missing evidence {evidence_id}")
    return errors
