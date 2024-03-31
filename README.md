![alt text](https://github.com/mullweisser/mac-weenu/blob/readme-update/weenu-logo.png?raw=true)
![alt text](https://github.com/mullweisser/mac-weenu/blob/readme-update/weenu-screenshot01.png?raw=true) ![alt text](https://github.com/mullweisser/mac-weenu/blob/readme-update/weenu-screenshot02.png?raw=true)

# WeeNu - Week Number in your macOS Menu Bar

WeeNu offers a sleek and minimalist solution for macOS users who frequently rely on week numbers, a common practice in Sweden and possibly elsewhere. 

Born from my own frustration with constantly having to open a calendar or visit the website [vecka.nu](https://vecka.nu) to check the current week number, this application brings that information directly to your macOS menu bar. 

Aiming to prioritize a minimalistic design and low compute resource usage, WeeNu ensures an unobtrusive presence while providing quick and easy access to the week number according to the ISO 8601 standard.

## Features

* Shows the current week number in the macOS menu bar, compliant with ISO 8601.
* Choose to show a prefix or only the week number.

## Installation

### Option 1: Download Precompiled Executable (Recommended for Most Users)

For ease of use, a precompiled version of WeeNu is available.

- Download the latest release from the [releases page](https://github.com/mullweisser/mac-weenu/releases).
- Mount the DMG-file.
- Drag&Drop the 'WeeNu.app' file to the 'Applications' folder.
- Launch 'WeeNu.app'

### Option 2: From Source

To install WeeNu from source, ensure you have Python and pip installed on your macOS. Follow these steps:

1. Clone the repository or download the source code:

```bash
git clone https://github.com/mullweisser/mac-weenu.git
cd weenu
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python WeeNu.py
```

## Usage

After installation, WeeNu runs in the background and adds an icon to your menu bar displaying the current week number. You can interact with it by clicking on the icon to see the dropdown menu with the following options:

- **Manual update:** Click to manually update the week number.
- **Settings > Show prefix/Hide prefix:** Toggle to display or hide the 'w.' prefix before the week number.
- **About WeeNu:** Opens the GitHub repository page in your default web browser.

## Development

Want to contribute? Great! WeeNu is open for contributions. Whether it's bug fixing, feature development, or suggestions, feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the [rumps](https://github.com/jaredks/rumps) framework.
