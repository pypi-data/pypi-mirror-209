"""
Licensio Library - AGPL Module

The AGPL module within the Licensio library provides a function to generate a GNU Affero General Public License (AGPL) license statement.
The AGPL is a copyleft license designed for software that is distributed over a network.
This module simplifies the process of generating AGPL license statements for your projects.

For more information on the AGPL license, please visit: <https://www.gnu.org/licenses/agpl-3.0.en.html>
"""

def getAGPL(year: int, name: str) -> str:
    """
    Generate a GNU Affero General Public License (AGPL) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The AGPL license statement.

    Example:
        >>> from licensio.agpl import getAGPL
        >>> agpl_license = getAGPL(year=2023, name="Walter Hartwell Black")
        >>> print(agpl_license)
    """
    template = f"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007

Copyright (C) [{year}] [{name}]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

    return template


if __name__ == "__main__":
    agpl_license = getAGPL(year=2023, name="Walter Hartwell Black")
    print(agpl_license)
