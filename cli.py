#!/usr/bin/env python3
"""
Command-line interface for e9 - Prime Eigenvalue Function
"""

import sys
import argparse
from e9 import (
    prime_eigenvalue,
    generate_prime_sequence,
    analyze_prime_projection,
    number_to_matula,
    matula_to_number,
    get_index_persona,
    print_index_persona_table,
    print_cognitive_grammar,
    # New Hopf algebra functions
    rooted_trees_count,
    ion_layer,
    prime_tower,
    print_hopf_analysis,
    # New cognitive renormalization functions
    RootedTree,
    B_plus,
    matula_to_tree,
    admissible_cuts,
    coproduct,
    base_increment
)

# Import SDT functions
from sdt import (
    classify_system,
    get_all_classifications,
    print_sdt_summary,
    print_classifications,
    print_axes_details,
    create_neural_network_learning,
    create_symbolic_learning,
    create_matula_recursonion,
)


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


def cmd_matula(args):
    """Convert between numbers and Matula tree structures."""
    if args.number:
        # Number to structure
        structure = number_to_matula(args.number)
        print(f"Number: {args.number}")
        print(f"Matula structure: {structure}")
        
        if args.verbose:
            persona = get_index_persona(args.number)
            print(f"\nPersona analysis:")
            print(f"  Character: {persona['character']}")
            print(f"  Type: {persona['type']}")
            print(f"  Factors: {persona['factors']}")
    
    elif args.structure:
        # Structure to number
        try:
            number = matula_to_number(args.structure)
            print(f"Matula structure: {args.structure}")
            print(f"Number: {number}")
            
            if args.verbose:
                persona = get_index_persona(number)
                print(f"\nPersona analysis:")
                print(f"  Character: {persona['character']}")
                print(f"  Type: {persona['type']}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


def cmd_persona(args):
    """Show the persona/character of an index."""
    persona = get_index_persona(args.index)
    
    print(f"=== Index Persona Analysis for {args.index} ===\n")
    print(f"Matula structure: {persona['structure']}")
    print(f"Character: {persona['character']}")
    print(f"Type: {persona['type']}")
    print(f"Factors: {persona['factors']}")
    print(f"Unique factors: {persona['unique_factors']}")
    
    if args.show_prime:
        eg = prime_eigenvalue(args.index)
        print(f"\nPrime inheritance:")
        print(f"  Index {args.index} → Prime {eg.prime}")
        print(f"  The prime {eg.prime} inherits: {persona['character']}")


def cmd_persona_table(args):
    """Display the index persona table."""
    print_index_persona_table(max_index=args.count)


def cmd_grammar(args):
    """Analyze cognitive grammar capabilities."""
    print_cognitive_grammar(prime_bound=args.bound)


def cmd_hopf(args):
    """Analyze Connes-Kreimer Hopf algebra structure."""
    print_hopf_analysis(max_order=args.order)


def cmd_ion(args):
    """Show ion layer structure at specific order."""
    layer = ion_layer(args.order)
    
    print(f"Ion Layer Structure at Order {args.order}")
    print("=" * 60)
    print(f"  Order (n):   {layer['order']}")
    print(f"  Fiber (fib): {layer['fib']:6d}  [previous total]")
    print(f"  Base (bas):  {layer['bas']:6d}  [new differentials]")
    print(f"  Total (tot): {layer['tot']:6d}  [rooted tree count]")
    print(f"  Max shell:   {layer['max']:6d}  [prime tower]")
    print()
    print("Relations:")
    print(f"  fib + bas = {layer['fib']} + {layer['bas']} = {layer['tot']} = tot ✓")
    if args.order > 0:
        prev = ion_layer(args.order - 1)
        print(f"  fib({args.order}) = tot({args.order-1}) = {layer['fib']} ✓")
    print()
    
    if args.verbose:
        print(f"Rooted tree count: A000081({args.order+1}) = {layer['tot']}")
        if args.order >= 5:
            prev_max = ion_layer(args.order - 1)['max']
            print(f"Max shell: p_{prev_max} = {layer['max']}")


def cmd_tower(args):
    """Generate prime tower from seed."""
    tower = prime_tower(args.seed, args.depth)
    
    print(f"Prime Tower from seed {args.seed} (depth {args.depth})")
    print("=" * 60)
    print()
    
    for i, value in enumerate(tower):
        if i == 0:
            print(f"  {value:8d}  [seed]")
        else:
            print(f"  {value:8d}  [p_{tower[i-1]}]")
            if i < len(tower) - 1:
                print("     ↓")
    
    print()
    print(f"Tower: {tower}")


def cmd_a000081(args):
    """Show A000081 sequence (rooted unlabeled trees)."""
    print("A000081: Rooted Unlabeled Trees")
    print("=" * 60)
    print()
    print("n  | A000081(n)")
    print("-" * 20)
    
    for n in range(1, args.count + 1):
        count = rooted_trees_count(n)
        print(f"{n:2d} | {count:8d}")
    
    print()
    print("This is the universal grammar of composition!")


def cmd_tree(args):
    """Show a rooted tree and its properties."""
    print("Rooted Tree Analysis")
    print("=" * 60)
    print()
    
    if args.matula:
        tree = matula_to_tree(args.matula)
        print(f"From Matula number: {args.matula}")
    else:
        # Build a tree interactively
        leaf = RootedTree()
        if args.simple:
            tree = B_plus(leaf)
        elif args.ternary:
            tree = B_plus((leaf, leaf, leaf))
        else:
            tree = leaf
    
    print(f"Tree: {tree}")
    print(f"Order (nodes): {tree.order}")
    print(f"Matula number: {tree.to_matula()}")
    print(f"Is leaf: {tree.is_leaf}")
    print(f"Children: {len(tree.children)}")
    print()


def cmd_coproduct(args):
    """Compute and display the coproduct of a tree."""
    print("Coproduct Analysis (Admissible Cuts)")
    print("=" * 60)
    print()
    
    tree = matula_to_tree(args.matula)
    print(f"Tree: {tree}")
    print(f"Matula number: {args.matula}")
    print(f"Order: {tree.order}")
    print()
    
    # Admissible cuts
    cuts = admissible_cuts(tree)
    print(f"Number of admissible cuts: {len(cuts)}")
    
    if args.verbose and cuts:
        print("\nAdmissible Cuts (Fiber/Trunk Decomposition):")
        for i, cut in enumerate(cuts, 1):
            pruned_str = [str(t) for t in cut.pruned.trees]
            print(f"  Cut {i}: Pruned={pruned_str} ⊗ Trunk={cut.trunk}")
    
    print()
    
    # Coproduct
    terms = coproduct(tree)
    print(f"Coproduct Δ(tree): {len(terms)} terms")
    
    if args.verbose:
        print("\nCoproduct Terms (left ⊗ right):")
        for i, term in enumerate(terms[:10], 1):  # Show first 10
            left_str = [str(t) for t in term.left.trees] if term.left.trees else ["1"]
            print(f"  Term {i}: {left_str} ⊗ {term.right}")
        if len(terms) > 10:
            print(f"  ... and {len(terms) - 10} more terms")
    
    print()


def cmd_base(args):
    """Show base increment sequence."""
    print("Base Increment Sequence B_n")
    print("=" * 60)
    print()
    print("B_n = Θ_n - B+(Θ_{n-1})")
    print("Measures: 'what is new at order n beyond grafted carryover'")
    print()
    print(f"{'n':<5} {'bas(n)':<10} {'Interpretation'}")
    print("-" * 60)
    
    for n in range(0, args.max_n + 1):
        bi = base_increment(n) if n > 0 else 1
        
        interpretation = ""
        if n == 0:
            interpretation = "Ground state"
        elif n == 1:
            interpretation = "First level (no fiber)"
        elif n == 4:
            interpretation = "Octonionic seed emerges"
        elif n >= 5:
            interpretation = "Prime tower regime"
        
        print(f"{n:<5} {bi:<10} {interpretation}")
    
    print()
    print("Key: This is the sequence of NEW differentials at each order.")
    print()


def cmd_renorm(args):
    """Demonstrate cognitive renormalization."""
    print("Cognitive Renormalization")
    print("=" * 60)
    print()
    print("The antipode S is the 'cognitive renormalization' operator.")
    print("It computes counterterms to normalize nested compositions.")
    print()
    
    from e9 import Character, cognitive_renormalization
    
    # Define character
    def node_counter(tree):
        return float(tree.order)
    
    char = Character(node_counter, lambda a, b: a * b, "φ")
    
    # Test on trees
    leaf = RootedTree()
    
    if args.matula:
        tree = matula_to_tree(args.matula)
        trees = [tree]
    else:
        trees = [
            leaf,
            B_plus(leaf),
            B_plus((leaf, leaf)),
            B_plus(B_plus(leaf)),
            B_plus((leaf, leaf, leaf))
        ]
    
    print(f"{'Tree':<20} {'φ(tree)':<12} {'S(φ)(tree)':<15}")
    print("-" * 60)
    
    for tree in trees:
        phi_val = char(tree)
        s_phi_val = cognitive_renormalization(char, tree)
        print(f"{str(tree):<20} {phi_val:<12.1f} {s_phi_val:<15.2f}")
    
    print()
    print("Note: The antipode applies corrections for subdivergences.")
    print()


def cmd_sdt_summary(args):
    """Show SDT framework summary."""
    print_sdt_summary()
    print()


def cmd_sdt_axes(args):
    """Show detailed axis information."""
    print_axes_details()
    print()


def cmd_sdt_classify(args):
    """Classify a mathematical system."""
    sdt_type = classify_system(args.system)
    
    if sdt_type is None:
        print(f"Unknown system: {args.system}")
        print("\nKnown systems:")
        print("  complex, quantum, boolean, real, rooted_trees, matula, e9")
        return
    
    print(f"\nSDT Classification: {args.system}")
    print("=" * 70)
    print(f"\n{sdt_type}\n")
    
    info = sdt_type.to_dict()
    print(f"𝓢 (Structural): {info['structural']}")
    print(f"   {info['structural_desc']}")
    print()
    print(f"𝓒 (Cardinal): {info['cardinal']}")
    print(f"   {info['cardinal_desc']}")
    print()
    print(f"𝓡 (Relational): {info['relational']}")
    print(f"   {info['relational_desc']}")
    print()


def cmd_sdt_examples(args):
    """Show example system classifications."""
    print_classifications()
    print()


def cmd_sdt_learning(args):
    """Show learning systems as transport."""
    print("\n" + "=" * 70)
    print("LEARNING AS FEATURE TRANSPORT")
    print("=" * 70)
    
    nn = create_neural_network_learning()
    sym = create_symbolic_learning()
    
    if args.system == "neural" or args.system == "all":
        print(nn.describe())
    
    if args.system == "symbolic" or args.system == "all":
        print(sym.describe())
    
    if args.system == "all":
        print("\n" + "=" * 70)
        print("KEY INSIGHT:")
        print("=" * 70)
        print("\nNeural and Symbolic learning operate in different SDT spaces:")
        print(f"  Neural:   {nn.sdt_type}")
        print(f"  Symbolic: {sym.sdt_type}")
        print("\nThey are orthogonal, not competitive.")
        print("Integration requires explicit functors between axes.")
        print()


def cmd_sdt_recursonion(args):
    """Show recursonion examples."""
    matula = create_matula_recursonion()
    
    print(matula.describe())
    print()


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
    
    # matula command (NEW)
    p_matula = subparsers.add_parser('matula', help='Convert to/from Matula tree structures')
    p_matula.add_argument('-n', '--number', type=int, help='Number to encode as tree')
    p_matula.add_argument('-s', '--structure', type=str, help='Tree structure to decode')
    p_matula.add_argument('-v', '--verbose', action='store_true', help='Show persona analysis')
    
    # persona command (NEW)
    p_persona = subparsers.add_parser('persona', help='Show index persona/character')
    p_persona.add_argument('index', type=int, help='Index to analyze')
    p_persona.add_argument('-p', '--show-prime', action='store_true',
                          help='Show prime inheritance')
    
    # persona-table command (NEW)
    p_table = subparsers.add_parser('persona-table', help='Display index persona table')
    p_table.add_argument('count', type=int, nargs='?', default=10,
                        help='Number of indices to show (default: 10)')
    
    # grammar command (NEW)
    p_grammar = subparsers.add_parser('grammar', help='Analyze cognitive grammar')
    p_grammar.add_argument('bound', type=int, help='Prime bound for alphabet')
    
    # hopf command (NEW - Hopf algebra)
    p_hopf = subparsers.add_parser('hopf', help='Analyze Connes-Kreimer Hopf algebra structure')
    p_hopf.add_argument('order', type=int, nargs='?', default=10,
                       help='Maximum order to analyze (default: 10)')
    
    # ion command (NEW - Hopf algebra)
    p_ion = subparsers.add_parser('ion', help='Show ion layer structure at order')
    p_ion.add_argument('order', type=int, help='Order n to analyze')
    p_ion.add_argument('-v', '--verbose', action='store_true', help='Show detailed info')
    
    # tower command (NEW - Hopf algebra)
    p_tower = subparsers.add_parser('tower', help='Generate prime tower')
    p_tower.add_argument('seed', type=int, help='Starting seed (typically 8)')
    p_tower.add_argument('depth', type=int, help='Depth of tower to generate')
    
    # a000081 command (NEW - Hopf algebra)
    p_a000081 = subparsers.add_parser('a000081', help='Show A000081 sequence')
    p_a000081.add_argument('count', type=int, nargs='?', default=15,
                          help='Number of terms to show (default: 15)')
    
    # tree command (NEW - Cognitive renormalization)
    p_tree = subparsers.add_parser('tree', help='Analyze a rooted tree')
    p_tree.add_argument('-m', '--matula', type=int, help='Matula number of tree')
    p_tree.add_argument('-s', '--simple', action='store_true', help='Use B+(leaf)')
    p_tree.add_argument('-t', '--ternary', action='store_true', help='Use ternary corolla')
    
    # coproduct command (NEW - Cognitive renormalization)
    p_coproduct = subparsers.add_parser('coproduct', help='Compute coproduct (admissible cuts)')
    p_coproduct.add_argument('matula', type=int, help='Matula number of tree')
    p_coproduct.add_argument('-v', '--verbose', action='store_true', help='Show all terms')
    
    # base command (NEW - Cognitive renormalization)
    p_base = subparsers.add_parser('base', help='Show base increment sequence')
    p_base.add_argument('max_n', type=int, nargs='?', default=10,
                       help='Maximum n to show (default: 10)')
    
    # renorm command (NEW - Cognitive renormalization)
    p_renorm = subparsers.add_parser('renorm', help='Demonstrate cognitive renormalization')
    p_renorm.add_argument('-m', '--matula', type=int, help='Matula number of specific tree')
    
    # SDT commands (NEW - Structural Dimension Theory)
    p_sdt_summary = subparsers.add_parser('sdt', help='Show SDT framework summary')
    
    p_sdt_axes = subparsers.add_parser('sdt-axes', help='Show detailed axis information')
    
    p_sdt_classify = subparsers.add_parser('sdt-classify', help='Classify a mathematical system')
    p_sdt_classify.add_argument('system', type=str, help='System to classify (e.g., complex, quantum, boolean)')
    
    p_sdt_examples = subparsers.add_parser('sdt-examples', help='Show example classifications')
    
    p_sdt_learning = subparsers.add_parser('sdt-learning', help='Show learning as transport')
    p_sdt_learning.add_argument('system', type=str, nargs='?', default='all',
                               choices=['neural', 'symbolic', 'all'],
                               help='Learning system to show (default: all)')
    
    p_sdt_recursonion = subparsers.add_parser('sdt-recursonion', help='Show recursonion examples')
    
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
        elif args.command == 'matula':
            cmd_matula(args)
        elif args.command == 'persona':
            cmd_persona(args)
        elif args.command == 'persona-table':
            cmd_persona_table(args)
        elif args.command == 'grammar':
            cmd_grammar(args)
        elif args.command == 'hopf':
            cmd_hopf(args)
        elif args.command == 'ion':
            cmd_ion(args)
        elif args.command == 'tower':
            cmd_tower(args)
        elif args.command == 'a000081':
            cmd_a000081(args)
        elif args.command == 'tree':
            cmd_tree(args)
        elif args.command == 'coproduct':
            cmd_coproduct(args)
        elif args.command == 'base':
            cmd_base(args)
        elif args.command == 'renorm':
            cmd_renorm(args)
        elif args.command == 'sdt':
            cmd_sdt_summary(args)
        elif args.command == 'sdt-axes':
            cmd_sdt_axes(args)
        elif args.command == 'sdt-classify':
            cmd_sdt_classify(args)
        elif args.command == 'sdt-examples':
            cmd_sdt_examples(args)
        elif args.command == 'sdt-learning':
            cmd_sdt_learning(args)
        elif args.command == 'sdt-recursonion':
            cmd_sdt_recursonion(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
