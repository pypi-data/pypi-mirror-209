"""
Licensio Library - MIT Module

The MIT module within the Licensio library provides a function to generate a MIT License (MIT) license statement.
The MIT License is a permissive open-source license that allows users to use, modify, and distribute the software.
This module simplifies the process of generating MIT License statements for your projects.

For more information on the MIT License, please visit: <https://opensource.org/licenses/MIT>
"""

def getMIT(year: int, name: str) -> str:
    """
    Generate a MIT License (MIT) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The MIT license statement.

    Example:
        >>> from licensio.mit import getMIT
        >>> mit_license = getMIT(year=2023, name="Walter Hartwell Black")
        >>> print(mit_license)
    """
    template = f"""
MIT License

Copyright (C) [{year}] [{name}]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    return template


if __name__ == "__main__":
    mit_license = getMIT(year=2023, name="Walter Hartwell Black")
    print(mit_license)
