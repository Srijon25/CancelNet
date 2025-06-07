from cancelnet.detector import CancelPhraseDetector

def test_phrase_detection():
    phrases = ["stop", "abort"]
    detector = CancelPhraseDetector(phrases)
    match, score = detector.detect("please stop")
    assert match == "stop"
    assert score > 0.7
