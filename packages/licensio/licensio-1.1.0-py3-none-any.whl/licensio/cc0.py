"""
Licensio Library - CC0 Module

The CC0 module within the Licensio library provides a simple function to generate a Creative Commons Zero (CC0) license statement.
CC0 is a public domain dedication that allows users to waive all rights and place their work into the public domain.
This module simplifies the process of generating CC0 license statements for your projects.

For more information on the CC0 license, please visit: <https://creativecommons.org/publicdomain/zero/1.0/>
"""

def getCC0(year: int, name: str) -> str:
    """
    Generate a Creative Commons Zero (CC0) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The CC0 license statement.

    Example:
        >>> from licensio.cc0 import getCC0
        >>> cc0_license = getCC0(year=2023, name="Walter Hartwell Black")
        >>> print(cc0_license)
    """
    template = f"""
CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

Copyright (C) [{year}] [{name}]

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of their rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.

For more information, please visit: <https://creativecommons.org/publicdomain/zero/1.0/>
"""

    return template


if __name__ == "__main__":
    cc0_license = getCC0(year=2023, name="Walter Hartwell Black")
    print(cc0_license)
