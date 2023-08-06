"""Karrio TNT settings."""

import attr
from karrio.providers.tnt.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """TNT connection settings."""

    # Carrier specific properties
    username: str
    password: str
    account_number: str = None
    account_country_code: str = None
    metadata: dict = {}
    config: dict = {}

    # Base properties
    id: str = None
    test_mode: bool = False
    carrier_id: str = "tnt"
