# Ship Battle: Multithreaded Operating Systems Simulation

A small Python course project that models a simplified ship battle using one thread per ship.

## Overview

The program creates a set of named ships. Each ship is represented by a thread that waits for a random preparation delay, selects another active ship as a target, and attempts an attack. The shared state tracks which ships remain active.

## Run

Requirements: Python 3.8+

```bash
python project1.py
```

When prompted, enter a number of ships from **2 to 24** (the source code contains 24 predefined ship names).

## Concepts demonstrated

- Python threads and thread lifecycle
- Randomized delays and concurrent events
- Shared state across threads
- Basic modeling of competing processes

## Limitations

This is an educational assignment, not a robust concurrent simulation. The current source modifies shared lists and dictionaries from multiple threads without explicit synchronization. Race conditions and non-deterministic behavior are therefore possible. The output can vary between runs, and the implementation should be reviewed before using it as an example of thread-safe design.

## Repository contents

- `project1.py` — main simulation
