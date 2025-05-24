PASCAL_MOD_5 = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 1, 4, 1] 
]

def _get_coefficient_mod_10_impl(K, j):
    if j < 0 or j > K:
        return 0

    val_mod_2 = 1 if (K & j) == j else 0

    val_mod_5 = 1
    temp_K, temp_j = K, j
    while temp_K > 0 or temp_j > 0:
        K_digit = temp_K % 5
        j_digit = temp_j % 5
        
        if j_digit > K_digit:
            val_mod_5 = 0
            break
        
        val_mod_5 = (val_mod_5 * PASCAL_MOD_5[K_digit][j_digit]) % 5
        
        temp_K //= 5
        temp_j //= 5
    
    return (val_mod_2 * 5 + val_mod_5 * 6) % 10

class Solution:
  def hasSameDigits(self, s: str) -> bool:
    n = len(s)
    digits = [int(c) for c in s]
    K = n - 2 

    f0_sum = 0
    f1_sum = 0
    
    coeff_memo = {}

    for j_idx in range(K + 1):
        if j_idx in coeff_memo:
            coeff = coeff_memo[j_idx]
        else:
            coeff = _get_coefficient_mod_10_impl(K, j_idx)
            coeff_memo[j_idx] = coeff

        if coeff == 0:
            continue

        f0_sum = (f0_sum + coeff * digits[j_idx]) % 10
        f1_sum = (f1_sum + coeff * digits[j_idx + 1]) % 10
            
    return f0_sum == f1_sum
        