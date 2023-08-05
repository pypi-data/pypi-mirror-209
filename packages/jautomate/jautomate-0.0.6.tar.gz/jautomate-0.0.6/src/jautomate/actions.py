"""Module to handle various actions performed with Jamf"""

from typing import Dict, List
from jautomate.api import jamf_p, jamf_c
from jautomate.assets import Asset, Assets
from jautomate.logger import j_logger
from jautomate import utils


def get_all_mobile_devices_modified() -> List[Dict]:
    """
    Returns dict of all mobile devices from Jamf using Pro API

    Returns:
        List[Dict]: List of all mobile devices from Jamf Pro API
    """
    # Pro API max page size is 2000
    page_size = 2000
    page = 0
    remaining_results = 10000
    device_list = []
    while remaining_results > 0:
        response = jamf_p.get_mobile_devices(
            page=page, page_size=page_size)

        if remaining_results == 10000:
            remaining_results = int(response['totalCount']) - page_size
        else:
            remaining_results -= page_size

        device_list.extend(response['results'])
        page += 1
    return device_list


def get_all_mobile_devices() -> List[Dict]:
    """
    Returns all mobile devices from Jamf Classic API

    This function looks for a saved search on Jamf that is
    set up return only Jamf ID, Serial Number, and Asset Tag.
    The name used was 'All iPads by Asset Tag'.

    This is done because Jamf does not include asset tag in their
    default information that gets returned. A custom search number be
    saved first from the Jamf Pro GUI.

    Also, note the structure of the response that is returned as there
    is a lot of other unneeded info returned with the saved search.

    Returns:
        List[Dict]: List of Dicts for all mobile devices on Jamf.
    """
    response = jamf_c.get_advanced_mobile_device_search(
        name='All iPads by Asset Tag',
        data_type='json')
    return response['advanced_mobile_device_search']['mobile_devices']


def get_mobile_device_jamf_ids_by_serial_number(asset_list: Assets) -> Assets:
    """
    Gets the Jamf IDs of the local assets by checking the serial number against those in Jamf.

    Compares the serial numbers of local assets to those retrieved from Jamf servers
    and sets the jamf_id proptery of each asset object. This is done because most of the
    Jamf API endpoints work off of the id jamf gives each asset.

    This is used when assigning assets as the serial numbers are typically more
    accurate of a comparison when assigning

    Args:
        asset_list (Assets): Obj of assets being worked with. See Assets class for structure.

    Returns:
        Assets: Asset object with lists of both local and remote assets
    """
    serial_format = utils.determine_serial_number_key_format(
        asset_list.remote[0])

    for asset in asset_list.local:
        matching_device = next(
            (device for device in asset_list.remote
                if device[serial_format] == asset.serial_number), None)
        if matching_device:
            asset.jamf_id = matching_device['id']
    return asset_list


def get_mobile_device_jamf_ids_by_asset_tag(asset_list: Assets) -> Assets:
    """
    Gets the Jamf IDs of the local assets by checking the asset tag against those in Jamf.

    Compares the asset tags of local assets to those retrieved from Jamf servers
    and sets the jamf_id proptery of each asset object.

    This is used mostly for unassigning assets where it is more likely the
    asset tag has been set and is accurate.

    Args:
        asset_list (Assets): Obj of assets being worked with. See Assets class for structure.

    Returns:
        Assets: Asset object with lists of both local and remote assets
    """
    for asset in asset_list.local:
        matching_device = next(
            (device for device in asset_list.remote
                if device['Asset_Tag'] == asset.asset_tag), None)
        if matching_device:
            asset.jamf_id = matching_device['id']
            # This isn't ideal, but we need to sync the serial
            # number so it stays in jamf
            if asset.serial_number is None:
                asset.serial_number = matching_device['Serial_Number']
    return asset_list


def get_building_id(building_name: str) -> str:
    """
    Gets building Id used by Jamf from string abbreviation 

    Args:
        building_name (str): String abbreviation of building

    Returns:
        String: String representation of building ID number
    """
    response = jamf_p.get_buildings()
    jamf_buildings = []
    jamf_buildings.extend(response['results'])
    return [building['id'] for building in jamf_buildings
            if building['name'] == building_name][0]


def sync_assets_to_jamf(asset_list: List[Asset]) -> None:
    """
    Syncs data from local assets to Jamf Pro server.

    Structure of payload can be found on Jamf's API doc:
    https://developer.jamf.com/jamf-pro/reference/patch_v2-mobile-devices-id

    Args:
        asset_list (Assets): Obj of assets being worked with. See Assets class for structure.
    """
    j_logger.debug('Syncing assets to Jamf')
    for asset in asset_list:
        payload = {
            "location": {
                "realName": asset.student_name,
                "room": asset.homeroom,
                "buildingId": get_building_id(asset.building)
            },
            "updatedExtensionAttributes": [
                {
                    "value": [asset.student_grade],
                    "name": "Grade"
                },
                {
                    "value": ["prek-2"],
                    "name": "Owner"
                }
            ],
            # This is set because it allows techs to see asset tag from settings on device
            "name": asset.asset_tag,
            "enforceName": True
        }
        jamf_p.update_mobile_device(payload, asset.jamf_id)
        j_logger.debug("Asset: %s Ok", asset.asset_tag)


def unassign_devices_in_jamf(asset_list: List[Asset]) -> None:
    """
    Removes user and location info from asset in Jamf Pro

    Most values passed as empty strings to clear them in Jamf Pro.
    Structure of payload can be found on Jamf's API doc:
    https://developer.jamf.com/jamf-pro/reference/patch_v2-mobile-devices-id

    Args:
        asset_list (Assets): Obj of assets being worked with. See Assets class for structure.
    """
    j_logger.debug('Unassigning assets in Jamf')
    for asset in asset_list:
        payload = {
            "location": {
                "realName": asset.student_name,
                "room": asset.homeroom,
                "buildingId": 0
            },
            "updatedExtensionAttributes": [
                {
                    "value": [asset.student_grade],
                    "name": "Grade"
                },
                {
                    "value": [""],
                    "name": "Owner"
                }
            ],
            # This is set because it allows techs to see asset tag from settings on device
            "name": asset.asset_tag,
            "enforceName": True
        }
        j_logger.debug(asset)
        jamf_p.update_mobile_device(payload, asset.jamf_id)
        j_logger.debug("Asset: %s Unassigned", asset.asset_tag)
