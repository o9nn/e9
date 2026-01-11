"""
Structural Dimension Theory (SDT) - Ordo ab Neuro, Radix ex Matula

A framework for classifying mathematical and computational systems along three 
independent orthogonal axes, none of which refines the others.

Core Axioms:
1. Structural Primacy: All systems possess ordinal structure independent of metric measure
2. Cardinal Decoration: Metrics quantify degrees within fixed structure; they do not define it
3. Relational Mediation: Interaction is governed by algebraic structure orthogonal to logic and measure
4. Axis Orthogonality: Structural, cardinal, and relational axes are independent
5. Learning as Transport: Learning is feature transport over ordinal graphs under relational constraints

Key Insight:
    Boolean, Real, and Complex are not stages of refinement.
    They are coordinates in a three-axis space of meaning.
    
    Logic defines what may exist.
    Metrics define how finely it is seen.
    Algebra defines how it interacts.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto


# ============================================================================
# Axis 𝓢 — Structural / Ordinal Axis
# ============================================================================

class StructuralAxis(Enum):
    """
    Structural (Ordinal) Axis: What compositions are admissible?
    
    This axis is categorical, operadic, and logical.
    Elements of 𝓢 are arity systems, not values.
    
    Key property: 𝓢 defines what can exist and compose.
    Metrics are meaningless without it.
    """
    UNARY = "unary"
    BINARY = "binary"
    TERNARY = "ternary"
    N_ARY = "n_ary"
    SELF_SIMILAR = "self_similar"
    FRACTAL = "fractal"
    CONTINUUM_OPERADIC = "continuum_operadic"
    
    def __str__(self) -> str:
        return self.value.replace("_", " ").title()
    
    @property
    def description(self) -> str:
        """Get description of this structural axis value."""
        descriptions = {
            StructuralAxis.UNARY: "Single compositional stream, no logical branching",
            StructuralAxis.BINARY: "Boolean logic, two-way branching (true/false)",
            StructuralAxis.TERNARY: "Three-way branching, triadic composition",
            StructuralAxis.N_ARY: "Finite n-way branching for arbitrary n",
            StructuralAxis.SELF_SIMILAR: "Recursive self-similar structure",
            StructuralAxis.FRACTAL: "Infinite self-similarity at all scales",
            StructuralAxis.CONTINUUM_OPERADIC: "Continuous arity systems, limit structures"
        }
        return descriptions[self]


# ============================================================================
# Axis 𝓒 — Cardinal / Feature Axis
# ============================================================================

class CardinalAxis(Enum):
    """
    Cardinal (Feature / Resolution) Axis: How finely can differences be resolved?
    
    This axis is metric, measurable, quantitative.
    
    Key property: 𝓒 decorates structure with degree, not meaning.
    """
    FINITE = "finite"
    NATURAL = "natural"
    INTEGER = "integer"
    RATIONAL = "rational"
    REAL = "real"
    MEASURE_SPACE = "measure_space"
    DISTRIBUTION = "distribution"
    
    def __str__(self) -> str:
        return self.value.replace("_", " ").title()
    
    @property
    def description(self) -> str:
        """Get description of this cardinal axis value."""
        descriptions = {
            CardinalAxis.FINITE: "Finite discrete values",
            CardinalAxis.NATURAL: "ℕ - Counting numbers",
            CardinalAxis.INTEGER: "ℤ - Signed integers",
            CardinalAxis.RATIONAL: "ℚ - Ratio/fraction precision",
            CardinalAxis.REAL: "ℝ - Dense continuous values",
            CardinalAxis.MEASURE_SPACE: "Measure-theoretic quantification",
            CardinalAxis.DISTRIBUTION: "Probabilistic/distributional resolution"
        }
        return descriptions[self]


# ============================================================================
# Axis 𝓡 — Relational / Interaction Axis
# ============================================================================

class RelationalAxis(Enum):
    """
    Relational (Interaction) Axis: How do entities interfere, transform, and relate?
    
    This axis is algebraic, geometric, topological.
    
    Key property: 𝓡 defines interaction semantics, not precision.
    """
    MONION = "monion"
    DYONION = "dyonion"
    TRIONION = "trionion"
    POLYNONION = "polynonion"
    RECURSONION = "recursonion"
    
    def __str__(self) -> str:
        return self.value.title()
    
    @property
    def description(self) -> str:
        """Get description of this relational axis value."""
        descriptions = {
            RelationalAxis.MONION: "Scalar identity, no orthogonal structure",
            RelationalAxis.DYONION: "One orthogonal DOF (e.g., ℂ with i²=-1)",
            RelationalAxis.TRIONION: "Triadic phase, three-way interaction",
            RelationalAxis.POLYNONION: "Higher phase systems, noncommuting observables",
            RelationalAxis.RECURSONION: "Self-referential interaction, operadic fixed points"
        }
        return descriptions[self]


# ============================================================================
# SDT System Classification
# ============================================================================

@dataclass(frozen=True)
class SDTType:
    """
    A system's type in Structural Dimension Theory.
    
    Every mathematical or computational system is classified by the triple:
    (𝓢, 𝓒, 𝓡)
    
    where:
    - 𝓢: Structural (Ordinal) axis
    - 𝓒: Cardinal (Feature) axis  
    - 𝓡: Relational (Interaction) axis
    
    Key Axiom: No axis refines or approximates another.
    Any transition between axes must be an explicit functor.
    """
    structural: StructuralAxis
    cardinal: CardinalAxis
    relational: RelationalAxis
    
    def __str__(self) -> str:
        return f"({self.structural}, {self.cardinal}, {self.relational})"
    
    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary representation."""
        return {
            "structural": str(self.structural),
            "cardinal": str(self.cardinal),
            "relational": str(self.relational),
            "structural_desc": self.structural.description,
            "cardinal_desc": self.cardinal.description,
            "relational_desc": self.relational.description
        }


# ============================================================================
# Standard Mathematical System Classifications
# ============================================================================

# Complex numbers: (Unary, Real, Dyonion)
COMPLEX_NUMBERS = SDTType(
    structural=StructuralAxis.UNARY,
    cardinal=CardinalAxis.REAL,
    relational=RelationalAxis.DYONION
)

# Quantum Mechanics: (Unary, Real, Polynonion)
QUANTUM_MECHANICS = SDTType(
    structural=StructuralAxis.UNARY,
    cardinal=CardinalAxis.REAL,
    relational=RelationalAxis.POLYNONION
)

# Boolean Logic: (Binary, Finite, Monion)
BOOLEAN_LOGIC = SDTType(
    structural=StructuralAxis.BINARY,
    cardinal=CardinalAxis.FINITE,
    relational=RelationalAxis.MONION
)

# Real Numbers: (Unary, Real, Monion)
REAL_NUMBERS = SDTType(
    structural=StructuralAxis.UNARY,
    cardinal=CardinalAxis.REAL,
    relational=RelationalAxis.MONION
)

# Rooted Trees (e9/Matula): (Self-Similar, Natural, Recursonion)
ROOTED_TREES = SDTType(
    structural=StructuralAxis.SELF_SIMILAR,
    cardinal=CardinalAxis.NATURAL,
    relational=RelationalAxis.RECURSONION
)


# ============================================================================
# Learning as Feature Transport
# ============================================================================

@dataclass
class LearningSystem:
    """
    Learning as Feature Transport over Ordinal Graphs.
    
    Definition:
        Learning is the transport of cardinal features along ordinal structures,
        constrained by relational compatibility.
    
    Formally:
    - Let G be an ordinal graph/category (𝓢)
    - Let F: G → Vect or Meas be a feature functor (𝓒)
    - Let ∇ be a transport/compatibility structure (𝓡)
    
    Then learning consists of:
        updating F such that transport along G becomes coherent under ∇
    
    Key Insights:
    - Structure ≠ learned (the graph G is given)
    - Features ≠ structure (F decorates but doesn't define G)
    - Weights ≠ meaning (weights are cardinal, meaning is structural)
    
    This explains:
    - Why embeddings lose structure
    - Why symbolic learning fails when treated metrically
    - Why "neuro-symbolic" must be two-layered
    """
    name: str
    ordinal_graph: str  # Description of the structural graph G
    feature_space: str  # Description of the cardinal feature space
    transport_law: str  # Description of the relational transport ∇
    sdt_type: SDTType
    
    def __str__(self) -> str:
        return f"LearningSystem({self.name})"
    
    def describe(self) -> str:
        """Get full description of the learning system."""
        return f"""
Learning System: {self.name}
SDT Type: {self.sdt_type}

Ordinal Graph (𝓢): {self.ordinal_graph}
Feature Space (𝓒): {self.feature_space}
Transport Law (𝓡): {self.transport_law}

Learning = updating feature functor F such that transport along the graph
becomes coherent under the relational constraints.
"""


# ============================================================================
# Recursonion - Higher Operadic Algebras
# ============================================================================

@dataclass
class Recursonion:
    """
    Recursonion: A relational algebra whose multiplication is defined by an operad
    that includes itself as an operation.
    
    Formally:
    - Let 𝒪 be an operad
    - Let A be an algebra over 𝒪
    - If 𝒪 contains operations whose inputs or outputs are themselves 𝒪-algebras,
      then A is a Recursonion
    
    Key Features:
    - Self-reference
    - Higher associativity
    - Recursive transport
    - Stratified interaction laws
    
    Examples (conceptual):
    - Higher gauge theory
    - Type-theoretic universes
    - Reflective interpreters
    - Metagraph filesystems
    
    Formal Definition:
        Recursonion = Operadic Fixed-Point Algebra
    
    This is not exotic. It's the algebraic shadow of recursion itself.
    """
    name: str
    operad: str  # Description of the operad 𝒪
    self_reference: str  # How the operad includes itself
    examples: List[str]
    
    def __str__(self) -> str:
        return f"Recursonion({self.name})"
    
    def describe(self) -> str:
        """Get full description of the recursonion."""
        examples_str = "\n  - ".join(self.examples)
        return f"""
Recursonion: {self.name}
Operad: {self.operad}
Self-Reference: {self.self_reference}

Examples:
  - {examples_str}

A Recursonion is an operadic fixed-point algebra where the multiplication
is defined by an operad that includes itself as an operation.
"""


# ============================================================================
# Example System Classifications
# ============================================================================

def classify_system(name: str) -> Optional[SDTType]:
    """
    Classify a well-known mathematical system according to SDT.
    
    Args:
        name: Name of the system to classify
    
    Returns:
        SDTType classification, or None if system is unknown
    """
    classifications = {
        "complex": COMPLEX_NUMBERS,
        "complex_numbers": COMPLEX_NUMBERS,
        "ℂ": COMPLEX_NUMBERS,
        
        "quantum": QUANTUM_MECHANICS,
        "quantum_mechanics": QUANTUM_MECHANICS,
        "qm": QUANTUM_MECHANICS,
        
        "boolean": BOOLEAN_LOGIC,
        "boolean_logic": BOOLEAN_LOGIC,
        "bool": BOOLEAN_LOGIC,
        
        "real": REAL_NUMBERS,
        "real_numbers": REAL_NUMBERS,
        "ℝ": REAL_NUMBERS,
        
        "rooted_trees": ROOTED_TREES,
        "matula": ROOTED_TREES,
        "e9": ROOTED_TREES,
    }
    
    return classifications.get(name.lower())


def get_all_classifications() -> Dict[str, SDTType]:
    """Get all standard system classifications."""
    return {
        "Complex Numbers (ℂ)": COMPLEX_NUMBERS,
        "Quantum Mechanics": QUANTUM_MECHANICS,
        "Boolean Logic": BOOLEAN_LOGIC,
        "Real Numbers (ℝ)": REAL_NUMBERS,
        "Rooted Trees (e9/Matula)": ROOTED_TREES,
    }


# ============================================================================
# Example Learning Systems
# ============================================================================

def create_neural_network_learning() -> LearningSystem:
    """
    Neural networks as feature transport over computation graphs.
    """
    return LearningSystem(
        name="Neural Network",
        ordinal_graph="Directed acyclic computation graph (DAG)",
        feature_space="ℝⁿ vector spaces at each layer",
        transport_law="Backpropagation: adjoint transport of gradients",
        sdt_type=SDTType(
            structural=StructuralAxis.N_ARY,
            cardinal=CardinalAxis.REAL,
            relational=RelationalAxis.POLYNONION
        )
    )


def create_symbolic_learning() -> LearningSystem:
    """
    Symbolic learning as transport over discrete syntax trees.
    """
    return LearningSystem(
        name="Symbolic Learning",
        ordinal_graph="Abstract syntax trees (AST) / term graphs",
        feature_space="Discrete symbol vocabularies",
        transport_law="Structural recursion / tree homomorphisms",
        sdt_type=SDTType(
            structural=StructuralAxis.SELF_SIMILAR,
            cardinal=CardinalAxis.FINITE,
            relational=RelationalAxis.RECURSONION
        )
    )


# ============================================================================
# Example Recursonions
# ============================================================================

def create_matula_recursonion() -> Recursonion:
    """
    The Matula-Goebel encoding as a recursonion.
    """
    return Recursonion(
        name="Matula-Goebel Encoding",
        operad="Rooted tree operad with grafting (B_+)",
        self_reference="Trees composed of subtrees via prime factorization recursion",
        examples=[
            "Tree T with children [T₁, T₂, ...] maps to M(T) = p_{M(T₁)} × p_{M(T₂)} × ...",
            "Prime indices inject tree structure back into primes",
            "Recursive: to compute M(T), must compute M(child) for all children",
            "Fixed point: the encoding uses primes, which are indexed by trees"
        ]
    )


def create_type_universe_recursonion() -> Recursonion:
    """
    Type-theoretic universes as recursonions.
    """
    return Recursonion(
        name="Type Universe",
        operad="Dependent type theory operad",
        self_reference="Type : Type (universe hierarchy with self-containment)",
        examples=[
            "Universe U contains types, including function types A → B",
            "Universe hierarchy: U₀ : U₁ : U₂ : ...",
            "Self-reference through impredicative encodings",
            "Reflection: programs that manipulate their own types"
        ]
    )


# ============================================================================
# Utility Functions
# ============================================================================

def print_sdt_summary():
    """Print a summary of the SDT framework."""
    print("=" * 70)
    print("STRUCTURAL DIMENSION THEORY (SDT)")
    print("Ordo ab Neuro - Radix ex Matula")
    print("=" * 70)
    print()
    print("A system is typed by the triple (𝓢, 𝓒, 𝓡) where:")
    print()
    print("𝓢 — STRUCTURAL (ORDINAL) AXIS")
    print("  What compositions are admissible?")
    print("  Categorical, operadic, logical")
    print()
    print("𝓒 — CARDINAL (FEATURE) AXIS")
    print("  How finely can differences be resolved?")
    print("  Metric, measurable, quantitative")
    print()
    print("𝓡 — RELATIONAL (INTERACTION) AXIS")
    print("  How do entities interfere, transform, and relate?")
    print("  Algebraic, geometric, topological")
    print()
    print("KEY INSIGHT:")
    print("  Boolean, Real, and Complex are NOT stages of refinement.")
    print("  They are coordinates in a three-axis space of meaning.")
    print()
    print("  Logic defines what may exist.")
    print("  Metrics define how finely it is seen.")
    print("  Algebra defines how it interacts.")
    print("=" * 70)


def print_classifications():
    """Print all standard system classifications."""
    print("\nSTANDARD SYSTEM CLASSIFICATIONS:")
    print("-" * 70)
    
    classifications = get_all_classifications()
    for name, sdt_type in classifications.items():
        print(f"\n{name}:")
        print(f"  {sdt_type}")
        info = sdt_type.to_dict()
        print(f"  • Structural: {info['structural_desc']}")
        print(f"  • Cardinal: {info['cardinal_desc']}")
        print(f"  • Relational: {info['relational_desc']}")


def print_axes_details():
    """Print detailed information about all axes."""
    print("\nAXIS DETAILS:")
    print("=" * 70)
    
    print("\n𝓢 — STRUCTURAL (ORDINAL) AXIS:")
    print("-" * 70)
    for axis in StructuralAxis:
        print(f"  {str(axis):20s} - {axis.description}")
    
    print("\n𝓒 — CARDINAL (FEATURE) AXIS:")
    print("-" * 70)
    for axis in CardinalAxis:
        print(f"  {str(axis):20s} - {axis.description}")
    
    print("\n𝓡 — RELATIONAL (INTERACTION) AXIS:")
    print("-" * 70)
    for axis in RelationalAxis:
        print(f"  {str(axis):20s} - {axis.description}")
