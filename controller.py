class InterruptController:
    def __init__(self, detector, risk_profile):
        self.detector = detector
        self.risk_profile = risk_profile
        self.interrupt_log = []

    def handle_input(self, input_text):
        match, score = self.detector.detect(input_text, self.risk_profile.threshold)
        if match:
            self.log_interrupt(match, score)
            return True, match, score
        return False, None, score

    def log_interrupt(self, phrase, score):
        self.interrupt_log.append({"phrase": phrase, "score": score})
