# CancelNet

**CancelNet** is a modular, AI-powered framework for intelligent, phrase-based interrupt control in risk-sensitive environments. It enables applications to semantically recognize spoken or textual cancel phrases (like “stop now”, “abort mission”) and respond accordingly—based on customizable risk profiles and interrupt thresholds.

Designed with safety, flexibility, and developer usability in mind, CancelNet is ideal for robotics, voice-controlled systems, autonomous processes, and critical decision workflows.

---

## 🚀 Features

- 🔍 **Semantic Phrase Detection**  
  Uses Sentence-BERT to match user input to interrupt phrases even when phrased differently (e.g., “halt everything” ≈ “stop now”).

- ⚠️ **Risk-Sensitive Interrupt Control**  
  Choose behavior for high-, medium-, or low-risk applications.

- 🧪 **Simulation Mode**  
  Test phrase recognition and system reactions before deployment.

- 📊 **Logging & Confidence Scoring**  
  Track decisions, confidence levels, and triggered interrupts.

- ✅ **Modular & Lightweight**  
  Easy to integrate into existing systems or extend for new use cases.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Srijon25/CancelNet.git
cd CancelNet
pip install -r requirements.txt

Requires Python 3.8+


---

🧠 Quick Start

Run a demo simulation to test phrase-based interrupts:

python examples/demo_interrupt.py

Output includes matched phrases, confidence scores, and interrupt results based on the selected risk profile.


---

🧪 Run Tests

Unit tests cover the phrase detector and controller logic:

pytest


---

🧰 Project Structure

CancelNet/
├── cancelnet/         
│   ├── detector.py          # Phrase recognition (Sentence-BERT)
│   ├── controller.py        # Interrupt decision engine
│   ├── risk_profiles.py     # Risk tier configuration
│   ├── simulator.py         # Testing and simulation engine
│   ├── logger.py            # Event logging
│   └── utils.py             # Helper functions
├── tests/
│   ├── test_detector.py
│   ├── test_controller.py
├── examples/
│   └── demo_interrupt.py    # Sample run
├── README.md
├── paper.md                 # JOSS publication paper
├── LICENSE
├── CITATION.cff
├── requirements.txt
└── pyproject.toml


---

🧾 Citation

If you use CancelNet in your work, please cite:

@software{shill2025cancelnet,
  author = {Srijon Kumar Shill},
  title = {CancelNet: A Framework for Intelligent Phrase-Based Interrupt Control in Risk-Sensitive Applications},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/Srijon25/CancelNet},
  version = {1.0.0}
}

Or use the included CITATION.cff file.


---

📚 Use Cases

🩺 Voice-controlled surgical or diagnostic machines

🛸 Autonomous drone cancelation triggers

🏭 Industrial automation with emergency overrides

🧠 AI chatbots or assistants with safety clauses



---

🧑‍💻 Author

Srijon Kumar Shill
Independent Researcher
📧 theunpredictable157@gmail.com


---

📄 License

This project is licensed under the MIT License. See LICENSE for details.
