# -*- coding: utf-8 -*-
"""CM001 - Chapter 19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FchF5OGzIV06y7buzqmRrHiNSV8giK3N

#P (Polynomial Time)

P is the class of decision problems that can be solved by a deterministic Turing machine in polynomial time.
"""

def is_in_P(input_size):
    # O(n^2) time complexity example
    return input_size ** 2 <= 1000000

# Example usage
input_size = int(input("Enter input size: "))
print("Is in P:", is_in_P(input_size))

"""#NP (Nondeterministic Polynomial Time)

NP is the class of decision problems for which a proposed solution can be verified in polynomial time.
"""

def is_in_NP(problem_instance, proposed_solution):
    # Check if the proposed solution is correct for the given problem instance
    # O(n^2) time complexity example
    return proposed_solution ** 2 == problem_instance

# Example usage
problem_instance = int(input("Enter problem instance: "))
proposed_solution = int(input("Enter proposed solution: "))
print("Is in NP:", is_in_NP(problem_instance, proposed_solution))

"""#EXP (Exponential Time)

EXP is the class of decision problems that can be solved by a deterministic Turing machine in exponential time.
"""

def is_in_EXP(input_size):
    # O(2^n) time complexity example
    return 2 ** input_size <= 1000000

# Example usage
input_size = int(input("Enter input size: "))
print("Is in EXP:", is_in_EXP(input_size))

"""#R (Recursive Enumerable)

R is the class of decision problems that are recursively enumerable.
"""

def is_in_R(problem_instance):
    # Placeholder function, as checking if a problem is in R is non-trivial
    # This function always returns True for demonstration purposes
    return True

# Example usage
problem_instance = input("Enter problem instance: ")
print("Is in R:", is_in_R(problem_instance))

"""#Most problems are uncomputable

It's a fundamental result in computer science, established by Alan Turing, that most problems are uncomputable. This means that there are problems for which no algorithm can correctly solve all instances of the problem. One classic example is the Halting Problem, which asks whether a given program halts or runs forever on a given input. Here's a Python example demonstrating the uncomputability of the Halting Problem:
"""

def halts(program, input):
    # Placeholder function to simulate the Halting Problem
    # In reality, this function cannot be implemented as it's undecidable
    # This function always returns False for demonstration purposes
    return False

# Example usage
program = "print('Hello, world!')"  # Example program
input_data = "anything"  # Example input
print("Does the program halt?", halts(program, input_data))

"""#Hardness:

Hardness refers to how difficult a problem is to solve. A problem is said to be hard if there is no efficient algorithm known for solving it. In complexity theory, we often talk about two types of hardness:


*   Time Complexity Hardness: This refers to problems for which no algorithm with a better-than-polynomial time complexity is known. These problems are often referred to as "intractable" or "computationally expensive."
*  Space Complexity Hardness: This refers to problems for which no algorithm with a better-than-polynomial space complexity is known. These problems consume a large amount of memory.

#Completeness:

An algorithm is considered complete if for any input it correctly reports whether there is a solution in a finite amount of time.
Completeness refers to the property of a problem within a certain class of problems (e.g., NP-complete) such that every problem in that class can be reduced to it. If a problem is both hard and complete within a certain class, it is called "NP-hard." If, in addition, it belongs to the class itself, it is called "NP-complete."
"""

class Problem:
    def __init__(self):
        pass

    def is_solution(self, candidate_solution):
        """
        Check if the candidate solution satisfies the problem's constraints.
        """
        pass

    def solve(self):
        """
        Attempt to solve the problem.
        """
        pass

class TimeComplexityHardness(Problem):
    def __init__(self):
        super().__init__()

    def solve(self):
        """
        Since this problem is time complexity hard, a polynomial-time algorithm is not known.
        """
        print("This problem is time complexity hard.")

class SpaceComplexityHardness(Problem):
    def __init__(self):
        super().__init__()

    def solve(self):
        """
        Since this problem is space complexity hard, a polynomial-space algorithm is not known.
        """
        print("This problem is space complexity hard.")

class NPCompleteProblem(Problem):
    def __init__(self):
        super().__init__()

    def solve(self):
        """
        This is an example of an NP-complete problem.
        """
        print("This problem is NP-complete.")

class NPHardProblem(Problem):
    def __init__(self):
        super().__init__()

    def solve(self):
        """
        This is an example of an NP-hard problem.
        """
        print("This problem is NP-hard.")

# Example usage
if __name__ == "__main__":
    time_hard_problem = TimeComplexityHardness()
    space_hard_problem = SpaceComplexityHardness()
    np_complete_problem = NPCompleteProblem()
    np_hard_problem = NPHardProblem()

    time_hard_problem.solve()
    space_hard_problem.solve()
    np_complete_problem.solve()
    np_hard_problem.solve()

"""#Reduction for NP-Completeness"""

class Reduction:
    @staticmethod
    def reduce(problem_a, problem_b):
        """
        Reduce problem_a to problem_b.
        """
        print(f"Reducing {problem_a} to {problem_b}...")
        # Perform reduction steps here
        if problem_a.completeness == "NP-Complete" and problem_b.complexity == "NP-Hard":
            print(f"Reducing {problem_a} to {problem_b} by simulating a Turing machine.")
            print(f"{problem_a} reduced to {problem_b} successfully.")
            return True
        else:
            print("Reduction not possible.")
            return False

class Problem:
    def __init__(self, complexity=None, completeness=None):
        self.complexity = complexity
        self.completeness = completeness

    def solve(self):
        print("Solving the problem...")

    def __str__(self):
        complexity_str = self.complexity if self.complexity else "Not specified"
        completeness_str = self.completeness if self.completeness else "Not specified"
        return f"Problem: Complexity - {complexity_str}, Completeness - {completeness_str}"

class TimeComplexityHardness(Problem):
    def __init__(self):
        super().__init__(complexity="Time Complexity Hard")

    def solve(self):
        print("This problem is time complexity hard.")

class SpaceComplexityHardness(Problem):
    def __init__(self):
        super().__init__(complexity="Space Complexity Hard")

    def solve(self):
        print("This problem is space complexity hard.")

class NPCompleteProblem(Problem):
    def __init__(self):
        super().__init__(completeness="NP-Complete")

    def solve(self):
        print("This problem is NP-complete.")

class NPHardProblem(Problem):
    def __init__(self):
        super().__init__(complexity="NP-Hard")

    def solve(self):
        print("This problem is NP-hard.")

# Example usage
if __name__ == "__main__":
    time_hard_problem = TimeComplexityHardness()
    space_hard_problem = SpaceComplexityHardness()
    np_complete_problem = NPCompleteProblem()
    np_hard_problem = NPHardProblem()

    print(time_hard_problem)
    print(space_hard_problem)
    print(np_complete_problem)
    print(np_hard_problem)
    print()

    # Try reducing NP-complete problem to NP-hard problem
    if Reduction.reduce(np_complete_problem, np_hard_problem):
        print("Reduction successful!")
    else:
        print("Reduction failed.")