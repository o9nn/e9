#!/usr/bin/env python3
"""
Unit tests for Structural Dimension Theory (SDT)
"""

import unittest
from sdt import (
    # Enums
    StructuralAxis,
    CardinalAxis,
    RelationalAxis,
    # Core types
    SDTType,
    # Standard classifications
    COMPLEX_NUMBERS,
    QUANTUM_MECHANICS,
    BOOLEAN_LOGIC,
    REAL_NUMBERS,
    ROOTED_TREES,
    # Classes
    LearningSystem,
    Recursonion,
    # Functions
    classify_system,
    get_all_classifications,
    create_neural_network_learning,
    create_symbolic_learning,
    create_matula_recursonion,
    create_type_universe_recursonion,
)


class TestStructuralAxis(unittest.TestCase):
    """Test the Structural (Ordinal) Axis."""
    
    def test_structural_axis_values(self):
        """Test that all structural axis values exist."""
        self.assertEqual(StructuralAxis.UNARY.value, "unary")
        self.assertEqual(StructuralAxis.BINARY.value, "binary")
        self.assertEqual(StructuralAxis.TERNARY.value, "ternary")
        self.assertEqual(StructuralAxis.N_ARY.value, "n_ary")
        self.assertEqual(StructuralAxis.SELF_SIMILAR.value, "self_similar")
        self.assertEqual(StructuralAxis.FRACTAL.value, "fractal")
        self.assertEqual(StructuralAxis.CONTINUUM_OPERADIC.value, "continuum_operadic")
    
    def test_structural_axis_string(self):
        """Test string representation."""
        self.assertEqual(str(StructuralAxis.UNARY), "Unary")
        self.assertEqual(str(StructuralAxis.BINARY), "Binary")
        self.assertEqual(str(StructuralAxis.SELF_SIMILAR), "Self Similar")
    
    def test_structural_axis_description(self):
        """Test that all axes have descriptions."""
        for axis in StructuralAxis:
            self.assertIsInstance(axis.description, str)
            self.assertGreater(len(axis.description), 0)


class TestCardinalAxis(unittest.TestCase):
    """Test the Cardinal (Feature) Axis."""
    
    def test_cardinal_axis_values(self):
        """Test that all cardinal axis values exist."""
        self.assertEqual(CardinalAxis.FINITE.value, "finite")
        self.assertEqual(CardinalAxis.NATURAL.value, "natural")
        self.assertEqual(CardinalAxis.INTEGER.value, "integer")
        self.assertEqual(CardinalAxis.RATIONAL.value, "rational")
        self.assertEqual(CardinalAxis.REAL.value, "real")
        self.assertEqual(CardinalAxis.MEASURE_SPACE.value, "measure_space")
        self.assertEqual(CardinalAxis.DISTRIBUTION.value, "distribution")
    
    def test_cardinal_axis_string(self):
        """Test string representation."""
        self.assertEqual(str(CardinalAxis.NATURAL), "Natural")
        self.assertEqual(str(CardinalAxis.REAL), "Real")
        self.assertEqual(str(CardinalAxis.MEASURE_SPACE), "Measure Space")
    
    def test_cardinal_axis_description(self):
        """Test that all axes have descriptions."""
        for axis in CardinalAxis:
            self.assertIsInstance(axis.description, str)
            self.assertGreater(len(axis.description), 0)


class TestRelationalAxis(unittest.TestCase):
    """Test the Relational (Interaction) Axis."""
    
    def test_relational_axis_values(self):
        """Test that all relational axis values exist."""
        self.assertEqual(RelationalAxis.MONION.value, "monion")
        self.assertEqual(RelationalAxis.DYONION.value, "dyonion")
        self.assertEqual(RelationalAxis.TRIONION.value, "trionion")
        self.assertEqual(RelationalAxis.POLYNONION.value, "polynonion")
        self.assertEqual(RelationalAxis.RECURSONION.value, "recursonion")
    
    def test_relational_axis_string(self):
        """Test string representation."""
        self.assertEqual(str(RelationalAxis.MONION), "Monion")
        self.assertEqual(str(RelationalAxis.DYONION), "Dyonion")
        self.assertEqual(str(RelationalAxis.RECURSONION), "Recursonion")
    
    def test_relational_axis_description(self):
        """Test that all axes have descriptions."""
        for axis in RelationalAxis:
            self.assertIsInstance(axis.description, str)
            self.assertGreater(len(axis.description), 0)


class TestSDTType(unittest.TestCase):
    """Test the SDT classification type."""
    
    def test_sdt_type_creation(self):
        """Test creating an SDT type."""
        sdt = SDTType(
            structural=StructuralAxis.UNARY,
            cardinal=CardinalAxis.REAL,
            relational=RelationalAxis.DYONION
        )
        self.assertEqual(sdt.structural, StructuralAxis.UNARY)
        self.assertEqual(sdt.cardinal, CardinalAxis.REAL)
        self.assertEqual(sdt.relational, RelationalAxis.DYONION)
    
    def test_sdt_type_string(self):
        """Test string representation."""
        sdt = SDTType(
            structural=StructuralAxis.UNARY,
            cardinal=CardinalAxis.REAL,
            relational=RelationalAxis.DYONION
        )
        s = str(sdt)
        self.assertIn("Unary", s)
        self.assertIn("Real", s)
        self.assertIn("Dyonion", s)
    
    def test_sdt_type_to_dict(self):
        """Test conversion to dictionary."""
        sdt = SDTType(
            structural=StructuralAxis.BINARY,
            cardinal=CardinalAxis.FINITE,
            relational=RelationalAxis.MONION
        )
        d = sdt.to_dict()
        self.assertIn("structural", d)
        self.assertIn("cardinal", d)
        self.assertIn("relational", d)
        self.assertIn("structural_desc", d)
        self.assertIn("cardinal_desc", d)
        self.assertIn("relational_desc", d)
    
    def test_sdt_type_immutable(self):
        """Test that SDT types are immutable."""
        sdt = SDTType(
            structural=StructuralAxis.UNARY,
            cardinal=CardinalAxis.REAL,
            relational=RelationalAxis.DYONION
        )
        with self.assertRaises(AttributeError):
            sdt.structural = StructuralAxis.BINARY


class TestStandardClassifications(unittest.TestCase):
    """Test standard system classifications."""
    
    def test_complex_numbers(self):
        """Test classification of complex numbers."""
        self.assertEqual(COMPLEX_NUMBERS.structural, StructuralAxis.UNARY)
        self.assertEqual(COMPLEX_NUMBERS.cardinal, CardinalAxis.REAL)
        self.assertEqual(COMPLEX_NUMBERS.relational, RelationalAxis.DYONION)
    
    def test_quantum_mechanics(self):
        """Test classification of quantum mechanics."""
        self.assertEqual(QUANTUM_MECHANICS.structural, StructuralAxis.UNARY)
        self.assertEqual(QUANTUM_MECHANICS.cardinal, CardinalAxis.REAL)
        self.assertEqual(QUANTUM_MECHANICS.relational, RelationalAxis.POLYNONION)
    
    def test_boolean_logic(self):
        """Test classification of boolean logic."""
        self.assertEqual(BOOLEAN_LOGIC.structural, StructuralAxis.BINARY)
        self.assertEqual(BOOLEAN_LOGIC.cardinal, CardinalAxis.FINITE)
        self.assertEqual(BOOLEAN_LOGIC.relational, RelationalAxis.MONION)
    
    def test_real_numbers(self):
        """Test classification of real numbers."""
        self.assertEqual(REAL_NUMBERS.structural, StructuralAxis.UNARY)
        self.assertEqual(REAL_NUMBERS.cardinal, CardinalAxis.REAL)
        self.assertEqual(REAL_NUMBERS.relational, RelationalAxis.MONION)
    
    def test_rooted_trees(self):
        """Test classification of rooted trees (e9/Matula)."""
        self.assertEqual(ROOTED_TREES.structural, StructuralAxis.SELF_SIMILAR)
        self.assertEqual(ROOTED_TREES.cardinal, CardinalAxis.NATURAL)
        self.assertEqual(ROOTED_TREES.relational, RelationalAxis.RECURSONION)
    
    def test_complex_not_refinement_of_real(self):
        """Test that complex numbers are not a refinement of reals."""
        # Same structural and cardinal axes
        self.assertEqual(COMPLEX_NUMBERS.structural, REAL_NUMBERS.structural)
        self.assertEqual(COMPLEX_NUMBERS.cardinal, REAL_NUMBERS.cardinal)
        # Different relational axes
        self.assertNotEqual(COMPLEX_NUMBERS.relational, REAL_NUMBERS.relational)
    
    def test_quantum_not_different_logic(self):
        """Test that quantum mechanics has same structural axis as classical."""
        # Quantum has same structural axis as real numbers (Unary)
        self.assertEqual(QUANTUM_MECHANICS.structural, REAL_NUMBERS.structural)
        # But different relational axis
        self.assertNotEqual(QUANTUM_MECHANICS.relational, REAL_NUMBERS.relational)


class TestClassifySystem(unittest.TestCase):
    """Test system classification function."""
    
    def test_classify_complex(self):
        """Test classifying complex numbers."""
        self.assertEqual(classify_system("complex"), COMPLEX_NUMBERS)
        self.assertEqual(classify_system("complex_numbers"), COMPLEX_NUMBERS)
        self.assertEqual(classify_system("ℂ"), COMPLEX_NUMBERS)
    
    def test_classify_quantum(self):
        """Test classifying quantum mechanics."""
        self.assertEqual(classify_system("quantum"), QUANTUM_MECHANICS)
        self.assertEqual(classify_system("quantum_mechanics"), QUANTUM_MECHANICS)
        self.assertEqual(classify_system("qm"), QUANTUM_MECHANICS)
    
    def test_classify_boolean(self):
        """Test classifying boolean logic."""
        self.assertEqual(classify_system("boolean"), BOOLEAN_LOGIC)
        self.assertEqual(classify_system("bool"), BOOLEAN_LOGIC)
    
    def test_classify_real(self):
        """Test classifying real numbers."""
        self.assertEqual(classify_system("real"), REAL_NUMBERS)
        self.assertEqual(classify_system("ℝ"), REAL_NUMBERS)
    
    def test_classify_rooted_trees(self):
        """Test classifying rooted trees."""
        self.assertEqual(classify_system("rooted_trees"), ROOTED_TREES)
        self.assertEqual(classify_system("matula"), ROOTED_TREES)
        self.assertEqual(classify_system("e9"), ROOTED_TREES)
    
    def test_classify_unknown(self):
        """Test classifying unknown system."""
        self.assertIsNone(classify_system("unknown_system"))
    
    def test_classify_case_insensitive(self):
        """Test that classification is case-insensitive."""
        self.assertEqual(classify_system("COMPLEX"), COMPLEX_NUMBERS)
        self.assertEqual(classify_system("Complex"), COMPLEX_NUMBERS)


class TestGetAllClassifications(unittest.TestCase):
    """Test getting all classifications."""
    
    def test_get_all_classifications(self):
        """Test that all classifications are returned."""
        classifications = get_all_classifications()
        self.assertIsInstance(classifications, dict)
        self.assertGreater(len(classifications), 0)
        
        # Check that all standard systems are included
        self.assertIn(COMPLEX_NUMBERS, classifications.values())
        self.assertIn(QUANTUM_MECHANICS, classifications.values())
        self.assertIn(BOOLEAN_LOGIC, classifications.values())
        self.assertIn(REAL_NUMBERS, classifications.values())
        self.assertIn(ROOTED_TREES, classifications.values())


class TestLearningSystem(unittest.TestCase):
    """Test learning system representation."""
    
    def test_neural_network_learning(self):
        """Test neural network as learning system."""
        nn = create_neural_network_learning()
        self.assertIsInstance(nn, LearningSystem)
        self.assertEqual(nn.name, "Neural Network")
        self.assertIsInstance(nn.sdt_type, SDTType)
        self.assertIn("graph", nn.ordinal_graph.lower())
        self.assertIn("vector", nn.feature_space.lower())
        self.assertIn("backpropagation", nn.transport_law.lower())
    
    def test_symbolic_learning(self):
        """Test symbolic learning system."""
        sym = create_symbolic_learning()
        self.assertIsInstance(sym, LearningSystem)
        self.assertEqual(sym.name, "Symbolic Learning")
        self.assertIsInstance(sym.sdt_type, SDTType)
        self.assertIn("tree", sym.ordinal_graph.lower())
        self.assertIn("symbol", sym.feature_space.lower())
    
    def test_learning_system_describe(self):
        """Test that learning systems can be described."""
        nn = create_neural_network_learning()
        desc = nn.describe()
        self.assertIsInstance(desc, str)
        self.assertIn("Neural Network", desc)
        self.assertIn("Learning", desc)
    
    def test_neural_vs_symbolic_different_axes(self):
        """Test that neural and symbolic learning are on different axes."""
        nn = create_neural_network_learning()
        sym = create_symbolic_learning()
        
        # They should differ in structural axis
        self.assertNotEqual(nn.sdt_type.structural, sym.sdt_type.structural)
        # They should differ in cardinal axis
        self.assertNotEqual(nn.sdt_type.cardinal, sym.sdt_type.cardinal)
        # They should differ in relational axis
        self.assertNotEqual(nn.sdt_type.relational, sym.sdt_type.relational)


class TestRecursonion(unittest.TestCase):
    """Test recursonion representation."""
    
    def test_matula_recursonion(self):
        """Test Matula encoding as recursonion."""
        matula = create_matula_recursonion()
        self.assertIsInstance(matula, Recursonion)
        self.assertEqual(matula.name, "Matula-Goebel Encoding")
        self.assertIn("tree", matula.operad.lower())
        self.assertIn("prime", matula.self_reference.lower())
        self.assertGreater(len(matula.examples), 0)
    
    def test_type_universe_recursonion(self):
        """Test type universe as recursonion."""
        universe = create_type_universe_recursonion()
        self.assertIsInstance(universe, Recursonion)
        self.assertEqual(universe.name, "Type Universe")
        self.assertIn("type", universe.operad.lower())
        self.assertGreater(len(universe.examples), 0)
    
    def test_recursonion_describe(self):
        """Test that recursonions can be described."""
        matula = create_matula_recursonion()
        desc = matula.describe()
        self.assertIsInstance(desc, str)
        self.assertIn("Recursonion", desc)
        self.assertIn("Matula", desc)
    
    def test_recursonion_self_reference(self):
        """Test that recursonions have self-reference property."""
        matula = create_matula_recursonion()
        # Should mention recursion or self-reference
        self.assertTrue(
            "recurs" in matula.self_reference.lower() or
            "self" in matula.self_reference.lower()
        )


class TestSDTAxioms(unittest.TestCase):
    """Test that SDT axioms are respected."""
    
    def test_axiom_orthogonality(self):
        """Test that axes are orthogonal (no automatic refinement)."""
        # Complex and Real differ only in relational axis
        self.assertEqual(COMPLEX_NUMBERS.structural, REAL_NUMBERS.structural)
        self.assertEqual(COMPLEX_NUMBERS.cardinal, REAL_NUMBERS.cardinal)
        self.assertNotEqual(COMPLEX_NUMBERS.relational, REAL_NUMBERS.relational)
        
        # This proves that relational axis is independent
        # (ℂ is not "more precise" than ℝ, just relationally different)
    
    def test_axiom_structural_primacy(self):
        """Test that structure exists independent of measure."""
        # Boolean logic has structure (Binary) independent of its cardinality (Finite)
        self.assertEqual(BOOLEAN_LOGIC.structural, StructuralAxis.BINARY)
        # Even if we had infinite-valued logic, it would still be Binary structurally
    
    def test_axiom_cardinal_decoration(self):
        """Test that cardinality decorates but doesn't define structure."""
        # Real and Complex both have Real cardinality but different structures
        # (in relational sense)
        self.assertEqual(REAL_NUMBERS.cardinal, COMPLEX_NUMBERS.cardinal)
        # The cardinality is the same, but relational structure differs
    
    def test_learning_is_transport(self):
        """Test that learning systems follow transport paradigm."""
        nn = create_neural_network_learning()
        # Should have ordinal graph (structure)
        self.assertIsInstance(nn.ordinal_graph, str)
        # Should have feature space (cardinality)
        self.assertIsInstance(nn.feature_space, str)
        # Should have transport law (relational)
        self.assertIsInstance(nn.transport_law, str)


if __name__ == '__main__':
    unittest.main()
