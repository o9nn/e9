#!/usr/bin/env python3
"""
Command-line interface for e9 - Prime Eigenvalue Function
"""

import sys
import argparse
from e9 import prime_eigenvalue, generate_prime_sequence, analyze_prime_projection


def cmd_eigenvalue(args):
    """Get the prime eigenvalue for a given index."""
    egregore = prime_eigenvalue(args.index)
    print(f"Index: {egregore.index}")
    print(f"Prime eigenvalue: {egregore.prime}")
    
    if args.verbose:
        print("\nEncapsulated ensemble:")
        ensemble = egregore.encapsulate()
        print(f"  Partitions: {len(ensemble['partitions'])}")
        print(f"  Divisors: {ensemble['divisors']}")
        print(f"  Prime factorization of index: {ensemble['prime_factorization']}")
        print(f"  Composite structure: {ensemble['composite_structure']}")


def cmd_sequence(args):
    """Generate a sequence of prime egregores."""
    egregores = generate_prime_sequence(args.count)
    
    if args.format == 'simple':
        for eg in egregores:
            print(f"{eg.index}: {eg.prime}")
    else:
        print(f"{'Index':>5} | {'Prime':>5} | {'Partitions':>10}")
        print("-" * 30)
        for eg in egregores:
            ensemble = eg.encapsulate()
            print(f"{eg.index:5d} | {eg.prime:5d} | {len(ensemble['partitions']):10d}")


def cmd_analyze(args):
    """Perform full analysis on a prime egregore."""
    egregore = prime_eigenvalue(args.index)
    analysis = analyze_prime_projection(egregore, limit=args.limit)
    
    print(f"=== Analysis of Prime Egregore at Index {args.index} ===\n")
    print(f"Prime eigenvalue: {analysis['prime']}")
    print(f"Purified value: {analysis['purified_value']}")
    
    print("\nEnsemble Structure:")
    ensemble = analysis['ensemble_structure']
    print(f"  Partitions: {len(ensemble['partitions'])} ways to decompose {args.index}")
    print(f"  Divisors: {ensemble['divisors']}")
    print(f"  Prime factorization: {ensemble['prime_factorization']}")
    print(f"  Index is prime: {ensemble['composite_structure']['is_prime']}")
    
    print("\nProjection (Daemon's Reach):")
    proj = analysis['projection']
    print(f"  Multiples (up to {args.limit}): {proj['multiples_count']}")
    print(f"  Projection density: {proj['projection_density']:.2%}")
    
    if args.show_multiples:
        print(f"  Multiples: {proj['multiples'][:20]}")
        if len(proj['multiples']) > 20:
            print(f"  ... and {len(proj['multiples']) - 20} more")


def cmd_daemon(args):
    """Show the three-phase daemon process."""
    egregore = prime_eigenvalue(args.index)
    
    print(f"=== Prime Egregore Daemon Process for Index {args.index} ===\n")
    
    print("Phase 1: ENCAPSULATE")
    print("  Capturing computational ensemble of index...")
    ensemble = egregore.encapsulate()
    print(f"  ✓ Partitions: {len(ensemble['partitions'])}")
    print(f"  ✓ Divisors: {ensemble['divisors']}")
    print(f"  ✓ Structure: {ensemble['composite_structure']}")
    
    print("\nPhase 2: PURIFY")
    print("  Transforming into irreducible eigenvalue...")
    prime = egregore.purify()
    print(f"  ✓ Prime eigenvalue: {prime}")
    
    print("\nPhase 3: PROJECT")
    print(f"  Projecting identity through multiples (up to {args.limit})...")
    multiples = egregore.project(limit=args.limit)
    print(f"  ✓ Multiples: {sorted(multiples)[:10]}")
    if len(multiples) > 10:
        print(f"  ✓ ... and {len(multiples) - 10} more")
    print(f"  ✓ Total reach: {len(multiples)} numbers")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='e9 - Prime Eigenvalue Function CLI',
        epilog='Concept: pₙ = prime shell around ensemble structure of n'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # eigenvalue command
    p_eigen = subparsers.add_parser('eigenvalue', help='Get prime eigenvalue for index')
    p_eigen.add_argument('index', type=int, help='Index n (1-indexed)')
    p_eigen.add_argument('-v', '--verbose', action='store_true', help='Show detailed info')
    
    # sequence command
    p_seq = subparsers.add_parser('sequence', help='Generate prime sequence')
    p_seq.add_argument('count', type=int, help='Number of primes to generate')
    p_seq.add_argument('-f', '--format', choices=['simple', 'table'], default='table',
                      help='Output format')
    
    # analyze command
    p_analyze = subparsers.add_parser('analyze', help='Full analysis of prime egregore')
    p_analyze.add_argument('index', type=int, help='Index n (1-indexed)')
    p_analyze.add_argument('-l', '--limit', type=int, default=100,
                          help='Limit for multiples (default: 100)')
    p_analyze.add_argument('-m', '--show-multiples', action='store_true',
                          help='Show list of multiples')
    
    # daemon command
    p_daemon = subparsers.add_parser('daemon', help='Show daemon process phases')
    p_daemon.add_argument('index', type=int, help='Index n (1-indexed)')
    p_daemon.add_argument('-l', '--limit', type=int, default=100,
                         help='Limit for projection (default: 100)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == 'eigenvalue':
            cmd_eigenvalue(args)
        elif args.command == 'sequence':
            cmd_sequence(args)
        elif args.command == 'analyze':
            cmd_analyze(args)
        elif args.command == 'daemon':
            cmd_daemon(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
