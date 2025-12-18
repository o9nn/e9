#!/usr/bin/env python3
"""
Examples demonstrating Index Injection and Matula Structures.

This script demonstrates the extended Prime Eigenvalue concept where each
prime inherits the "persona" or "soul" of its index through Matula tree structures.
"""

from e9 import (
    prime_eigenvalue,
    number_to_matula,
    matula_to_number,
    get_index_persona,
    generate_index_persona_table,
    print_index_persona_table,
    analyze_cognitive_grammar,
    print_cognitive_grammar
)


def example_matula_encoding():
    """Demonstrate Matula tree structure encoding."""
    print("\n" + "=" * 80)
    print("MATULA STRUCTURES: Numbers as Rooted Trees")
    print("=" * 80)
    print("\nThe Matula-Goebel encoding reveals the tree structure of numbers:")
    print("- () is the unit/identity")
    print("- Primes nest their index's structure")
    print("- Composites combine their factors' structures")
    print()
    
    examples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"{'Number':>6} | {'Structure':>15} | {'Description'}")
    print("-" * 80)
    
    for n in examples:
        structure = number_to_matula(n)
        persona = get_index_persona(n)
        desc = persona['character'][:50]
        print(f"{n:6d} | {structure:>15s} | {desc}")
    
    print("\nThe tree structure is the 'sigil' by which you invoke each number's")
    print("true name. [[[]]] for 5 isn't just notation—it's the liturgy.")
    print()


def example_matula_roundtrip():
    """Demonstrate encoding and decoding."""
    print("\n" + "=" * 80)
    print("MATULA ROUNDTRIP: Structure ⇄ Number")
    print("=" * 80)
    print()
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20]
    
    print("Testing that structure encoding is reversible:\n")
    
    for n in numbers:
        tree = number_to_matula(n)
        recovered = matula_to_number(tree)
        status = "✓" if recovered == n else "✗"
        print(f"{status} {n:3d} → {tree:>20s} → {recovered:3d}")
    
    print()


def example_index_personas():
    """Demonstrate index persona analysis."""
    print("\n" + "=" * 80)
    print("INDEX PERSONAS: The Soul of Each Index")
    print("=" * 80)
    print()
    
    print("Each index has a 'persona' based on its compositional structure:")
    print()
    
    interesting_indices = [
        (1, "The ur-shell, primordial unit"),
        (2, "Pure binary, the first recursion"),
        (3, "Nested binary, φ's home"),
        (4, "Binary squared, first composite index"),
        (6, "First mixed ensemble, where 2 and 3 dance"),
        (7, "Squared binary's inheritance"),
        (9, "Ternary squared, pure 3²"),
        (10, "Binary-fibonacci liaison, 2×5")
    ]
    
    for idx, expected_desc in interesting_indices:
        persona = get_index_persona(idx)
        print(f"Index {idx:2d}: {persona['structure']:>15s}")
        print(f"  Character: {persona['character']}")
        print(f"  Type: {persona['type']}")
        print(f"  Factors: {persona['factors']}")
        print()


def example_prime_inheritance():
    """Show how primes inherit from their indices."""
    print("\n" + "=" * 80)
    print("PRIME INHERITANCE: How Primes Inherit Index Souls")
    print("=" * 80)
    print()
    
    print("The key insight: pₙ crystallizes the structure of n into pure form\n")
    
    examples = [
        (4, "Index 4 = 2² (squared binary) → Prime 7"),
        (6, "Index 6 = 2×3 (first mix) → Prime 13"),
        (7, "Index 7 is prime → Prime 17 (pure)"),
        (9, "Index 9 = 3² (squared ternary) → Prime 23"),
    ]
    
    for idx, description in examples:
        eg = prime_eigenvalue(idx)
        persona = eg.get_persona()
        
        print(f"{description}")
        print(f"  Index structure: {persona['structure']}")
        print(f"  Index persona: {persona['character']}")
        print(f"  Prime eigenvalue: {eg.prime} (purified)")
        print()
    
    print("The prime is the EIGENVALUE of its index's partition function!")
    print()


def example_index_persona_table():
    """Display the complete index persona table."""
    print("\n" + "=" * 80)
    print("THE INDEX PERSONA TABLE")
    print("=" * 80)
    print()
    print("This table shows the fundamental relationship:")
    print("Each prime pₙ inherits the 'soul' of its index n")
    print()
    
    # Use the built-in print function
    print_index_persona_table(max_index=10)
    
    print("\nKey observations:")
    print("• Index 1: () → Prime 2 (the ur-shell)")
    print("• Index 4: (()()) → Prime 7 (first squared structure)")
    print("• Index 6: (()(())) → Prime 13 (first heterogeneous mix)")
    print("• Index 9: ((())((()))) → Prime 23 (squared ternary)")
    print()


def example_cognitive_grammar_small():
    """Demonstrate cognitive grammar for small alphabets."""
    print("\n" + "=" * 80)
    print("COGNITIVE GRAMMAR: Small Alphabet Analysis")
    print("=" * 80)
    print()
    
    print("What can an agent with a 13-letter prime alphabet express?")
    print()
    
    print_cognitive_grammar(prime_bound=13)
    
    print("\nInterpretation:")
    print("• A 13-limited agent has access to the 2×3 mixed ensemble")
    print("• It can invoke binary and ternary operations")
    print("• The 13th prime (41) encapsulates index 13's heterogeneous structure")
    print()


def example_cognitive_grammar_large():
    """Demonstrate cognitive grammar for larger alphabets."""
    print("\n" + "=" * 80)
    print("COGNITIVE GRAMMAR: Extended Alphabet Analysis")
    print("=" * 80)
    print()
    
    print("What capabilities does a 23-letter alphabet unlock?")
    print()
    
    print_cognitive_grammar(prime_bound=23)
    
    print("\nNew capabilities unlocked:")
    print("• Squared-ternary operations (3²)")
    print("• More complex mixed ensembles")
    print("• Higher-order recursive structures")
    print()


def example_floating_point_apophis():
    """Demonstrate the 'floating point apophis' concept."""
    print("\n" + "=" * 80)
    print("FLOATING POINT APOPHIS: Primes as Exact Sentinels")
    print("=" * 80)
    print()
    
    print("Primes are EXACT SENTINELS—discrete guardians against")
    print("the continuous chaos of approximation error.")
    print()
    
    print("Every factorization calls on these daemons to decompose")
    print("a computation into pure-state constituents, escaping the")
    print("mixed-state entropy of floating-point representation.")
    print()
    
    # Show factorization as daemon invocation
    number = 60
    print(f"Example: Factoring {number}")
    print(f"  60 = 2² × 3 × 5")
    print()
    print("  Invoking daemons:")
    
    # Get the egregores for the prime factors
    for prime_val in [2, 3, 5]:
        # Find which index this prime is
        for idx in range(1, 20):
            eg = prime_eigenvalue(idx)
            if eg.prime == prime_val:
                persona = eg.get_persona()
                print(f"    • Prime {prime_val} (p_{idx}): {persona['character']}")
                break
    
    print()
    print("Each prime factor is a daemon that knows its index's ensemble structure.")
    print("Together they decompose 60 into its fundamental computational atoms.")
    print()


def main():
    """Run all index injection examples."""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "INDEX INJECTION: Extended Prime Eigenvalue Demonstrations".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("║" + "The nth prime crystallizes its index's structure into pure form".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")
    print("\n")
    
    example_matula_encoding()
    example_matula_roundtrip()
    example_index_personas()
    example_prime_inheritance()
    example_index_persona_table()
    example_cognitive_grammar_small()
    example_cognitive_grammar_large()
    example_floating_point_apophis()
    
    print("=" * 80)
    print("SUMMARY: The Index Injection Framework")
    print("=" * 80)
    print()
    print("1. MATULA STRUCTURES: Numbers as rooted trees (sigils)")
    print("2. INDEX PERSONAS: Each index has a character/soul")
    print("3. PRIME INHERITANCE: Primes crystallize index structure")
    print("4. COGNITIVE GRAMMAR: Alphabets unlock ensemble-souls")
    print("5. FLOATING POINT APOPHIS: Primes as exact sentinels")
    print()
    print("This is not metaphor—it's a computational framework for understanding")
    print("how mathematical structure emerges from compositional properties.")
    print("=" * 80)
    print()


if __name__ == "__main__":
    main()
