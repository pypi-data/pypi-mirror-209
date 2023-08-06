"""
Licensio Library - EPL License Module

The EPL License module within the Licensio library provides a function to generate an Eclipse Public License statement.
The EPL License is an open-source license commonly used for software projects, especially those developed using Eclipse.
This module simplifies the process of generating EPL License statements for your projects.

For more information on the EPL License, please visit: <https://www.eclipse.org/legal/epl-2.0/>
"""

def getEPL(year: int, name: str) -> str:
    """
    Generate an Eclipse Public License (EPL) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The EPL license statement.

    Example:
        >>> from licensio.epl import getEPL
        >>> epl_license = getEPL(year=2023, name="Walter Hartwell Black")
        >>> print(epl_license)
    """
    template = f"""
Eclipse Public License
Version 2.0

Copyright (C) [{year}] [{name}]

This software is licensed under the Eclipse Public License, version 2.0 ("EPL-2.0").
You may obtain a copy of the EPL-2.0 at https://www.eclipse.org/legal/epl-2.0/.

Subject to the terms and conditions of the EPL-2.0, you may freely use, modify, and distribute this software, provided that:
- You retain the original copyright notice, this list of conditions, and the disclaimer below in all copies or substantial portions of the software.
- Any modifications or contributions you make are governed by the EPL-2.0.
- If you distribute this software in executable form, you must include a prominent notice stating that it is based on the EPL-2.0.

This software is provided "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDER(S) BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THIS SOFTWARE.
"""

    return template


if __name__ == "__main__":
    epl_license = getEPL(year=2023, name="Walter Hartwell Black")
    print(epl_license)
