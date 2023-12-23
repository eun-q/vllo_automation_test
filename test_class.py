from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from accessibility_Id import Idcomp
import time, os, random
from datetime import datetime

class Tester:

    # 탭 동작
    def tap(driver, element, name):
        driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element).click()
        if name is not None:
            print(name)

    # 탭 동작 XPATH 값
    def tap_xpath(driver, element, name):
        #xpath 값들로 보이는 것들은 모두 접근성 아이디 지정이 필요합니다 테스트 시 임시로 사용해주세요!
        driver.find_element(by=MobileBy.XPATH, value=element).click()
        if name is not None:
            print(name)

    # 드래그 동작
    def drag(driver, element1, element2):

        # 클립 좌측 핸들
        a = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element1)
        # 클립 우측 핸들
        b = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element2)

        time.sleep(2)

        # 클립 좌측 핸들 1회 조절
        TouchAction(driver).press(a).wait(200).move_to(b).release().perform()

    # 더블 탭 동작
    def double_tap(driver, element):
        actions = TouchAction(driver)
        actions.double_tap(element).perform()

    # 롱프레스
    def long_press(driver, element, long_press_time):
        # element = 롱프레스할 요소
        # long_press_time = 롱프레스할 시간 ex) 1000 = 1초
        a = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element)

        TouchAction(driver).long_press(a, duration=long_press_time).release().perform()

    def long_press_with_offset(driver, element, long_press_time, offset_x, offset_y):
        # element = 롱프레스할 요소
        # long_press_time = 롱프레스할 시간
        # offset_x = X축으로 이동할 오프셋 값
        # offset_y = Y축으로 이동할 오프셋 값

        a = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element)
        size = a.size
        location = a.location

        new_x = location['x'] + size['width'] // 2 + offset_x
        new_y = location['y'] + size['height'] // 2 + offset_y

        TouchAction(driver).long_press(x=new_x, y=new_y, duration=long_press_time).release().perform()

    # 롱프레스 후 드래그
    def long_press_drag(driver, element1, element2, speed):
        # element1 = 드래그 시작할 위치
        # element2 = 드래그 끝낼 위치
        # speed = 드래그 속도 / 1000 = 1초
        # a에 드래그 시작할 아이디 지정
        a = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element1)
        # b에 드래그 끝낼 아이디 지정
        b = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element2)
        # a부터 b까지 speed의 값으로 롱프레스 후 드래그
        TouchAction(driver).long_press(a).wait(speed).move_to(b).release().perform()

    # 카테고리 체크
    def category_check(driver, element1):
        # element1 = 체크하고싶은 리스트 넣으면 됨
        # 순차적으로 클릭
        for element in element1:  # 리스트에 있는 요소들을 하나씩 `element` 변수에 넣어서 반복문을 실행
            elem = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=element)
            if len(elem) > 0:  # `elem` 리스트의 길이가 0보다 큰 요소를 찾으면 아래 코드를 실행
                elem[0].click()  # `elem` 리스트의 첫 번째 요소를 클릭 이때, 리스트에는 하나의 요소만 있을 것이므로, 첫 번째 요소를 선택
        print("순차적으로 실행")
        # 역순으로 클릭
        for element in reversed(element1):  # 리스트에 있는 요소들을 역순으로 하나씩 `element` 변수에 넣어서 반복문을 실행
            elem = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=element)
            if len(elem) > 0:
                elem[0].click()
        print("역순으로 실행")

    # 텍스트 입력
    def text_input(driver, element, text):
        # element = 텍스트 입력할 영역의 아이디
        # text = 작성하고 싶은 내용
        # input_title에 텍스트 입력할 영역 변수로 할당
        input_title = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=element)
        # input_title에 있는 내용 지우기
        input_title.clear()
        # input_title에 text값 작성
        input_title.send_keys(text)

    # 시간
    def time(driver, seconds):
        # seconds = 대기할 시간 값
        time.sleep(seconds)

    # 하나의 아이디만 판별이 필요한 경우
    def identify(driver, name, Accessibility_Id, done_id, action):
        try:
            # Accessibility_Id_1 변수에 할당
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Accessibility_Id)
            # el1일 경우 아래 내용 실행
            if el1:
                # el1이 화면에 보일 때
                el1[0].is_displayed()
                # el1 클릭
                el1[0].click()
                # nametext + 선택 문구 출력
                print("%s 선택" % name)
                # 2초 대기
                Tester.time(driver, 2)
                action()
                if done_id is not None:
                    Tester.tap(driver, done_id, None)

        # 판별 자체가 실패할 경우 예외처리
        except Exception as e:
            print("%s 없는 항목" % name, e)

    # 두 개의 아이디 판별이 필요한 경우
    def identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id, action):
        Tester.time(driver, 2)
        try:
            # Accessibility_Id_1, 2 변수에 할당
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Accessibility_Id_1)
            # el1일 경우 아래 내용 실행
            if el1:
                # el1 선택
                Tester.wait_tap(driver, 3, Accessibility_Id_1, "%s 선택" % name1)
                # 2초 대기
                Tester.time(driver, 2)
                # 각 클래스의 액션들
                action()
                # 완료 아이디
                if done_id is not None:
                    Tester.tap(driver, done_id, None)
                    print("%s 완료 선택" % name)

            # el2일 경우 아래 내용 실행
            elif not el1:
                # el2 선택
                Tester.wait_tap(driver, 3, Accessibility_Id_2, "%s 선택" % name2)
                # 2초 대기
                Tester.time(driver, 2)
                # 각 클래스의 액션들
                action()
                if done_id is not None:
                    # 완료 아이디
                    Tester.tap(driver, done_id, None)
                    print("%s 완료 선택" % name)

        # 판별 자체가 실패할 경우 예외처리
        except Exception as e:
            print("%s 없는 항목" % name, e)

    # 기다렸다가 요소를 찾으면 탭
    def wait_tap(driver, seconds , Accessibility_Id, name):
        # seconds = 요소가 나타날 때까지 대기할 시간
        # Accessibility_Id = 클릭할 접근성 아이디
        # 요소가 나타날 때까지 대기
        element = WebDriverWait(driver, seconds).until(
            EC.presence_of_element_located((By.ID, Accessibility_Id))
        )
        # 요소를 클릭
        element.click()

        if name is not None:
            print(name)

    # 팝업 체크
    def popup_check(driver, name, Accessibility_Id):
        Tester.wait_tap(driver, 2, Accessibility_Id, "%s 버튼 선택" % name)
        print("%s 팝업 확인" % name)
        Tester.wait_tap(driver, 2, Idcomp.alert_1, "%s 취소 선택" % name)
        Tester.wait_tap(driver, 2, Accessibility_Id, "%s 버튼 선택" % name)
        Tester.wait_tap(driver, 2, Idcomp.popup_close, "%s 닫기 선택" % name)
        Tester.wait_tap(driver, 2, Accessibility_Id, "%s 버튼 선택" % name)
        Tester.wait_tap(driver, 2, Idcomp.alert_0, "%s 확인 선택" % name)
        print("%s 팝업 확인 완료" % name)

    # 백그라운드의 VLLO 앱 활성화
    def activateApp(self):
        self.driver.activate_app(Idcomp.activate_vllo)
        print("백그라운드의 VLLO 앱 활성화")

    # 클립 추가
    def add_clip(driver, name, Accessibility_Id_1):
        try:
            Tester.wait_tap(driver, 2, Idcomp.add_button, "%s 추가 버튼 선택" % name)
            Tester.wait_tap(driver, 2, Idcomp.album, "최근 항목 선택")
            Tester.wait_tap(driver, 2, Idcomp.Appium, "Appium 폴더 선택")
            if Accessibility_Id_1 is not None:
                Tester.wait_tap(driver, 2, Accessibility_Id_1, "%s 선택" % name)
                Tester.wait_tap(driver, 2, Idcomp.asset1, "%s 1번 선택" % name)
                Tester.wait_tap(driver, 2, Idcomp.icon_next, "다음 버튼 선택")
            else:
                Tester.wait_tap(driver, 2, Idcomp.insert_blank, "%s 선택" % name)
                Tester.wait_tap(driver, 2, Idcomp.icon_next, "다음 버튼 선택")

        except Exception as e:
            print("클립 추가 중 문제 발생", e)

    def decoBookMarkCheck(driver, contents_id, add_tap_id, name):
        try:
            Tester.wait_tap(driver, 2, add_tap_id, "%s 카테고리 선택" % name)
            Tester.time(driver, 1)
            Tester.long_press(driver, contents_id, 2000)
            Tester.time(driver, 1)
            Tester.long_press(driver, contents_id, 2000)
            Tester.tap(driver, Idcomp.popup_done, "완료")
            Tester.time(driver, 1)
            Tester.long_press(driver, contents_id, 2000)
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value="Bookmark(1)")
            if el1:
                Tester.tap(driver, Idcomp.popup_none, "완료")
            if not el1:
                Tester.tap(driver, Idcomp.popup_done, "완료")
        except Exception as e:
            print("데코 북마크 중 문제 발생", e)

    def bookMarkCheck(driver, bookmark_id, contents_id1, contents_id2,add_tap_id, name):
        Tester.wait_tap(driver, 2, add_tap_id, "%s 카테고리 선택" % name)
        Tester.time(driver, 2)
        Tester.long_press(driver, contents_id1, 2000)
        Tester.time(driver, 2)
        Tester.long_press(driver, contents_id1, 2000)
        Tester.tap(driver, Idcomp.popup_done, "완료")
        Tester.tap(driver, Idcomp.category_Recents, "최근 사용")
        Tester.wait_tap(driver, 2, bookmark_id, "북마크")
        Tester.time(driver, 2)
        try:
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value="Bookmark(1)")
            print("상단 북마크 태그 보이는지 확인")
            if el1:
                print("상단 북마크 태그 확인됨")
                Tester.long_press(driver, contents_id2, 2000)
                Tester.wait_tap(driver, 3, Idcomp.popup_red, "빨강 선택")
                Tester.wait_tap(driver, 3, Idcomp.popup_done, "완료")
                Tester.wait_tap(driver, 3, "Red(1)", None)

                Tester.long_press(driver, contents_id2, 2000)
                Tester.wait_tap(driver, 3, Idcomp.popup_yellow, "노랑 선택")
                Tester.wait_tap(driver, 3, Idcomp.popup_done, "완료")
                Tester.wait_tap(driver, 3, "Yellow(1)", None)


                Tester.long_press(driver, contents_id2, 2000)
                Tester.wait_tap(driver, 3, Idcomp.popup_none, "삭제 선택")
                Tester.wait_tap(driver, 3, Idcomp.popup_done, "완료")

            elif not el1:
                Tester.long_press_drag(driver, contents_id2, Idcomp.add_cancel, 1000)
                Tester.long_press(driver, contents_id2, 2000)
                Tester.wait_tap(driver, 3, Idcomp.popup_red, "빨강 선택")
                Tester.wait_tap(driver, 3, Idcomp.popup_done, "완료")
                Tester.wait_tap(driver, 3, "Red(1)", None)

                Tester.long_press(driver, contents_id2, 2000)
                Tester.wait_tap(driver, 3, Idcomp.popup_yellow, "노랑 선택")
                Tester.wait_tap(driver, 3, Idcomp.popup_done, "완료")
                Tester.wait_tap(driver, 3, "Yellow(1)", None)

                Tester.long_press(driver, contents_id2, 2000)
                Tester.wait_tap(driver, 3, Idcomp.popup_none, "삭제 선택")
                Tester.wait_tap(driver, 3, Idcomp.popup_done, "완료")

        except Exception as e:
            print("%s 북마크 확인 중 문제 발생" % name, e)

    # 스크린샷
    def screenshot(self, name):
        driver = self.driver
        print("%s 스크린샷" % name)
        format_data = "%Y-%m-%d %H:%M:%S"
        now_str = datetime.now().strftime(format_data)
        file_name = now_str + str(name) + ".png"
        os.chdir('/' + os.path.join('Users', 'vimo', 'PycharmProjects', 'appium_test2', 'screenshot file', 'fulltest'))
        driver.save_screenshot(os.getcwd() + file_name)

    # def testFuncs(self, funcs, a):
        # 랜덤으로 실행
        # print("편집 메뉴 랜덤으로 실행")
        # for func in random.sample(funcs, a):
        #     func(self)
        # 순차적으로 실행
        # print("편집 메뉴 순차적으로 실행")
        # for i in range(a):
        #     func = funcs[i % len(funcs)]
        #     func(self)

    # 풀테스틑 실행 시 순차적으로 실행할 것인지 랜덤으로 실행할 것인지 여기서 작성
    testFuncsKeyword = "In turn"
    def testFuncs(self, funcs, a, keyword):
        if keyword == "random":
            # 랜덤으로 실행
            print("편집 메뉴 랜덤으로 실행")
            for func in random.sample(funcs, a):
                func(self)
        elif keyword == "In turn":
            # 순차적으로 실행
            print("편집 메뉴 순차적으로 실행")
            for i in range(a):
                func = funcs[i % len(funcs)]
                func(self)
        else:
            print("잘못된 키워드입니다.")