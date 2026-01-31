def add_five_numbers(a, b, c, d, e):
    """
    Addiert 5 Zahlen und gibt das Ergebnis zurück.

    Args:
        a: Erste Zahl
        b: Zweite Zahl
        c: Dritte Zahl
        d: Vierte Zahl
        e: Fünfte Zahl

    Returns:
        Die Summe der fünf Zahlen
    """
    return a + b + c + d + e


if __name__ == "__main__":
    # Beispielaufruf
    result = add_five_numbers(1, 2, 3, 4, 5)
    print(f"Die Summe von 1, 2, 3, 4, 5 ist: {result}")
