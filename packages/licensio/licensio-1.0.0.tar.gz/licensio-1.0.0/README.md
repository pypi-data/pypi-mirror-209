# Licensio

Licensio is a Python library that provides a collection of functions to generate license statements for various open source licenses. It simplifies the process of including license information in your projects by providing ready-to-use license templates.

## Installation

You can install Licensio using pip:

```bash
pip install licensio
```


## Usage

To use Licensio, import the desired license module and call the corresponding function to generate the license statement. Here's an example of how to generate a license statement using the MIT license module:

```python
from licensio.mit import getMIT

# Generate MIT license statement
mit_license = getMIT(year=2023, name="Your Name")

# Print the license statement
print(mit_license)
```

Replace "Your Name" with your name and modify the year accordingly. You can find similar functions for other licenses in the `licensio` library.


## Supported Licenses
Licensio currently supports the following open source licenses:

- MIT License (MIT)
- Apache License (Apache)
- BSD 3-Clause License (BSD)
- Eclipse Public License (EPL)
- GNU General Public License (GPL)
- GNU Lesser General Public License (LGPL)
- DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE (WTFPL)
- Creative Commons Zero (CC0)

Each license module provides a function that accepts the year and the name of the person making the dedication and returns the corresponding license statement.

## Documentation

For detailed documentation, please refer to the [docs](./docs) folder.

The "docs" folder contains individual markdown files for each license module, providing information about the module and usage examples.


## Examples
For more examples on how to use Licensio, refer to the example code snippets provided in the documentation of each license module.

## License 
Licensio itself is released under the MIT License. You can find the full license text in the [LICENSE](LICENSE) file.


## Contributing
Contributions to Licensio are welcome! If you encounter any issues, have suggestions for improvements, or would like to add support for additional licenses, please open an issue or submit a pull request on the GitHub repository.

When contributing, please ensure that your code adheres to the existing code style and includes appropriate tests.

## Acknowledgments
Licensio is inspired by the need for a simple and convenient way to include license information in open source projects. It relies on the standardized license templates provided by various open source organizations.

## Developer
Licensio is developed and maintained by [Zayed Malick](https://github.com/zayedmalick).

## Contact
For any inquiries or feedback, you can reach me at zayedalmalick@gmail.com.

## Disclaimer
Licensio is provided as-is, without any warranty or guarantee of its functionality or suitability for any particular purpose. Use it at your own risk.
