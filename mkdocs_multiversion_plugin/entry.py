# -*- coding: utf-8 -*-
import os
import json
import tempfile
import logging

from pkg_resources import iter_entry_points
from natsort import natsorted
from mkdocs.exceptions import PluginError
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.config import Config
from mkdocs.structure.files import File, Files
from mkdocs_multiversion_plugin.git import Git

logger = logging.getLogger('mkdocs.plugins.mkdocs_multiversion_plugin')


def get_theme_dir(theme_name: str) -> str:
    """
    Gets plugin theme directory path.

    Arguments:
        theme_name (str): The theme name.

    Returns:
        str: Path to the theme.
    """
    themes = list(iter_entry_points('mkdocs_multiversion_plugin.themes', theme_name))
    if len(themes) == 0:
        raise ValueError("theme '{}' unsupported".format(theme_name))
    return os.path.dirname(themes[0].load().__file__)


class Multiversion(BasePlugin):

    CONFIG_VERSION_IN_SITE_NAME = 'version_in_site_name'
    CONFIG_BRANCH_WHITELIST = 'branch_whitelist'
    CONFIG_TAG_WHITELIST = 'tag_whitelist'
    CONFIG_LATEST_VERSION_NAME_FORMAT = 'latest_version_name_format'
    CONFIG_VERSION_NAME_FORMAT = 'version_name_format'
    CONFIG_CSS_DIR = 'css_dir'
    CONFIG_JS_DIR = 'javascript_dir'
    CURRENT_VERSION_FILENAME = 'multiversion-current.js'
    CURRENT_VERSION_JSON_FILENAME = 'multiversion.json'

    config_scheme = (
        # Add version number to site name
        (CONFIG_VERSION_IN_SITE_NAME, config_options.Type(bool, default=True)),
        # Whitelist pattern for branches (set to None to ignore all branches)
        (CONFIG_BRANCH_WHITELIST, config_options.Type(str, default=r'^.*$')),
        # Whitelist pattern for tags (set to None to ignore all tags)
        (CONFIG_TAG_WHITELIST, config_options.Type(str, default=r'^.*$')),
        # Latest version name format
        (CONFIG_LATEST_VERSION_NAME_FORMAT, config_options.Type(str, default='latest release ({version})')),
        # Version name format
        (CONFIG_VERSION_NAME_FORMAT, config_options.Type(str, default='{version}')),
        (CONFIG_CSS_DIR, config_options.Type(str, default='css')),
        (CONFIG_JS_DIR, config_options.Type(str, default='js')),
    )

    def __init__(self):
        self.version = None
        self.site_dir = ''
        self.build = False

    def on_config(self, glob_config: Config, **kwargs) -> Config:
        """
        Adds files into the collection.

        Arguments:
            glob_config (Config): Global configuration object.

        Returns:
            Config: Returns global configuration object.
        """
        self.version = Multiversion.get_version()

        if self.CONFIG_VERSION_IN_SITE_NAME not in self.config or self.config[self.CONFIG_VERSION_IN_SITE_NAME]:
            glob_config['site_name'] = glob_config['site_name'] + ' - ' + self.version
        if not Multiversion.is_serving(glob_config['site_dir']):
            self.site_dir = glob_config['site_dir']
            self.build = True
            new_site_dir = os.path.join(glob_config['site_dir'], self.version)
            glob_config['site_dir'] = new_site_dir
        else:
            self.build = False
            self.site_dir = glob_config['site_dir']

        return glob_config

    def on_files(self, files: Files, config: Config):
        """
        Adds files into the collection.

        Arguments:
            files (Files): Global files collection.
            config (Config) Global configuration object.

        Returns:
            Files: Returns global files collection.
        """
        try:
            theme_dir = get_theme_dir(config['theme'].name)
        except ValueError:
            return files

        for path, prop in [('css', 'css'), ('js', 'javascript')]:
            cfg_value = self.config[prop + '_dir']
            src_dir = os.path.join(theme_dir, path)
            dst_dir = os.path.join(config['site_dir'], cfg_value)

            extra_kind = 'extra_' + prop
            norm_extras = [os.path.normpath(i) for i in config[extra_kind]]
            for f in os.listdir(src_dir):
                relative_dest = os.path.join(cfg_value, f)
                if relative_dest in norm_extras:
                    raise PluginError('{!r} is already included in {!r}'
                                      .format(relative_dest, extra_kind))

                files.append(File(f, src_dir, dst_dir, False))
                config[extra_kind].append(relative_dest)

        src_dir = tempfile.gettempdir()
        dst_dir = os.path.join(config['site_dir'], self.config[self.CONFIG_JS_DIR])
        relative_dst = os.path.join(self.config[self.CONFIG_JS_DIR], self.CURRENT_VERSION_FILENAME)
        f = open(os.path.join(src_dir, self.CURRENT_VERSION_FILENAME), "w")
        f.write("var multiversion = { 'current_version': '%s'};" % self.version)
        f.close()
        files.append(File(self.CURRENT_VERSION_FILENAME, src_dir, dst_dir, False))
        config[extra_kind].append(relative_dst)
        return files

    def on_post_build(self, config: Config, **kwargs):
        """
        Generates `self.CURRENT_VERSION_JSON_FILENAME` file containing versions in format:
            var versions = {
                'stable': {
                    'name':'stable',
                    'latest':false
                },
                '0.2.0': {
                    'latest':true
                    'name':'latest release (0.2.0)'
                },
                '0.1.0':{
                    'latest':false
                    'name':'0.1.0'
                }
            };

        Arguments:
            config (Config): global configuration object.
        """

        Multiversion.delete_file(os.path.join(tempfile.gettempdir(), self.CURRENT_VERSION_FILENAME))
        # get versions from git
        try:
            gitrefs = Git.get_refs(self.config[self.CONFIG_TAG_WHITELIST], self.config[self.CONFIG_BRANCH_WHITELIST])
            refs = natsorted(gitrefs, key=lambda x: x.name.removeprefix('v').replace('.', '~') + 'z', reverse=True)

            def make_obj(text, latest):
                return {'name': text, 'latest': latest}

            versions = {}
            latest_found = False
            for ver in refs:
                if not latest_found and ver.source == 'tags':
                    latest_found = True
                    versions[ver.name] = make_obj(
                        self.config[self.CONFIG_LATEST_VERSION_NAME_FORMAT].format(version=ver.name),
                        True
                    )
                else:
                    versions[ver.name] = make_obj(
                        self.config[self.CONFIG_VERSION_NAME_FORMAT].format(version=ver.name),
                        False
                    )

            y = json.dumps(versions)
            f = open(os.path.join(self.site_dir, self.CURRENT_VERSION_JSON_FILENAME), "w")
            f.write(y)
            f.close()
        except Exception as ex:
            raise PluginError('[multiversion] %s' % ex)

    @staticmethod
    def get_version() -> str:
        """
        Extracts the version from repo.

        Returns:
            str: Returns the branch or tag name from repo as a string.
        """
        try:
            logger.debug("Get version from git.")
            version = Git.get_name()
            return version
        except Exception as e:
            logger.error(e)
            raise PluginError('[multiversion] Unable to get version number from repo. Maybe it\'s not a git '
                              'repository. %s' % e)

    @staticmethod
    def is_serving(site_path: str) -> bool:
        """
        Detects if mkdocs is serving or building by looking at the site_dir in config. if site_dir is a temp
        directory, it assumes mkdocs is serving.

        Arguments:
            site_path (str): The site_dir path.

        Returns:
            bool: Returns True if serving, False otherwise.
        """

        if tempfile.gettempdir() in site_path:
            return True
        else:
            return False

    @staticmethod
    def delete_file(path: str) -> bool:
        """
        Deletes the file.

        Arguments:
            path (str): Path to the file.

        Returns:
            bool: Returns status of operation, True if success , False otherwise.
        """
        try:
            if os.path.exists(path):
                os.remove(path)
                return True
        except Exception as e:
            logger.error(e)
        return False

