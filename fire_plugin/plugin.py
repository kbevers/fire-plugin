"""
Tilføj plugin til fire applikationen
"""


import fire.cli
import click


@click.group()
def plugin():

    """
    Dummy entry point
    """
    pass

@plugin.command()
def demo():
    fire.cli.print("Dette er bare en demonstration", fg="green")

@plugin.command()
def test():
    fire.cli.print("Dette er bare en test", fg="red")