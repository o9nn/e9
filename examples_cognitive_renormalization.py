#!/usr/bin/env python3
"""
Examples demonstrating Cognitive Renormalization & Prime Lift Theorems

This module demonstrates the implementation of the Connes-Kreimer Hopf algebra
structures for the e9 library, including:

1. Rooted trees as basis elements
2. The coproduct Δ (admissible cuts)
3. The antipode S (cognitive renormalization)
4. Characters and convolution
5. The B+ grafting operator (prime lift)
6. Base increments and the inevitability chain
"""

from e9 import (
    RootedTree,
    Forest,
    admissible_cuts,
    coproduct,
    antipode,
    Character,
    cognitive_renormalization,
    B_plus,
    theta_n,
    base_increment,
    matula_to_tree,
    tree_to_matula,
    rooted_trees_count,
    ion_layer,
    prime_tower
)


def example_1_rooted_trees():
    """Example 1: Creating and working with rooted trees."""
    print("=" * 80)
    print("EXAMPLE 1: Rooted Trees as Basis Elements")
    print("=" * 80)
    print()
    
    # Create a leaf (single node)
    leaf = RootedTree()
    print(f"Leaf: {leaf}")
    print(f"  Order (number of nodes): {leaf.order}")
    print(f"  Matula number: {leaf.to_matula()}")
    print()
    
    # Create B+(leaf) - a tree with one child
    tree2 = B_plus(leaf)
    print(f"B+(leaf): {tree2}")
    print(f"  Order: {tree2.order}")
    print(f"  Matula number: {tree2.to_matula()}")
    print()
    
    # Create the ternary corolla (octonionic seed)
    corolla = B_plus((leaf, leaf, leaf))
    print(f"Ternary corolla B+(leaf, leaf, leaf): {corolla}")
    print(f"  Order: {corolla.order}")
    print(f"  Matula number: {corolla.to_matula()} (the octonionic seed!)")
    print()
    
    # Build a tower by iterated grafting
    print("Prime Tower (Iterated B+ application):")
    t = leaf
    for i in range(5):
        matula = t.to_matula()
        print(f"  Step {i}: {t} → Matula = {matula}")
        t = B_plus(t)
    print()


def example_2_admissible_cuts():
    """Example 2: Admissible cuts and the coproduct."""
    print("=" * 80)
    print("EXAMPLE 2: Admissible Cuts & The Coproduct Δ")
    print("=" * 80)
    print()
    
    leaf = RootedTree()
    tree = B_plus((leaf, leaf))  # Tree with 2 children
    
    print(f"Tree: {tree}")
    print(f"Order: {tree.order}")
    print()
    
    # Get admissible cuts
    cuts = admissible_cuts(tree)
    print(f"Number of admissible cuts: {len(cuts)}")
    print()
    
    print("Admissible cuts (fiber/trunk decomposition):")
    for i, cut in enumerate(cuts, 1):
        print(f"  Cut {i}:")
        print(f"    Pruned (fiber): {[str(t) for t in cut.pruned.trees]}")
        print(f"    Trunk (base): {cut.trunk}")
    print()
    
    # Compute coproduct
    print("Coproduct Δ(tree):")
    terms = coproduct(tree)
    print(f"Number of terms: {len(terms)}")
    for i, term in enumerate(terms[:5], 1):  # Show first 5
        left_str = [str(t) for t in term.left.trees] if term.left.trees else ["1"]
        print(f"  Term {i}: {left_str} ⊗ {term.right}")
    if len(terms) > 5:
        print(f"  ... and {len(terms) - 5} more terms")
    print()


def example_3_cognitive_renormalization():
    """Example 3: Cognitive renormalization via the antipode."""
    print("=" * 80)
    print("EXAMPLE 3: Cognitive Renormalization (The Antipode S)")
    print("=" * 80)
    print()
    
    print("The antipode S is the 'cognitive renormalization' operator.")
    print("It computes counterterms to normalize nested compositions.")
    print()
    
    # Define a simple character: count nodes
    def node_counter(tree):
        return float(tree.order)
    
    char = Character(node_counter, lambda a, b: a * b, "node_count")
    
    # Test on various trees
    leaf = RootedTree()
    trees = [
        leaf,
        B_plus(leaf),
        B_plus((leaf, leaf)),
        B_plus(B_plus(leaf))
    ]
    
    print("Character φ: counts nodes in the tree")
    print()
    print(f"{'Tree':<20} {'φ(tree)':<10} {'S(φ)(tree)':<15} {'Interpretation'}")
    print("-" * 80)
    
    for tree in trees:
        phi_val = char(tree)
        s_phi_val = cognitive_renormalization(char, tree)
        
        interpretation = ""
        if tree.is_leaf:
            interpretation = "Pure element (negated)"
        elif len(tree.children) == 1:
            interpretation = "Linear composition"
        else:
            interpretation = f"{len(tree.children)}-way branching"
        
        print(f"{str(tree):<20} {phi_val:<10.1f} {s_phi_val:<15.2f} {interpretation}")
    
    print()
    print("Note: The antipode applies negative signs and recursive corrections")
    print("to account for all subdivergences (admissible cuts).")
    print()


def example_4_character_convolution():
    """Example 4: Convolution of characters."""
    print("=" * 80)
    print("EXAMPLE 4: Character Convolution (φ * ψ)")
    print("=" * 80)
    print()
    
    print("Characters form a group under convolution:")
    print("  (φ * ψ)(tree) = Σ φ(left) · ψ(right)")
    print("where the sum is over coproduct terms left⊗right in Δ(tree)")
    print()
    
    # Define two characters
    def count_nodes(tree):
        return tree.order
    
    def constant_one(tree):
        return 1
    
    char1 = Character(count_nodes, lambda a, b: a * b, "φ")
    char2 = Character(constant_one, lambda a, b: a * b, "ψ")
    
    # Convolve them
    conv_char = char1.convolve(char2)
    
    print(f"Character φ: counts nodes")
    print(f"Character ψ: returns 1 (unit)")
    print(f"Convolution φ*ψ:")
    print()
    
    leaf = RootedTree()
    trees = [leaf, B_plus(leaf), B_plus((leaf, leaf))]
    
    for tree in trees:
        val1 = char1(tree)
        val2 = char2(tree)
        conv_val = conv_char(tree)
        print(f"  Tree {tree}:")
        print(f"    φ(tree) = {val1}")
        print(f"    ψ(tree) = {val2}")
        print(f"    (φ*ψ)(tree) = {conv_val}")
        print()


def example_5_base_increments():
    """Example 5: Base increments and the inevitability chain."""
    print("=" * 80)
    print("EXAMPLE 5: Base Increments B_n (The Inevitability Chain)")
    print("=" * 80)
    print()
    
    print("Base increment B_n = Θ_n - B+(Θ_{n-1})")
    print("Measures: 'what is new at order n beyond grafted carryover'")
    print()
    
    print(f"{'n':<5} {'tot(n)':<10} {'fib(n)':<10} {'bas(n)':<10} {'max(n)':<10} {'Meaning'}")
    print("-" * 80)
    
    for n in range(0, 10):
        layer = ion_layer(n)
        
        meaning = ""
        if n == 0:
            meaning = "Ground state"
        elif n == 1:
            meaning = "First level (no fiber)"
        elif n == 4:
            meaning = "Octonionic seed emerges"
        elif n >= 5:
            meaning = "Prime tower regime"
        
        print(f"{n:<5} {layer['tot']:<10} {layer['fib']:<10} "
              f"{layer['bas']:<10} {layer['max']:<10} {meaning}")
    
    print()
    print("Key Insight:")
    print("  • tot(n) = A000081(n+1): Total rooted trees at order n")
    print("  • fib(n) = tot(n-1): Fiber (previous total)")
    print("  • bas(n) = tot(n) - fib(n): New differentials at this order")
    print("  • max(n): Prime tower (iterated p_n indexing)")
    print()
    print("The 'inevitability chain': Once you have iterated composition,")
    print("rooted trees are forced. Their structure is the universal grammar.")
    print()


def example_6_theta_enumeration():
    """Example 6: Explicit tree enumeration via Θ_n."""
    print("=" * 80)
    print("EXAMPLE 6: Tree Enumeration via Θ_n")
    print("=" * 80)
    print()
    
    print("Θ_n: all rooted trees with exactly n nodes (A000081)")
    print()
    
    for n in [1, 2, 3, 4]:
        count = rooted_trees_count(n + 1)
        print(f"Order n={n}: A000081({n+1}) = {count} trees")
        
        try:
            trees = theta_n(n)
            print(f"  Explicit enumeration:")
            for i, tree in enumerate(trees, 1):
                print(f"    Tree {i}: {tree} (Matula = {tree.to_matula()})")
        except NotImplementedError:
            print(f"  (Explicit enumeration not implemented for n > 4)")
        print()
    
    print("Note: For n > 4, explicit enumeration becomes combinatorially complex.")
    print("We use counts via A000081 instead.")
    print()


def example_7_prime_lift_theorem():
    """Example 7: The Prime Lift Theorem."""
    print("=" * 80)
    print("EXAMPLE 7: The Prime Lift Theorem")
    print("=" * 80)
    print()
    
    print("Theorem: The 'prime-lift' objects form the B+-closure of the")
    print("         ternary corolla inside H_CK (Connes-Kreimer Hopf algebra)")
    print()
    
    # Start with octonionic seed
    leaf = RootedTree()
    seed = B_plus((leaf, leaf, leaf))
    
    print(f"Octonionic seed (ternary corolla): {seed}")
    print(f"  Matula number: {seed.to_matula()}")
    print()
    
    print("Prime tower (iterated B+ application):")
    tower_matula = prime_tower(8, 5)
    
    current = seed
    for i, matula in enumerate(tower_matula):
        if i == 0:
            print(f"  Level {i}: {current} → Matula = {matula} (seed)")
        else:
            current = B_plus(current)
            print(f"  Level {i}: (nested) → Matula = {matula} (= p_{tower_matula[i-1]})")
    
    print()
    print("Key insight: B+ is the grafting operator that 'adds a root'")
    print("In Matula coordinates: graft(tree) = p_M(tree)")
    print("This creates the 'shell structure' beyond division algebras.")
    print()


def example_8_universal_property():
    """Example 8: The Universal Property."""
    print("=" * 80)
    print("EXAMPLE 8: The Universal Property (Why This is Inevitable)")
    print("=" * 80)
    print()
    
    print("Universal Property of Rooted Trees:")
    print()
    print("1. Rooted trees are the canonical basis for the free pre-Lie algebra")
    print("2. Pre-Lie algebras govern 'insert into' operations")
    print("3. The Connes-Kreimer Hopf algebra is the enveloping algebra")
    print()
    print("Consequence: Once you assume 'iterated operator products with")
    print("insertion-like composition,' you are FORCED into rooted trees.")
    print()
    print("The Inevitability Chain:")
    print()
    print("  Division Algebras (R, C, H, O)")
    print("       ↓")
    print("  Privileged ternary corolla at 8 (triality)")
    print("       ↓")
    print("  Adding composite branching forces full rooted-tree operad")
    print("       ↓")
    print("  Rooted-tree operads demand prime factor coordinates (Matula)")
    print("       ↓")
    print("  Prime powers = natural stratification of composition depth")
    print()
    print("A000081 is not interpretive. It is the universal grammar")
    print("that both geometry (via octonions) and dynamics (via trees)")
    print("must speak.")
    print()


def main():
    """Run all examples."""
    examples = [
        example_1_rooted_trees,
        example_2_admissible_cuts,
        example_3_cognitive_renormalization,
        example_4_character_convolution,
        example_5_base_increments,
        example_6_theta_enumeration,
        example_7_prime_lift_theorem,
        example_8_universal_property,
    ]
    
    for example in examples:
        example()
        input("Press Enter to continue to next example...\n")


if __name__ == '__main__':
    main()
