---
title: "CancelNet: A Framework for Intelligent Phrase-Based Interrupt Control in Risk-Sensitive Applications"
authors:
  - name: Srijon Kumar Shill
    affiliation: 1
affiliations:
  - name: Independent Researcher
    index: 1
date: 2025-06-07
tags:
  - natural language processing
  - interrupt control
  - risk-sensitive systems
  - semantic phrase detection
  - artificial intelligence
repository: https://github.com/Srijon25/CancelNet
archive: https://zenodo.org/record/...
---

# Summary

**CancelNet** is an open-source software framework for intelligent, phrase-based interrupt control in risk-sensitive environments. It combines natural language processing (NLP), semantic similarity, and configurable risk profiles to detect and act on spoken or written cancel commands like “abort mission,” “stop immediately,” or “halt process.” CancelNet is designed for seamless integration into AI-enabled systems where misinterpreting or missing an interrupt command could result in harm, error, or significant cost.

This software allows developers to implement robust interruption logic in domains such as autonomous systems, robotics, critical care devices, industrial automation, and real-time voice interfaces. CancelNet’s modular architecture, test simulation capabilities, and risk tiering ensure flexibility, transparency, and reliability in high-stakes environments.

# Statement of Need

While voice-activated systems and automation have grown exponentially, most lack built-in intelligent interrupt mechanisms that can semantically understand variations of cancel/stop commands. Traditional systems rely heavily on hardcoded keywords or exact phrase matching, which often fails in real-world, high-noise, or emotionally stressed scenarios.

CancelNet addresses this critical gap by:
- Recognizing a wide range of semantically similar phrases using Sentence-BERT embeddings.
- Adjusting interrupt thresholds based on user-defined risk levels.
- Simulating interrupt triggers in test environments before deployment.
- Providing logging for audits and failure analysis.

No current open-source framework combines phrase-level semantic detection with contextual risk profiling in a reusable, developer-friendly package. CancelNet fulfills this unmet need.

# Functionality

CancelNet consists of the following key modules:

- **Phrase Detection (`detector.py`)**  
  Utilizes pretrained Sentence-BERT models to measure the similarity of incoming phrases to known cancel/interrupt patterns.

- **Risk Profiles (`risk_profiles.py`)**  
  Users can define how sensitive the system should be to interrupts under different contexts: high, medium, or low risk. This helps balance safety vs. operational continuity.

- **Interrupt Controller (`controller.py`)**  
  Central logic that processes phrases, determines matches, consults the active risk profile, and decides whether to trigger an interrupt event.

- **Simulator (`simulator.py`)**  
  Enables users to test cancel phrase detection under simulated scenarios to audit behavior and adjust thresholds.

- **Logger (`logger.py`)**  
  Captures when interrupts are triggered, along with matched phrase confidence scores, allowing transparency and review.

- **Tests (`tests/`)**  
  Unit tests covering phrase detection and control logic to ensure correctness and maintainability.

# Example Use Case

In a robotic surgical system, CancelNet can detect phrases like “cancel procedure” or “stop surgery now” even if phrased differently by different users. If configured under a high-risk profile, the system would halt immediately upon detecting semantically similar phrases with high confidence, preventing further action.

Similarly, in a voice-controlled drone, phrases like “abort flight,” “come back,” or “emergency return” would be semantically matched to the interrupt set and processed based on environmental risk settings.

# Quality Control

CancelNet includes:
- Automated unit tests with `pytest`
- Logging for every matched phrase and outcome
- Phrase simulator for test-driven evaluation
- Modular design for clear extension and adaptation

All components are documented with inline comments, and the `README.md` provides usage examples.

# Acknowledgements

This work is an independent research initiative by **Srijon Kumar Shill**. The author thanks the open-source NLP community, particularly the creators of Sentence-BERT, for enabling practical semantic similarity search.

# References

1. Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. *arXiv preprint arXiv:1908.10084*.
2. Vaswani, A., et al. (2017). Attention is All You Need. *Advances in Neural Information Processing Systems*, 30.
3. JOSS Submission Guidelines: https://joss.readthedocs.io/en/latest/submitting.html
