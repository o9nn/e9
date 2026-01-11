#!/usr/bin/env python3
"""
Examples demonstrating Structural Dimension Theory (SDT)

This script demonstrates the key concepts of SDT including:
- The three orthogonal axes (Structural, Cardinal, Relational)
- Classification of mathematical systems
- Complex numbers as relational extension of reals
- Quantum mechanics as relational geometry
- Learning as feature transport
- Recursonions and operadic fixed points
"""

from sdt import (
    # Core types
    StructuralAxis,
    CardinalAxis,
    RelationalAxis,
    SDTType,
    # Standard classifications
    COMPLEX_NUMBERS,
    QUANTUM_MECHANICS,
    BOOLEAN_LOGIC,
    REAL_NUMBERS,
    ROOTED_TREES,
    # Functions
    classify_system,
    get_all_classifications,
    create_neural_network_learning,
    create_symbolic_learning,
    create_matula_recursonion,
    create_type_universe_recursonion,
    print_sdt_summary,
)


def example_1_basic_classification():
    """Example 1: Basic system classification."""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic System Classification")
    print("=" * 70)
    
    print("\nComplex numbers (ℂ):")
    print(f"  Classification: {COMPLEX_NUMBERS}")
    print(f"  Structural: {COMPLEX_NUMBERS.structural} - no logical branching")
    print(f"  Cardinal: {COMPLEX_NUMBERS.cardinal} - dense real values")
    print(f"  Relational: {COMPLEX_NUMBERS.relational} - one orthogonal DOF (phase)")
    
    print("\nKey insight:")
    print("  ℂ is NOT 'more precise' than ℝ.")
    print("  It's ℝ extended along the RELATIONAL axis.")
    print("  Precision (cardinal) and phase (relational) are orthogonal.")


def example_2_complex_vs_real():
    """Example 2: Complex numbers are not a refinement of reals."""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Complex vs Real - Not a Refinement")
    print("=" * 70)
    
    print("\nReal Numbers (ℝ):")
    print(f"  {REAL_NUMBERS}")
    
    print("\nComplex Numbers (ℂ):")
    print(f"  {COMPLEX_NUMBERS}")
    
    print("\nComparison:")
    print(f"  Same Structural axis: {REAL_NUMBERS.structural == COMPLEX_NUMBERS.structural}")
    print(f"  Same Cardinal axis:   {REAL_NUMBERS.cardinal == COMPLEX_NUMBERS.cardinal}")
    print(f"  Same Relational axis: {REAL_NUMBERS.relational == COMPLEX_NUMBERS.relational}")
    
    print("\nConclusion:")
    print("  ℂ differs from ℝ ONLY in the relational axis.")
    print("  This is an EXTENSION (Monion → Dyonion), not a refinement.")
    print("  The precision is identical (both use ℝ cardinal values).")


def example_3_quantum_not_logic():
    """Example 3: Quantum mechanics is relational geometry, not weird logic."""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Quantum Mechanics - Relational, Not Logical")
    print("=" * 70)
    
    print("\nQuantum Mechanics:")
    print(f"  {QUANTUM_MECHANICS}")
    
    print("\nKey points:")
    print(f"  • Structural axis: {QUANTUM_MECHANICS.structural}")
    print("    → No multi-valued logic, no branching computation")
    print(f"  • Cardinal axis: {QUANTUM_MECHANICS.cardinal}")
    print("    → Probabilities and amplitudes are real-valued")
    print(f"  • Relational axis: {QUANTUM_MECHANICS.relational}")
    print("    → Noncommuting observables, phase interference")
    
    print("\nMisconception vs Reality:")
    print("  ❌ Misconception: QM involves 'quantum logic' (structural change)")
    print("  ✓ Reality: QM is relational geometry (Polynonion)")
    print("\nQuantum weirdness is RELATIONAL, not LOGICAL.")


def example_4_learning_as_transport():
    """Example 4: Learning as feature transport over ordinal graphs."""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Learning as Feature Transport")
    print("=" * 70)
    
    nn = create_neural_network_learning()
    sym = create_symbolic_learning()
    
    print("\nNeural Networks:")
    print(f"  SDT Type: {nn.sdt_type}")
    print(f"  Ordinal Graph (𝓢): {nn.ordinal_graph}")
    print(f"  Feature Space (𝓒): {nn.feature_space}")
    print(f"  Transport Law (𝓡): {nn.transport_law}")
    
    print("\nSymbolic Learning:")
    print(f"  SDT Type: {sym.sdt_type}")
    print(f"  Ordinal Graph (𝓢): {sym.ordinal_graph}")
    print(f"  Feature Space (𝓒): {sym.feature_space}")
    print(f"  Transport Law (𝓡): {sym.transport_law}")
    
    print("\nKey Insight:")
    print("  These systems operate in DIFFERENT SDT spaces.")
    print("  They are ORTHOGONAL, not competitive.")
    print("  Integration requires explicit functors between axes.")
    
    print("\nWhat this explains:")
    print("  • Why embeddings lose structure (𝓒 ≠ 𝓢)")
    print("  • Why symbolic learning fails when treated metrically")
    print("  • Why 'neuro-symbolic' must be two-layered")


def example_5_recursonion():
    """Example 5: Recursonions as operadic fixed points."""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Recursonions - Operadic Fixed Points")
    print("=" * 70)
    
    matula = create_matula_recursonion()
    
    print(f"\n{matula.name}:")
    print(f"  Operad: {matula.operad}")
    print(f"  Self-reference: {matula.self_reference}")
    
    print("\nHow it works:")
    for i, example in enumerate(matula.examples, 1):
        print(f"  {i}. {example}")
    
    print("\nWhy it's a Recursonion:")
    print("  • The encoding uses PRIMES to encode TREES")
    print("  • Primes are indexed by NATURAL NUMBERS")
    print("  • Natural numbers have TREE STRUCTURE (via Matula)")
    print("  • This creates a FIXED POINT: trees → primes → trees")
    
    print("\nClassification:")
    print(f"  e9/Matula: {ROOTED_TREES}")
    print("  The Recursonion property is visible in the RELATIONAL axis.")


def example_6_all_classifications():
    """Example 6: All standard classifications."""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: All Standard System Classifications")
    print("=" * 70)
    
    classifications = get_all_classifications()
    
    for name, sdt_type in classifications.items():
        print(f"\n{name}:")
        print(f"  {sdt_type}")


def example_7_axis_orthogonality():
    """Example 7: Demonstrating axis orthogonality."""
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Axis Orthogonality (The Core Correction)")
    print("=" * 70)
    
    print("\nCommon mistake: thinking these are refinements:")
    print("  Boolean → Real → Complex")
    print("  (as if each is 'more precise' than the last)")
    
    print("\nActual SDT classifications:")
    print(f"  Boolean: {BOOLEAN_LOGIC}")
    print(f"  Real:    {REAL_NUMBERS}")
    print(f"  Complex: {COMPLEX_NUMBERS}")
    
    print("\nWhat changed:")
    print("  Boolean → Real:")
    print("    𝓢: Binary → Unary (logical branching removed)")
    print("    𝓒: Finite → Real (precision increased)")
    print("    𝓡: Monion → Monion (no relational change)")
    
    print("\n  Real → Complex:")
    print("    𝓢: Unary → Unary (no structural change)")
    print("    𝓒: Real → Real (no precision change)")
    print("    𝓡: Monion → Dyonion (relational extension)")
    
    print("\nConclusion:")
    print("  These are movements through a 3D space, not a 1D ladder.")
    print("  Each axis is INDEPENDENT and ORTHOGONAL.")


def example_8_custom_classification():
    """Example 8: Creating a custom SDT classification."""
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Custom System Classification")
    print("=" * 70)
    
    # Create a classification for a hypothetical system
    fuzzy_logic = SDTType(
        structural=StructuralAxis.CONTINUUM_OPERADIC,
        cardinal=CardinalAxis.REAL,
        relational=RelationalAxis.MONION
    )
    
    print("\nFuzzy Logic (hypothetical):")
    print(f"  {fuzzy_logic}")
    print(f"  • Structural: {fuzzy_logic.structural.description}")
    print(f"  • Cardinal: {fuzzy_logic.cardinal.description}")
    print(f"  • Relational: {fuzzy_logic.relational.description}")
    
    print("\nReasoning:")
    print("  • Continuum-operadic: truth values form a continuum (not discrete)")
    print("  • Real: truth values in [0,1] ⊂ ℝ")
    print("  • Monion: no additional interaction structure")


def run_all_examples():
    """Run all examples in sequence."""
    print_sdt_summary()
    
    example_1_basic_classification()
    example_2_complex_vs_real()
    example_3_quantum_not_logic()
    example_4_learning_as_transport()
    example_5_recursonion()
    example_6_all_classifications()
    example_7_axis_orthogonality()
    example_8_custom_classification()
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  1. Mathematical systems live in a 3-axis space (𝓢, 𝓒, 𝓡)")
    print("  2. Complex ≠ 'more precise' than Real (different relational axis)")
    print("  3. Quantum ≠ 'weird logic' (relational geometry, not structural)")
    print("  4. Learning = transport of features over structure")
    print("  5. Neural and Symbolic are orthogonal (different axes)")
    print("  6. Recursonions = operadic fixed points (e.g., Matula encoding)")
    print("\nThe Core Insight:")
    print("  Logic defines what may exist.")
    print("  Metrics define how finely it is seen.")
    print("  Algebra defines how it interacts.")
    print()


if __name__ == '__main__':
    run_all_examples()
