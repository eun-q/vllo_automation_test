from appium.webdriver.common.mobileby import MobileBy
from accessibility_Id import Idcomp
from selenium.common import NoSuchElementException
from test_class import Tester
from appium.webdriver.common.touch_action import TouchAction

class MainAction:
    def __init__(self, driver):
        self.driver = driver

    def start_main(self):
        MainAction.start_testing(self)
        MainAction.main_act(self)
        projectCreate.project_create_all(self)
        EditMainAction.before_entering_the_Clip(self)

    # 테스트 시작 시 가장 먼저 필요함
    def start_testing(self):
        MainAction.create_pre_project(self)
        MainAction.project_color(self)
        MainAction.project_type(self)
        MainAction.project_option(self)
        MainAction.project_recycle_bin(self)

    # 메인 동작 (랜덤으로 실행해도 괜찮음)
    def main_act(self):
        funcs = [MainAction.main_banner, MainAction.vllo_setting,
                 MainAction.store, MainAction.main_middle_menu]
        Tester.testFuncs(self, funcs, 4, Tester.testFuncsKeyword)

    # 배너 동작
    def main_banner(self):
        driver = self.driver
        try:
            element = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.bannerRightSideImage)
            print("배너 유무 확인")
            if element:
                print("배너 있음 스와이프 동작 실행")
                for i in range (0, 5):
                    try:
                        Tester.long_press_drag(driver, Idcomp.bannerRightSideImage, Idcomp.SettingButton, 0.5)
                    except Exception as e:
                            print("배너 넘어가는 와중에 동작 실행", e)
                            continue

            print("배너 스와이프 확인 완료")
            Tester.tap(driver, Idcomp.BannerMenu, "배너 선택")
            Tester.time(driver, 5)
            print("유튜브 링크 대기")
            element = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.Youtubeplayer)
            print("유튜브 링크가 있는 영상인지 판별")
            if element:
                print("유튜브 링크 있음")
                Tester.tap(driver, Idcomp.bannerplay, "재생")
                Tester.time(driver, 10)
                Tester.tap(driver, Idcomp.premium_icon_close, "닫기 선택")
            if not element:
                print("유튜브 링크 없음")
                Tester.tap(driver, Idcomp.premium_icon_close, "닫기 선택")

        except Exception as e:
            name = "mainBanner"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.premium_icon_close, None)
            print("배너 확인 정상 동작하지 않음", e)

    # 설정
    def vllo_setting(self):
        driver = self.driver
        try:
            Tester.time(driver, 3)
            Tester.wait_tap(driver, 3, Idcomp.SettingButton, "설정 버튼 선택")
            MainAction.Setting_help(self)
            Tester.wait_tap(driver, 3, Idcomp.review, None)
            Tester.activateApp(self)
            Tester.time(driver, 2)

            for i in range (0, 2):
                Tester.wait_tap(driver, 4, Idcomp.show_touch, None)

            Tester.wait_tap(driver, 3, Idcomp.youtube, "유튜브 공유 선택")
            Tester.activateApp(self)
            Tester.wait_tap(driver, 3, Idcomp.instagram, "인스타 공유 선택")
            Tester.activateApp(self)
            Tester.wait_tap(driver, 3, Idcomp.facebook, "페이스북 공유 선택")
            Tester.activateApp(self)

            Tester.tap(driver, Idcomp.icon_back, "뒤로가기")

        except Exception as e:
            name = "vlloSetting"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.icon_back, "뒤로가기")
            print("설정 확인 중 문제 발생", e)
    # 도움말 동작
    def Setting_help(self):
        driver = self.driver

        try:
            Tester.tap(driver, Idcomp.help, "도움말 버튼 선택")
            Tester.tap(driver, "다른 OS 간의 기기 변경 시 구매 연동이 가능한가요?", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "무료체험/구독은 자동으로 갱신되나요?", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "프로젝트는 자동 저장 되나요?", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "추출이 진행되지 않아요!", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "VLLO 저작권이 궁금해요!", None)
            Tester.tap(driver, Idcomp.faq_close, None)

            Tester.popup_check(driver, "문의하기", Idcomp.contact_us)
            Tester.time(driver, 3)
            # 백그라운드의 VLLO 앱 활성화
            Tester.activateApp(self)
            MainAction.Setting_tutorial(self)
            MainAction.Setting_license(self)
            MainAction.Setting_tutorial_keyboard(self)

        except Exception as e:
            name = "Setting_help"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.icon_back, None)
            print("도움말 정상 동작하지 않음", e)
    # 도움말 튜토리얼
    def Setting_tutorial(self):
        driver = self.driver
        try:
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 2, Idcomp.tutorial, None)
            Tester.category_check(driver, Idcomp.tutorial_category)

        except Exception as e:
            name = "Setting_tutorial"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.icon_back, None)
            print("튜토리얼 정상 동작하지 않음", e)
    # 도움말 저작권
    def Setting_license(self):
        driver = self.driver
        try:
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.license, "저작권 버튼 선택")
            Tester.tap(driver, "VLLO 저작권이 궁금해요!", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "타 프로그램과 함께 편집해도 되나요?", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "VLLO로 제작한 영상을 공모전 및 기타 홍보물에 사용해도 되나요?", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "콘텐츠 공유가 가능한가요? (Youtube, SNS,웹사이트 등)", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.tap(driver, "Youtube 업로드 후 저작권 침해신고를 받았어요!", None)
            Tester.tap(driver, Idcomp.faq_close, None)
            Tester.popup_check(driver, "저작권 문의하기", Idcomp.contact_us)
            Tester.time(driver, 2)
            # 백그라운드의 VLLO 앱 활성화
            Tester.activateApp(self)

        except Exception as e:
            name = "Setting_license"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.icon_back, None)
            print("저작권 정상 동작하지 않음", e)

    # 도움말 키보드 단축키
    def Setting_tutorial_keyboard(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 1, Idcomp.tutorial_keyboard, "키보드 단축키 정상 진입 완료")
            Tester.tap(driver, Idcomp.icon_back, "뒤로가기 선택")

        except Exception as e:
            name = "Setting_tutorial_keyboard"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.icon_back, "뒤로가기 선택")
            print("키보드 단축키 진입 불가능", e)

    # 상점
    def store(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.main_store, "상점 화면 진입")
            Tester.wait_tap(driver, 3, Idcomp.store_help, "도움말 선택")
            Tester.wait_tap(driver, 2, Idcomp.help_done, "도움말 완료 선택")
            Tester.tap(driver, Idcomp.terms_of_use, "이용 약관 선택")
            Tester.activateApp(self)
            Tester.tap(driver, Idcomp.privacy_policy, "개인 정보 정책")
            Tester.activateApp(self)
            Tester.time(driver, 5)
            el1 = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value="Premium icon close")
            el1.click()
        except Exception as e:
            name = "store"
            Tester.screenshot(self, name)
            el1 = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value="Premium icon close")
            el1.click()
            print("상점 확인 중 문제 발생", e)

    def main_middle_menu(self):
        funcs = [MainAction.project_fit_fill, MainAction.project_sort, MainAction.project_choice]
        Tester.testFuncs(self, funcs, 3, Tester.testFuncsKeyword)

    def project_fit_fill(self):
        driver = self.driver
        try:
            for i in range(0,2):
                Tester.tap(driver, Idcomp.fill_icon, "비율 확인 버튼 선택")
        except Exception as e:
            name = "projectFitFill"
            Tester.screenshot(self, name)
            print("프로젝트 썸네일 비율 확인 중 문제 발생", e)
    def project_sort(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.project_sort_down, "썸네일 정렬 아이콘 선택")
            Tester.tap(driver, Idcomp.project_created, "생성한 날짜")
            Tester.tap(driver, Idcomp.project_sort_up, "썸네일 정렬 아이콘 선택")
            Tester.tap(driver, Idcomp.project_opened, "마지막으로 열어본 날짜 선택")
            Tester.tap(driver, Idcomp.project_sort_down, "썸네일 정렬 아이콘 선택")
            Tester.tap(driver, Idcomp.project_name, "이름 선택")
            Tester.tap(driver, Idcomp.project_sort_up, "썸네일 정렬 아이콘 선택")
            Tester.tap(driver, Idcomp.project_opened, "마지막으로 열어본 날짜 선택")
        except Exception as e:
            name = "projectSort"
            Tester.screenshot(self, name)
            print("프로젝트 정렬 확인 중 문제 발생", e)
    def project_choice(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.project_select_button, "프로젝트 선택")
            Tester.tap(driver, Idcomp.project1, "프로젝트 1 선택")
            Tester.popup_check(driver, "프로젝트 삭제", Idcomp.ProjectDeleteButton)
            Tester.time(driver, 2)
            for i in range(0,2):
                Tester.tap(driver, Idcomp.project_select_all_button, "모두선택, 선택해제")
            Tester.tap(driver, Idcomp.project_select_button, "닫기")
        except Exception as e:
            name = "projectChoice"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.project_select_button, "닫기")
            print("프로젝트 선택 확인 중 문제 발생", e)

    def create_pre_project(self):
        driver = self.driver
        try:
            print("새 프로젝트 생성 시작")
            Tester.tap(driver, Idcomp.new_project, "새 프로젝트")
            Tester.tap(driver, Idcomp.insert_blank, "빈 장면 추가")
            Tester.tap(driver, Idcomp.icon_next, "다음으로")
            Tester.tap(driver, Idcomp.create_project, "프로젝트 생성하기")
            Tester.tap(driver, Idcomp.icon_back, "뒤로가기")
            for i in range(0, 4):
                Tester.tap(driver, Idcomp.project_edit_buttom1, "프로젝트1 메뉴 버튼(···) 선택")
                Tester.tap(driver, Idcomp.popup_duplicate, "복제 선택")
            Tester.time(driver, 2)

        except Exception as e:
            print("프로젝트 생성 확인 중 문제 발생", e)
            name = "createPreProject"
            Tester.screenshot(self, name)

    def project_color(self):
        driver = self.driver
        colors = [Idcomp.popup_tag_red, Idcomp.popup_tag_yellow, Idcomp.popup_tag_green, Idcomp.popup_tag_blue,
                  Idcomp.popup_tag_purple]

        for i in range(5):
            try:
                Tester.tap(driver, getattr(Idcomp, f'project_edit_buttom{i + 1}'), None)
                Tester.tap(driver, colors[i], None)
                print(f"프로젝트{i + 1} 메뉴 버튼(···) 선택, 프로젝트 분류 색상 변경 완료")
            except Exception as e:
                name = "projectColor"
                Tester.screenshot(self, name)
                print(f"프로젝트{i + 1} 메뉴 버튼(···) 선택, 프로젝트 분류 색상 변경 중 문제 발생", e)

    def project_type(self):
        driver = self.driver
        colors = [Idcomp.popup_red, Idcomp.popup_yellow, Idcomp.popup_green, Idcomp.popup_blue, Idcomp.popup_purple]
        try:
            Tester.tap(driver, Idcomp.start_my_project_button, "왼쪽 상단 내 프로젝트 선택")
            for color in colors:
                Tester.tap(driver, color, f"{color} 선택")
                # 왼쪽 상단 토글 버튼 (색상) 선택
                Tester.tap(driver, Idcomp.start_my_project_button, f"왼쪽 상단 토글 버튼 ({color}) 선택")
            # 내 프로젝트 선택
            Tester.tap(driver, Idcomp.popup_all, "내 프로젝트 선택")
        except Exception as e:
            name = "projectType"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.popup_all, None)
            print(f"내 프로젝트 확인 중 문제 발생", e)

    def project_recycle_bin(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.start_my_project_button, "왼쪽 상단 내 프로젝트 선택")
            Tester.wait_tap(driver, 50, Idcomp.popup_recycle_bin, "최근 삭제된 항목 선택")
            Tester.tap(driver, Idcomp.common_bottom_icon_close, "X 버튼 선택")
            Tester.tap(driver, Idcomp.start_my_project_button, "왼쪽 상단 내 프로젝트 선택")
            Tester.tap(driver, Idcomp.popup_recycle_bin, "최근 삭제된 항목 선택")
            Tester.tap(driver, Idcomp.project1, "프로젝트1 선택 (포커싱 on)")
            Tester.tap(driver, Idcomp.project1, "프로젝트1 선택 (포커싱 off)")
            Tester.tap(driver, Idcomp.select_all, "모두 선택")
            Tester.tap(driver, Idcomp.deselect_all, "선택 해제")
            Tester.tap(driver, Idcomp.project1, "프로젝트1 선택 (포커싱 on)")
            Tester.tap(driver, Idcomp.restore, "복원")
            Tester.tap(driver, Idcomp.project2, "프로젝트2 선택")
            Tester.popup_check(driver, "프로젝트 영구 삭제", Idcomp.delete_permanently)
            Tester.tap(driver, Idcomp.common_bottom_icon_close, "X 버튼 선택")
        except Exception as e:
            name = "projectRecycleBin"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.common_bottom_icon_close, "X 버튼 선택")
            print(f"최근 삭제된 항목 확인 중 문제 발생", e)

    def project_option(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.project_edit_buttom1, "프로젝트1 메뉴 버튼(···) 선택")
            # Tester.tap(driver, Idcomp.project_share, "프로젝트 공유하기 선택")
            # Tester.wait_tap(driver, 2, Idcomp.close, "닫기 선택")
            Tester.tap(driver, Idcomp.popup_rename, "이름 변경 선택")
            Tester.text_input(driver, Idcomp.input_title, "appium test")
            Tester.tap(driver, Idcomp.input_title_done_button, "V버튼 선택")
            Tester.tap(driver, Idcomp.project_edit_buttom1, "프로젝트1 메뉴 버튼(···) 선택")
            Tester.tap(driver, Idcomp.popup_duplicate, "복제 선택")
            Tester.tap(driver, Idcomp.project_edit_buttom1, "프로젝트1 메뉴 버튼(···) 선택")
            Tester.popup_check(driver, "프로젝트 삭제", Idcomp.popup_delete)
            Tester.tap(driver, Idcomp.project_edit_buttom1, "프로젝트1 메뉴 버튼(···) 선택")
            Tester.popup_check(driver, "프로젝트 삭제", Idcomp.popup_delete)
        except Exception as e:
            name = "projectOption"
            Tester.screenshot(self, name)
            print(f"프로젝트 메뉴 항목 확인 중 문제 발생", e)

class projectCreate:
    def __init__(self, driver):
        self.driver = driver

    def project_create_all(self):
        driver = self.driver
        projectCreate.project_create(self)
        projectCreate.camera(self)
        projectCreate.stock(self)
        projectCreate.project(self)
        Tester.tap(driver, Idcomp.icon_next, "프로젝트 생성")
        projectCreate.project_setting(self)
        Tester.tap(driver, Idcomp.create_project, "프로젝트 생성하기 선택")

    def project_create(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.new_project, "새 프로젝트")
        Tester.tap(driver, Idcomp.album , "최근 사용 선택")
        Tester.tap(driver, Idcomp.Appium, "에피움 폴더 선택")
        Tester.tap(driver, Idcomp.insert_blank, "빈 장면 선택")
        Tester.tap(driver, Idcomp.category_all, "전체 선택")
        Tester.tap(driver, Idcomp.category_video, "비디오 선택")
        Tester.tap(driver, Idcomp.asset_1, "1번 항목 선택")
        projectCreate.asset_expand(self)
        Tester.tap(driver, Idcomp.category_photo, "사진 선택")
        Tester.tap(driver, Idcomp.asset_1, "1번 항목 선택")
        Tester.tap(driver, Idcomp.category_gif, "gif 선택")
        Tester.tap(driver, Idcomp.asset_1, "1번 항목 선택")
        Tester.tap(driver, Idcomp.category_all, "전체 선택")

    def asset_expand(self):
        driver = self.driver
        try:
            asset_expand = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value="asset_expand_1_0")
            if asset_expand:
                Tester.tap(driver, Idcomp.asset_expand, "가운데 클립 전체보기")
                Tester.tap(driver, Idcomp.screen_icon_pause, "일시정지")
                Tester.tap(driver, Idcomp.screen_icon_play, "재생")
                Tester.tap(driver, Idcomp.preview_close, "닫기")
            if not asset_expand:
                Tester.tap(driver, Idcomp.content_expand0, "가운데 스톡 전체보기")
                Tester.tap(driver, Idcomp.screen_icon_pause, "일시정지")
                Tester.tap(driver, Idcomp.screen_icon_play, "재생")
                Tester.tap(driver, Idcomp.preview_close, "닫기")
        except Exception as e:
            name = "asset_expand"
            Tester.screenshot(self, name)
            print("에셋 전체 화면 부분 정상 동작하지 않음", e)

    def camera(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.camera, "카메라 선택")
            camera_first_popup = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value="확인")
            if camera_first_popup:
                Tester.time(driver, 10)
                print("최조 진입 시 팝업 허용 후")
                Tester.wait_tap(driver, 500, Idcomp.photo_capture, "카메라 촬영")
                Tester.wait_tap(driver, 2, Idcomp.use_photo, "사진 사용")
                Tester.wait_tap(driver, 2, Idcomp.selected_delete_5, "사진 삭제")

            elif not camera_first_popup:
                Tester.wait_tap(driver, 500, Idcomp.photo_capture, "카메라 촬영")
                Tester.wait_tap(driver, 10, Idcomp.use_photo, "사진 사용")
                Tester.wait_tap(driver, 10, Idcomp.selected_delete_5, "사진 삭제")

        except Exception as e:
            name = "camera"
            Tester.screenshot(self, name)
            print("카메라 부분 정상 동작하지 않음", e)

    def stock(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.media_stock, "스톡 선택")
        stock_category = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_All, *Idcomp.midea_stock_category
                          ]
        Tester.category_check(driver, stock_category)
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.midea_stock_1, None)
        # try:
        print("스톡 다운로드 아이콘 판별")
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.content1, "스톡 추가")
        stock_download_icon = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.asset_selected_4)
        Tester.time(driver, 2)
        if stock_download_icon:
            print("스톡 다운로드 아이콘 없음")
            projectCreate.asset_expand(self)

        elif not stock_download_icon:
            print("스톡 다운로드 아이콘 있음")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content1, "스톡 추가")
            projectCreate.asset_expand(self)

        # except Exception as e:
        #     print("스톡 부분 정상 동작하지 않음", e)

    def project(self):
        driver = self.driver
        try:
            project_check = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value="project_0")
            print("프로젝트 리스트에 프로젝트 있는지 판별")
            if project_check:
                print("프로젝트 있음")
                for i in range(0, 2):
                    Tester.tap(driver, Idcomp.project, None)
                print("프로젝트 선택 후 취소")

            elif not project_check:
                print("프로젝트 없음")
        except Exception as e:
            print("프로젝트 부분 정상 동작하지 않음", e)

    def project_setting(self):
        driver = self.driver
        Tester.time(driver, 2)
        Tester.text_input(driver, Idcomp.project_title, " appium_test")
        Tester.tap(driver, Idcomp.input_title_done_button, "완료 선택")
        Tester.time(driver, 2)
        Tester.category_check(driver, Idcomp.project_setting_category1)
        Tester.category_check(driver, Idcomp.project_setting_category2)
        Tester.tap(driver, Idcomp.screen16_9, "16 : 9 선택")

class EditMainAction:
    def __init__(self, driver):
        self.driver = driver
    # 튜토리얼
    def editor_tutorial(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.top_icon_tutorial, "상단 튜토리얼 버튼")
            Tester.tap(driver, Idcomp.popup_close, "닫기")
        except Exception as e:
            Tester.tap(driver, Idcomp.popup_close, "닫기")
            print("편집화면 튜토리얼 부분 정상 동작하지 않음", e)
    # 상단 설정
    def main_editor_setting(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.editor_setting, "상단 설정 선택")
            projectCreate.project_setting(self)
            Tester.tap(driver, Idcomp.top_icon_done, "완료 선택")
        except Exception as e:
            print("상단 설정 부분 정상 동작하지 않음", e)
    # 재생, 정지
    def play_pause(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.edit_play, "재생 선택")
            Tester.time(driver, 3)
            Tester.tap(driver, Idcomp.edit_play, "일시 정지 선택")
        except Exception as e:
            print("재생, 정지 동작하지 않음", e)
    # 전체 화면
    def full_screen(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.screen_icon_full, "전체 화면으로 보기 선택")
            Tester.time(driver, 2)
            for i in range(0, 2):
                Tester.tap(driver, Idcomp.icon_skip_next, "10초 이후로 이동 버튼 선택")
            for i in range(0, 2):
                Tester.tap(driver, Idcomp.icon_skip_previous, "10초 이전으로 이동 버튼 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.speed_full_screen, "배속 버튼 선택")
            Tester.tap(driver, Idcomp.full_screen_speed_0_5, "0.5x 선택")
            Tester.tap(driver, Idcomp.full_screen_speed_1, "1x 선택")
            Tester.tap(driver, Idcomp.full_screen_speed_1_5, "1.5x 선택")
            Tester.tap(driver, Idcomp.full_screen_speed_2, "2x 선택")
            Tester.tap(driver, Idcomp.speed_done, "완료 버튼 선택")
            Tester.tap(driver, Idcomp.play_full_screen, "재생 선택")
            Tester.tap(driver, Idcomp.play_full_screen, "일시 정지 선택")
            Tester.tap(driver, Idcomp.capture_full_screen, "전체 화면 캡쳐 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.exit_full_screen, "전체 화면 끄기")
        except Exception as e:
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.popup_close)
            if el1:
                Tester.tap(driver, Idcomp.exit_full_screen, "전체 화면 끄기")
            elif el1:
                action = TouchAction(driver)
                action.tap(x=440, y=185).perform()
                Tester.tap(driver, Idcomp.exit_full_screen, "속도 저하로 풀스크린 ui 사라짐")
            print("전체 화면 부분 정상 동작하지 않음", e)
    # 프레임 이동
    def move_frame(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.move_pre_clip, "l◁ 클립 처음으로 이동하기")
            Tester.tap(driver, Idcomp.move_next_clip, "▷l 클립 끝으로 이동하기")
            Tester.long_press(driver, Idcomp.move_pre_clip, 5000)
            print("l◁ 영상 맨 처음으로 이동하기 (롱프레스)")
            Tester.long_press(driver, Idcomp.move_next_clip, 5000)
            print("▷l 영상 맨 끝으로 이동하기(롱프레스)")
            Tester.tap(driver, Idcomp.move_pre_frame, "◁l 1프레임씩 이동하기 선택")
            Tester.long_press(driver, Idcomp.move_pre_frame, 5000)
            print("◁l 1프레임씩 이동하기 (롱프레스)")
            Tester.tap(driver, Idcomp.move_next_frame, "▷l 1프레임씩 이동하기 선택")
            Tester.long_press(driver, Idcomp.move_next_frame, 5000)
            print("▷l 1프레임씩 이동하기 (롱프레스)")
            Tester.long_press(driver, Idcomp.move_pre_clip, 5000)
            print("l◁ 영상 맨 처음으로 이동하기 (롱프레스)")
        except Exception as e:
            Tester.tap(driver, Idcomp.edit_done, None)
            print("프레임 이동 부분 정상 동작하지 않음", e)
    # 클립 진입 전 동작들 종합 (안에 함수들 랜덤으로 돌아도 괜찮음)
    def before_entering_the_Clip(self):
        funcs = [EditMainAction.editor_tutorial, EditMainAction.main_editor_setting, EditMainAction.play_pause,
                 EditMainAction.move_frame]
               # editMainAction.fullScreen <- 자꾸 ui 사라져서 해결책 찾으면 들어가야함
        Tester.testFuncs(self, funcs, 4, Tester.testFuncsKeyword)

    # 클립 진입 후 동작들 종합 (안에 함수들 랜덤으로 돌아도 괜찮음)
    def after_entering_the_Clip(self):
        funcs = [EditMainAction.media_mode, EditMainAction.quick_btn, EditMainAction.waveform_bubble_view, EditMainAction.main_edit, EditMainAction.edit_main_handle]
        Tester.testFuncs(self, funcs, 5, Tester.testFuncsKeyword)
    # 편집화면 핸들
    def edit_main_handle(self):
        driver = self.driver
        try:
            Tester.long_press_drag(driver, Idcomp.overlay_top_crop, Idcomp.overlay_bottom_crop, 1000)
            Tester.tap(driver, Idcomp.undo_button, None)
            Tester.long_press_drag(driver, Idcomp.overlay_bottom_crop, Idcomp.overlay_top_crop, 1000)
            Tester.tap(driver, Idcomp.undo_button, None)
            Tester.long_press_drag(driver, Idcomp.overlay_right_crop, Idcomp.overlay_left_crop, 1000)
            Tester.tap(driver, Idcomp.undo_button, None)
            Tester.long_press_drag(driver, Idcomp.overlay_left_crop, Idcomp.overlay_right_crop, 1000)
            Tester.tap(driver, Idcomp.undo_button, None)
            Tester.long_press_drag(driver, Idcomp.overlay_rotate, Idcomp.overlay_top_crop, 1000)
            Tester.tap(driver, Idcomp.undo_button, None)
            Tester.long_press_drag(driver, Idcomp.overlay_resize, Idcomp.overlay_top_crop, 1000)
            Tester.tap(driver, Idcomp.undo_button, None)
            print("편집 화면 핸들 조절 완료")
        except Exception as e:
            print("편집화면 핸들 부분 정상 동작하지 않음", e)
    # 편집화면 가운데, 끼움, 채움
    def media_mode(self):
        driver = self.driver
        try:
            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.mediamode_cen)
            print("클립, 데코 판별")
            print("클립으로 확인")
            Tester.wait_tap(driver, 2, Idcomp.mediamode_cen, "가운데")
            Tester.wait_tap(driver, 2, Idcomp.mediamode_fit, "끼움")
            Tester.wait_tap(driver, 2, Idcomp.mediamode_fil, "채움")

        except NoSuchElementException:
            print("데코로 확인")
            print("가운데, 끼움, 채움 없는 항목")
        except Exception as e:
            print("편집화면 가운데, 끼움, 채움 부분 정상 동작하지 않음", e)
    # 상단 눈, 그리드, 자석
    def quick_btn(self):
        driver = self.driver
        try:
            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.clip_top_icon_eye)
            print("클립, 데코 판별")
            print("클립으로 확인")
            # 리스트 정의 (아이콘 정보)
            icon_list = [
                (Idcomp.clip_top_icon_eye, "상단 눈 아이콘"),
                (Idcomp.clip_top_icon_grid, "상단 그리드 아이콘"),
                (Idcomp.clip_top_icon_magnet, "상단 자석 아이콘")
            ]

            for icon, name in icon_list:
                for i in range(0, 2):
                    try:
                        Tester.wait_tap(driver, 2, icon, None)
                        if i == 0:
                            print(f"{name} off")  # f-string
                        if i == 1:
                            print(f"{name} on")

                    finally:
                        pass

        except NoSuchElementException:
            print("데코로 확인")
            # 리스트 정의 (아이콘 정보)
            icon_list = [
                (Idcomp.clip_top_icon_grid, "상단 그리드 아이콘"),
                (Idcomp.clip_top_icon_magnet, "상단 자석 아이콘")
            ]

            for icon, name in icon_list:
                for i in range(0, 2):
                    try:
                        Tester.wait_tap(driver, 2, icon, None)
                        if i == 0:
                            print(f"{name} off")  # f-string
                        if i == 1:
                            print(f"{name} on")

                    finally:
                        pass

        except Exception as e:
            Tester.tap(driver, Idcomp.edit_done, None)
            print("클립 퀵 버튼 부분 정상 동작하지 않음", e)
    # 말풍선 뷰, 웨이브폼 뷰
    def waveform_bubble_view(self):
        driver = self.driver

        try:
            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.deco_type_button)
            print("클립, 데코 판별")
            print("데코로 확인")
            Tester.wait_tap(driver, 5, Idcomp.deco_type_button, "말풍선 뷰 옵션 열기")
            Tester.tap(driver, Idcomp.deco_type_arrow_left, "말풍선 옵션 왼쪽으로 넘기기")
            Tester.tap(driver, Idcomp.deco_type_arrow_right, "말풍선 옵션 오른쪽으로 넘기기")
            for i in range(0, 7):
                Tester.tap(driver, Idcomp.waveform_type_arrow_right, None)
            print("웨이브폼 옵션 오른쪽으로 넘기기 완료")
            Tester.tap(driver, Idcomp.deco_type_button, "말풍선 뷰 옵션 닫기")

        except NoSuchElementException:
            print("클립으로 확인")
            Tester.wait_tap(driver, 5, Idcomp.waveform_type_button, "웨이브폼 뷰 옵션 열기")
            for i in range(0, 7):
                Tester.tap(driver, Idcomp.waveform_type_arrow_right, None)
            print("웨이브폼 옵션 오른쪽으로 넘기기 완료")
            Tester.tap(driver, Idcomp.waveform_type_button, "웨이브폼 뷰 옵션 닫기")

        except Exception as e:
            Tester.tap(driver, Idcomp.edit_done, None)
            print("말풍선 뷰, 웨이브폼 뷰  정상 동작하지 않음", e)
    # 메인 화면 타임라인 부분
    def main_edit(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.move_pre_clip, "앞으로 이동")
            Tester.drag(driver, Idcomp.move_start_time_view, Idcomp.story_board_button)
            Tester.tap(driver, Idcomp.undo_button, "실행 취소")
            Tester.tap(driver, Idcomp.move_next_clip, "뒤로 이동")
            Tester.tap(driver, Idcomp.move_pre_clip, "l◁ 클립 처음으로 이동하기")
            Tester.drag(driver, Idcomp.move_end_time_view, Idcomp.add_button)
            print("클립 우측 핸들 1회 조절")
            Tester.tap(driver, Idcomp.undo_button, "실행 취소")
            Tester.tap(driver, Idcomp.move_pre_clip, "클립 처음으로 이동하기")
            Tester.long_press(driver, Idcomp.move_next_frame, 3000)
            print("▷l 1프레임씩 이동하기 (롱프레스)")
            Tester.tap(driver, Idcomp.from_now, "여기부터 선택")
            Tester.tap(driver, Idcomp.undo_button, "실행 취소 선택")
            Tester.tap(driver, Idcomp.until_now, "여기까지 선택")
            Tester.tap(driver, Idcomp.undo_button, "실행 취소 선택")
            Tester.tap(driver, Idcomp.split, "분할 선택")
            Tester.tap(driver, Idcomp.undo_button, "실행 취소 선택")
            Tester.drag(driver, Idcomp.until_the_end, Idcomp.delete)
            Tester.tap(driver, Idcomp.move_to_end, "맨 뒤로 선택")
            Tester.tap(driver, Idcomp.move_to_left, "왼쪽으로 이동 선택")
            Tester.tap(driver, Idcomp.move_to_right, "오른쪽으로 이동 선택")
            Tester.tap(driver, Idcomp.move_to_start, "맨 앞으로")
        except Exception as e:
            Tester.tap(driver, Idcomp.edit_done, None)
            print("메인 타임라인 부분 정상 동작하지 않음", e)

    def main_timeline_clip(self):
        driver = self.driver
        Tester.wait_tap(driver, 500, Idcomp.timeline_clip2, "클립 1번 선택")