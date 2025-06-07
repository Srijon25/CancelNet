class RiskProfile:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold

RISK_PROFILES = {
    "high": RiskProfile("high", 0.6),
    "medium": RiskProfile("medium", 0.75),
    "low": RiskProfile("low", 0.85),
}
