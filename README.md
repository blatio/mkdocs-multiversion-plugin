# mkdocs-multiversion-plugin
[![PyPI Version][pypi-image]][pypi-link]

`mkdocs-multiversion-plugin` is a plugin for [mkdocs](https://www.mkdocs.org/) - a **fast**, **simple** and **downright gorgeous** gorgeous static site generator that's geared towards building project documentation. 

`mkdocs-multiversion-plugin` allows you to build and have different versions of your project documentation.

![mkdocs-multiversion-plugin-demo-screen](https://github.com/blatio/mkdocs-multiversion-plugin/raw/master/doc/img/screen.png?raw=true "mkdocs-multiversion-plugin demo screen")

## How It Works

`mkdocs-multiversion-plugin` works by creating a new version of documentation inside mkdocs `site_dir/<version>` directory and adds configuration file containing information about versions to `site_dir/multiversion.json`. The plugin doesn't create new branches in your git repository.

## Setup

Install the plugin using pip:

```bash
pip install mkdocs-multiversion-plugin
```

Next, add the following lines to your `mkdocs.yml`:

```yml
plugins:
  - multiversion
```

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

## Configuration

Guide to all available configuration settings.

To change some behavior of the plugin you need to set proper config option in `mkdocs.yml` under plugin section.
```yml
plugins:
  - multiversion:
    branch_whitelist: None
    version_in_site_name: False
```
List of available config options:

| Name | Type | Default value | Description |
| :- | :-: | :-: | :- |
| `version_in_site_name` | string | `True` | Adds the version name to the mkdocs `site_name` config. |
| `branch_whitelist` | string | `^.*$` | Whitelist branch names, regex. |
| `tag_whitelist` | string | `^.*$` | Whitelist tag names, regex. |
| `latest_version_name_format` | string | `latest release ({version})` | Latest version name format, argument: `{version}`. |
| `version_name_format` | string | `{version}` | Version name format, argument: `{version`. |
| `css_dir` | string | `css` | The name of the directory for css files. |
| `javascript_dir` | string | `js` |  The name of the directory for javascript files. |
| `versions_url` | string | '' | The URL for the versions file. |
| `versions_file_name` | string | `multiversion.json`, `index.php` | The name for the file on the server containing generated versions. |
| `generate_versions_file` | bool | true | Specifies whether to generate a file with versions. |
| `versions_provider` | string | `static` | Available version providers: `php`, `static`. |

> If the `generate_versions_file` configuration option is false, you need to deliver the file with the available versions yourself.

The file should contain JSON in the format:
```json
{
    "stable" : {
        "name" : "stable",
        "latest" : false
    },
    "0.2.0" : {
        "latest" : true,
        "name" : "latest release (0.2.0)"
    },
    "0.1.0" : {
        "latest" : false,
        "name" : "0.1.0"
    }
}
```

### Versions provider
There are two documentation versions providers:
* static - static json file generated during building documentation containing versions from git repository.
* php - the dynamic engine that generates a list of available versions on the server. A server with PHP support is required for its operation. Generated versions are a list of directories on the server.
#### Static provider configuration:
```yml
plugins:
  - multiversion
```

#### PHP provider configuration:
```yml
plugins:
  - multiversion:
    versions_provider: php
```

> It is possible to override name of the static file: `versions_file_name`. Be careful to enter the correct path to the file. In case it is a relative path, the name will be prefixed with the path to the base directory: `base_url`.


## Contributing 

Please note that `mkdocs-multiversion-plugin` is currently in **Beta** and there may be missing feature/documentation so if you could help out by either:

1. finding and reporting bugs
2. contributing by checking out the [issues](https://github.com/blatio/mkdocs-multiversion-plugin/issues)

### License
[BSD-3-Clause](https://github.com/blatio/mkdocs-multiversion-plugin/blob/master/LICENSE)

<!-- Badges -->
[pypi-image]: https://img.shields.io/pypi/v/mkdocs-multiversion-plugin
[pypi-link]: https://pypi.org/project/mkdocs-multiversion-plugin/