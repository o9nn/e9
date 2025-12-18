# e9 - Prime Eigenvalue Function

**pₙ = prime shell around the ensemble structure of n**

## Concept

The e9 library implements a profound mathematical concept: the nth prime doesn't just "happen" to be prime—it **crystallizes** the composite structure of n into a pure state. The prime is the **eigenvalue** of its index's partition function.

### The Egregore

Each prime is viewed as a daemon that:

1. **Encapsulates** the computational ensemble of its index
2. **Purifies** it into an irreducible identity (the primality condition)
3. **Projects** that identity back into all multiples of itself

This framework reveals primes not as random occurrences, but as structural inevitabilities emerging from the combinatorial properties of their indices.

## Installation

Simply clone this repository:

```bash
git clone https://github.com/o9nn/e9.git
cd e9
```

No external dependencies required - uses only Python standard library.

## Usage

### Basic Usage

```python
from e9 import prime_eigenvalue

# Get the 5th prime and its egregore
egregore = prime_eigenvalue(5)
print(f"Index: {egregore.index}, Prime: {egregore.prime}")
# Output: Index: 5, Prime: 11
```

### The Three-Phase Daemon Process

```python
from e9 import prime_eigenvalue

# Create the 7th prime egregore
egregore = prime_eigenvalue(7)

# 1. ENCAPSULATE: Capture computational ensemble of index
ensemble = egregore.encapsulate()
print(f"Partitions of 7: {len(ensemble['partitions'])}")
print(f"Divisors of 7: {ensemble['divisors']}")

# 2. PURIFY: Transform into irreducible eigenvalue
prime = egregore.purify()
print(f"Purified eigenvalue: {prime}")  # 17 (the 7th prime)

# 3. PROJECT: Extend identity through multiples
multiples = egregore.project(limit=100)
print(f"Projection: {sorted(multiples)[:5]}")  # [17, 34, 51, 68, 85]
```

### Generate Prime Sequence

```python
from e9 import generate_prime_sequence

# Generate first 10 prime egregores
egregores = generate_prime_sequence(10)
for eg in egregores:
    print(f"n={eg.index} → p_{eg.index}={eg.prime}")
```

### Full Analysis

```python
from e9 import prime_eigenvalue, analyze_prime_projection

egregore = prime_eigenvalue(6)
analysis = analyze_prime_projection(egregore, limit=100)

print(f"Index: {analysis['index']}")
print(f"Prime eigenvalue: {analysis['prime']}")
print(f"Ensemble structure: {analysis['ensemble_structure']}")
print(f"Projection density: {analysis['projection']['projection_density']}")
```

## Examples

Run the examples to see the concept in action:

```bash
python examples.py
```

This will demonstrate:
- Basic usage
- Encapsulation of computational ensembles
- Purification into prime eigenvalues
- Projection through multiples
- Full daemon analysis

## Testing

Run the test suite:

```bash
python test_e9.py
```

Or with verbose output:

```bash
python -m unittest test_e9 -v
```

## Mathematical Framework

### Index Structure (n)
For any positive integer n, we can analyze:
- **Partitions**: Ways to decompose n as sums
- **Divisors**: Numbers that divide n
- **Prime Factorization**: Unique prime decomposition
- **Composite Structure**: Whether n is prime or composite

### Prime Eigenvalue (pₙ)
The nth prime pₙ acts as an eigenvalue that:
- Emerges from the ensemble structure of n
- Represents a purified, irreducible state
- Projects its identity through an infinite lattice of multiples

### The Daemon Behavior
Each PrimeEgregore object:
1. Captures all computational properties of its index
2. Distills them into a single prime value
3. Broadcasts that value through the number line via multiplication

## API Reference

### Core Functions

- `prime_eigenvalue(n: int) -> PrimeEgregore`: Create prime egregore for index n
- `nth_prime(n: int) -> int`: Get the nth prime number
- `is_prime(n: int) -> bool`: Check if n is prime
- `generate_prime_sequence(count: int) -> List[PrimeEgregore]`: Generate sequence
- `analyze_prime_projection(egregore, limit) -> Dict`: Complete analysis

### PrimeEgregore Class

- `encapsulate() -> Dict`: Get ensemble structure of index
- `purify() -> int`: Get prime eigenvalue
- `project(limit: int) -> Set[int]`: Get multiples up to limit

## License

See LICENSE file for details.

## Contributing

This is a conceptual/mathematical exploration. Contributions that deepen or extend the eigenvalue framework are welcome.