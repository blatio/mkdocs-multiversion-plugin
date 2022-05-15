import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkdcos-multiversion-plugin",
    version="0.1.0",
    author="blatio",
    author_email="blatio@gmail.com",
    license='BSD',
    description="A plugin that allows you to have several versions of the documentation built with mkdocs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blatio/mkdocs-multiversion-plugin",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9'
    ],
    entry_points={
        'mkdocs.plugins': [
            'multiversion = mkdcos_multiversion_plugin.entry:Multiversion'
        ],
        'mkdcos_multiversion_plugin.themes': [
            'mkdocs = mkdcos_multiversion_plugin.themes.mkdocs',
            'readthedocs = mkdcos_multiversion_plugin.themes.readthedocs',

            # Bootswatch themes
            'bootstrap = mkdcos_multiversion_plugin.themes.mkdocs',
            'cerulean = mkdcos_multiversion_plugin.themes.mkdocs',
            'cosmo = mkdcos_multiversion_plugin.themes.mkdocs',
            'cyborg = mkdcos_multiversion_plugin.themes.mkdocs',
            'darkly = mkdcos_multiversion_plugin.themes.mkdocs',
            'flatly = mkdcos_multiversion_plugin.themes.mkdocs',
            'journal = mkdcos_multiversion_plugin.themes.mkdocs',
            'litera = mkdcos_multiversion_plugin.themes.mkdocs',
            'lumen = mkdcos_multiversion_plugin.themes.mkdocs',
            'lux = mkdcos_multiversion_plugin.themes.mkdocs',
            'materia = mkdcos_multiversion_plugin.themes.mkdocs',
            'minty = mkdcos_multiversion_plugin.themes.mkdocs',
            'pulse = mkdcos_multiversion_plugin.themes.mkdocs',
            'sandstone = mkdcos_multiversion_plugin.themes.mkdocs',
            'simplex = mkdcos_multiversion_plugin.themes.mkdocs',
            'slate = mkdcos_multiversion_plugin.themes.mkdocs',
            'solar = mkdcos_multiversion_plugin.themes.mkdocs',
            'spacelab = mkdcos_multiversion_plugin.themes.mkdocs',
            'superhero = mkdcos_multiversion_plugin.themes.mkdocs',
            'united = mkdcos_multiversion_plugin.themes.mkdocs',
            'yeti = mkdcos_multiversion_plugin.themes.mkdocs',

            # Bootswatch classic themes
            'amelia = mkdcos_multiversion_plugin.themes.mkdocs',
            'readable = mkdcos_multiversion_plugin.themes.mkdocs',
            'mkdocs-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'amelia-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'bootstrap-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'cerulean-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'cosmo-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'cyborg-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'flatly-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'journal-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'readable-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'simplex-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'slate-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'spacelab-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'united-classic = mkdcos_multiversion_plugin.themes.mkdocs',
            'yeti-classic = mkdcos_multiversion_plugin.themes.mkdocs',
        ],
    },
    python_requires='>=3.9',
    project_urls={
        'Documentation': ''
    },
    install_requires=[
        'mkdocs >= 1.3',
        'natsort',
    ],
)
