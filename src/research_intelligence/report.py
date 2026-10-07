from .models import ResearchReport
from .quality import evidence_coverage, unsupported_claims

def render_markdown(report: ResearchReport) -> str:
    claims = list(report.claims)
    lines = [f"# {report.title}", "", f"**Research question:** {report.question}", "", f"**Evidence coverage:** {evidence_coverage(claims):.0%}", "", "## Claims", ""]
    for claim in claims:
        evidence = ", ".join(claim.evidence_ids) or "NONE"
        lines.append(f"- **{claim.claim_type.value}** `{claim.claim_id}` — {claim.text} — Evidence: {evidence}")
    lines.extend(["", "## Sources", ""])
    for source in report.sources:
        lines.append(f"- `{source.source_id}` — {source.title} ({source.publisher}) — {source.url}")
    unsupported = unsupported_claims(claims)
    if unsupported:
        lines.extend(["", "## Review Required", ""])
        for claim in unsupported:
            lines.append(f"- `{claim.claim_id}` has no supporting evidence.")
    return "\n".join(lines) + "\n"
