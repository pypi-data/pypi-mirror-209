"""
Licensio Library - Apache License Module

The Apache License module within the Licensio library provides a function to generate an Apache License 2.0 license statement.
The Apache License is a permissive open-source license that allows users to use, modify, and distribute the software.
This module simplifies the process of generating Apache License statements for your projects.

For more information on the Apache License, please visit: <https://www.apache.org/licenses/LICENSE-2.0>
"""

def getApache(year: int, name: str) -> str:
    """
    Generate an Apache License (Apache) license statement.

    Args:
        year (int): The year of the dedication.
        name (str): The name of the person making the dedication.

    Returns:
        str: The Apache license statement.

    Example:
        >>> from licensio.apache import getApache
        >>> apache_license = getApache(year=2023, name="Walter Hartwell Black")
        >>> print(apache_license)
    """
    template = f"""
Apache License
Version 2.0, January 2004

Copyright (C) [{year}] [{name}]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

    return template


if __name__ == "__main__":
    apache_license = getApache(year=2023, name="Walter Hartwell Black")
    print(apache_license)
