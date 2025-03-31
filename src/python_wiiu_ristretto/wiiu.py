import requests

from .hardware import WiiUHardwareVersion


class WiiU:
    def __init__(self, ip_address: str, ristretto_port: int):
        self.ip_address = ip_address
        self.ristretto_port = ristretto_port
        self._base_url = f'http://{self.ip_address}:{self.ristretto_port}/'


    def get_device_hardware_version(self) -> WiiUHardwareVersion:
        return WiiUHardwareVersion(requests.get(self._base_url  + 'device/hardware_version').text)

    def get_device_model_number(self) -> str:
        return requests.get(self._base_url + 'device/model_number').text

    def get_device_serial_id(self) -> str:
        return requests.get(self._base_url + 'device/serial_id').text

    def get_device_version(self) -> str:
        return requests.get(self._base_url + 'device/version').text



    def get_gamepad_battery(self) -> int:
        return int(requests.get(self._base_url + 'gamepad/battery').text)



    def launch_menu(self):
        return requests.post(self._base_url + 'launch/menu').status_code

    def launch_mii_studio(self):
        return requests.post(self._base_url + 'launch/miistudio').status_code

    def launch_notifications_applet(self):
        return requests.post(self._base_url + 'launch/notifications').status_code

    def launch_parental_controls(self):
        return requests.post(self._base_url + 'launch/parental').status_code

    def launch_settings(self):
        return requests.post(self._base_url + 'launch/settings').status_code

    #  The Title ID must be in base 10
    def launch_title(self, title_id: int):
        return requests.post(self._base_url + 'launch/title', json={"title": str(title_id)}).status_code




    def launch_internet_settings(self):
        return requests.post(self._base_url + 'launch/settings/internet').status_code

    def launch_data_management_settings(self):
        return requests.post(self._base_url + 'launch/settings/data_management').status_code

    def launch_tv_remote_settings(self):
        return requests.post(self._base_url + 'launch/settings/tv_remote').status_code

    def launch_date_time_settings(self):
        return requests.post(self._base_url + 'launch/settings/date_time').status_code

    def launch_country_settings(self):
        return requests.post(self._base_url + 'launch/settings/country').status_code

    def launch_quick_start_settings(self):
        return requests.post(self._base_url + 'launch/settings/quick_start').status_code

    def launch_tv_connection_settings(self):
        return requests.post(self._base_url + 'launch/settings/tv_connection').status_code



    def get_odd_title_id(self) -> str:
        return requests.get(self._base_url + 'odd/titleid').text



    def get_powered_on(self) -> bool:
        return requests.get(self._base_url).status_code == 200

    def reboot(self):
        return requests.post(self._base_url + 'power/reboot').status_code

    def shutdown(self):
        return requests.post(self._base_url + 'power/shutdown').status_code



    # Not all titles have emanuals
    def switch_to_emanual(self) -> bool:
        return requests.post(self._base_url + 'switch/emanual').status_code == 200

    # USE WITH CAUTION
    def switch_to_hbm(self) -> bool:
        return requests.post(self._base_url + 'switch/hbm').status_code == 200



    def get_current_title_name(self) -> str:
        return requests.get(self._base_url + 'title/current').text

    def get_title_list(self):
        return requests.get(self._base_url + 'title/list').json()



    def launch_vwii_menu(self):
        return requests.post(self._base_url + 'vwii/launch/menu').status_code


    def launch_vwii_data_manager(self):
        return requests.post(self._base_url + 'vwii/launch/data_manager').status_code
