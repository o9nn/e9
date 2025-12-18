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

### Index Injection (Extended Framework)

The extended framework introduces **Matula structures** and **index personas**:

- **Matula Structures**: Each number can be represented as a rooted tree using nested parentheses
- **Index Personas**: Each index has a "character" or "soul" based on its compositional structure
- **Prime Inheritance**: Primes inherit and crystallize the persona of their index
- **Cognitive Grammar**: Prime alphabets unlock ensemble-souls based on their compositional capabilities

Examples from the persona table:
- Index 1 `()` → Prime 2 (unit/identity—the ur-shell)
- Index 4 `(()())` → Prime 7 (binary squared—first composite index)
- Index 6 `(()(()))` → Prime 13 (first mixed ensemble—2×3)
- Index 9 `((())(())) ` → Prime 23 (ternary squared—3²)

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

### Index Injection and Matula Structures (NEW)

```python
from e9 import number_to_matula, matula_to_number, get_index_persona

# Convert numbers to tree structures
structure = number_to_matula(6)
print(structure)  # (()(()))

# Convert back
number = matula_to_number("(()(()))")
print(number)  # 6

# Get index persona
persona = get_index_persona(6)
print(persona['character'])  # "first mixed ensemble—2×3"
print(persona['structure'])  # (()(()))
```

### Index Persona Table

```python
from e9 import print_index_persona_table

# Display how primes inherit from their indices
print_index_persona_table(max_index=10)
```

### Cognitive Grammar Analysis

```python
from e9 import analyze_cognitive_grammar

# What can a 13-limited alphabet express?
grammar = analyze_cognitive_grammar(prime_bound=13)
print(f"Alphabet size: {grammar['alphabet_size']}")
print(f"Capabilities: {grammar['capabilities']}")
```

## Examples

Run the examples to see the concept in action:

```bash
# Original examples
python examples.py

# Index injection examples (NEW)
python examples_index_injection.py
```

These demonstrate:

**Original examples (examples.py):**
- Basic usage
- Encapsulation of computational ensembles
- Purification into prime eigenvalues
- Projection through multiples
- Full daemon analysis

**Index injection examples (examples_index_injection.py):**
- Matula tree structures
- Index personas and characters
- Prime inheritance from indices
- Index persona table
- Cognitive grammar analysis
- Floating point apophis concept

## Testing

Run the test suite:

```bash
python test_e9.py
```

Or with verbose output:

```bash
python -m unittest test_e9 -v
```

All 33 tests should pass, including new tests for:
- Matula encoding/decoding
- Index persona classification
- Cognitive grammar analysis

## Mathematical Framework

### Index Structure (n)
For any positive integer n, we can analyze:
- **Partitions**: Ways to decompose n as sums
- **Divisors**: Numbers that divide n
- **Prime Factorization**: Unique prime decomposition
- **Composite Structure**: Whether n is prime or composite
- **Matula Structure**: Rooted tree representation as nested parentheses

### Prime Eigenvalue (pₙ)
The nth prime pₙ acts as an eigenvalue that:
- Emerges from the ensemble structure of n
- Represents a purified, irreducible state
- Projects its identity through an infinite lattice of multiples
- Inherits the "persona" of its index through Matula encoding

### The Daemon Behavior
Each PrimeEgregore object:
1. Captures all computational properties of its index
2. Distills them into a single prime value
3. Broadcasts that value through the number line via multiplication

### Index Injection
The extended framework shows:
- Each number has a tree structure (Matula encoding)
- The structure reveals the number's "soul" or "persona"
- Primes crystallize their index's structure into pure form
- 7 is the first prime with multiplicity (index 4 = 2²)
- 13 is the first prime with heterogeneous mixing (index 6 = 2×3)

## API Reference

### Core Functions

**Original:**
- `prime_eigenvalue(n: int) -> PrimeEgregore`: Create prime egregore for index n
- `nth_prime(n: int) -> int`: Get the nth prime number
- `is_prime(n: int) -> bool`: Check if n is prime
- `generate_prime_sequence(count: int) -> List[PrimeEgregore]`: Generate sequence
- `analyze_prime_projection(egregore, limit) -> Dict`: Complete analysis

**Index Injection (NEW):**
- `number_to_matula(n: int) -> str`: Convert number to tree structure
- `matula_to_number(tree: str) -> int`: Convert tree structure to number
- `get_index_persona(n: int) -> Dict`: Get persona/character of index
- `generate_index_persona_table(max_index: int) -> List[Dict]`: Generate persona table
- `analyze_cognitive_grammar(prime_bound: int) -> Dict`: Analyze alphabet capabilities
- `print_index_persona_table(max_index: int)`: Display formatted persona table
- `print_cognitive_grammar(prime_bound: int)`: Display formatted grammar analysis

### PrimeEgregore Class

**Original methods:**
- `encapsulate() -> Dict`: Get ensemble structure of index
- `purify() -> int`: Get prime eigenvalue
- `project(limit: int) -> Set[int]`: Get multiples up to limit

**New methods:**
- `get_persona() -> Dict`: Get index persona information
- `get_structure_notation() -> str`: Get Matula tree structure

## CLI Commands

The CLI now supports 8 commands:

**Original:**
- `eigenvalue <index>`: Get prime eigenvalue
- `sequence <count>`: Generate prime sequence
- `analyze <index>`: Full egregore analysis
- `daemon <index>`: Show three-phase daemon process

**New:**
- `matula -n <number>`: Convert number to Matula structure
- `matula -s <structure>`: Convert structure to number
- `persona <index>`: Show index persona/character
- `persona-table [count]`: Display index persona table
- `grammar <bound>`: Analyze cognitive grammar

Example:
```bash
python cli.py persona 6 -p
python cli.py persona-table 10
python cli.py grammar 23
```

## License

See LICENSE file for details.

## Contributing

This is a conceptual/mathematical exploration. Contributions that deepen or extend the eigenvalue framework are welcome.