
import click
from gui_util import gui


@click.group()
def cli():
    pass


@cli.command()
def current_window():
    window = gui.get_current_window()
    print(window)
    return True


@cli.command()
def focus_on_window():
    print('[START]')
    gui.focus_on_window('chrome')
    print('[END]')
    return True


if __name__ == "__main__":
    cli()