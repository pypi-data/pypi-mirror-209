# Bit-Saver

Bit-Saver is a Python library for fetching and saving OHLCV (Open, High, Low, Close, Volume) data from Upbit exchange to local storage.

## Installation

You need to have Python 3 or higher installed. Installation of the library can be done simply with pip:

```
pip install bit-saver
```

## Usage

Here's a basic example of how to use Bit-Saver:

```python
from bit_saver import BitSaver

bit_saver = BitSaver()
bit_saver.save_all_data('your_directory_path')
```

## Features
- Fetches OHLCV data for all coins from Upbit on a daily basis.
- Saves the data locally in CSV format.

## License
This project is distributed under the MIT license. For more information, see the LICENSE file.

## Contact
If you encounter any problems or have any questions, please open an issue on our Github issues page.
