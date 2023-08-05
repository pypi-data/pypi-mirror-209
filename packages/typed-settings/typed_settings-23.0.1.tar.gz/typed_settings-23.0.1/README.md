# Typed Settings

Merge settings from multiple different sources and present them in a structured, typed, and validated way!

## Why?

There are many different config file formats and libraries.
Many of them have a narrow scope, don't integrate well with other libs, or lack in typing support.

Typed Settings' goal is to enable you to load settings from any source (e.g., env vars, config files, vaults)
and can convert values to anything you need.

You can extend Typed Settings to support config sources that aren't supported yet
and its extensive documentation will help you on your way.

## What can it be used for?

You can use Typed Settings in any context, e.g.:

- server processes
- containerized apps
- command line applications
- scripts and tools for scientific experiments and data analysis

## What does it do?

- It loads settings from multiple sources (e.g., env vars, config files, vaults) in a unified way and merges the loaded values.
  You can add loaders for sources we cannot imagine yet.

- It can post-process loaded values.
  This allows value interpolation/templating or calling helpers that retrieve secrets from vaults.
  You can create and add any processors you can image if the built-in ones are not enought.

- You can add a CLI on top to let users update the loaded settings via command line arguments.
  [Click](https://click.palletsprojects.com) and [argparse](https://docs.python.org/3/library/argparse.html) are currently supported.

- Settings are cleanly structured and typed.
  The type annotations are used to convert the loaded settings to the proper types.
  This also includes higher level structures like dates, paths and various collections (lists, dicts, …).
  This is currently done with [attrs](https://www.attrs.org) and [cattrs](https://cattrs.readthedocs.io)) (but we know people also love Pydantic or dataclasses).

The documentation contains a [full list](https://typed-settings.readthedocs.io/en/latest/why.html#comprehensive-list-of-features) of all features.


## Installation

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```console
$ python -m pip install typed-settings
```

You can install dependencies for optional features via

```console
$ python -m pip install typed-settings[<feature>,...]
```

Available features:

- `typed-settings[click]`: Enable support for Click options
- `typed-settings[option-groups]`: Enable support for Click and Click option groups
- `typed-settings[jinja]`: Enable support for value interpolation with Jinja templates
- `typed-settings[all]`: Install all optional requirements

## Examples

### Hello, World!, with env. vars.

This is a very simple example that demonstrates how you can load settings from environment variables.

```python
# example.py
import typed_settings as ts

@ts.settings
class Settings:
    option: str

settings = ts.load(cls=Settings, appname="example")
print(settings)
```

```console
$ EXAMPLE_OPTION="Hello, World!" python example.py
Settings(option='Hello, World!')
```


### Nested classes and config files

Settings classes can be nested.
Config files define a different section for each class.

```python
# example.py
import click

import typed_settings as ts

@ts.settings
class Host:
    name: str
    port: int

@ts.settings(kw_only=True)
class Settings:
    host: Host
    endpoint: str
    retries: int = 3

settings = ts.load(
    cls=Settings, appname="example", config_files=["settings.toml"]
)
print(settings)
```

```toml
# settings.toml
[example]
endpoint = "/spam"

[example.host]
name = "example.com"
port = 443
```

```console
$ python example.py
Settings(host=Host(name='example.com', port=443), endpoint='/spam', retries=3)
```


### Configurable settings loaders

The first example used a convenience shortcut with pre-configured settings loaders.
However, Typed Settings lets you explicitly configure which loaders are used and how they work:

```python
# example.py
import typed_settings as ts

@ts.settings
class Settings:
    option: str

settings = ts.load_settings(
    cls=Settings,
    loaders=[
        ts.FileLoader(
            files=[],
            env_var="EXAMPLE_SETTINGS",
            formats={
                "*.toml": ts.TomlFormat("example"),
            },
        ),
        ts.EnvLoader(prefix="EXAMPLE_"),
      ],
)
print(settings)
```

```console
$ EXAMPLE_OPTION="Hello, World!" python example.py
Settings(option='Hello, World!')
```

In order to write your own loaders or support new file formats, you need to implement the `Loader` or `FileFormat` [protocols](https://typed-settings.readthedocs.io/en/latest/apiref.html#module-typed_settings.loaders).

You can also pass a custom [cattrs converter](https://cattrs.readthedocs.io/en/latest/index.html) to add support for additional Python types.


### Command Line Interfaces

Typed Settings can generate a command line interfaces (CLI) based on your settings.
These CLIs will load settings as described above and let users override the loades settings with command line argumments.

Typed Settings supports `argparse` and `click`.


#### Argparse

```python
# example.py
import typed_settings as ts

@ts.settings
class Settings:
    a_str: str = ts.option(default="default", help="A string")
    an_int: int = ts.option(default=3, help="An int")

@ts.cli(Settings, "example")
def main(settings):
    print(settings)

if __name__ == "__main__":
    main()
```

```console
$ python example.py --help
usage: example.py [-h] [--a-str TEXT] [--an-int INT]

options:
  -h, --help    show this help message and exit

Settings:
  Settings options

  --a-str TEXT  A string [default: default]
  --an-int INT  An int [default: 3]
$ python example.py --a-str=spam --an-int=1
Settings(a_str='spam', an_int=1)
```

#### Click


```python
# example.py
import click
import typed_settings as ts

@ts.settings
class Settings:
    a_str: str = ts.option(default="default", help="A string")
    an_int: int = ts.option(default=3, help="An int")

@click.command()
@ts.click_options(Settings, "example")
def main(settings):
    print(settings)

if __name__ == "__main__":
    main()
```

```console
$ python example.py --help
Usage: example.py [OPTIONS]

Options:
  --a-str TEXT      A string  [default: default]
  --an-int INTEGER  An int  [default: 3]
  --help            Show this message and exit.
$ python example.py --a-str=spam --an-int=1
Settings(a_str='spam', an_int=1)
```


## Features

- Settings are defined as type-hinted `attrs` classes.

- Typed Settings’ `settings` decorator is an alias to `attrs.define` and can optionally make your settings frozen (immutable).

- `option()` and `secret()` are wrappers around `attrs.field()` and add meta data handling for Click options.

- `secret()` attributes have string representation that masks the actual value, so that you can safely print or log settings instances.

- Settings can currently be loaded from:

  - TOML files
  - Python files
  - Environment variables
  - *Click* command line options

- Settings are converted to their correct type using [cattrs](https://cattrs.readthedocs.io).

  - Users can extend the default converter with hooks for custom types
  - Lists can be loaded from strings from environment variables.
    String-to-list conversion can be configured.
    Strings can be JSON structues or simple comma (or colon) speparated lists (e.g., `"1,2,3"` or `"path1:path2"`).

- Paths to settings files can be

  - “hard-coded” into your code,
  - dynamically searched from the CWD upwards via `find(filename)`, or
  - specified via an environment variable.

- Order of precedence:

  - Default value from settings class
  - First file from hard-coded config files list
  - ...
  - Last file from hard-coded config files list
  - First file from config files env var
  - ...
  - Last file from config files env var
  - Environment variable `{PREFIX}_{SETTING_NAME}`
  - (Value passed to Click option)

- Config files are “optional” by default – no error is raised if a specified file does not exist.

- Config files can be marked as mandatory by prefixing them with an `!`.
