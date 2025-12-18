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
    PrimeEgregore
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


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()
