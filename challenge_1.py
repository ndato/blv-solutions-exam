from typing import Union, Dict


def shift_char(m: str, N: int) -> str:
    """Shift Single Characters based on N. Retain if m is not an
       uppercase or lowercase letter.

    Args:
        m (str): Single Character.
        N (int): Shift right if positive, shift left if negative.

    Raises:
        ValueError: If m is not a Single Character.

    Returns:
        str: Shifted Single Character.
    """
    # Set up character bounds if either lowercase or uppercase.
    if m.islower():
        a, z = (ord("a"), ord("z"))
    elif m.isupper():
        a, z = (ord("A"), ord("Z"))
    else:
        # If character is not an alphabet character, return as is.
        return m

    # Shift character N places.
    m_char = ord(m) + N

    # Handle overflow to go back to 'A' or 'Z'
    if m_char > z:
        m_char = a + (m_char - z - 1)
    elif m_char < a:
        m_char = z - (a - 1 - m_char)

    return chr(m_char)


def replace_char(m: str, N: Dict[str, str]) -> str:
    """Replace Single Character with N. Retain if N
       is not an Alphabet character or not in N.

    Args:
        m (str): Single Character to be replaced.
        N (Dict[str, str]): Dictionary containing replacements.

    Returns:
        str: Single Replaced Character.
    """
    if m.isalpha():
        return N.get(m, m)
    return m


def cipher_text(m: str, N: Union[int, Dict[str, str]]) -> str:
    """Do a Caesar Cipher if N is an integer, or do a
       replacement if N is a dictionary.

    Args:
        m (str): String to be ciphered.
        N (Union[int, Dict[str, str]]): If integer, shift characters
                                        left or right if it's positive
                                        or negative. If Dictionary,
                                        replace characters indicated.

    Raises:
        ValueError: N is not in the range of -25 and 25.
        ValueError: N is not either a dictionary or integer.

    Returns:
        str: The ciphered text.
    """
    # Check input N if it's an Integer or Dictionary and set the
    # appropriate character mutation.
    if type(N) is int:
        # Check if N is within -25 to 25.
        if N > 25 or N < -25:
            raise ValueError("N should be in the range of -25 to 25.")
        change_char = shift_char
    elif type(N) is dict:
        # Get replacement from N if the character is an alphabet character.
        change_char = replace_char
    else:
        raise ValueError("Incorrect Input Data Type for N.")
    
    output = ""

    # Cipher the text per character.
    for char in m:
        output += change_char(char, N)
    print(m, "->", N, "->", output)
    return output


if __name__ == "__main__":
    # Simple Tests
    tests_in = (
        ("AbCdE", 5),
        ("vWxYz", 5),
        ("@bCdE", 25),
        ("AbCdE", -1),
        ("AbCdE", -5),
        ("@bCdE", -5),
        ("@bCdE", -25),
        ("AbCdE", {"A": "X", "C": "T", "E": "F"}),
        ("AbC$E", {"A": "X", "C": "T", "E": "F", "$": "%"}),
    )
    tests_out = (
        "FgHiJ",
        "aBcDe",
        "@aBcD",
        "ZaBcD",
        "VwXyZ",
        "@wXyZ",
        "@cDeF",
        "XbTdF",
        "XbT$F",
    )

    for test_in, test_out in zip(tests_in, tests_out):
        assert test_out == cipher_text(*test_in)
