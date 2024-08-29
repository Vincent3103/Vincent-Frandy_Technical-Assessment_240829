import re

def validate_input(N, M, A, B):
    # Validasi N dan M
    if not (1 <= N <= 100 and 1 <= M <= 100):
        raise ValueError("N dan M harus antara 1 dan 100")

    # Validasi A dan B
    for a in A:
        if not (1 <= a <= 1000):
            raise ValueError("Tingkat kemahiran (A) harus antara 1 dan 1000")

    for b in B:
        if not (1 <= b <= 1000):
            raise ValueError("Increment (B) harus antara 1 dan 1000")

def max_skill_level(N, M, A, B):
    # Validasi Input
    validate_input(N, M, A, B)

    # Buat pasangan (tingkat kemahiran, increment)
    opponents = list(zip(A, B))
    
    # Urutkan lawan berdasarkan tingkat kemahiran
    opponents.sort()
    
    current_skill = M

    for skill, increment in opponents:
        if skill <= current_skill:
            current_skill += increment
    
    return current_skill

# Input
try:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Output
    print(max_skill_level(N, M, A, B))
except ValueError as e:
    print(f"Error: {e}")
