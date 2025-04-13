"""WiiU Ristretto API Wrapper"""

import requests
import aiohttp

from .hardware import WiiUHardwareVersion


class WiiU:
    """
    A class to interact with the WiiU Ristretto API.

    This class provides methods to send HTTP requests to the WiiU Ristretto server
    and perform various operations such as retrieving device information, launching
    applications, and managing power settings.

    Attributes:
        ip_address (str): The IP address of the WiiU device.
        ristretto_port (int): The port number for the Ristretto API.
        timeout (int): The timeout for HTTP requests in seconds.
        session (aiohttp.ClientSession): The aiohttp session for asynchronous requests.
    """

    def __init__(
            self,
            ip_address: str,
            ristretto_port: int,
            timeout: int = 5,
            session: aiohttp.ClientSession = None):
        """
        Initialize the WiiU class.

        Args:
            ip_address (str): The IP address of the WiiU device.
            ristretto_port (int): The port number for the Ristretto API.
            timeout (int, optional): The timeout for HTTP requests in seconds. Defaults to 5.
            session (aiohttp.ClientSession, optional): An existing aiohttp session. Defaults to None.
        """
        self.ip_address = ip_address
        self.ristretto_port = ristretto_port
        self._base_url = f'http://{self.ip_address}:{self.ristretto_port}/'
        self.timeout = timeout
        self.session = aiohttp.ClientSession() if session is None else session

    async def async_send_http_request(self, method: str, endpoint: str, **kwargs):
        """
        Send an asynchronous HTTP request to the WiiU Ristretto server.

        Args:
            method (str): The HTTP method (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint to send the request to.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            tuple: A tuple containing the response text and the status code.
        """
        url = f'{self._base_url}{endpoint}'
        async with self.session.request(method, url, timeout=self.timeout, **kwargs) as response:
            response_text = await response.text()
            return response_text, response.status

    def send_http_request(self, method: str, endpoint: str, **kwargs):
        """
        Send a synchronous HTTP request to the WiiU Ristretto server.

        Args:
            method (str): The HTTP method (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint to send the request to.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            tuple: A tuple containing the response text and the status code.
        """
        url = f'{self._base_url}{endpoint}'
        response = requests.request(method, url, timeout=self.timeout, **kwargs)
        return response.text, response.status_code

    def get_device_hardware_version(self) -> WiiUHardwareVersion:
        """Retrieve the hardware version of the WiiU device."""
        response_text, _ = self.send_http_request('GET', 'device/hardware_version')
        return WiiUHardwareVersion(int(response_text))

    async def async_get_device_hardware_version(self) -> WiiUHardwareVersion:
        """Retrieve the hardware version of the WiiU device."""
        response_text, _ = await self.async_send_http_request('GET', 'device/hardware_version')
        return WiiUHardwareVersion(int(response_text))

    def get_device_model_number(self) -> str:
        """Retrieve the model number of the WiiU device."""
        response_text, _ = self.send_http_request('GET', 'device/model_number')
        return response_text

    async def async_get_device_model_number(self) -> str:
        """Retrieve the model number of the WiiU device asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', 'device/model_number')
        return response_text

    def get_device_serial_id(self) -> str:
        """Retrieve the serial ID of the WiiU device."""
        response_text, _ = self.send_http_request('GET', 'device/serial_id')
        return response_text

    async def async_get_device_serial_id(self) -> str:
        """Retrieve the serial ID of the WiiU device asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', 'device/serial_id')
        return response_text

    def get_device_version(self) -> str:
        """Retrieve the version of the WiiU device."""
        response_text, _ = self.send_http_request('GET', 'device/version')
        return response_text

    async def async_get_device_version(self) -> str:
        """Retrieve the version of the WiiU device asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', 'device/version')
        return response_text

    def get_gamepad_battery(self) -> int:
        """
        Retrieve the gamepad battery level.

        Returns:
            int: The battery level as a percentage.
        """
        response_text, _ = self.send_http_request('GET', 'gamepad/battery')
        return int(response_text)

    async def async_get_gamepad_battery(self) -> int:
        """Retrieve the gamepad battery level asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', 'gamepad/battery')
        return int(response_text)

    def launch_menu(self):
        """
        Launch the WiiU menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/menu')
        return status_code

    async def async_launch_menu(self) -> int:
        """Launch the WiiU menu asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'launch/menu')
        return status_code

    def launch_mii_studio(self):
        """
        Launch the Mii Studio.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/miistudio')
        return status_code

    async def async_launch_mii_studio(self) -> int:
        """Launch the Mii Studio asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'launch/miistudio')
        return status_code

    def launch_notifications_applet(self):
        """
        Launch the notifications applet.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/notifications')
        return status_code

    async def async_launch_notifications_applet(self) -> int:
        """Launch the notifications applet asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'launch/notifications')
        return status_code

    def launch_parental_controls(self):
        """
        Launch the parental controls.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/parental')
        return status_code

    async def async_launch_parental_controls(self) -> int:
        """Launch the parental controls asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'launch/parental')
        return status_code

    def launch_settings(self):
        """
        Launch the settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings')
        return status_code

    async def async_launch_settings(self) -> int:
        """Launch the settings asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'launch/settings')
        return status_code

    #  The Title ID must be in base 10
    def launch_title(self, title_id: int):
        """
        Launch a title by its ID.

        Args:
            title_id (int): The title ID in base 10.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/title', json={"title": str(title_id)})
        return status_code

    async def async_launch_title(self, title_id: int) -> int:
        """Launch a title by its ID asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'launch/title', json={"title": str(title_id)})
        return status_code

    def launch_internet_settings(self):
        """
        Launch the internet settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings/internet')
        return status_code

    def launch_data_management_settings(self):
        """
        Launch the data management settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings/data_management')
        return status_code

    def launch_tv_remote_settings(self):
        """
        Launch the TV remote settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings/tv_remote')
        return status_code

    def launch_date_time_settings(self):
        """
        Launch the date and time settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings/date_time')
        return status_code

    def launch_country_settings(self):
        """
        Launch the country settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings/country')
        return status_code

    def launch_quick_start_settings(self):
        """
        Launch the quick start settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings/quick_start')
        return status_code

    def launch_tv_connection_settings(self):
        """
        Launch the TV connection settings menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'launch/settings/tv_connection')
        return status_code

    def get_odd_title_id(self) -> str:
        """Get the title ID of the currently inserted disc."""
        response_text, _ = self.send_http_request('GET', 'odd/titleid')
        return response_text

    async def async_get_odd_title_id(self) -> str:
        """Get the title ID of the currently inserted disc asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', 'odd/titleid')
        return response_text

    def get_powered_on(self) -> bool:
        response_text, _ = self.send_http_request('GET', '')
        return response_text == 'Ristretto'

    async def async_get_powered_on(self) -> bool:
        """Check if the WiiU device is powered on asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', '')
        return response_text == 'Ristretto'

    def reboot(self):
        """Reboot the WiiU device."""
        return self.send_http_request('POST', 'power/reboot')

    async def async_reboot(self):
        """Reboot the WiiU device asynchronously."""
        return await self.async_send_http_request('POST', 'power/reboot')

    def shutdown(self):
        """Shutdown the WiiU device."""
        return self.send_http_request('POST', 'power/shutdown')

    async def async_shutdown(self):
        """Shutdown the WiiU device asynchronously."""
        return await self.async_send_http_request('POST', 'power/shutdown')

    # Not all titles have emanuals
    def switch_to_emanual(self) -> bool:
        """
        Switch to the electronic manual.

        Returns:
            bool: True if the request was successful, False otherwise.
        """
        _, status_code = self.send_http_request('POST', 'switch/emanual')
        return status_code == 200

    # USE WITH CAUTION
    def switch_to_hbm(self) -> bool:
        """
        Switch to Homebrew Menu (HBM).

        USE WITH CAUTION.

        Returns:
            bool: True if the request was successful, False otherwise.
        """
        _, status_code = self.send_http_request('POST', 'switch/hbm')
        return status_code == 200

    def get_current_title_name(self) -> str:
        """Get the name of the currently running title."""
        response_text, _ = self.send_http_request('GET', 'title/current')
        return response_text

    async def async_get_current_title_name(self) -> str:
        """Get the name of the currently running title asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', 'title/current')
        return response_text

    def get_title_list(self):
        """Get the list of titles on the WiiU device."""
        response_text, _ = self.send_http_request('GET', 'title/list')
        return response_text

    async def async_get_title_list(self):
        """Get the list of titles on the WiiU device asynchronously."""
        response_text, _ = await self.async_send_http_request('GET', 'title/list')
        return response_text

    def launch_vwii_menu(self):
        """
        Launch the vWii menu.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'vwii/launch/menu')
        return status_code

    async def async_launch_vwii_menu(self) -> int:
        """Launch the vWii menu asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'vwii/launch/menu')
        return status_code

    def launch_vwii_data_manager(self):
        """
        Launch the vWii data manager.

        Returns:
            int: The HTTP status code of the request.
        """
        _, status_code = self.send_http_request('POST', 'vwii/launch/data_manager')
        return status_code

    async def async_launch_vwii_data_manager(self) -> int:
        """Launch the vWii data manager asynchronously."""
        _, status_code = await self.async_send_http_request('POST', 'vwii/launch/data_manager')
        return status_code
