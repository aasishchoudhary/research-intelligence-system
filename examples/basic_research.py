from research_intelligence.models import Claim, ClaimType, Evidence, ResearchReport, Source
from research_intelligence.report import render_markdown
from research_intelligence.quality import validate_provenance

source = Source("S1", "Example technical source", "Example Publisher", "https://example.com/source", "2026-10-01")
evidence = Evidence("E1", "S1", "The system increased throughput under the tested workload.", "paragraph-4")
claim = Claim("C1", "The system increased throughput under the tested workload.", ClaimType.FACT, ("E1",), 0.95)
report = ResearchReport("Example Evidence Report", "What does the supplied source support?", (claim,), (source,), (evidence,))
errors = validate_provenance([claim], [evidence])
if errors:
    raise SystemExit("\n".join(errors))
print(render_markdown(report))
