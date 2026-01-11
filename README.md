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
- Index 9 `((())((()))` → Prime 23 (ternary squared—3²)

### Structural Dimension Theory (SDT)

**NEW:** The framework now includes **Structural Dimension Theory (SDT)** - a classification system for mathematical and computational systems along three independent orthogonal axes:

- **𝓢 (Structural/Ordinal)**: What compositions are admissible? (categorical, operadic, logical)
- **𝓒 (Cardinal/Feature)**: How finely can differences be resolved? (metric, measurable, quantitative)
- **𝓡 (Relational/Interaction)**: How do entities interfere and relate? (algebraic, geometric, topological)

**Key Insight:** Boolean, Real, and Complex are not stages of refinement—they are coordinates in a three-axis space of meaning.

#### SDT Classifications

- **Complex Numbers (ℂ)**: (Unary, Real, Dyonion) - ℂ is ℝ extended along the relational axis
- **Quantum Mechanics**: (Unary, Real, Polynonion) - Relational geometry, not weird logic
- **e9/Matula Trees**: (Self-similar, Natural, Recursonion) - Operadic fixed points

See [SDT.md](SDT.md) for the complete framework and [examples_sdt.py](examples_sdt.py) for demonstrations.

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

### Structural Dimension Theory (SDT) (NEW)

```python
from sdt import classify_system, COMPLEX_NUMBERS, QUANTUM_MECHANICS

# Classify a mathematical system
sdt_type = classify_system("complex")
print(sdt_type)  # (Unary, Real, Dyonion)

# Access standard classifications
print(COMPLEX_NUMBERS)  # (Unary, Real, Dyonion)
print(QUANTUM_MECHANICS)  # (Unary, Real, Polynonion)

# Understanding learning as transport
from sdt import create_neural_network_learning
nn = create_neural_network_learning()
print(nn.sdt_type)  # (N-ary, Real, Polynonion)
```

## Examples

Run the examples to see the concept in action:

```bash
# Original examples
python examples.py

# Index injection examples
python examples_index_injection.py

# Structural Dimension Theory examples (NEW)
python examples_sdt.py
```

These demonstrate:

**Original examples (examples.py):**
- Basic usage
- Encapsulation of computational ensembles
- Purification into prime eigenvalues
- Projection through multiples
- Full daemon analysis

**SDT examples (examples_sdt.py) (NEW):**
- Three-axis classification system (𝓢, 𝓒, 𝓡)
- Complex numbers as relational extension of reals
- Quantum mechanics as relational geometry
- Learning as feature transport over ordinal graphs
- Recursonions and operadic fixed points
- Axis orthogonality demonstrations

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
# Test e9 framework
python test_e9.py

# Test SDT framework (NEW)
python test_sdt.py

# Or run all tests with verbose output
python -m unittest test_e9 test_sdt -v
```

All 115 tests should pass (75 for e9, 40 for SDT), including tests for:
- Original prime eigenvalue functions (18 tests)
- Matula encoding/decoding (4 tests)
- Index persona classification (5 tests)
- Cognitive grammar analysis (3 tests)
- Connes-Kreimer Hopf algebra (15 tests):
  - A000081 rooted tree counts
  - Ion layer structure and Butcher recursion
  - Prime tower generation
  - Grafting operation
  - Complete Hopf algebra analysis
- Cognitive renormalization (30 tests):
  - Rooted trees and forests
  - Admissible cuts
  - Coproduct computation
  - Antipode (renormalization)
  - Characters and convolution
  - B+ grafting operator
  - Base increments
- **Structural Dimension Theory (40 tests - NEW)**:
  - Axis definitions (Structural, Cardinal, Relational)
  - SDT type system
  - Standard system classifications
  - Complex numbers as relational extension
  - Quantum mechanics classification
  - Learning as feature transport
  - Recursonions and operadic fixed points
  - Axis orthogonality verification
  - A000081 rooted tree counts
  - Ion layer structure and Butcher recursion
  - Prime tower generation
  - Grafting operation
  - Complete Hopf algebra analysis

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

**Connes-Kreimer Hopf Algebra:**
- `rooted_trees_count(n: int) -> int`: Get A000081(n) - rooted unlabeled trees
- `ion_layer(n: int) -> Dict`: Calculate ion layer with Butcher recursion
- `generate_ion_sequence(max_order: int) -> List[Dict]`: Generate ion sequence
- `prime_tower(seed: int, depth: int) -> List[int]`: Generate prime tower (unary grafting)
- `graft_operation(matula_number: int) -> int`: Grafting in Matula coordinates
- `analyze_hopf_structure(max_order: int) -> Dict`: Complete Hopf algebra analysis
- `print_hopf_analysis(max_order: int)`: Display formatted Hopf analysis

**Cognitive Renormalization (NEW):**
- `RootedTree(children: Tuple[RootedTree, ...])`: Tree node in H_CK
- `Forest(trees: Tuple[RootedTree, ...])`: Disjoint union of trees
- `admissible_cuts(tree: RootedTree) -> List[AdmissibleCut]`: Compute all admissible cuts
- `coproduct(tree: RootedTree) -> List[CoproductTerm]`: Compute Δ(tree)
- `antipode(tree: RootedTree) -> RootedTree`: Compute S(tree) structure
- `Character(eval_func, multiply, name)`: Algebra morphism φ: H_CK → A
- `char.convolve(other) -> Character`: Compute convolution (φ * ψ)
- `cognitive_renormalization(char, tree) -> Any`: Apply antipode semantics
- `B_plus(tree_or_forest) -> RootedTree`: Grafting operator (adds root)
- `theta_n(n: int) -> List[RootedTree]`: All trees with n nodes
- `base_increment(n: int) -> int`: Compute B_n = Θ_n - B+(Θ_{n-1})
- `matula_to_tree(n: int) -> RootedTree`: Convert Matula to tree
- `tree_to_matula(tree: RootedTree) -> int`: Convert tree to Matula

### PrimeEgregore Class

**Original methods:**
- `encapsulate() -> Dict`: Get ensemble structure of index
- `purify() -> int`: Get prime eigenvalue
- `project(limit: int) -> Set[int]`: Get multiples up to limit

**New methods:**
- `get_persona() -> Dict`: Get index persona information
- `get_structure_notation() -> str`: Get Matula tree structure

## CLI Commands

The CLI now supports 23 commands:

**Original:**
- `eigenvalue <index>`: Get prime eigenvalue
- `sequence <count>`: Generate prime sequence
- `analyze <index>`: Full egregore analysis
- `daemon <index>`: Show three-phase daemon process

**Index Injection:**
- `matula -n <number>`: Convert number to Matula structure
- `matula -s <structure>`: Convert structure to number
- `persona <index>`: Show index persona/character
- `persona-table [count]`: Display index persona table
- `grammar <bound>`: Analyze cognitive grammar

**Connes-Kreimer Hopf Algebra:**
- `hopf [order]`: Analyze Hopf algebra structure (default: order 10)
- `ion <order>`: Show ion layer at specific order
- `tower <seed> <depth>`: Generate prime tower
- `a000081 [count]`: Show A000081 sequence (default: 15 terms)

**Cognitive Renormalization:**
- `tree [-m MATULA | -s | -t]`: Analyze a rooted tree
- `coproduct <matula> [-v]`: Compute coproduct (admissible cuts)
- `base [max_n]`: Show base increment sequence
- `renorm [-m MATULA]`: Demonstrate cognitive renormalization (antipode)

**Structural Dimension Theory (NEW):**
- `sdt`: Show SDT framework summary
- `sdt-axes`: Show detailed axis information
- `sdt-classify <system>`: Classify a mathematical system
- `sdt-examples`: Show example classifications
- `sdt-learning [neural|symbolic|all]`: Show learning as transport
- `sdt-recursonion`: Show recursonion examples

Example:
```bash
# Index injection
python cli.py persona 6 -p
python cli.py persona-table 10
python cli.py grammar 23

# Hopf algebra
python cli.py hopf 8
python cli.py ion 5 -v
python cli.py tower 8 5
python cli.py a000081 10

# Cognitive renormalization
python cli.py tree -t                # Analyze ternary corolla
python cli.py coproduct 8 -v         # Show coproduct of Matula 8
python cli.py base 10                # Show base increments
python cli.py renorm                 # Demonstrate antipode

# Structural Dimension Theory (NEW)
python cli.py sdt                    # Show framework summary
python cli.py sdt-classify complex   # Classify complex numbers
python cli.py sdt-examples           # Show all classifications
python cli.py sdt-learning neural    # Neural networks as transport
```

## Mathematical Framework (Extended)

### Cognitive Renormalization Theorem (NEW)

The implementation now includes the **Connes-Kreimer Hopf algebra** structures for cognitive renormalization:

**Core Structures:**
- `RootedTree`: Basis elements in H_CK (the Connes-Kreimer Hopf algebra)
- `Forest`: Disjoint union of trees (free commutative monoid)
- `admissible_cuts(tree)`: Decompose tree into fiber/trunk pairs
- `coproduct(tree)`: Compute Δ(tree) = all admissible cut terms
- `antipode(tree)`: The S operator for cognitive renormalization

**The Coproduct (Δ):**
```
Δ(t) = t⊗1 + 1⊗t + Σ_{c∈Adm(t)} P^c(t)⊗R^c(t)
```
where:
- `P^c(t)`: pruned forest (fiber - stuff cut off)
- `R^c(t)`: trunk (base - root component after cutting)

This captures the "fiber/base splitting" - all ways a tree can decompose.

**The Antipode (S) - Cognitive Renormalization:**
```
S(t) = -t - Σ_{c∈Adm(t)} S(P^c(t)) · R^c(t)
```

The antipode computes **counterterms** to normalize nested compositions:
- Identifies subdivergences (admissible cuts)
- Subtracts them recursively (antipode)
- Produces renormalized finite result

This is exactly what renormalization does in physics and what the mind does when managing semantic infinities from deeply nested concepts.

**Characters and Convolution:**
- `Character`: Algebra morphism φ: H_CK → A (evaluation into target algebra)
- `char1.convolve(char2)`: Compute (φ * ψ) via coproduct
- `cognitive_renormalization(char, tree)`: Apply antipode semantics

Characters form a group under convolution, with inverse φ^(-1) = φ ∘ S.

### Prime Lift Theorem (NEW)

**Theorem:** The "prime-lift" objects form the B+-closure of the ternary corolla inside H_CK.

**Key Operations:**
- `B_plus(tree)`: Grafting operator - adds a root above tree/forest
- `theta_n(n)`: All rooted trees with n nodes (Θ_n element)
- `base_increment(n)`: B_n = Θ_n - B+(Θ_{n-1})

**In Matula Coordinates:**
```
graft(tree) = p_M(tree)
```

Starting from the octonionic seed (Matula 8 = ternary corolla):
```
8 → p_8=19 → p_19=67 → p_67=331 → p_331=2221 → ...
```

This creates the "shell structure" beyond division algebras.

**Bridge Functions:**
- `matula_to_tree(n)`: Convert Matula number to RootedTree
- `tree_to_matula(tree)`: Convert RootedTree to Matula number

### Connes-Kreimer Hopf Algebra

The implementation now includes the deep mathematical structures from the research notes:

**A000081 - Rooted Unlabeled Trees:**
- The universal grammar of composition
- Basis objects for elementary differentials (Butcher trees)
- Foundation of B-series in numerical analysis
- Core of the Connes-Kreimer Hopf algebra

**The Butcher Recursion (Ion Layers):**
```
fib(n) = tot(n-1)        # fiber = previous total
tot(n) = A000081(n+1)    # total = rooted tree count  
bas(n) = tot(n) - fib(n) # base = new differentials
max(n) = p_max(n-1)      # unary graft (n≥5, max(4)=8)
```

This captures the fiber/base/total decomposition that mirrors the Connes-Kreimer coproduct.

**Prime Tower (Unary Grafting):**
- The B_+ operator: adding a single root to a tree
- In Matula coordinates: graft(tree) = p_Matula(tree)
- Starting from octonionic seed (8): 8 → 19 → 67 → 331 → 2221 → 19577 → 219613 → 3042161 → 50728129 → 997525853 → ...
- Creates shell structure beyond division algebra limit
- See [PRIME_TOWER_INSIGHTS.md](PRIME_TOWER_INSIGHTS.md) for detailed analysis of each tower element

**Connection to Moonshine:**
- Monster VOA partition function: J(τ) = j(τ) - 744
- The constant 744 = A000081(10) + 5² = 719 + 25
- Both structures expand in the same universal operadic basis
- The -744 is the renormalization constant (vacuum subtraction)

### The Inevitability Chain

1. Division algebras give privileged ternary corolla at 8 (triality)
2. Adding composite branching forces the full rooted-tree operad
3. Rooted-tree operads demand prime factor coordinates (Matula)
4. Prime powers appear as natural stratification of composition depth

> "Octonions end geometry at 8. Rooted trees take over dynamics beyond it. A000081 is the universal grammar both sides must speak."

## Examples

Run the examples to see the concepts in action:

```bash
# Original examples
python examples.py

# Index injection examples
python examples_index_injection.py

# Connes-Kreimer Hopf algebra examples
python examples_hopf_algebra.py

# Cognitive renormalization examples (NEW)
python examples_cognitive_renormalization.py
```

The cognitive renormalization examples demonstrate:
- Rooted trees as basis elements in H_CK
- Admissible cuts and the coproduct Δ
- The antipode S (cognitive renormalization)
- Characters and convolution
- The B+ grafting operator (prime lift)
- Base increments and the inevitability chain
- The universal property of rooted trees

The Hopf algebra examples demonstrate:
- A000081 (rooted unlabeled trees)
- The Butcher recursion (ion layers)
- Prime tower (unary grafting)
- Fiber/base/total decomposition
- Connection to moonshine
- Complete Hopf algebra analysis

## Documentation

For deeper mathematical insights, see:

- **[SDT.md](SDT.md)** - Complete Structural Dimension Theory framework (NEW)
  - Three-axis classification system (𝓢, 𝓒, 𝓡)
  - Axioms and formal definitions
  - Standard system classifications (ℂ, QM, Boolean, etc.)
  - Learning as feature transport
  - Recursonions and operadic fixed points
  - Connection to e9/Matula framework

- **[PRIME_TOWER_INSIGHTS.md](PRIME_TOWER_INSIGHTS.md)** - Comprehensive analysis of the extended prime tower (levels 0-9)
  - Detailed properties of each number: 8, 19, 67, 331, 2221, 19577, 219613, 3042161, 50728129, 997525853
  - Growth rate analysis and patterns
  - Digital root cycles and digit count progressions
  - Connection to Hopf algebra and tree structures
  - Computational considerations and OEIS references

- **[INEVITABILITY_CHAIN.md](INEVITABILITY_CHAIN.md)** - Why rooted trees are universal
- **[COGNITIVE_RENORMALIZATION.md](COGNITIVE_RENORMALIZATION.md)** - The antipode and renormalization
- **[prime-lift-theorem.md](prime-lift-theorem.md)** - The formal statement of the prime lift theorem
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Technical implementation details

## License

See LICENSE file for details.

## Contributing

This is a conceptual/mathematical exploration. Contributions that deepen or extend the eigenvalue framework are welcome.