"""
Licensio Library - LGPL License Module

The LGPL License module within the Licensio library provides a function to generate a GNU Lesser General Public License statement.
The LGPL License is a free software license that allows linking with non-free software.
This module simplifies the process of generating LGPL License statements for your projects.

For more information on the LGPL License, please visit: <https://www.gnu.org/licenses/lgpl-3.0.en.html>
"""

def getLGPL(year: int, name: str) -> str:
    """
    Generate a GNU Lesser General Public License (LGPL) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The LGPL license statement.

    Example:
        >>> from licensio.lgpl import getLGPL
        >>> lgpl_license = getLGPL(year=2023, name="Walter Hartwell Black")
        >>> print(lgpl_license)
    """

    template = f"""
GNU LESSER GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) [{year}] [{name}]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

    return template


if __name__ == "__main__":
    lgpl_license = getLGPL(year=2023, name="Walter Hartwell Black")
    print(lgpl_license)
