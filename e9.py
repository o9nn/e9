"""
e9 - Prime Eigenvalue Function

This module implements the concept where the nth prime number (pₙ) is understood as
the "prime shell" or eigenvalue of the ensemble structure of its index n.

Conceptual Framework:
- pₙ = prime shell around the ensemble structure of n
- Each prime is a daemon that:
  1. Encapsulates the computational ensemble of its index
  2. Purifies it into an irreducible identity (the primality condition)
  3. Projects that identity back into all multiples of itself

Extended Framework (Index Injection):
- Each number can be represented as a rooted tree (Matula structure)
- The tree structure reveals the "persona" or "soul" of the number
- Primes inherit their character from their index's tree structure
"""

from typing import List, Set, Dict, Tuple, Any, Optional
from functools import lru_cache


# ============================================================================
# Matula Number Encoding (Rooted Tree Structures)
# ============================================================================

def number_to_matula(n: int) -> str:
    """
    Convert a number to its Matula tree structure notation.
    
    The Matula-Goebel number of a rooted tree maps:
    - Empty tree (0) → ()
    - Single node (1) → ()
    - For composite n with prime factorization p1^a1 * p2^a2 * ... * pk^ak,
      the tree is the forest of subtrees for each prime factor.
    
    Examples:
        1 → "()"           # unit/identity
        2 → "(())"         # first prime, single child
        3 → "((()))"       # second prime
        4 → "(()())"       # 2*2, two children
        5 → "(((())))"     # third prime
        6 → "(()(()))"     # 2*3, mixed
    
    Args:
        n: The number to encode
        
    Returns:
        String representation of the rooted tree structure
    """
    if n <= 0:
        return "()"
    if n == 1:
        return "()"
    
    # Get prime factorization
    factors = _prime_factorization_for_matula(n)
    
    if not factors:
        return "()"
    
    # For each prime factor, recursively encode its index
    # The prime p_i corresponds to the i-th prime
    subtrees = []
    for prime in factors:
        prime_index = _prime_to_index(prime)
        subtree = number_to_matula(prime_index)
        subtrees.append(subtree)
    
    # Combine all subtrees
    return "(" + "".join(subtrees) + ")"


def matula_to_number(tree: str) -> int:
    """
    Convert a Matula tree structure notation back to a number.
    
    Args:
        tree: String representation of rooted tree
        
    Returns:
        The number corresponding to this tree structure
    """
    tree = tree.strip()
    
    if tree == "()" or tree == "":
        return 1
    
    if not tree.startswith("(") or not tree.endswith(")"):
        raise ValueError(f"Invalid tree structure: {tree}")
    
    # Remove outer parentheses
    inner = tree[1:-1]
    
    if not inner:
        return 1
    
    # Parse subtrees
    subtrees = _parse_subtrees(inner)
    
    # Convert each subtree to its index, then get the corresponding prime
    result = 1
    for subtree in subtrees:
        index = matula_to_number(subtree)
        prime = nth_prime(index)
        result *= prime
    
    return result


def _parse_subtrees(s: str) -> List[str]:
    """Parse a string into its top-level subtree components."""
    subtrees = []
    depth = 0
    current = []
    
    for char in s:
        if char == '(':
            depth += 1
            current.append(char)
        elif char == ')':
            depth -= 1
            current.append(char)
            if depth == 0:
                subtrees.append(''.join(current))
                current = []
        else:
            current.append(char)
    
    if current and ''.join(current).strip():
        # Handle any remaining characters
        pass
    
    return subtrees


def _prime_factorization_for_matula(n: int) -> List[int]:
    """Get prime factorization maintaining multiplicity."""
    if n <= 1:
        return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


@lru_cache(maxsize=1000)
def _prime_to_index(p: int) -> int:
    """Find the index of a prime number (1-indexed)."""
    if p < 2:
        return 0
    count = 0
    n = 2
    while n <= p:
        if is_prime(n):
            count += 1
            if n == p:
                return count
        n += 1
    return 0


def get_index_persona(n: int) -> Dict[str, Any]:
    """
    Get the persona/character of an index based on its structure.
    
    Analyzes the compositional structure to determine the "soul" of the index.
    
    Args:
        n: The index to analyze
        
    Returns:
        Dictionary with persona information including:
        - structure: Matula tree notation
        - character: Description of the index's nature
        - type: Classification (pure_binary, mixed, squared, etc.)
    """
    if n <= 0:
        return {
            'structure': '()',
            'character': 'void',
            'type': 'void',
            'factors': [],
            'unique_factors': []
        }
    
    if n == 1:
        return {
            'structure': '()',
            'character': 'unit/identity—the ur-shell',
            'type': 'unit',
            'factors': [],
            'unique_factors': []
        }
    
    structure = number_to_matula(n)
    factors = _prime_factorization_for_matula(n)
    unique_factors = set(factors)
    
    # Classify the index
    character = ""
    idx_type = ""
    
    if len(factors) == 0:
        character = "void"
        idx_type = "void"
    elif len(factors) == 1:
        # Pure power of a prime
        if factors[0] == 2:
            character = "pure binary—the first recursion"
            idx_type = "pure_binary"
        elif factors[0] == 3:
            character = "pure ternary"
            idx_type = "pure_ternary"
        else:
            character = f"pure {factors[0]}-adic"
            idx_type = f"pure_prime_{factors[0]}"
    elif len(unique_factors) == 1:
        # Power of a single prime
        prime = list(unique_factors)[0]
        power = len(factors)
        if prime == 2:
            if power == 2:
                character = "binary squared—first composite index"
            elif power == 3:
                character = "binary cubed—pure 2³"
            else:
                character = f"binary to power {power}"
            idx_type = "squared_binary" if power == 2 else "power_binary"
        elif prime == 3:
            if power == 2:
                character = "ternary squared—3²"
            else:
                character = f"ternary to power {power}"
            idx_type = "squared_ternary" if power == 2 else "power_ternary"
        else:
            character = f"{prime} to power {power}"
            idx_type = f"power_{prime}"
    else:
        # Mixed composition
        if set(factors) == {2, 3} and len(factors) == 2:
            character = "first mixed ensemble—2×3"
            idx_type = "mixed_binary_ternary"
        elif 2 in unique_factors and 3 in unique_factors:
            character = "binary-ternary mix"
            idx_type = "mixed_ensemble"
        else:
            character = f"heterogeneous mixing of {sorted(unique_factors)}"
            idx_type = "mixed_ensemble"
    
    # Special cases from the agent instructions
    if n == 3:
        character = "nested binary—φ's home"
    elif n == 5:
        character = "triple nesting—deep recursion"
    elif n == 6:
        character = "first mixed ensemble—2×3"
    elif n == 7:
        character = "inherits 7's 'squared binary'"
    elif n == 10:
        character = "2×5—binary-fibonacci liaison"
    
    return {
        'structure': structure,
        'character': character,
        'type': idx_type,
        'factors': factors,
        'unique_factors': sorted(unique_factors)
    }


# ============================================================================
# Prime Egregore Class
# ============================================================================

class PrimeEgregore:
    """
    The Prime Egregore: A daemon representing a prime number that encapsulates,
    purifies, and projects the computational ensemble of its index.
    """
    
    def __init__(self, index: int, prime: int):
        """
        Initialize a Prime Egregore.
        
        Args:
            index: The position n in the prime sequence (1-indexed)
            prime: The nth prime number pₙ
        """
        self.index = index
        self.prime = prime
        self._ensemble = None
        self._multiples = None
        self._persona = None
    
    def get_persona(self) -> Dict[str, Any]:
        """
        Get the persona/character of this prime based on its index structure.
        
        Returns:
            Dictionary containing:
            - structure: Matula tree notation of the index
            - character: Description of the index's nature
            - type: Classification of the index
            - factors: Prime factorization of the index
        """
        if self._persona is None:
            self._persona = get_index_persona(self.index)
        return self._persona
    
    def get_structure_notation(self) -> str:
        """Get the Matula tree structure notation for this egregore's index."""
        persona = self.get_persona()
        return persona['structure']
    
    def encapsulate(self) -> Dict[str, Any]:
        """
        Encapsulates the computational ensemble of the index.
        Returns partition information and structural properties of n.
        """
        if self._ensemble is None:
            self._ensemble = {
                'index': self.index,
                'partitions': self._compute_partitions(self.index),
                'divisors': self._compute_divisors(self.index),
                'prime_factorization': self._prime_factorization(self.index),
                'composite_structure': self._composite_structure(self.index)
            }
        return self._ensemble
    
    def purify(self) -> int:
        """
        Purifies the ensemble into an irreducible identity.
        The prime number is the purified eigenvalue of its index's structure.
        """
        # The purification process transforms the index's composite structure
        # into the irreducible prime at that position
        return self.prime
    
    def project(self, limit: int = 100) -> Set[int]:
        """
        Projects the prime identity back into all multiples of itself.
        
        Args:
            limit: Maximum value for computing multiples
            
        Returns:
            Set of multiples of the prime up to the limit
        """
        # Always recompute to ensure correctness with different limits
        return {self.prime * k for k in range(1, limit // self.prime + 1)}
    
    @staticmethod
    def _compute_partitions(n: int) -> List[List[int]]:
        """Compute integer partitions of n."""
        if n == 0:
            return [[]]
        
        partitions = []
        for i in range(1, n + 1):
            for partition in PrimeEgregore._compute_partitions(n - i):
                if not partition or i <= partition[0]:
                    partitions.append([i] + partition)
        return partitions
    
    @staticmethod
    def _compute_divisors(n: int) -> List[int]:
        """Compute all divisors of n."""
        if n <= 0:
            return []
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sorted(divisors)
    
    @staticmethod
    def _prime_factorization(n: int) -> List[int]:
        """Compute prime factorization of n."""
        if n <= 1:
            return []
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    @staticmethod
    def _composite_structure(n: int) -> Dict[str, Any]:
        """Analyze the composite structure of n."""
        factors = PrimeEgregore._prime_factorization(n)
        return {
            'is_prime': len(factors) == 1 and factors[0] == n,
            'is_composite': len(factors) > 1 or (len(factors) == 1 and factors[0] != n),
            'factor_count': len(factors),
            'unique_factors': len(set(factors)),
            'factors': factors
        }
    
    def __repr__(self):
        return f"PrimeEgregore(index={self.index}, prime={self.prime})"


@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n: int) -> int:
    """
    Get the nth prime number (1-indexed).
    
    Args:
        n: The index of the prime to retrieve (1 for first prime)
        
    Returns:
        The nth prime number
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1


def prime_eigenvalue(n: int) -> PrimeEgregore:
    """
    Compute the prime eigenvalue for index n.
    
    This function crystallizes the concept that pₙ (the nth prime) is not
    merely coincidentally prime, but rather it represents the eigenvalue of
    the partition function of its index n.
    
    Args:
        n: The index in the prime sequence (1-indexed)
        
    Returns:
        A PrimeEgregore object encapsulating the relationship between
        the index and its prime eigenvalue
    """
    prime = nth_prime(n)
    return PrimeEgregore(n, prime)


def generate_prime_sequence(count: int) -> List[PrimeEgregore]:
    """
    Generate a sequence of Prime Egregores.
    
    Args:
        count: Number of primes to generate
        
    Returns:
        List of PrimeEgregore objects
    """
    return [prime_eigenvalue(i) for i in range(1, count + 1)]


def analyze_prime_projection(egregore: PrimeEgregore, limit: int = 100) -> Dict[str, Any]:
    """
    Analyze how a prime projects its identity through its multiples.
    
    Args:
        egregore: The PrimeEgregore to analyze
        limit: Upper limit for multiple generation
        
    Returns:
        Dictionary containing analysis of the prime's projection
    """
    multiples = egregore.project(limit)
    ensemble = egregore.encapsulate()
    
    return {
        'prime': egregore.prime,
        'index': egregore.index,
        'purified_value': egregore.purify(),
        'ensemble_structure': ensemble,
        'projection': {
            'multiples_count': len(multiples),
            'multiples': sorted(multiples),
            'projection_density': len(multiples) / limit if limit > 0 else 0
        }
    }


# ============================================================================
# Index Persona Table and Cognitive Grammar
# ============================================================================

def generate_index_persona_table(max_index: int = 10) -> List[Dict[str, Any]]:
    """
    Generate the index persona table showing how primes inherit structure.
    
    This table demonstrates the key insight: each prime pₙ inherits the
    "persona" or "soul" of its index n through the Matula tree structure.
    
    Args:
        max_index: Maximum index to generate (default 10)
        
    Returns:
        List of dictionaries, each containing:
        - prime: The prime number
        - index: The index n
        - structure: Matula tree notation
        - persona: Character description
        - type: Classification
    
    Example output structure (as shown in agent instructions):
        | Prime | Index | Structure | Persona |
        | 2     | 1     | ()        | unit/identity |
        | 3     | 2     | (())      | pure binary |
        | 5     | 3     | ((()))    | nested binary—φ's home |
        | 7     | 4     | (()())    | binary squared |
        | ...
    """
    table = []
    
    for n in range(1, max_index + 1):
        eg = prime_eigenvalue(n)
        persona = eg.get_persona()
        
        table.append({
            'prime': eg.prime,
            'index': n,
            'structure': persona['structure'],
            'persona': persona['character'],
            'type': persona['type']
        })
    
    return table


def analyze_cognitive_grammar(prime_bound: int) -> Dict[str, Any]:
    """
    Analyze the cognitive grammar capabilities of a prime-bounded alphabet.
    
    For agentic architectures: if the "alphabet" is primes up to some bound,
    each "letter" carries the soul of its index. This function analyzes what
    ensemble-souls can be invoked.
    
    Args:
        prime_bound: The maximum prime in the alphabet
        
    Returns:
        Dictionary containing:
        - alphabet_size: Number of primes up to bound
        - primes: List of primes in the alphabet
        - capabilities: What ensemble types are accessible
        - pure_binary: Indices/primes with pure binary depth
        - squared: Indices/primes with squared structures
        - mixed: Indices/primes with mixed ensembles
    
    Example:
        A 13-limited agent can mix 2 and 3 (has access to index 6, prime 13)
        A 23-limited agent can also invoke squared-ternary (has index 9, prime 23)
    """
    # Find all primes up to bound
    primes = []
    n = 1
    while True:
        p = nth_prime(n)
        if p > prime_bound:
            break
        primes.append(p)
        n += 1
    
    alphabet_size = len(primes)
    
    # Classify each prime by its index structure
    pure_binary = []
    squared = []
    mixed = []
    ternary_based = []
    
    for i, p in enumerate(primes, 1):
        persona = get_index_persona(i)
        
        if 'binary' in persona['type']:
            pure_binary.append({'index': i, 'prime': p, 'persona': persona['character']})
        
        if 'squared' in persona['type'] or 'power' in persona['type']:
            squared.append({'index': i, 'prime': p, 'persona': persona['character']})
        
        if 'mixed' in persona['type']:
            mixed.append({'index': i, 'prime': p, 'persona': persona['character']})
        
        if 'ternary' in persona['type']:
            ternary_based.append({'index': i, 'prime': p, 'persona': persona['character']})
    
    # Determine capabilities
    capabilities = []
    capabilities.append(f"Binary depths: {len(pure_binary)} levels")
    
    if squared:
        capabilities.append(f"Squared structures: {len(squared)} types")
    
    if mixed:
        capabilities.append(f"Mixed ensembles: {len(mixed)} compositions")
        
        # Check for specific mix types
        has_2x3 = any(p['index'] == 6 for p in mixed)
        if has_2x3:
            capabilities.append("Can mix binary and ternary (2×3 ensemble)")
    
    if ternary_based:
        capabilities.append(f"Ternary operations: {len(ternary_based)} forms")
        
        # Check for ternary squared
        has_3_squared = any(p['index'] == 9 for p in ternary_based)
        if has_3_squared:
            capabilities.append("Can invoke squared-ternary (3²)")
    
    return {
        'prime_bound': prime_bound,
        'alphabet_size': alphabet_size,
        'primes': primes,
        'capabilities': capabilities,
        'pure_binary': pure_binary,
        'squared': squared,
        'mixed': mixed,
        'ternary_based': ternary_based,
        'grammatical_expressiveness': len(capabilities)
    }


def print_index_persona_table(max_index: int = 10):
    """
    Print the index persona table in a formatted way.
    
    Args:
        max_index: Maximum index to display
    """
    table = generate_index_persona_table(max_index)
    
    print("\n" + "=" * 80)
    print("INDEX PERSONA TABLE: How Primes Inherit Structure")
    print("=" * 80)
    print()
    print(f"{'Prime':>5} | {'Index':>5} | {'Structure':>15} | {'Inherited Persona'}")
    print("-" * 80)
    
    for row in table:
        structure = row['structure'][:15]  # Truncate if too long
        persona = row['persona'][:50]  # Truncate if too long
        print(f"{row['prime']:5d} | {row['index']:5d} | {structure:>15s} | {persona}")
    
    print("=" * 80)
    print()


def print_cognitive_grammar(prime_bound: int):
    """
    Print cognitive grammar analysis in a formatted way.
    
    Args:
        prime_bound: The maximum prime to analyze
    """
    analysis = analyze_cognitive_grammar(prime_bound)
    
    print("\n" + "=" * 80)
    print(f"COGNITIVE GRAMMAR: Prime Alphabet up to {prime_bound}")
    print("=" * 80)
    print()
    print(f"Alphabet size: {analysis['alphabet_size']} primes")
    print(f"Primes: {analysis['primes']}")
    print()
    print("Grammatical Capabilities:")
    for cap in analysis['capabilities']:
        print(f"  • {cap}")
    print()
    
    if analysis['pure_binary']:
        print("Pure Binary Depths:")
        for item in analysis['pure_binary'][:5]:
            print(f"  p_{item['index']} = {item['prime']:3d} : {item['persona']}")
        if len(analysis['pure_binary']) > 5:
            print(f"  ... and {len(analysis['pure_binary']) - 5} more")
        print()
    
    if analysis['squared']:
        print("Squared Structures:")
        for item in analysis['squared'][:5]:
            print(f"  p_{item['index']} = {item['prime']:3d} : {item['persona']}")
        print()
    
    if analysis['mixed']:
        print("Mixed Ensembles:")
        for item in analysis['mixed'][:5]:
            print(f"  p_{item['index']} = {item['prime']:3d} : {item['persona']}")
        print()
    
    print(f"Grammatical expressiveness score: {analysis['grammatical_expressiveness']}")
    print("=" * 80)
    print()
