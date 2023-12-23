import unittest
import HtmlTestRunner
from appium import webdriver
from edit_main import MainAction, EditMainAction
from edit_menu import Clip, Audio, Graphics, Text, Pip, Effect, Export
import json
# import base64
# from appium.webdriver.appium_service import AppiumService
# from appium import webdriver
# from selenium.webdriver.common.by import By
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.common import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
# import time, random
# import numpy as np
with open("info.json") as f:
    info = json.load(f)

"""
블로 자동화
"""
class VLLOTest(unittest.TestCase):

    def setUp(self):
            self.driver = webdriver.Remote(
                    command_executor= info.get('url'),
                    desired_capabilities={
                            "deviceName": info.get('DEVICE_NAME'),
                            "platformVersion": info.get('PLATFORM_VERSION'),
                            "platformName": info.get('PLATFORM_NAME'),
                            "automationName": info.get('AUTOMATION_NAME'),
                            "Team ID": info.get('TEAM_ID'),
                            "xcodeSigningId": info.get('iPhone Developer'),
                            "xcodeSigninId": info.get('iPhoneDeveloper'),
                            "cacheld": info.get('cacheld'),
                            "udid": info.get('UDID'),  # 아이폰 13
                            # "udid": "00008101-000160690AD0001E",
                            # "udid": "00008120-0009048E11BBC01E", # 아이폰 14 프로
                            # "udid": "00008027-001D50410C0A402E", # 아이패드 프로 2세대 11형
                            # "udid": "00008030-001A0D903E53C02E", # 아이패드 9세대
                            # "udid": "00008020-001235D93AD8003A", # 아이폰 XS
                            # "udid": "00008030-000928E626BA802E", #아이폰 11
                            # "udid": "00008101-000814362E40001E", #아이폰 12 mini
                            # "udid": "00008101-000814362E40001E", #아이폰 12 mini
                            "bundleld": info.get('bundleld'),
                            "app": info.get('APP'),
                            "XCODE_ORG_ID" : info.get('XCODE_ORG_ID'),
                            "wdaBaseUrl": info.get('WDA_BASE_URL'),
                            'autoGrantPermissions': True,
                            "shouldTerminateApp": False,
                            "autoAcceptAlerts": True,
                            "autoDismissAlerts": True,
                            "noReset": True,
                            "fullReset": False,
                            "skipServerInstallatio": True,
                    }
            )

    def test1_main(self):
        MainAction.start_main(self)
        EditMainAction.main_timeline_clip(self)

    def test2_clip(self):
        EditMainAction.after_entering_the_Clip(self)
        Clip.clip_all(self)

    def test3_audio(self):
        Audio.audio_all(self)

    def test4_graphic(self):
        Graphics.graphics_all(self)

    def test5_text(self):
        Text.text_test_all(self)

    def test6_pip(self):
        Pip.pip_all(self)

    def test7_effect(self):
        Effect.effect_all(self)

    def test8_export(self):
        Export.export_all(self)

    if __name__ == '__main__':
        reportFolder = "ReportTest"
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportFolder))