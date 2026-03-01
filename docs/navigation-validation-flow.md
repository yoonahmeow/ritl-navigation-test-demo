# Navigation Validation Flow

1. System becomes ready after software update or reboot
2. Test runner reads navigation scenarios from configuration
3. Navigation is triggered through UI-equivalent actions
4. Robot executes navigation on physical hardware
5. Navigation data is collected
6. Metrics are computed and evaluated
7. Results are summarized in a report

---

## Failure Detection

- Goal not reached within timeout
- Excessive final position error
- Orientation misalignment
- Velocity violations in constrained areas
