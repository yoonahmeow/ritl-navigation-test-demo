# Navigation Metrics Definition

## Goal Position Error
Distance between final robot pose and target location (cm).

## Orientation Error
Yaw difference at goal arrival (degrees).

## Velocity Compliance
Maximum and average linear velocity during navigation.

## Path Deviation
Deviation between executed trajectory and planned path.

---

## Why Metrics Matter

Binary success signals hide degradation.
Metrics expose:
- Gradual autonomy regression
- Environment-sensitive failures
- Safety-related behavior changes
