"""
Licensio Library - WTFPL License Module

The WTFPL License module within the Licensio library provides a function to generate a DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE statement.
The WTFPL License is a permissive license that allows you to do whatever you want with the software.
This module simplifies the process of generating WTFPL License statements for your projects.

For more information on the WTFPL License, please visit: <http://www.wtfpl.net/about/>
"""

def getWTFPL(year: int, name: str) -> str:
    """
    Generate a DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE (WTFPL) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The WTFPL license statement.

    Example:
        >>> from licensio.wtfpl import getWTFPL
        >>> wtfpl_license = getWTFPL(year=2023, name="Walter Hartwell Black")
        >>> print(wtfpl_license)
    """

    template = f"""
DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE
Version 2, December 2004

Copyright (C) [{year}] [{name}]

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE F*CK YOU WANT TO.
"""

    return template


if __name__ == "__main__":
    wtfpl_license = getWTFPL(year=2023, name="Walter Hartwell Black")
    print(wtfpl_license)
