"""
Licensio Library - GNU License Module

The GNU License module within the Licensio library provides a function to generate a GNU General Public License statement.
The GNU License is a widely used open-source license for software projects.
This module simplifies the process of generating GNU License statements for your projects.

For more information on the GNU License, please visit: <https://www.gnu.org/licenses/>
"""

def getGNU(year: int, name: str) -> str:
    """
    Generate a GNU General Public License (GPL) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The GNU license statement.

    Example:
        >>> from licensio.gnu import getGNU
        >>> gnu_license = getGNU(year=2023, name="Walter Hartwell Black")
        >>> print(gnu_license)
    """

    template = f"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) [{year}] [{name}]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

    return template


if __name__ == "__main__":
    gnu_license = getGNU(year=2023, name="Walter Hartwell Black")
    print(gnu_license)
