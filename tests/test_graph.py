from research_intelligence.graph import detect_explicit_contradictions

def test_explicit_opposing_polarities_are_detected():
    results = detect_explicit_contradictions([("C1", "throughput", "POSITIVE"), ("C2", "throughput", "NEGATIVE")])
    assert len(results) == 1
    assert results[0].left_claim_id == "C1"
    assert results[0].right_claim_id == "C2"

def test_unrelated_topics_do_not_contradict():
    assert detect_explicit_contradictions([("C1", "throughput", "POSITIVE"), ("C2", "latency", "NEGATIVE")]) == []
