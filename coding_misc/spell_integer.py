
# convert integer number into word representation
# 19 -> "nineteen"
# 800 -> "eight hundred"
# 482910231 -> "four hundred eighty two million nine hundred ten thousand two hundred thirty one"

dig20 = {0:'', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens  = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 
         6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

# -----------------------------------------------
def spell_period(N):
    """
    # gets number in range 0...999
    # spells it - returns the string
    """
    arr = []
    N_hundreds = N // 100
    if N_hundreds >= 1:
        arr.append(dig20[N_hundreds] + " hundred")
    N_tens = (N % 100) // 10
    if N_tens >= 2:
        arr.append(tens[N_tens])
        last_digit = N % 10
        if last_digit > 0:
            arr.append(dig20[last_digit])
    else:
        last_two_digits = N % 100
        if last_two_digits > 0:
            arr.append(dig20[last_two_digits])

    return " ".join(arr)

# -----------------------------------------------
def spell_num(num):
    """
    # convert int number into sentence in English
    # 32 bit, range approx +/-2,000,000,000
    """
    if num == 0:
        return "zero"
    ss = []
    if num < 0:
        ss += ["minus"]
        num = -num

    # ---------------------------------
    # split number into 4 periods: 
    Nb = num // 10**9           # billons (0-2)
    Nm = num % 10**9 // 10**6   # millions (0-999)
    Nt = num % 10**6 // 10**3   # thousands(0-999)
    Nn = num % 10**3            # normal(0-999)
    # ---------------------------------
    if Nb> 0:
        ss.append(spell_period(Nb) + " billion")
    if Nm> 0:
        ss.append(spell_period(Nm) + " million")
    if Nt> 0:
        ss.append(spell_period(Nt) + " thousand")
    if Nn> 0:
        ss.append(spell_period(Nn))

    return " ".join(ss)

# -----------------------------------------------
# main portion - test the code
# -----------------------------------------------
tests = [0, 10, 11, 19, 
         100, 101, 110, 120, 
         800, 1001, 
         482910231, 2010020001]

for num in tests:
    ss = spell_num(num)
    print(f'{num} -> "{ss}"')

