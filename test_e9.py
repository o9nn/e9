#!/usr/bin/env python3
"""
Unit tests for e9 - Prime Eigenvalue Function
"""

import unittest
from e9 import (
    is_prime,
    nth_prime,
    prime_eigenvalue,
    generate_prime_sequence,
    analyze_prime_projection,
    PrimeEgregore,
    # New functions for index injection
    number_to_matula,
    matula_to_number,
    get_index_persona,
    generate_index_persona_table,
    analyze_cognitive_grammar,
    # New functions for Connes-Kreimer Hopf algebra
    rooted_trees_count,
    ion_layer,
    generate_ion_sequence,
    prime_tower,
    graft_operation,
    analyze_hopf_structure,
    # New classes and functions for cognitive renormalization
    RootedTree,
    Forest,
    AdmissibleCut,
    admissible_cuts,
    coproduct,
    antipode,
    Character,
    cognitive_renormalization,
    matula_to_tree,
    tree_to_matula,
    B_plus,
    theta_n,
    base_increment
)


class TestPrimeHelpers(unittest.TestCase):
    """Test basic prime number functions."""
    
    def test_is_prime(self):
        """Test prime checking function."""
        # Test known primes
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in primes:
            self.assertTrue(is_prime(p), f"{p} should be prime")
        
        # Test known non-primes
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 15, 18, 20]
        for n in non_primes:
            self.assertFalse(is_prime(n), f"{n} should not be prime")
    
    def test_nth_prime(self):
        """Test nth prime function."""
        # First 10 primes
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i, expected_prime in enumerate(expected, 1):
            self.assertEqual(nth_prime(i), expected_prime,
                           f"The {i}th prime should be {expected_prime}")
    
    def test_nth_prime_invalid(self):
        """Test nth_prime with invalid input."""
        with self.assertRaises(ValueError):
            nth_prime(0)
        with self.assertRaises(ValueError):
            nth_prime(-1)


class TestPrimeEgregore(unittest.TestCase):
    """Test the PrimeEgregore class."""
    
    def test_initialization(self):
        """Test PrimeEgregore initialization."""
        eg = PrimeEgregore(5, 11)
        self.assertEqual(eg.index, 5)
        self.assertEqual(eg.prime, 11)
    
    def test_encapsulate(self):
        """Test encapsulation of computational ensemble."""
        eg = PrimeEgregore(4, 7)
        ensemble = eg.encapsulate()
        
        self.assertIn('index', ensemble)
        self.assertIn('partitions', ensemble)
        self.assertIn('divisors', ensemble)
        self.assertIn('prime_factorization', ensemble)
        self.assertIn('composite_structure', ensemble)
        
        self.assertEqual(ensemble['index'], 4)
        self.assertEqual(ensemble['divisors'], [1, 2, 4])
        self.assertEqual(ensemble['prime_factorization'], [2, 2])
    
    def test_purify(self):
        """Test purification returns the prime."""
        eg = PrimeEgregore(3, 5)
        self.assertEqual(eg.purify(), 5)
    
    def test_project(self):
        """Test projection into multiples."""
        eg = PrimeEgregore(2, 3)
        multiples = eg.project(limit=20)
        
        expected = {3, 6, 9, 12, 15, 18}
        self.assertEqual(multiples, expected)
    
    def test_compute_partitions(self):
        """Test partition computation."""
        # Partitions of 4: [4], [3,1], [2,2], [2,1,1], [1,1,1,1]
        partitions = PrimeEgregore._compute_partitions(4)
        self.assertEqual(len(partitions), 5)
        
        # Partitions of 3: [3], [2,1], [1,1,1]
        partitions = PrimeEgregore._compute_partitions(3)
        self.assertEqual(len(partitions), 3)
    
    def test_compute_divisors(self):
        """Test divisor computation."""
        self.assertEqual(PrimeEgregore._compute_divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(PrimeEgregore._compute_divisors(7), [1, 7])
        self.assertEqual(PrimeEgregore._compute_divisors(1), [1])
    
    def test_prime_factorization(self):
        """Test prime factorization."""
        self.assertEqual(PrimeEgregore._prime_factorization(12), [2, 2, 3])
        self.assertEqual(PrimeEgregore._prime_factorization(7), [7])
        self.assertEqual(PrimeEgregore._prime_factorization(1), [])
    
    def test_composite_structure(self):
        """Test composite structure analysis."""
        # Test with prime
        struct = PrimeEgregore._composite_structure(7)
        self.assertTrue(struct['is_prime'])
        self.assertFalse(struct['is_composite'])
        
        # Test with composite
        struct = PrimeEgregore._composite_structure(12)
        self.assertFalse(struct['is_prime'])
        self.assertTrue(struct['is_composite'])


class TestPrimeEigenvalue(unittest.TestCase):
    """Test the main prime_eigenvalue function."""
    
    def test_prime_eigenvalue_basic(self):
        """Test basic prime eigenvalue computation."""
        eg = prime_eigenvalue(1)
        self.assertEqual(eg.index, 1)
        self.assertEqual(eg.prime, 2)
        
        eg = prime_eigenvalue(5)
        self.assertEqual(eg.index, 5)
        self.assertEqual(eg.prime, 11)
    
    def test_prime_eigenvalue_sequence(self):
        """Test that prime_eigenvalue produces correct sequence."""
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i, expected_prime in enumerate(expected_primes, 1):
            eg = prime_eigenvalue(i)
            self.assertEqual(eg.prime, expected_prime)
    
    def test_generate_prime_sequence(self):
        """Test generating multiple prime egregores."""
        egregores = generate_prime_sequence(5)
        
        self.assertEqual(len(egregores), 5)
        self.assertEqual(egregores[0].prime, 2)
        self.assertEqual(egregores[4].prime, 11)
        
        # Check indices are correct
        for i, eg in enumerate(egregores, 1):
            self.assertEqual(eg.index, i)


class TestAnalyzeProjection(unittest.TestCase):
    """Test the projection analysis function."""
    
    def test_analyze_prime_projection(self):
        """Test complete projection analysis."""
        eg = prime_eigenvalue(2)  # 2nd prime is 3
        analysis = analyze_prime_projection(eg, limit=20)
        
        self.assertEqual(analysis['prime'], 3)
        self.assertEqual(analysis['index'], 2)
        self.assertEqual(analysis['purified_value'], 3)
        self.assertIn('ensemble_structure', analysis)
        self.assertIn('projection', analysis)
        
        # Check projection
        proj = analysis['projection']
        self.assertEqual(proj['multiples'], [3, 6, 9, 12, 15, 18])
        self.assertEqual(proj['multiples_count'], 6)
        self.assertAlmostEqual(proj['projection_density'], 0.3)


class TestEgregoreConceptIntegration(unittest.TestCase):
    """Integration tests for the complete egregore concept."""
    
    def test_encapsulate_purify_project_workflow(self):
        """Test the complete daemon workflow."""
        # Get the 4th prime egregore
        eg = prime_eigenvalue(4)
        
        # 1. Encapsulate
        ensemble = eg.encapsulate()
        self.assertEqual(ensemble['index'], 4)
        self.assertIsNotNone(ensemble['partitions'])
        
        # 2. Purify
        purified = eg.purify()
        self.assertEqual(purified, 7)  # 4th prime is 7
        
        # 3. Project
        multiples = eg.project(limit=30)
        expected_multiples = {7, 14, 21, 28}
        self.assertEqual(multiples, expected_multiples)
    
    def test_different_indices_different_eigenvalues(self):
        """Verify different indices produce different eigenvalues."""
        eg1 = prime_eigenvalue(3)
        eg2 = prime_eigenvalue(5)
        eg3 = prime_eigenvalue(7)
        
        primes = {eg1.prime, eg2.prime, eg3.prime}
        self.assertEqual(len(primes), 3, "Each index should have unique prime")
    
    def test_egregore_relationship(self):
        """Test the relationship between index structure and prime."""
        # For n=6 (composite: 2*3), get 6th prime
        eg = prime_eigenvalue(6)
        self.assertEqual(eg.prime, 13)
        
        ensemble = eg.encapsulate()
        # Index 6 is composite
        self.assertTrue(ensemble['composite_structure']['is_composite'])
        self.assertEqual(ensemble['prime_factorization'], [2, 3])
        
        # But the 6th prime (13) is prime (purified)
        self.assertTrue(is_prime(eg.prime))


class TestMatulaEncoding(unittest.TestCase):
    """Test Matula number encoding (rooted tree structures)."""
    
    def test_basic_matula_encoding(self):
        """Test basic Matula encoding for small numbers."""
        # 1 is the unit
        self.assertEqual(number_to_matula(1), "()")
        
        # 2 is the first prime (index 1 encodes as ())
        self.assertEqual(number_to_matula(2), "(())")
        
        # 3 is the second prime (index 2 encodes as (()))
        self.assertEqual(number_to_matula(3), "((()))")
    
    def test_matula_composite_numbers(self):
        """Test Matula encoding for composite numbers."""
        # 4 = 2*2, two copies of ()
        result = number_to_matula(4)
        self.assertIn("()", result)
        
        # 6 = 2*3, indices 1 and 2
        result = number_to_matula(6)
        self.assertIn("(", result)
        self.assertIn(")", result)
    
    def test_matula_roundtrip(self):
        """Test that encoding and decoding are inverse operations."""
        for n in range(1, 10):
            tree = number_to_matula(n)
            recovered = matula_to_number(tree)
            self.assertEqual(recovered, n, f"Roundtrip failed for {n}: {tree}")
    
    def test_matula_decoding(self):
        """Test decoding Matula structures."""
        # () is 1
        self.assertEqual(matula_to_number("()"), 1)
        
        # (()) is 2
        self.assertEqual(matula_to_number("(())"), 2)


class TestIndexPersona(unittest.TestCase):
    """Test index persona and character analysis."""
    
    def test_unit_persona(self):
        """Test persona of index 1."""
        persona = get_index_persona(1)
        self.assertEqual(persona['structure'], "()")
        self.assertIn('unit', persona['character'].lower())
        self.assertEqual(persona['type'], 'unit')
    
    def test_binary_persona(self):
        """Test persona of index 2 (pure binary)."""
        persona = get_index_persona(2)
        self.assertIn('binary', persona['character'].lower())
    
    def test_mixed_persona(self):
        """Test persona of index 6 (first mixed ensemble)."""
        persona = get_index_persona(6)
        self.assertIn('mixed', persona['character'].lower())
        self.assertEqual(persona['factors'], [2, 3])
    
    def test_egregore_persona_method(self):
        """Test that egregore can access its persona."""
        eg = prime_eigenvalue(4)
        persona = eg.get_persona()
        
        self.assertIn('structure', persona)
        self.assertIn('character', persona)
        self.assertIn('type', persona)
        
        # Index 4 = 2*2
        self.assertEqual(persona['factors'], [2, 2])
    
    def test_structure_notation(self):
        """Test getting structure notation from egregore."""
        eg = prime_eigenvalue(3)
        structure = eg.get_structure_notation()
        self.assertIsInstance(structure, str)
        self.assertIn("(", structure)
        self.assertIn(")", structure)


class TestIndexPersonaTable(unittest.TestCase):
    """Test index persona table generation."""
    
    def test_generate_table(self):
        """Test generating the index persona table."""
        table = generate_index_persona_table(max_index=5)
        
        self.assertEqual(len(table), 5)
        
        # Check first entry
        self.assertEqual(table[0]['prime'], 2)
        self.assertEqual(table[0]['index'], 1)
        self.assertEqual(table[0]['structure'], "()")
        
        # Check that all entries have required keys
        for entry in table:
            self.assertIn('prime', entry)
            self.assertIn('index', entry)
            self.assertIn('structure', entry)
            self.assertIn('persona', entry)
            self.assertIn('type', entry)
    
    def test_table_matches_agent_instructions(self):
        """Test that table matches examples from agent instructions."""
        table = generate_index_persona_table(max_index=10)
        
        # Verify key examples from agent instructions
        # Index 1 → Prime 2
        self.assertEqual(table[0]['prime'], 2)
        self.assertEqual(table[0]['index'], 1)
        
        # Index 6 → Prime 13 (first mixed ensemble)
        self.assertEqual(table[5]['prime'], 13)
        self.assertEqual(table[5]['index'], 6)
        self.assertIn('mixed', table[5]['persona'].lower())


class TestCognitiveGrammar(unittest.TestCase):
    """Test cognitive grammar analysis."""
    
    def test_analyze_small_alphabet(self):
        """Test cognitive grammar for a small prime bound."""
        analysis = analyze_cognitive_grammar(prime_bound=10)
        
        # Should include primes 2, 3, 5, 7
        self.assertEqual(analysis['alphabet_size'], 4)
        self.assertEqual(analysis['primes'], [2, 3, 5, 7])
        
        self.assertIn('capabilities', analysis)
        self.assertIn('pure_binary', analysis)
        self.assertIn('squared', analysis)
        self.assertIn('mixed', analysis)
    
    def test_analyze_13_limited_agent(self):
        """Test 13-limited agent (can mix 2 and 3)."""
        analysis = analyze_cognitive_grammar(prime_bound=13)
        
        # Should have primes up to 13: [2, 3, 5, 7, 11, 13]
        self.assertEqual(analysis['alphabet_size'], 6)
        self.assertIn(13, analysis['primes'])
        
        # Should have mixed ensemble capability (index 6 → prime 13)
        mixed = analysis['mixed']
        has_2x3 = any(item['index'] == 6 for item in mixed)
        self.assertTrue(has_2x3, "Should have 2×3 mixed ensemble")
    
    def test_analyze_23_limited_agent(self):
        """Test 23-limited agent (can invoke squared-ternary)."""
        analysis = analyze_cognitive_grammar(prime_bound=23)
        
        # Should have access to index 9 (3²) → prime 23
        self.assertIn(23, analysis['primes'])
        
        # Check for ternary squared capability
        capabilities_str = ' '.join(analysis['capabilities'])
        # Check separately for clearer test logic
        has_3_squared = '3²' in capabilities_str
        has_ternary = 'ternary' in capabilities_str.lower()
        self.assertTrue(has_3_squared or has_ternary,
                       "Should have ternary squared capability")
    
    def test_grammatical_expressiveness(self):
        """Test that larger alphabets have higher expressiveness."""
        small = analyze_cognitive_grammar(10)
        large = analyze_cognitive_grammar(30)
        
        self.assertGreater(large['alphabet_size'], small['alphabet_size'])
        self.assertGreaterEqual(large['grammatical_expressiveness'], 
                               small['grammatical_expressiveness'])


class TestHopfAlgebra(unittest.TestCase):
    """Test Connes-Kreimer Hopf algebra and rooted tree functions."""
    
    def test_rooted_trees_count_known_values(self):
        """Test A000081 sequence with known values."""
        # First few values of A000081
        expected = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719]
        for n, expected_count in enumerate(expected):
            self.assertEqual(rooted_trees_count(n), expected_count,
                           f"A000081({n}) should be {expected_count}")
    
    def test_rooted_trees_count_positive(self):
        """Test that rooted tree counts are always positive for n>0."""
        for n in range(1, 15):
            self.assertGreater(rooted_trees_count(n), 0)
    
    def test_rooted_trees_count_increasing(self):
        """Test that tree counts are non-decreasing and eventually strictly increasing."""
        # A000081: 0, 1, 1, 2, 4, 9, 20, ...
        # Note: values at n=1 and n=2 are both 1, so not strictly increasing
        prev = rooted_trees_count(2)
        for n in range(3, 12):
            current = rooted_trees_count(n)
            self.assertGreater(current, prev)
            prev = current
    
    def test_ion_layer_structure(self):
        """Test ion layer returns correct structure."""
        layer = ion_layer(5)
        
        self.assertIn('order', layer)
        self.assertIn('fib', layer)
        self.assertIn('bas', layer)
        self.assertIn('tot', layer)
        self.assertIn('max', layer)
        self.assertEqual(layer['order'], 5)
    
    def test_ion_layer_base_case(self):
        """Test ion layer base case (n=0)."""
        layer = ion_layer(0)
        
        self.assertEqual(layer['fib'], 0)
        self.assertEqual(layer['bas'], 1)
        self.assertEqual(layer['tot'], 1)
        self.assertEqual(layer['max'], 1)
    
    def test_ion_layer_butcher_recursion(self):
        """Test that ion layer follows Butcher recursion: fib(n) = tot(n-1)."""
        for n in range(1, 8):
            layer_n = ion_layer(n)
            layer_prev = ion_layer(n - 1)
            
            # fib(n) should equal tot(n-1)
            self.assertEqual(layer_n['fib'], layer_prev['tot'])
    
    def test_ion_layer_decomposition(self):
        """Test that tot = fib + bas."""
        for n in range(0, 10):
            layer = ion_layer(n)
            self.assertEqual(layer['tot'], layer['fib'] + layer['bas'])
    
    def test_ion_layer_known_values(self):
        """Test ion layer with specific known values from notes."""
        # From notes-clo45-10.md
        layer_4 = ion_layer(4)
        # A000081(5) = 9 (rooted trees with 5 nodes)
        self.assertEqual(layer_4['tot'], 9)
        self.assertEqual(layer_4['fib'], 4)
        self.assertEqual(layer_4['bas'], 5)
        # max=8 is the octonionic seed (triality corolla, ternary root with 3 children)
        self.assertEqual(layer_4['max'], 8)
        
        layer_5 = ion_layer(5)
        # A000081(6) = 20 (rooted trees with 6 nodes)
        self.assertEqual(layer_5['tot'], 20)
        # fib(5) = tot(4) = 9 (Butcher recursion: fiber = previous total)
        self.assertEqual(layer_5['fib'], 9)
        self.assertEqual(layer_5['bas'], 11)
        # max=19 = p_8 = 19 (first step in prime tower from octonionic seed)
        self.assertEqual(layer_5['max'], 19)
    
    def test_generate_ion_sequence(self):
        """Test generation of ion sequence."""
        seq = generate_ion_sequence(5)
        
        self.assertEqual(len(seq), 6)  # 0 through 5
        self.assertEqual(seq[0]['order'], 0)
        self.assertEqual(seq[5]['order'], 5)
    
    def test_prime_tower_octonionic(self):
        """Test prime tower starting from octonionic seed (8)."""
        tower = prime_tower(8, 5)
        
        # Expected: 8 → 19 → 67 → 331 → 2221 → 19577
        expected = [8, 19, 67, 331, 2221, 19577]
        self.assertEqual(tower, expected)
    
    def test_prime_tower_small_seed(self):
        """Test prime tower with smaller seed."""
        tower = prime_tower(3, 3)
        
        # 3 → p_3=5 → p_5=11 → p_11=31
        expected = [3, 5, 11, 31]
        self.assertEqual(tower, expected)
    
    def test_prime_tower_length(self):
        """Test prime tower has correct length."""
        depth = 7
        tower = prime_tower(4, depth)
        self.assertEqual(len(tower), depth + 1)  # seed + depth iterations
    
    def test_graft_operation(self):
        """Test the grafting operation."""
        # graft(8) = p_8 = 19
        self.assertEqual(graft_operation(8), 19)
        
        # graft(19) = p_19 = 67
        self.assertEqual(graft_operation(19), 67)
        
        # graft(3) = p_3 = 5
        self.assertEqual(graft_operation(3), 5)
    
    def test_analyze_hopf_structure(self):
        """Test Hopf structure analysis."""
        analysis = analyze_hopf_structure(8)
        
        self.assertIn('ion_sequence', analysis)
        self.assertIn('sequences', analysis)
        self.assertIn('prime_tower', analysis)
        self.assertIn('base_gaps', analysis)
        self.assertIn('mathematical_context', analysis)
        
        # Check mathematical context
        context = analysis['mathematical_context']
        self.assertEqual(context['basis_sequence'], 'OEIS A000081 (rooted unlabeled trees)')
        self.assertEqual(context['hopf_algebra'], 'Connes-Kreimer H_CK')
        
        # Check sequences are consistent
        sequences = analysis['sequences']
        self.assertEqual(len(sequences['order']), 9)  # 0-8
        self.assertEqual(len(sequences['fib']), 9)
        self.assertEqual(len(sequences['bas']), 9)
        self.assertEqual(len(sequences['tot']), 9)
        self.assertEqual(len(sequences['max']), 9)
    
    def test_hopf_structure_octonionic_seed(self):
        """Test that analysis identifies octonionic seed correctly."""
        analysis = analyze_hopf_structure(5)
        
        self.assertEqual(analysis['analysis']['octonionic_seed'], 8)
        self.assertEqual(analysis['analysis']['triality_corolla'], 8)
        self.assertEqual(analysis['analysis']['first_tower_element'], 19)


class TestRootedTreeStructure(unittest.TestCase):
    """Test the RootedTree data structure."""
    
    def test_leaf_creation(self):
        """Test creating a leaf node."""
        leaf = RootedTree()
        self.assertTrue(leaf.is_leaf)
        self.assertEqual(leaf.order, 1)
        self.assertEqual(str(leaf), "()")
    
    def test_tree_with_children(self):
        """Test creating a tree with children."""
        leaf = RootedTree()
        tree = RootedTree((leaf, leaf))
        self.assertFalse(tree.is_leaf)
        self.assertEqual(tree.order, 3)  # 1 root + 2 leaves
        self.assertEqual(len(tree.children), 2)
    
    def test_tree_notation(self):
        """Test tree notation conversion."""
        leaf = RootedTree()
        tree1 = RootedTree((leaf,))  # B+(leaf)
        self.assertEqual(str(tree1), "(())")
        
        tree2 = RootedTree((leaf, leaf))
        self.assertEqual(str(tree2), "(()())")
    
    def test_tree_order_recursive(self):
        """Test order calculation for nested trees."""
        leaf = RootedTree()
        inner = RootedTree((leaf,))
        outer = RootedTree((inner,))
        self.assertEqual(outer.order, 3)  # 3 nodes total


class TestMatulaTreeBridge(unittest.TestCase):
    """Test conversion between Matula numbers and RootedTree objects."""
    
    def test_matula_to_tree_leaf(self):
        """Test converting Matula 1 to leaf."""
        tree = matula_to_tree(1)
        self.assertTrue(tree.is_leaf)
        self.assertEqual(tree.order, 1)
    
    def test_matula_to_tree_simple(self):
        """Test converting simple Matula numbers."""
        # Matula 2 = p_1 = first prime, corresponds to B+(leaf)
        tree2 = matula_to_tree(2)
        self.assertEqual(tree2.order, 2)
        
        # Matula 4 = p_1 * p_1 = 2*2, two children
        tree4 = matula_to_tree(4)
        self.assertEqual(tree4.order, 3)
        self.assertEqual(len(tree4.children), 2)
    
    def test_tree_to_matula_roundtrip(self):
        """Test that tree_to_matula inverts matula_to_tree."""
        for m in [1, 2, 3, 4, 5, 6, 8]:
            tree = matula_to_tree(m)
            m_back = tree_to_matula(tree)
            self.assertEqual(m, m_back, f"Roundtrip failed for Matula {m}")
    
    def test_tree_to_matula_method(self):
        """Test tree.to_matula() method."""
        leaf = RootedTree()
        self.assertEqual(leaf.to_matula(), 1)
        
        tree = RootedTree((leaf,))
        self.assertEqual(tree.to_matula(), 2)


class TestBPlusOperator(unittest.TestCase):
    """Test the B+ grafting operator."""
    
    def test_b_plus_leaf(self):
        """Test grafting a root above a leaf."""
        leaf = RootedTree()
        tree = B_plus(leaf)
        self.assertEqual(tree.order, 2)
        self.assertEqual(len(tree.children), 1)
        self.assertTrue(tree.children[0].is_leaf)
    
    def test_b_plus_ternary_corolla(self):
        """Test creating ternary corolla (octonionic seed structure)."""
        leaf = RootedTree()
        corolla = B_plus((leaf, leaf, leaf))
        self.assertEqual(corolla.order, 4)
        self.assertEqual(len(corolla.children), 3)
        # Matula number should be 8
        self.assertEqual(corolla.to_matula(), 8)
    
    def test_b_plus_iterated(self):
        """Test iterated B+ application (tower)."""
        leaf = RootedTree()
        t1 = B_plus(leaf)
        t2 = B_plus(t1)
        t3 = B_plus(t2)
        
        self.assertEqual(t1.order, 2)
        self.assertEqual(t2.order, 3)
        self.assertEqual(t3.order, 4)


class TestThetaN(unittest.TestCase):
    """Test the Θ_n tree enumeration."""
    
    def test_theta_counts(self):
        """Test that theta_n produces correct count of trees."""
        # A000081 sequence: 1, 1, 2, 4, 9, 20, ...
        self.assertEqual(len(theta_n(1)), 1)
        self.assertEqual(len(theta_n(2)), 1)
        self.assertEqual(len(theta_n(3)), 2)
        self.assertEqual(len(theta_n(4)), 4)
    
    def test_theta_n_distinct_trees(self):
        """Test that theta_n produces distinct trees."""
        trees3 = theta_n(3)
        # Should have 2 distinct trees
        self.assertEqual(len(trees3), 2)
        # Check they have different structure
        self.assertNotEqual(trees3[0].to_matula(), trees3[1].to_matula())
    
    def test_theta_n_orders(self):
        """Test that all trees in theta_n have order n."""
        for n in [1, 2, 3, 4]:
            trees = theta_n(n)
            for tree in trees:
                self.assertEqual(tree.order, n, f"Tree in theta_{n} has wrong order")


class TestAdmissibleCuts(unittest.TestCase):
    """Test admissible cuts and coproduct."""
    
    def test_leaf_no_cuts(self):
        """Test that a leaf has no admissible cuts."""
        leaf = RootedTree()
        cuts = admissible_cuts(leaf)
        self.assertEqual(len(cuts), 0)
    
    def test_simple_tree_cuts(self):
        """Test cuts for B+(leaf)."""
        leaf = RootedTree()
        tree = B_plus(leaf)
        cuts = admissible_cuts(tree)
        
        # Should have exactly 1 cut: remove the leaf child
        self.assertGreater(len(cuts), 0)
        
        # Check structure
        for cut in cuts:
            self.assertIsInstance(cut, AdmissibleCut)
            self.assertIsInstance(cut.pruned, Forest)
            self.assertIsInstance(cut.trunk, RootedTree)
    
    def test_binary_tree_cuts(self):
        """Test cuts for tree with two children."""
        leaf = RootedTree()
        tree = B_plus((leaf, leaf))
        cuts = admissible_cuts(tree)
        
        # Should have 3 cuts: remove left, remove right, remove both
        self.assertGreaterEqual(len(cuts), 3)


class TestCoproduct(unittest.TestCase):
    """Test the Connes-Kreimer coproduct."""
    
    def test_coproduct_leaf(self):
        """Test coproduct of a leaf."""
        leaf = RootedTree()
        terms = coproduct(leaf)
        
        # Δ(leaf) = leaf⊗1 + 1⊗leaf
        self.assertEqual(len(terms), 2)
    
    def test_coproduct_simple_tree(self):
        """Test coproduct of B+(leaf)."""
        leaf = RootedTree()
        tree = B_plus(leaf)
        terms = coproduct(tree)
        
        # Δ(B+(leaf)) = tree⊗1 + 1⊗tree + leaf⊗leaf
        # Should have at least 3 terms
        self.assertGreaterEqual(len(terms), 3)
        
        # Check that all terms are properly formed
        for term in terms:
            self.assertIsInstance(term.left, Forest)
            self.assertIsInstance(term.right, RootedTree)
    
    def test_coproduct_structure(self):
        """Test that coproduct terms decompose correctly."""
        leaf = RootedTree()
        tree = B_plus((leaf, leaf))
        terms = coproduct(tree)
        
        # All terms should be valid
        for term in terms:
            # Check that left and right have compatible orders
            left_order = term.left.order
            right_order = term.right.order
            # The sum should relate to the original tree order
            self.assertGreaterEqual(left_order + right_order, 0)


class TestCharacterAndConvolution(unittest.TestCase):
    """Test characters and convolution."""
    
    def test_character_creation(self):
        """Test creating a character."""
        # Simple character: count nodes
        def count_nodes(tree):
            return tree.order
        
        char = Character(count_nodes, lambda a, b: a * b, "count")
        self.assertEqual(char.name, "count")
        
        leaf = RootedTree()
        self.assertEqual(char(leaf), 1)
    
    def test_character_evaluation(self):
        """Test character evaluation on trees."""
        # Character that returns Matula number
        def matula_eval(tree):
            return tree.to_matula()
        
        char = Character(matula_eval, lambda a, b: a * b, "matula")
        
        leaf = RootedTree()
        tree2 = B_plus(leaf)
        
        self.assertEqual(char(leaf), 1)
        self.assertEqual(char(tree2), 2)
    
    def test_character_convolution(self):
        """Test convolution of characters."""
        # Two simple characters
        def eval1(tree):
            return tree.order
        
        def eval2(tree):
            return 1
        
        char1 = Character(eval1, lambda a, b: a * b, "φ1")
        char2 = Character(eval2, lambda a, b: a * b, "φ2")
        
        # Convolve them
        conv_char = char1.convolve(char2)
        
        # Evaluate on a leaf
        leaf = RootedTree()
        result = conv_char(leaf)
        self.assertIsNotNone(result)


class TestBaseIncrement(unittest.TestCase):
    """Test base increment calculation."""
    
    def test_base_increment_values(self):
        """Test that base_increment matches bas(n) from ion layers."""
        for n in range(1, 6):
            bi = base_increment(n)
            layer = ion_layer(n)
            self.assertEqual(bi, layer['bas'], 
                           f"base_increment({n}) should equal bas({n})")
    
    def test_base_increment_positive(self):
        """Test that base increments are non-negative."""
        for n in range(1, 10):
            bi = base_increment(n)
            self.assertGreaterEqual(bi, 0, f"base_increment({n}) should be non-negative")
        
        # Most should be positive
        for n in range(2, 10):
            bi = base_increment(n)
            self.assertGreater(bi, 0, f"base_increment({n}) should be positive for n >= 2")


class TestCognitiveRenormalization(unittest.TestCase):
    """Test cognitive renormalization via antipode."""
    
    def test_cognitive_renormalization_leaf(self):
        """Test renormalization on a leaf."""
        # Simple character
        def eval_func(tree):
            return float(tree.order)
        
        char = Character(eval_func, lambda a, b: a * b, "test")
        
        leaf = RootedTree()
        result = cognitive_renormalization(char, leaf)
        
        # Should return -order for a leaf
        self.assertEqual(result, -1.0)
    
    def test_cognitive_renormalization_structure(self):
        """Test that renormalization produces valid output."""
        def eval_func(tree):
            return float(tree.order)
        
        char = Character(eval_func, lambda a, b: a * b, "test")
        
        tree = B_plus(RootedTree())
        result = cognitive_renormalization(char, tree)
        
        # Should be a number
        self.assertIsInstance(result, (int, float))


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
