"""
Setup script for `fire-plugin`
"""


from setuptools import setup


setup(
    name='fire_plugin',
    version='0.1dev0',
    packages=['fire_plugin'],
    entry_points='''
        [fire.cli.fire_commands]
        plugin=fire_plugin.plugin:plugin
    '''
)