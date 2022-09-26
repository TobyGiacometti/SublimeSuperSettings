# SublimeSuperSettings

A [Sublime Text][1] package that enables per-directory configuration.

## Table of Contents

- [Why?](#why)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
    - [Package Control](#package-control)
    - [Manual](#manual)
- [Usage](#usage)
    - [General Settings Files](#general-settings-files)
    - [Syntax-Specific Settings Files](#syntax-specific-settings-files)
    - [Settings File Format](#settings-file-format)
    - [Example](#example)

## Why?

Sublime Text can be configured easily without having to go through a dozen different menus and windows: Just adjust a single JSON file and be done with it. However, out of the box, configuration is limited to one global settings file and a single settings file per project. On top of that, syntax-specific settings for a project cannot be adjusted. SublimeSuperSettings takes care of all these limitations by enabling per-directory configuration.

## Features

- Sublime Text settings are automatically adjusted using per-directory settings files.
- In addition to the general per-directory configuration functionality, settings can further be split by syntax.
- The complete directory tree is searched to discover and merge settings files.

## Requirements

SublimeSuperSettings works with Sublime Text 3.

## Installation

### Package Control

Installing SublimeSuperSettings through [Package Control][2] is recommended. Please note that the package you need to install is called `SuperSettings`. Check out the Package Control [installation instructions][3] if you need help.

### Manual

Following steps can be used if you prefer to manually manage your Sublime Text packages:

1. [Download][4] SublimeSuperSettings.
2. Extract the downloaded archive.
3. Rename the extracted directory to `SublimeSuperSettings`.
4. Move the directory to your Sublime Text packages directory. You can access the Sublime Text packages directory by opening the command palette *(Tools → Command Palette)* and entering `Browse Packages`.

## Usage

### General Settings Files

Simply place a file called `Preferences.sublime-settings` inside a directory. Any Sublime Text tab for a file inside that directory (and subdirectories) will be configured accordingly. Settings files that are lower in the directory tree have higher priority and override settings that are defined in files higher up.

### Syntax-Specific Settings Files

You can also split settings inside a directory by syntax. For example, to apply settings to JavaScript files inside a directory, use following steps:

1. Open a JavaScript file with Sublime Text.
2. Access the command palette *(Tools → Command Palette)* and enter `Settings Syntax Specific`. This will open a syntax-specific settings file for JavaScript.
3. Note the name of the open settings file. It will be `JavaScript.sublime-settings` in this example.
4. Create an equally named file inside the desired directory.

The syntax-specific settings files follow the same discovery and merge logic as the general settings files.

### Settings File Format

The settings files for SublimeSuperSettings have the same format as the default Sublime Text settings files. For example:

```json
{
    "tab_size": 4,
    "rulers": [80],
    "translate_tabs_to_spaces": true
}
```

> **Note:** You cannot use comments inside settings files.

### Example

```
example/
	Preferences.sublime-settings
	HTML.sublime-settings
	JavaScript.sublime-settings

	js/
		Preferences.sublime-settings
		form.js

	index.html
```

- The file `example/index.html` uses settings from `example/Preferences.sublime-settings` and `example/HTML.sublime-settings`.
- The file `example/js/form.js` uses settings from `example/js/Preferences.sublime-settings`, `example/Preferences.sublime-settings` and `example/JavaScript.sublime-settings`.

[1]: https://www.sublimetext.com
[2]: https://packagecontrol.io
[3]: https://packagecontrol.io/installation
[4]: https://github.com/TobyGiacometti/SublimeSuperSettings/releases
