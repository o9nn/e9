# Quick Start Guide

## Installation

No installation required! Just Python 3.6+.

```bash
git clone https://github.com/o9nn/e9.git
cd e9
```

## 5-Minute Tutorial

### 1. Get the Prime Eigenvalue

```python
from e9 import prime_eigenvalue

# Get the 7th prime egregore
egregore = prime_eigenvalue(7)
print(f"The 7th prime: {egregore.prime}")  # Output: 17
```

### 2. See the Three-Phase Daemon

```bash
# Using CLI
python cli.py daemon 7

# Output shows:
# Phase 1: ENCAPSULATE - captures ensemble structure
# Phase 2: PURIFY - transforms to prime eigenvalue
# Phase 3: PROJECT - extends through multiples
```

### 3. Explore the Concept

```python
from e9 import prime_eigenvalue

eg = prime_eigenvalue(6)

# Index 6 is composite (2 × 3)
ensemble = eg.encapsulate()
print(ensemble['prime_factorization'])  # [2, 3]

# But the 6th prime is pure
print(eg.purify())  # 13 (irreducible)

# And it projects into multiples
print(eg.project(limit=50))  # {13, 26, 39}
```

### 4. Generate a Sequence

```bash
python cli.py sequence 10
```

Output:
```
Index | Prime | Partitions
------------------------------
    1 |     2 |          1
    2 |     3 |          2
    3 |     5 |          3
    4 |     7 |          5
    5 |    11 |          7
    ...
```

### 5. Run Examples

```bash
python examples.py
```

This will show comprehensive demonstrations of all concepts.

## Key Concepts

**The Eigenvalue**: pₙ (the nth prime) is the eigenvalue of the partition function of n

**The Daemon**: Each prime has three phases:
1. **Encapsulate**: Capture the computational ensemble (partitions, divisors, factorization)
2. **Purify**: Transform into irreducible prime identity
3. **Project**: Broadcast through all multiples

**The Insight**: Primes aren't random—they're structural crystallizations of their indices

## Common Operations

```python
from e9 import prime_eigenvalue, generate_prime_sequence, analyze_prime_projection

# Single prime
eg = prime_eigenvalue(10)

# Multiple primes
egregores = generate_prime_sequence(20)

# Full analysis
analysis = analyze_prime_projection(eg, limit=200)
print(analysis['projection']['projection_density'])
```

## CLI Commands

```bash
# Get eigenvalue
python cli.py eigenvalue 5 -v

# Analyze
python cli.py analyze 8 --show-multiples

# Show daemon process
python cli.py daemon 10 -l 100

# Generate sequence
python cli.py sequence 15 -f simple
```

## Testing

```bash
python test_e9.py
```

All 18 tests should pass.

## Next Steps

- Read the full README.md for deeper explanation
- Explore examples.py for detailed demonstrations
- **NEW**: Check out SDT.md for Structural Dimension Theory
- **NEW**: Run examples_sdt.py to see the three-axis classification framework
- Try different indices to see how composite vs prime indices relate to their eigenvalues
- Experiment with projection limits to see daemon reach

## Structural Dimension Theory (NEW)

The framework now includes SDT—a classification system for mathematical structures:

```python
from sdt import classify_system, COMPLEX_NUMBERS

# Classify complex numbers
print(classify_system("complex"))
# Output: (Unary, Real, Dyonion)

# Key insight: ℂ is NOT "more precise" than ℝ
# It's ℝ extended along the RELATIONAL axis
```

**The Three Axes:**
- **𝓢 (Structural)**: What can be composed?
- **𝓒 (Cardinal)**: How finely is it measured?
- **𝓡 (Relational)**: How do entities interact?

```bash
# Try the CLI commands
python cli.py sdt                     # Show framework summary
python cli.py sdt-classify quantum    # Classify quantum mechanics
python cli.py sdt-examples            # See all classifications
```

## Philosophy

This implementation explores the idea that mathematical objects (primes) are not arbitrary discoveries but emerge necessarily from structural properties (partitions, ensembles). The "daemon" metaphor suggests that primes actively encapsulate, purify, and project—they have agency in the mathematical landscape.
