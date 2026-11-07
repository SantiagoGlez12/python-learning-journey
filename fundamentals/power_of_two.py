"""Identify whether an integer is a power of two.

Introductory Python exercise: input validation, while loops and functions.
"""

def es_potencia_de_2(numero):
    """Return True when numero is a positive integer power of 2."""
    if isinstance(numero, bool) or not isinstance(numero, int) or numero < 1:
        return False
    while numero > 1:
        if numero % 2 != 0:
            return False
        numero //= 2
    return True


if __name__ == "__main__":
    for valor in (2, 4, 7, 16, 100000):
        print(f"{valor}: {es_potencia_de_2(valor)}")
