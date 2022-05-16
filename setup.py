import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkdocs-multiversion-plugin",
    version="0.2.0",
    author="blatio",
    author_email="blatio@gmail.com",
    license='BSD',
    description="A plugin that allows you to have several versions of the documentation built with mkdocs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blatio/mkdocs-multiversion-plugin",
    project_urls={
        "Bug Tracker": "https://github.com/blatio/mkdocs-multiversion-plugin/issues",
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'mkdocs.plugins': [
            'multiversion = mkdocs_multiversion_plugin.entry:Multiversion'
        ],
        'mkdocs_multiversion_plugin.themes': [
            'mkdocs = mkdocs_multiversion_plugin.themes.mkdocs',
            'readthedocs = mkdocs_multiversion_plugin.themes.readthedocs',

            # Bootswatch themes
            'bootstrap = mkdocs_multiversion_plugin.themes.mkdocs',
            'cerulean = mkdocs_multiversion_plugin.themes.mkdocs',
            'cosmo = mkdocs_multiversion_plugin.themes.mkdocs',
            'cyborg = mkdocs_multiversion_plugin.themes.mkdocs',
            'darkly = mkdocs_multiversion_plugin.themes.mkdocs',
            'flatly = mkdocs_multiversion_plugin.themes.mkdocs',
            'journal = mkdocs_multiversion_plugin.themes.mkdocs',
            'litera = mkdocs_multiversion_plugin.themes.mkdocs',
            'lumen = mkdocs_multiversion_plugin.themes.mkdocs',
            'lux = mkdocs_multiversion_plugin.themes.mkdocs',
            'materia = mkdocs_multiversion_plugin.themes.mkdocs',
            'minty = mkdocs_multiversion_plugin.themes.mkdocs',
            'pulse = mkdocs_multiversion_plugin.themes.mkdocs',
            'sandstone = mkdocs_multiversion_plugin.themes.mkdocs',
            'simplex = mkdocs_multiversion_plugin.themes.mkdocs',
            'slate = mkdocs_multiversion_plugin.themes.mkdocs',
            'solar = mkdocs_multiversion_plugin.themes.mkdocs',
            'spacelab = mkdocs_multiversion_plugin.themes.mkdocs',
            'superhero = mkdocs_multiversion_plugin.themes.mkdocs',
            'united = mkdocs_multiversion_plugin.themes.mkdocs',
            'yeti = mkdocs_multiversion_plugin.themes.mkdocs',

            # Bootswatch classic themes
            'amelia = mkdocs_multiversion_plugin.themes.mkdocs',
            'readable = mkdocs_multiversion_plugin.themes.mkdocs',
            'mkdocs-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'amelia-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'bootstrap-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'cerulean-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'cosmo-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'cyborg-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'flatly-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'journal-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'readable-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'simplex-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'slate-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'spacelab-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'united-classic = mkdocs_multiversion_plugin.themes.mkdocs',
            'yeti-classic = mkdocs_multiversion_plugin.themes.mkdocs',
        ],
    },
    python_requires='>=3.7',
    install_requires=[
        'mkdocs >= 1.3',
        'natsort',
    ],
)
