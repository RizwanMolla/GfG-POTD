"""
Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

"""
class Solution:
    def primeList(self, head):
        # Helper function to check if a number is prime
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        # Helper function to find nearest prime
        def find_nearest_prime(num):
            if is_prime(num):
                return num
            
            # Search in both directions
            lower = num - 1
            higher = num + 1
            
            while True:
                # Check lower first (smaller prime has priority)
                if lower > 0 and is_prime(lower):
                    return lower
                
                # Then check higher
                if is_prime(higher):
                    return higher
                
                lower -= 1
                higher += 1

        current = head
        while current:
            current.val = find_nearest_prime(current.val)
            current = current.next
        
        return head