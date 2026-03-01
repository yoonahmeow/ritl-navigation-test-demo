# System Architecture

This project follows a modular validation architecture designed
for real-world robotic autonomy systems.

---

## Components

### 1. Navigation Test Runner
Responsible for:
- Triggering navigation actions (UI-based)
- Monitoring navigation completion
- Managing test execution order

### 2. Metric Extraction Module
Responsible for:
- Processing recorded navigation data
- Computing accuracy, stability, and compliance metrics
- Producing deterministic pass/fail results

### 3. Configuration Layer
- YAML-based test definitions
- Threshold configuration independent from code

---

## Architectural Rationale

- UI-driven triggering reflects **actual user interaction paths**
- Decoupling metrics from execution enables offline analysis
- Configuration-first design simplifies regression testing

---

## What Is Intentionally Excluded

- Robot-specific firmware
- Internal communication protocols
- Production ROS topics
- Hardware identifiers
