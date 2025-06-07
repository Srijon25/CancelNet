from cancelnet.detector import CancelPhraseDetector
from cancelnet.controller import InterruptController
from cancelnet.risk_profiles import RISK_PROFILES
from cancelnet.simulator import Simulator

if __name__ == "__main__":
    phrases = ["stop", "cancel", "terminate", "abort"]
    detector = CancelPhraseDetector(phrases)
    controller = InterruptController(detector, RISK_PROFILES["medium"])
    sim = Simulator(controller)
    sim.simulate_inputs(["cancel it", "continue running", "abort now"])
