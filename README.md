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

## Contributing 

Please note that `mkdocs-multiversion-plugin` is currently in **Beta** and there may be missing feature/documentation so if you could help out by either:

1. finding and reporting bugs
2. contributing by checking out the [issues](https://github.com/blatio/mkdocs-multiversion-plugin/issues)

### License
[BSD-3-Clause](https://github.com/blatio/mkdocs-multiversion-plugin/blob/master/LICENSE)

<!-- Badges -->
[pypi-image]: https://img.shields.io/pypi/v/mkdocs-multiversion-plugin.svg
[pypi-link]: https://pypi.org/project/mkdocs-multiversion-plugin/