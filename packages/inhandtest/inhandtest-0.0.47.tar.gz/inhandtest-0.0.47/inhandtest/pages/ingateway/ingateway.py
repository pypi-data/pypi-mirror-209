# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 16:09:27
# @Author  : Pane Li
# @File    : ingateway.py
"""
ingateway

"""
from playwright.sync_api import Page
from inhandtest.base_page.base_page import BasePage
from inhandtest.pages.ingateway.network.network import Network
from inhandtest.pages.ingateway.overview.overview import Overview
from inhandtest.pages.locale import in_setting
from inhandtest.telnet import Telnet


class InGateway(BasePage):

    def __init__(self, host: str, super_user: str, super_password: str, page: Page = None, model='IG902',
                 language='en', protocol='https', port=443, username='adm', password='123456', telnet=True):
        super().__init__(host, username, password, protocol, port, model, language, page, locale=in_setting)
        if telnet:
            self.telnet = Telnet(model, host, super_user, super_password)
        else:
            self.telnet = None
        if self.language == 'en':
            self.telnet.send_cli(command='language English', type_='user')
        else:
            self.telnet.send_cli(command='language Chinese', type_='user')
        self.login()
        self.overview = Overview(host, username, password, protocol, port, model, language, self.page,
                                 locale=self.locale)
        self.network: Network = Network(host, username, password, protocol, port, model, language, self.page,
                                        locale=self.locale)


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO,
                        stream=sys.stdout)
    with InGateway('10.5.24.96', 'inhand', '64391099@inhand') as device:
        # device.network.ethernet.assert_ethernet_status(network_type='"${value}"=="static_ip"',
        #                                                ip_address='"${value}" == "10.5.24.96"',
        #                                                netmask='"${value}" == "255.255.255.0"',
        #                                                gateway='"${value}" == "10.5.24.254"',
        #                                                dns='"${value}" == "0.0.0.0"',
        #                                                mtu='"${value}" == "1500"',
        #                                                status='"${value}" == "up"',
        #                                                connection_time='"${value}".startswith("0 day 03")',
        #                                                description='"${value}" == "1111111"', )
        device.network.ethernet.config_ethernet(port='gigabitethernet 0/2', network_type='static_ip',
                                                ip_address='192.168.3.1',
                                                netmask='255.255.255.0',
                                                mtu=1400,
                                                speed_duplex='1000m full duplex',
                                                track_l2_state='enable',
                                                shutdown='enable',
                                                secondary_ip_settings=[('add', {"secondary_ip": "192.168.6.1", 'netmask': '255.255.255.0'})],
                                                submit=True, success_tip=True)
        device.page.wait_for_timeout(30000)
        # device.overview.assert_overview_status(wan_image='"${value}" =="enable"',
        #                                        wan_ip='"${value}" =="10.5.24.96"',
        #                                        wan_gateway='"${value}" =="10.5.24.254"', wan_dns='"${value}" =="0.0.0.0"',
        #                                        ge_01_image='"enable" == "${value}"', ge_01_ip='"${value}" =="10.5.24.96"',)
        # device.overview.assert_overview_status(cellular_dns='"${value}" =="0.0.0.0"',
        #                                        cellular_netmask='"${value}" =="0.0.0.0"',
        #                                        cellular_ip='"${value}" =="0.0.0.0"',
        #                                        cellular_connection_time='"${value}" =="0 day 00:00:00"',
        #                                        cellular_register_status='"${value}" =="registering"',
        #                                        cellular_status='"${value}" =="disconnect"',
        #                                        cellular_image='"enable" != "${value}"',
        #                                        wireless_ip='"${value}" =="0.0.0.0"',
        #                                        wireless_ssid='"${value}" =="123123123"',
        #                                        wireless_state='"${value}" =="disconnect"',
        #                                        wireless_role='"${value}" =="client"',
        #                                        wireless_image='"enable" == "${value}"',
        #                                        ge_02_image='"enable" != "${value}"',
        #                                        ge_02_ip='"${value}" =="0.0.0.0"',
        #                                        ge_02_netmask='"${value}" =="0.0.0.0"',
        #                                        )
