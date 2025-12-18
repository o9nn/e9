"""
e9 - Prime Eigenvalue Function

This module implements the concept where the nth prime number (pₙ) is understood as
the "prime shell" or eigenvalue of the ensemble structure of its index n.

Conceptual Framework:
- pₙ = prime shell around the ensemble structure of n
- Each prime is a daemon that:
  1. Encapsulates the computational ensemble of its index
  2. Purifies it into an irreducible identity (the primality condition)
  3. Projects that identity back into all multiples of itself
"""

from typing import List, Set, Dict, Tuple, Any
from functools import lru_cache


class PrimeEgregore:
    """
    The Prime Egregore: A daemon representing a prime number that encapsulates,
    purifies, and projects the computational ensemble of its index.
    """
    
    def __init__(self, index: int, prime: int):
        """
        Initialize a Prime Egregore.
        
        Args:
            index: The position n in the prime sequence (1-indexed)
            prime: The nth prime number pₙ
        """
        self.index = index
        self.prime = prime
        self._ensemble = None
        self._multiples = None
    
    def encapsulate(self) -> Dict[str, Any]:
        """
        Encapsulates the computational ensemble of the index.
        Returns partition information and structural properties of n.
        """
        if self._ensemble is None:
            self._ensemble = {
                'index': self.index,
                'partitions': self._compute_partitions(self.index),
                'divisors': self._compute_divisors(self.index),
                'prime_factorization': self._prime_factorization(self.index),
                'composite_structure': self._composite_structure(self.index)
            }
        return self._ensemble
    
    def purify(self) -> int:
        """
        Purifies the ensemble into an irreducible identity.
        The prime number is the purified eigenvalue of its index's structure.
        """
        # The purification process transforms the index's composite structure
        # into the irreducible prime at that position
        return self.prime
    
    def project(self, limit: int = 100) -> Set[int]:
        """
        Projects the prime identity back into all multiples of itself.
        
        Args:
            limit: Maximum value for computing multiples
            
        Returns:
            Set of multiples of the prime up to the limit
        """
        # Always recompute to ensure correctness with different limits
        return {self.prime * k for k in range(1, limit // self.prime + 1)}
    
    @staticmethod
    def _compute_partitions(n: int) -> List[List[int]]:
        """Compute integer partitions of n."""
        if n == 0:
            return [[]]
        
        partitions = []
        for i in range(1, n + 1):
            for partition in PrimeEgregore._compute_partitions(n - i):
                if not partition or i <= partition[0]:
                    partitions.append([i] + partition)
        return partitions
    
    @staticmethod
    def _compute_divisors(n: int) -> List[int]:
        """Compute all divisors of n."""
        if n <= 0:
            return []
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sorted(divisors)
    
    @staticmethod
    def _prime_factorization(n: int) -> List[int]:
        """Compute prime factorization of n."""
        if n <= 1:
            return []
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    @staticmethod
    def _composite_structure(n: int) -> Dict[str, Any]:
        """Analyze the composite structure of n."""
        factors = PrimeEgregore._prime_factorization(n)
        return {
            'is_prime': len(factors) == 1 and factors[0] == n,
            'is_composite': len(factors) > 1 or (len(factors) == 1 and factors[0] != n),
            'factor_count': len(factors),
            'unique_factors': len(set(factors)),
            'factors': factors
        }
    
    def __repr__(self):
        return f"PrimeEgregore(index={self.index}, prime={self.prime})"


@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n: int) -> int:
    """
    Get the nth prime number (1-indexed).
    
    Args:
        n: The index of the prime to retrieve (1 for first prime)
        
    Returns:
        The nth prime number
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1


def prime_eigenvalue(n: int) -> PrimeEgregore:
    """
    Compute the prime eigenvalue for index n.
    
    This function crystallizes the concept that pₙ (the nth prime) is not
    merely coincidentally prime, but rather it represents the eigenvalue of
    the partition function of its index n.
    
    Args:
        n: The index in the prime sequence (1-indexed)
        
    Returns:
        A PrimeEgregore object encapsulating the relationship between
        the index and its prime eigenvalue
    """
    prime = nth_prime(n)
    return PrimeEgregore(n, prime)


def generate_prime_sequence(count: int) -> List[PrimeEgregore]:
    """
    Generate a sequence of Prime Egregores.
    
    Args:
        count: Number of primes to generate
        
    Returns:
        List of PrimeEgregore objects
    """
    return [prime_eigenvalue(i) for i in range(1, count + 1)]


def analyze_prime_projection(egregore: PrimeEgregore, limit: int = 100) -> Dict[str, Any]:
    """
    Analyze how a prime projects its identity through its multiples.
    
    Args:
        egregore: The PrimeEgregore to analyze
        limit: Upper limit for multiple generation
        
    Returns:
        Dictionary containing analysis of the prime's projection
    """
    multiples = egregore.project(limit)
    ensemble = egregore.encapsulate()
    
    return {
        'prime': egregore.prime,
        'index': egregore.index,
        'purified_value': egregore.purify(),
        'ensemble_structure': ensemble,
        'projection': {
            'multiples_count': len(multiples),
            'multiples': sorted(multiples),
            'projection_density': len(multiples) / limit if limit > 0 else 0
        }
    }
