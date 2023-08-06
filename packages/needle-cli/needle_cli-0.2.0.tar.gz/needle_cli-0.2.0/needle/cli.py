"""
Utility functions for the CLI
"""
import click


click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")



if __name__ == '__main__':
    cli()

