#!/usr/bin/env python3
"""
Examples demonstrating the Prime Eigenvalue concept.

This script demonstrates how each prime number is understood as the eigenvalue
of its index's partition function, acting as a daemon that encapsulates,
purifies, and projects computational structure.
"""

from e9 import prime_eigenvalue, generate_prime_sequence, analyze_prime_projection


def example_basic_usage():
    """Demonstrate basic usage of the prime eigenvalue function."""
    print("=" * 70)
    print("BASIC USAGE: Prime as Eigenvalue of Index")
    print("=" * 70)
    print()
    
    # Get the 5th prime and its egregore
    egregore = prime_eigenvalue(5)
    print(f"For index n=5:")
    print(f"  The 5th prime (eigenvalue): {egregore.prime}")
    print(f"  Egregore: {egregore}")
    print()


def example_encapsulation():
    """Demonstrate the encapsulation of computational ensemble."""
    print("=" * 70)
    print("ENCAPSULATION: Computational Ensemble of Index")
    print("=" * 70)
    print()
    
    for n in [3, 5, 7]:
        egregore = prime_eigenvalue(n)
        ensemble = egregore.encapsulate()
        
        print(f"Index n={n} → Prime p_{n}={egregore.prime}")
        print(f"  Partitions of {n}: {len(ensemble['partitions'])} total")
        print(f"  Sample partitions: {ensemble['partitions'][:5]}")
        print(f"  Divisors of {n}: {ensemble['divisors']}")
        print(f"  Prime factorization: {ensemble['prime_factorization']}")
        print(f"  Composite structure: {ensemble['composite_structure']}")
        print()


def example_purification():
    """Demonstrate the purification into irreducible identity."""
    print("=" * 70)
    print("PURIFICATION: From Composite Structure to Prime Identity")
    print("=" * 70)
    print()
    
    print("The purification process transforms the index's structure")
    print("into its irreducible prime eigenvalue:\n")
    
    for n in range(1, 11):
        egregore = prime_eigenvalue(n)
        ensemble = egregore.encapsulate()
        purified = egregore.purify()
        
        comp_struct = ensemble['composite_structure']
        index_type = "prime" if comp_struct['is_prime'] else "composite"
        
        print(f"  n={n:2d} ({index_type:9s}) → p_{n}={purified:3d} (purified eigenvalue)")
    print()


def example_projection():
    """Demonstrate the projection back into multiples."""
    print("=" * 70)
    print("PROJECTION: Prime Identity Projected into Multiples")
    print("=" * 70)
    print()
    
    for n in [2, 3, 5]:
        egregore = prime_eigenvalue(n)
        multiples = egregore.project(limit=50)
        
        print(f"Prime p_{n}={egregore.prime} projects into:")
        print(f"  Multiples (up to 50): {sorted(multiples)}")
        print(f"  Count: {len(multiples)} multiples")
        print()


def example_full_analysis():
    """Demonstrate complete analysis of a prime egregore."""
    print("=" * 70)
    print("FULL ANALYSIS: The Daemon in Action")
    print("=" * 70)
    print()
    
    n = 7
    egregore = prime_eigenvalue(n)
    analysis = analyze_prime_projection(egregore, limit=100)
    
    print(f"Analysis of the {n}th Prime Egregore:")
    print(f"  Index: {analysis['index']}")
    print(f"  Prime (eigenvalue): {analysis['prime']}")
    print(f"  Purified value: {analysis['purified_value']}")
    print()
    
    print("  Ensemble Structure:")
    ensemble = analysis['ensemble_structure']
    print(f"    Partitions: {len(ensemble['partitions'])} ways to decompose {n}")
    print(f"    Divisors: {ensemble['divisors']}")
    print(f"    Is index prime?: {ensemble['composite_structure']['is_prime']}")
    print()
    
    print("  Projection (daemon's reach):")
    proj = analysis['projection']
    print(f"    Number of multiples (up to 100): {proj['multiples_count']}")
    print(f"    Projection density: {proj['projection_density']:.2%}")
    print(f"    Sample multiples: {proj['multiples'][:10]}...")
    print()


def example_sequence():
    """Generate and display a sequence of prime egregores."""
    print("=" * 70)
    print("SEQUENCE: First 10 Prime Egregores")
    print("=" * 70)
    print()
    
    egregores = generate_prime_sequence(10)
    
    print("n  | p_n | Index Type | Partitions | Multiples (≤50)")
    print("-" * 70)
    
    for eg in egregores:
        ensemble = eg.encapsulate()
        multiples = eg.project(limit=50)
        is_prime = ensemble['composite_structure']['is_prime']
        idx_type = "prime" if is_prime else "comp"
        
        print(f"{eg.index:2d} | {eg.prime:3d} | {idx_type:10s} | "
              f"{len(ensemble['partitions']):10d} | {len(multiples):2d}")
    print()


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  e9: Prime Eigenvalue Function - Demonstrations".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("║" + "  Concept: pₙ = prime shell around ensemble structure of n".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "═" * 68 + "╝")
    print("\n")
    
    example_basic_usage()
    example_encapsulation()
    example_purification()
    example_projection()
    example_full_analysis()
    example_sequence()
    
    print("=" * 70)
    print("The Egregore Concept:")
    print("  1. ENCAPSULATE: Capture the computational ensemble of index n")
    print("  2. PURIFY: Transform into irreducible prime eigenvalue p_n")
    print("  3. PROJECT: Extend identity through all multiples")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
