"""This module provides the Jautomate CLI."""

from pathlib import Path
from typing import Optional
import typer
from jautomate import actions, utils, __app_name__, __version__
from jautomate.assets import Asset, Assets, AssetType
from jautomate.logger import j_logger


app = typer.Typer(add_completion=False)


def _version(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def callback(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        help="Show the app version and exit",
        callback=_version,
        is_eager=True
    )
) -> None:
    """Tools to automate MDM tasks using the Jamf API."""
    # Used for cli description only


@app.command()
def sync(
    device_type: AssetType = typer.Argument(
        ...,
        case_sensitive=False,
        help='Type of device being updated'),
    file_path: Path = typer.Argument(
        ...,
        exists=True,
        help='The path to the csv file to be imported and synced with Jamf')
) -> None:
    """
    Syncs a csv file of asset information with Jamf Pro

    Args:
        device_type (str, required): Type of device being updated. 
            mobile or computer
        file_path (Path, required): The path to the csv file to be imported 
            and synced with Jamf
    """
    if device_type.value == 'computer':
        print('Computer functionality coming soon...')
        return

    j_logger.debug('%s sync is running...', device_type.value)

    imported_assets = utils.get_assets_from_csv(file_path)
    asset_list = Assets(imported_assets, actions.get_all_mobile_devices())
    asset_list = actions.get_mobile_device_jamf_ids_by_serial_number(
        asset_list)
    actions.sync_assets_to_jamf(asset_list.local)


@app.command()
def assign(
    device_type: AssetType = typer.Argument(
        ...,
        case_sensitive=False,
        help='Type of device being updated'),
    asset_tag: str = typer.Argument(
        ..., help='Asset tag should be a 6 digit number'),
    serial_number: str = typer.Argument(..., help='Serial Number of device'),
    student_name: str = typer.Argument(..., help=' Student full name'),
    homeroom: str = typer.Argument(..., help='Homeroom teachers last name'),
    student_grade: int = typer.Argument(..., help='Student grade as a number'),
    building: str = typer.Argument(
        ...,
        help='Three letter building abbreviation. ex: COA')




) -> None:
    """
    Assigns data to a single asset record in Jamf Pro.

    Args:
        device_type (str, required): Type of device being updated. mobile or computer
        asset_tag (str, required): Asset tag should be a 6 digit number
        serial_number (str, required): Serial Number of device
        student_name (str, required):  Student full name
        homeroom (str, required): Homeroom teachers last name
        student_grade (int, required): Student grade as a number
        building (_type_, required): Three letter building abbreviation. ex: COA
    """
    if device_type.value == 'computer':
        print('Computer functionality coming soon...')
        return

    j_logger.debug('%s asset assign is running...', device_type)
    asset = Asset(
        asset_tag=asset_tag,
        building=building,
        homeroom=homeroom,
        serial_number=serial_number,
        student_grade=student_grade,
        student_name=student_name
    )
    asset_list = Assets([asset], actions.get_all_mobile_devices())
    asset_list = actions.get_mobile_device_jamf_ids_by_serial_number(
        asset_list)

    j_logger.debug(asset_list.local)

    actions.sync_assets_to_jamf(asset_list.local)


@app.command()
def unassign(
    device_type: AssetType = typer.Argument(
        ...,
        case_sensitive=False,
        help='Type of device being updated'),
    asset_tag: str = typer.Argument(
        ..., help='Asset tag should be a 6 digit number'),
) -> None:
    """
    Unassigns data from a single asset record in Jamf Pro

    Args:
        device_type (str, required): Type of device being updated. mobile or computer
        asset_tag (str, required): Asset tag, should be a 6 digit number
    """
    if device_type.value == 'computer':
        print('Computer functionality coming soon...')
        return

    j_logger.debug('%s device unassign is running...', device_type)
    asset = Asset(
        asset_tag=asset_tag,
        building='',
        homeroom='',
        student_grade='',
        student_name=''
    )
    asset_list = Assets([asset], actions.get_all_mobile_devices())
    asset_list = actions.get_mobile_device_jamf_ids_by_asset_tag(
        asset_list)

    j_logger.debug(asset_list.local)

    actions.unassign_devices_in_jamf(asset_list.local)
