import click
import pandas as pd

from . import __version__


@click.group()
@click.version_option(version=__version__)
def parakeet() -> None:
    """Tool to easily convert between CSV and parquet files"""
    return None  # pragma: no cover


@parakeet.command()
@click.argument("file_in", type=click.Path(exists=True), nargs=1)
@click.argument("file_out", type=click.Path(), nargs=1)
def c2p(file_in, file_out):
    """Convert a CSV file to parquet format

    \b
    Arguments:
        FILE_IN: path to a csv file
        FILE_OUT: desired path for parquet output
    """
    pd.read_csv(file_in).to_parquet(path=file_out, index=False)


@parakeet.command()
@click.argument("file_in", type=click.Path(exists=True), nargs=1)
@click.argument("file_out", type=click.Path(), nargs=1)
def p2c(file_in, file_out):
    """Convert a parqet file to CSV format

    \b
    Arguments:
        FILE_IN: path to a parquet file
        FILE_OUT: desired path for csv output
    """
    pd.read_parquet(file_in).to_csv(path_or_buf=file_out, index=False)
