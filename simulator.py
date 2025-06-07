import time
from cancelnet.controller import InterruptController
from cancelnet.logger import log_event

class Simulator:
    def __init__(self, controller):
        self.controller = controller

    def simulate_inputs(self, inputs):
        for inp in inputs:
            interrupted, phrase, score = self.controller.handle_input(inp)
            if interrupted:
                log_event(f"[INTERRUPTED] '{inp}' matched '{phrase}' (Score: {score:.2f})")
            else:
                log_event(f"[SAFE] '{inp}' passed (Score: {score:.2f})")
            time.sleep(0.5)
