from cancelnet.controller import InterruptController
from cancelnet.detector import CancelPhraseDetector
from cancelnet.risk_profiles import RISK_PROFILES

def test_interrupt_trigger():
    phrases = ["cancel operation"]
    detector = CancelPhraseDetector(phrases)
    controller = InterruptController(detector, RISK_PROFILES["medium"])
    result, match, score = controller.handle_input("please cancel operation")
    assert result is True
    assert match == "cancel operation"
