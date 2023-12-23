import random
import time
from appium.webdriver.common.mobileby import MobileBy

from test_class import Tester
from accessibility_Id import Idcomp

# 클립
class Clip:

    def __init__(self, driver):
        self.driver = driver

    def clip_all(self):
        driver = self.driver
        funcs = [Clip.clip_video_all, Clip.clip_blank_all, Clip.clip_gif_all, Clip.clip_image_all]
        Tester.testFuncs(self, funcs, 4, Tester.testFuncsKeyword)
        Tester.tap(driver, Idcomp.edit_done, "완료 선택")

    def clip_video_all(self):
        Clip.clip_video(self)
        Clip.clip_video_test(self)
    def clip_video(self):
        driver = self.driver
        Tester.add_clip(driver, "비디오 클립", Idcomp.category_video)
    def clip_video_test(self):
        driver = self.driver
        try:
            funcs = [
            Resize.resize_module,
            Layout.layout_module,
            Background.background_Module,
            Mute.mute_module,
            Volume.volume_module,
            Fade.fade_module,
            AudioEffect.audio_effect_module,
            EchoReverb.echo_reverb_module,
            # 오디오 분리
            SilenceRemoval.silence_removal_module,
            Animation.animation_module,
            Effects.effect_module,
            Speed.speed_module,
            Opacity.opacity_module,
            Freeze.freeze_module,
            RemoveBg.remove_bg_module,
            Chromakey.chromakey_module,
            Blur.blur_module,
            Reverse.reverse_module,
            Duplicate.duplicate_module]
            Tester.testFuncs(self, funcs, 18, Tester.testFuncsKeyword)

        finally:
            # Pip_duplicate.Pip_duplicate_module(driver, action=clipVideo_inst.clipVideo)
            ClipReplace.replace_module(self)
            Tester.wait_tap(driver, 3, Idcomp.move_next_clip, ">l 선택")

    def clip_blank_all(self):
        driver = self.driver
        Tester.add_clip(driver, "빈 장면", None)
        try:
            funcs = [
            Background.background_Module,
            ClipTime.time_module,
            Duplicate.duplicate_module]
            Tester.testFuncs(self, funcs, 3, Tester.testFuncsKeyword)
        finally:
            ClipReplace.replace_module(self)
            Tester.tap(driver, Idcomp.move_next_clip, ">l 선택")

    def clip_gif_all(self):
        Clip.clip_gif(self)
        Clip.clip_gif_test(self)
    def clip_gif(self):
        driver = self.driver
        Tester.add_clip(driver, "GIF", Idcomp.category_gif)
    def clip_gif_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                Layout.layout_module,
                Background.background_Module,
                Animation.animation_module,
                Effects.effect_module,
                Speed.speed_module,
                Opacity.opacity_module,
                Freeze.freeze_module,
                RemoveBg.remove_bg_module,
                Chromakey.chromakey_module,
                Blur.blur_module,
                Reverse.reverse_module,
                Duplicate.duplicate_module]
            Tester.testFuncs(self, funcs, 13, Tester.testFuncsKeyword)
        finally:
            # Pip_duplicate.Pip_duplicate_module(driver, action=clipGif_inst.clipGif)
            ClipReplace.replace_module(self)
            Tester.tap(driver, Idcomp.move_next_clip, ">l 선택")

    def clip_image_all(self):
        Clip.clip_image(self)
        Clip.clip_image_test(self)
    def clip_image(self):
        driver = self.driver
        Tester.add_clip(driver, "사진", Idcomp.category_photo)
    def clip_image_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                Layout.layout_module,
                Background.background_Module,
                Animation.animation_module,
                Effects.effect_module,
                ClipTime.time_module,
                Opacity.opacity_module,
                RemoveBg.remove_bg_module,
                Chromakey.chromakey_module,
                Blur.blur_module,
                Duplicate.duplicate_module]
            Tester.testFuncs(self, funcs, 11, Tester.testFuncsKeyword)
        finally:
            # Pip_duplicate.Pip_duplicate_module(driver, action=clipImage_inst.clipImage)
            ClipReplace.replace_module(self)
            Tester.tap(driver, Idcomp.move_next_clip, ">l 선택")

# 오디오
class Audio:
    def __init__(self, driver):
        self.driver = driver

    def audio_all(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.bottom_audio, "하단 오디오 선택")
        funcs = [Audio.bgm_all, Audio.sound_effect_all, Audio.voice_over_all]
        Tester.testFuncs(self, funcs, 3, Tester.testFuncsKeyword)

    def bgm_all(self):
        Audio.add_bgm(self)
        Audio.bgm_test(self)
    def add_bgm(self):
        driver = self.driver
        try:
            Tester.long_press(driver, Idcomp.move_pre_clip, 2000)
            Tester.tap(driver, Idcomp.add_bgm_button, "BGM 추가")
            for i in range(0,2):
                Tester.tap(driver, Idcomp.fold, None)
            print("폴드 내리기, 올리기 확인")
            Tester.tap(driver, Idcomp.category_Search, "검색 선택")
            Tester.text_input(driver, Idcomp.search_searchbar, "drive")
            Tester.tap(driver, Idcomp.icon_back, "뒤로가기")
            print("bgm 카테고리")
            bgm_category = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_iTunes,
                    Idcomp.category_Files, Idcomp.category_All, *Idcomp.bgm_category]
            Tester.category_check(driver, bgm_category)
            Tester.time(driver, 2)
            Tester.bookMarkCheck(driver, Idcomp.category_Bookmark, Idcomp.content1, Idcomp.content1, Idcomp.category_New, "배경음악")
            Tester.tap(driver, Idcomp.category_New, "신규 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content1, "1번 콘텐츠 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content1, "1번 콘텐츠 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.play, "재생")
            Tester.time(driver, 3)
            Tester.tap(driver, Idcomp.play, "정지")
            Tester.tap(driver, Idcomp.bookmark_button, "북마크 지정")
            Tester.tap(driver, Idcomp.bookmark_button, "북마크 해제")
            Tester.tap(driver, Idcomp.popup_none, "삭제")
            Tester.tap(driver, Idcomp.popup_done, None)
            Tester.long_press_drag(driver, Idcomp.start_time, Idcomp.end_time, 1000)
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.start_time, Idcomp.add_cancel, 1000)
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.end_time, Idcomp.start_time, 1000)
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.end_time, Idcomp.content_add_done, 1000)
            Tester.tap(driver, Idcomp.add_tag_button, "하단 추가 선택")
            Tester.text_input(driver, Idcomp.file_text_field, "Appium")
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 3, Idcomp.add_tag_0, "+ 버튼 선택")
            Tester.tap(driver, Idcomp.tag_delete_button, "태그 삭제")
            Tester.tap(driver, Idcomp.content_add_done, "완료")

        except Exception as e:
            pass
            print("Bgm 추가 중 문제 발생", e)
    def bgm_test(self):
        try:
            funcs = [
            Mute.mute_module,
            Volume.volume_module,
            Fade.fade_module,
            AudioEffect.audio_effect_module,
            EchoReverb.echo_reverb_module,
            Equalizer.equalizer_module,
            Speed.speed_module,
            MoveToHere.move_to_here_module,
            Duplicate.duplicate_module]
            Tester.testFuncs(self, funcs, 9, Tester.testFuncsKeyword)
        finally:
            ClipReplace.deco_replace_action(self)

    def sound_effect_all(self):
        Audio.add_sound_effect(self)
        Audio.sound_effect_test(self)

    def add_sound_effect(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.sound_effect_button, "효과음 추가")
        for i in range(0, 2):
            Tester.tap(driver, Idcomp.fold, None)
        print("폴드 내리기, 올리기 확인")
        Tester.tap(driver, Idcomp.category_Search, "검색 선택")
        Tester.tap(driver, Idcomp.icon_back, "뒤로가기")
        print("효과음 카테고리")
        soundEffect_category = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_Files, Idcomp.category_All, *Idcomp.soundEffect_category]
        Tester.category_check(driver, soundEffect_category)
        Tester.bookMarkCheck(driver, Idcomp.category_Bookmark, Idcomp.content1, Idcomp.content1, Idcomp.category_New, "효과음")
        Tester.tap(driver, Idcomp.category_New, "신규 선택")
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.content1, "1번 콘텐츠 선택")
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.content1, "1번 콘텐츠 선택")
        try:
            Tester.tap(driver, Idcomp.play, "재생")
            Tester.time(driver, 3)
            Tester.tap(driver, Idcomp.play, "정지")
            Tester.tap(driver, Idcomp.bookmark_button, "북마크 지정")
            Tester.tap(driver, Idcomp.bookmark_button, "북마크 해제")
            Tester.tap(driver, Idcomp.popup_none, "삭제")
            Tester.tap(driver, Idcomp.popup_done, None)
            Tester.long_press_drag(driver, Idcomp.start_time, Idcomp.end_time, 1000)
            Tester.long_press_drag(driver, Idcomp.start_time, Idcomp.add_cancel, 1000)
            Tester.time(driver, 3)
            Tester.long_press_drag(driver, Idcomp.end_time, Idcomp.start_time, 1000)
            Tester.long_press_drag(driver, Idcomp.end_time, Idcomp.content_add_done, 1000)
            Tester.tap(driver, Idcomp.add_tag_button, "하단 추가 선택")
            Tester.time(driver, 2)
            Tester.text_input(driver, Idcomp.file_text_field, "Appium")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.add_tag_0, "+ 버튼 선택")
            Tester.tap(driver, Idcomp.tag_delete_button, "태그 삭제")
            Tester.tap(driver, Idcomp.content_add_done, "완료")

        except Exception as e:
            pass
            print("효과음 추가 중 문제 발생", e)

    def sound_effect_test(self):
        try:
            funcs = [
            Mute.mute_module,
            Volume.volume_module,
            Fade.fade_module,
            AudioEffect.audio_effect_module,
            EchoReverb.echo_reverb_module,
            Equalizer.equalizer_module,
            Speed.speed_module,
            MoveToHere.move_to_here_module,
            Duplicate.duplicate_module]
            Tester.testFuncs(self, funcs, 9, Tester.testFuncsKeyword)
        finally:
            ClipReplace.deco_replace_action(self)

    def voice_over_all(self):
        Audio.voice_over(self)
        Audio.voice_over_test(self)
    def voice_over(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_button, "음성 녹음 버튼 선택")
            Tester.wait_tap(driver, 3, Idcomp.voice_recording, "음성 녹음 진행")
            Tester.time(driver, 5)
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_stop, "음성 녹음 정지")
            Tester.wait_tap(driver, 4, Idcomp.file_name, "파일명 선택")
            Tester.text_input(driver, Idcomp.input_title, "appium test")
            Tester.wait_tap(driver, 3, Idcomp.input_title_done_button, "완료 선택")
            Tester.wait_tap(driver, 3, Idcomp.delete, "삭제 선택")
            Tester.wait_tap(driver, 3, Idcomp.voice_recording, "음성 녹음 진행")
            Tester.time(driver, 5)
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_stop, "음성 녹음 정지")
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_play, "재생")
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_pause, "정지")
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_replay, "다시 듣기")
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_pause, "정지")
            Tester.wait_tap(driver, 3, Idcomp.move_next_clip, ">l 버튼 선택")
            Tester.wait_tap(driver, 3, Idcomp.voice_recording_move_here, "여기로 이동")
            Tester.wait_tap(driver, 3, Idcomp.file_name, "파일명 선택")
            Tester.text_input(driver, Idcomp.input_title, "appium test")
            Tester.wait_tap(driver, 3, Idcomp.input_title_done_button, "완료 선택")
            Tester.wait_tap(driver, 3, Idcomp.voice_add_done, "완료 선택")
        except Exception as e:
            name = "voice_over"
            Tester.screenshot(driver, name)
            Tester.wait_tap(driver, 3, Idcomp.voice_add_done, "완료 선택")
            print("음성 녹음 추가 과정 문제 발생", e)
    def voice_over_test(self):
        driver = self.driver
        try:
            funcs = [
            Mute.mute_module,
            Volume.volume_module,
            Fade.fade_module,
            AudioEffect.audio_effect_module,
            EchoReverb.echo_reverb_module,
            Speed.speed_module,
            MoveToHere.move_to_here_module,
            Duplicate.duplicate_module]
            Tester.testFuncs(self, funcs, 8, Tester.testFuncsKeyword)
        finally:
            FileNameChange.file_name_change_module(self)
            Tester.tap(driver, Idcomp.edit_done, "완료")

# 그래픽
class Graphics:
    def __init__(self, driver):
        self.driver = driver

    def graphics_all(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.bottom_graphic, "하단 그래픽 선택")
        funcs = [Graphics.sticker_all, Graphics.frame_all, Graphics.template_all, Graphics.shape_drawing_all]
        Tester.testFuncs(self, funcs, 4, Tester.testFuncsKeyword)

    def sticker_all(self):
        Graphics.add_sticker(self)
        Graphics.sticker_test(self)
    def add_sticker(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.add_sticker_button, "스티커 선택")
            Tester.tap(driver, Idcomp.giphy_button, "GIPHY 선택")
            Graphics.giphy_popup(self)
            Tester.tap(driver, Idcomp.giphy_license_button, "GIPHY 저작권 선택")
            Tester.wait_tap(driver, 2, Idcomp.faq_close, "닫기 선택")
            Tester.wait_tap(driver, 2, Idcomp.popup_close, "닫기 선택")
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 2, Idcomp.giphy_bookmark_button, "GIPHY 북마크 선택")
            Tester.wait_tap(driver, 2, Idcomp.giphy_recents_button, "GIPHY 최근 사용 선택")
            Tester.wait_tap(driver, 2, Idcomp.giphy_trending_button, "GIPHY 홈 선택")
            Tester.tap(driver, Idcomp.giphy_search_button, "GIPHY 검색 선택")
            Tester.wait_tap(driver, 2, Idcomp.giphy_search_back_button, "뒤로 가기")
            Tester.wait_tap(driver, 3, Idcomp.content_add_done, "완료 선택")

            Tester.tap(driver, Idcomp.add_sticker_button, "스티커 선택")
            Tester.tap(driver, Idcomp.vllo_button, "블로탭 선택")
            print("스티커 카테고리")
            sticker_category = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_All, *Idcomp.sticker_category ]
            Tester.category_check(driver, sticker_category)
            Tester.bookMarkCheck(driver, Idcomp.category_Bookmark, Idcomp.content1, Idcomp.content1, Idcomp.category_New, "스티커")
            Tester.tap(driver, Idcomp.category_New, "New 선택")
            Tester.tap(driver, Idcomp.content1, "1번 선택")
            Tester.tap(driver, Idcomp.content2, "2번 선택")
            Tester.tap(driver, Idcomp.content3, "3번 선택")
            Tester.tap(driver, Idcomp.content4, "4번 선택")
            Tester.tap(driver, Idcomp.content5, "5번 선택")
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
        except Exception as e:
            pass
            name = "add_sticker"
            Tester.screenshot(driver, name)
            print("스티커 추가 중 문제 발생", e)
    def giphy_popup(self):
        driver = self.driver
        try:
            giphy_popup = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.copyright_check)
            if giphy_popup:
                Tester.wait_tap(driver, 3, Idcomp.copyright_check, name="저작원 확인 팝업 선택")
            elif not giphy_popup:
                pass
        except Exception as e:
            name = "giphy_popup"
            Tester.screenshot(driver, name)
            print("giphy 팝업 체크 실패", e)
            pass
    def sticker_test(self):
        try:
            funcs = [
            Resize.resize_module,
            Background.deco_color,
            Opacity.opacity_module,
            Animation.animation_module,
            Effects.effect_module,
            Speed.speed_module,
            PauseMotion.pause_motion_module,
            Tracking.tracking_module,
            Arrange.arrange_module,
            Blend.blend_module,
            MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 11, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.deco_replace_action(self)

    def frame_all(self):
        Graphics.add_frame(self)
        Graphics.frame_test(self)
    def add_frame(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.add_frame_button, "프레임 선택")
        print("프레임 카테고리")
        frame_category = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_All,
                            *Idcomp.frame_category]
        Tester.category_check(driver, frame_category)
        Tester.bookMarkCheck(driver, Idcomp.category_Bookmark, Idcomp.content1, Idcomp.content1, Idcomp.category_New, "프레임")
        Tester.tap(driver, Idcomp.category_New, "New탭 선택")
        Tester.time(driver, 2)
        for i in range(0, 4):
            Tester.wait_tap(driver, 2, Idcomp.content1, None)
            Tester.time(driver, 2)
        print("1번 항목 추가 완료")
        Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
    def frame_test(self):
        try:
            funcs = [
            Resize.resize_module,
            Background.deco_color,
            Opacity.opacity_module,
            Animation.animation_module,
            Effects.effect_module,
            Speed.speed_module,
            PauseMotion.pause_motion_module,
            Arrange.arrange_module,
            Blend.blend_module,
            MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 10, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.deco_replace_action(self)

    def template_all(self):
        Graphics.add_template(self)
        Graphics.template_test(self)
    def add_template(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.add_template_button, "템플릿 선택")
        print("템플릿 카테고리")
        template_category = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_All,
                          *Idcomp.template_category]
        Tester.category_check(driver, template_category)
        Tester.bookMarkCheck(driver, Idcomp.category_Bookmark, Idcomp.content1, Idcomp.content1, Idcomp.category_New, "템플릿")
        Tester.tap(driver, Idcomp.category_New, "New탭 선택")
        Tester.time(driver, 2)
        for i in range(0, 4):
            Tester.wait_tap(driver, 3, Idcomp.content1, None)
            Tester.time(driver, 2)
        print("1번 항목 추가 완료")
        Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
    def template_test(self):
        try:
            funcs = [
                Resize.resize_module,
                Background.deco_color,
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                Speed.speed_module,
                PauseMotion.pause_motion_module,
                Arrange.arrange_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 10, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.deco_replace_action(self)

    def shape_drawing_all(self):
        Graphics.add_drawing(self)
        Graphics.drawing_test(self)
        Graphics.add_line(self)
        Graphics.line_test(self)
        Graphics.add_shape(self)
        Graphics.shape_test(self)
    def add_drawing(self):
        driver = self.driver
        shape_drawing_list = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_All,
                              Idcomp.category_pkg_shape_drawing_line, *Idcomp.category_pkg_shape_shape]
        try:
            Tester.tap(driver, Idcomp.add_shape_button, "도형 선택")
            Tester.category_check(driver, shape_drawing_list)
            Tester.bookMarkCheck(driver, Idcomp.category_Bookmark, Idcomp.content1, Idcomp.content1, Idcomp.category_All, "도형")
            Tester.tap(driver, Idcomp.category_All, "전체 선택")
            for i in range(0, 2):
                Tester.tap(driver, Idcomp.fold, None)
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content1, "그리기 선택")
            Tester.wait_tap(driver, 2, Idcomp.palette_tool_pen, "펜 선택")
            # 별 그리기
            self.driver.swipe(195, 308, 133, 501, 500)
            self.driver.swipe(133, 501, 296, 379, 500)
            self.driver.swipe(296, 379, 99, 378, 500)
            self.driver.swipe(99, 378, 265, 496, 500)
            self.driver.swipe(265, 496, 195, 308, 500)
            driver.find_element(MobileBy.NAME,Idcomp.done1).click()

        except Exception as e:
            name = "add_drawing"
            Tester.screenshot(driver, name)
            print("도형 추가 중 문제 발생", e)
    def drawing_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                Arrange.arrange_module,
                Tracking.tracking_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 8, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            Tester.tap(driver, Idcomp.edit_done, "완료")

    def add_line(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.add_shape_button, "도형 선택")
            Tester.tap(driver, Idcomp.content2, "선 선택")
            Tester.tap(driver, Idcomp.content_add_done, "완료")
        except Exception as e:
            name = "add_line"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.content_add_done, "완료")
            print("선 추가 중 문제 발생", e)
    def line_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                # 테두리
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                Arrange.arrange_module,
                Tracking.tracking_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 8, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            Tester.tap(driver, Idcomp.edit_done, "완료")

    def add_shape(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 3, Idcomp.add_shape_button, "도형 선택")
            Tester.tap(driver, Idcomp.content01, "도형 선택")
            Tester.tap(driver, Idcomp.content_add_done, "완료")
        except Exception as e:
            name = "add_shape"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.content_add_done, "완료")
            print("도형 추가 중 문제 발생", e)
    def shape_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                # 채움
                # 테두리
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                Arrange.arrange_module,
                Tracking.tracking_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 8, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            Tester.tap(driver, Idcomp.edit_done, "완료")

# 글자
class Text:
    def __init__(self, driver):
        self.driver = driver
    def text_test_all(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.bottom_text, "하단 글자 선택")
        funcs = [Text.text_all, Text.label_all, Text.caption_all]
        Tester.testFuncs(self, funcs, 3, Tester.testFuncsKeyword)

    def text_all(self):
        Text.add_text(self)
        Text.text_test(self)
    def add_text(self):
        driver = self.driver
        text_list = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_All,
                     *Idcomp.text_category]
        try:
            Tester.tap(driver, Idcomp.add_text_button, "글자 선택")
            for i in range(0, 2):
                Tester.tap(driver, Idcomp.fold, None)
            Tester.category_check(driver, text_list)
            Tester.tap(driver, Idcomp.text_category1, "기본 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content1, "글자 선택")
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
        except Exception as e:
            name = "add_text"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
            print("글자 추가 중 문제 발생", e)
    def text_test(self):
        try:
            funcs = [
                Resize.resize_module,
                TextEdit.text_edit_module,
                Font.font_module,
                TextSize.text_size_module,
                TextFormat.text_format_module,
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                Tracking.tracking_module,
                Arrange.arrange_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 9, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.deco_replace_action(self)

    def label_all(self):
        Text.add_label(self)
        Text.label_test(self)
    def add_label(self):
        driver = self.driver
        label_list = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_All,
                     *Idcomp.label_category]
        try:
            Tester.tap(driver, Idcomp.add_label_button, "라벨 선택")
            for i in range(0, 2):
                Tester.tap(driver, Idcomp.fold, None)
            Tester.category_check(driver, label_list)
            Tester.wait_tap(driver, 3, Idcomp.label_category1, "노트 선택")
            Tester.wait_tap(driver, 3, Idcomp.content1, "라벨 선택")
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
        except Exception as e:
            name = "add_label"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
            print("라벨 추가 중 문제 발생", e)
    def label_test(self):
        try:
            funcs = [
                Resize.resize_module,
                TextEdit.text_edit_module,
                # 폰트
                Background.deco_color,
                Background.deco_label_color,
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                Speed.speed_module,
                PauseMotion.pause_motion_module,
                Tracking.tracking_module,
                Arrange.arrange_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 12, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.deco_replace_action(self)

    def caption_all(self):
        Text.add_caption(self)
        Text.caption_test(self)
    def add_caption(self):
        driver = self.driver
        caption_list = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_New, Idcomp.category_All,
                      *Idcomp.caption_category]
        try:
            Tester.tap(driver, Idcomp.add_caption_button, "자막 선택")
            for i in range(0, 2):
                Tester.tap(driver, Idcomp.fold, None)
            Tester.category_check(driver, caption_list)
            Tester.tap(driver, Idcomp.caption_category1, "기본 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content1, "자막 선택")
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
        except Exception as e:
            name = "add_caption"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")
            print("자막 추가 중 문제 발생", e)
    def caption_test(self):
        try:
            funcs = [
                Resize.resize_module,
                TextEdit.text_edit_module,
                # 폰트
                TextSize.text_size_module,
                Background.deco_color,
                Background.deco_label_color,
                Opacity.opacity_module,
                Animation.animation_module,
                Speed.speed_module,
                PauseMotion.pause_motion_module,
                Arrange.arrange_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 11, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.deco_replace_action(self)

# PIP
class Pip:
    def __init__(self, driver):
        self.driver = driver
    def pip_all(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.bottom_pip, "하단 pip 선택")
        funcs = [Pip.pip_image_all, Pip.pip_gif_all, Pip.pip_video_all]
        Tester.testFuncs(self, funcs, 3, Tester.testFuncsKeyword)

    def pip_image_all(self):
        Pip.add_pip_image(self)
        Pip.pip_image_test(self)
    def add_pip_image(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.pip_image, "PIP 이미지 선택")
            Tester.tap(driver, Idcomp.album, "앨범 선택 (열기)")
            Tester.tap(driver, Idcomp.Appium, "appium 앨범 선택")
            Tester.tap(driver, Idcomp.asset1, "1번 이미지 선택")
        except Exception as e:
            name = "add_pip_image"
            Tester.screenshot(self, name)
            print("%s 추가 중 문제 발생" % name, e)
    def pip_image_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                RemoveBg.remove_bg_module,
                Chromakey.chromakey_module,
                Tracking.tracking_module,
                Arrange.arrange_module,
                Blend.blend_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 10, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.replace_module(self)
            Tester.wait_tap(driver, 2, Idcomp.edit_done, "완료 선택")

    def pip_gif_all(self):
        Pip.add_pip_gif(self)
        Pip.pip_gif_test(self)
    def add_pip_gif(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 3, Idcomp.pip_gif, "PIP GIF 선택")
            Tester.tap(driver, Idcomp.album, "앨범 선택 (열기)")
            Tester.tap(driver, Idcomp.Appium, "appium 앨범 선택")
            Tester.tap(driver, Idcomp.asset1, "1번 이미지 선택")
        except Exception as e:
            name = "add_pip_gif"
            Tester.screenshot(self, name)
            print("%s 추가 중 문제 발생" % name, e)
    def pip_gif_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                RemoveBg.remove_bg_module,
                Chromakey.chromakey_module,
                Speed.speed_module,
                # Freeze.freeze_module,
                Tracking.tracking_module,
                Arrange.arrange_module,
                Blend.blend_module,
                Reverse.reverse_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 13, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.replace_module(self)
            Tester.wait_tap(driver, 2, Idcomp.edit_done, "완료 선택")

    def pip_video_all(self):
        Pip.add_pip_video(self)
        Pip.pip_vdieo_test(self)
    def add_pip_video(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 3, Idcomp.pip_video, "PIP 비디오 선택")
            Tester.tap(driver, Idcomp.album, "앨범 선택 (열기)")
            Tester.tap(driver, Idcomp.Appium, "appium 앨범 선택")
            Tester.tap(driver, Idcomp.asset1, "1번 이미지 선택")
        except Exception as e:
            name = "add_pip_video"
            Tester.screenshot(self, name)
            print("%s 추가 중 문제 발생" % name, e)
    def pip_vdieo_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                Mute.mute_module,
                Volume.volume_module,
                Fade.fade_module,
                AudioEffect.audio_effect_module,
                EchoReverb.echo_reverb_module,
                # audioDetach.audio_detach_action,
                Opacity.opacity_module,
                Animation.animation_module,
                Effects.effect_module,
                RemoveBg.remove_bg_module,
                Chromakey.chromakey_module,
                Speed.speed_module,
                # Freeze.freeze_module,
                Tracking.tracking_module,
                Arrange.arrange_module,
                Blend.blend_module,
                Reverse.reverse_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 18, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            ClipReplace.replace_module(self)
            Tester.wait_tap(driver, 2, Idcomp.edit_done, "완료 선택")

# 효과
class Effect:
    def __init__(self, driver):
        self.driver = driver

    def effect_all(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.bottom_effect, "효과 진입")
        Effect.add_filter(self)
        Effect.filter_test(self)
        Effect.add_adjustment(self)
        Effect.adjustment_test(self)
        Effect.add_effect(self)
        Effect.effect_test(self)
        Effect.add_distortion(self)
        Effect.distortion_test(self)

    def add_filter(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.add_filter_button, "필터 진입")
        filter_category = [Idcomp.category_Bookmark, Idcomp.category_Recents, *Idcomp.filter_category]
        Tester.category_check(driver, filter_category)
        Tester.tap(driver, Idcomp.filter_category1, "카테고리1 선택")
        Tester.tap(driver, Idcomp.content03, "Travel 1선택")
        Tester.time(driver, 3)
        Tester.long_press_drag(driver, Idcomp.add_filter_strength_ruler, Idcomp.edit_play, 2000)
        Tester.wait_tap(driver, 5, Idcomp.strength_ruler_reset, "강도 초기화")
        Tester.decoBookMarkCheck(driver, Idcomp.content03, Idcomp.filter_category1, "효과")
        Tester.tap(driver, Idcomp.filter_category1, "카테고리1 선택")
        Tester.tap(driver, Idcomp.content03, "Travel 1선택")
        Tester.wait_tap(driver, 5, Idcomp.content_add_done, "완료")

    def filter_test(self):
        driver = self.driver
        try:
            funcs = [
                TextIntensity.text_intensity_module,
                Arrange.arrange_module,
                MoveToHere.move_to_here_module,
            ]
            Tester.testFuncs(self, funcs, 2, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            Tester.tap(driver, Idcomp.edit_done, "완료")

    def add_adjustment(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.add_filter_button, "필터 진입")
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.adjustment, "보정 진입")

    def adjustment_test(self):
        driver = self.driver
        try:
            funcs = [
                # 보정
                Arrange.arrange_module,
                MoveToHere.move_to_here_module
            ]
            Tester.testFuncs(self, funcs, 2, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            # 내 필터
            Tester.tap(driver, Idcomp.edit_done, "완료")

    def add_effect(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.add_effect_button, "이펙트 선택")
        effectCategory = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_All, *Idcomp.effect_category]
        Tester.category_check(driver, effectCategory)
        Tester.tap(driver, Idcomp.category_All, "전체 선택")
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.content1, "1번 콘텐츠 선택")
        Tester.tap(driver, Idcomp.content_add_done, "완료")

    def effect_test(self):
        driver = self.driver
        try:
            funcs = [
                TextIntensity.text_intensity_module,
                Arrange.arrange_module,
                MoveToHere.move_to_here_module
            ]
            Tester.testFuncs(self, funcs, 2, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            Tester.tap(driver, Idcomp.edit_done, "완료")

    def add_distortion(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.add_distort_button, "왜곡 선택")
        chosen_category = random.choice(Idcomp.distort_category)
        Tester.tap(driver, chosen_category, "랜덤 항목 선택")
        rectangle = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value="사각형")
        try:
            if rectangle:
                print("상단 형태 지정이 있는 항목")
                Tester.tap(driver, Idcomp.rectangle, "사각형 선택")
                Tester.time(driver, 2)
                Tester.long_press_drag(driver, Idcomp.distort_intensity_ruler, Idcomp.edit_play, 2000)
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.intensity_ruler_reset, "초기화 선택")
                Tester.tap(driver, Idcomp.oval, "원 선택")
                Tester.long_press_drag(driver, Idcomp.distort_intensity_ruler, Idcomp.edit_play, 2000)
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.intensity_ruler_reset, "초기화 선택")

            elif not rectangle:
                print("상단 형태 지정이 없는 항목")
                Tester.time(driver, 2)
                Tester.long_press_drag(driver, Idcomp.distort_intensity_ruler, Idcomp.edit_play, 2000)
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.intensity_ruler_reset, "초기화 선택")
        finally:
            Tester.tap(driver, Idcomp.content_add_done, "완료 선택")

    def distortion_test(self):
        driver = self.driver
        try:
            funcs = [
                Resize.resize_module,
                # 도형
                Tracking.tracking_module,
                TextIntensity.text_intensity_module,
                # 페더
                # 반전
                Arrange.arrange_module,
                MoveToHere.move_to_here_module
            ]
            Tester.testFuncs(self, funcs, 4, Tester.testFuncsKeyword)
        finally:
            Duplicate.duplicate_module(self)
            Tester.tap(driver, Idcomp.edit_done, "완료")

# 추출
class Export:
    def __init__(self, driver):
        self.driver = driver

    def export_all(self):
        driver = self.driver
        Export.enter_export(self)
        Export.export_option(self)
        Export.export_resolution_video(self)
        Export.export_fps_video(self)
        Export.export_codec_alram(self)
        Tester.tap(driver, Idcomp.export_button, "추출하기")
        Tester.wait_tap(driver, 1000000, Idcomp.share_icon_done_line, "추출 완료")
        Tester.tap(driver, Idcomp.share_top_icon_home, "메인으로 이동")
        print("자동화 테스트 완료")
    def enter_export(self):
        driver = self.driver
        Tester.wait_tap(driver, 3, Idcomp.top_icon_export, "추출하기 선택")

    def export_option(self):
        driver = self.driver
        Tester.wait_tap(driver, 3, Idcomp.video2, "비디오 선택")
        Tester.category_check(driver, Idcomp.export_category)
        Tester.tap(driver, Idcomp.video, "비디오 선택")

    def export_resolution_video(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.resolution, "해상도 선택")
        Tester.category_check(driver, Idcomp.resolution_category)
        Tester.tap(driver, Idcomp.resolution_high, "고화질 선택")
        Tester.tap(driver, Idcomp.resolution, "해상도 선택")

    def export_fps_video(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.framerate, "프레임레이트 선택")
        Tester.category_check(driver, Idcomp.framerate_category)
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.framerate4, "30프레임 선택")
        Tester.tap(driver, Idcomp.framerate, "프레임레이트 선택")

    def export_codec_alram(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.iButton1, "코덱 추가 정보 선택")
        Tester.tap(driver, Idcomp.popup_close, "닫기 선택")
        Tester.tap(driver, Idcomp.h264, "H.264 선택")
        Tester.tap(driver, Idcomp.h265, "H.265 선택")
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.iButton2, "알람 추가 정보 선택")
        Tester.tap(driver, Idcomp.popup_close, "닫기 선택")
        Tester.tap(driver, Idcomp.alarm_on, "알람 on 선택")
        Tester.tap(driver, Idcomp.alarm_off, "알람 off 선택")
        Tester.tap(driver, Idcomp.alarm_on, "알람 on 선택")

# 시간
class ClipTime:

    def __init__(self, driver):
        self.driver = driver

    def time_module(self):
        driver = self.driver
        name = "시간"
        Accessibility_Id_1 = Idcomp.clip_menu_duration
        duration_inst = ClipTime(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify(driver, name, Accessibility_Id_1, done_id,
                                action=duration_inst.time_action)

        except Exception as e:
            Tester.screenshot(driver, name)
            print("%s 없는 항목" % name, e)

    def time_action(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.move_next_frame, "l> 선택")
            Tester.tap(driver, Idcomp.move_pre_clip, "l< 선택")
            Tester.category_check(driver, Idcomp.deco_duration_list)
            Tester.time(driver, 1)
            Tester.tap(driver, Idcomp.duration_ruler_reset, "초기화 선택")
            Tester.long_press_drag(driver, Idcomp.edit_duration_ruler, Idcomp.edit_play, 100)
            print("시간 롱프레스 후 드래그")
            Tester.time(driver, 1)
            Tester.tap(driver, Idcomp.duration_ruler_reset, "초기화 선택")
            # # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기 완료")
            Tester.time(driver, 2)
        except Exception as e:
            name = "time_action"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("시간 동작 중 문제 발생", e)

# 변형
class Resize:
    def __init__(self, driver):
        self.driver = driver

    def resize_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 변형"
        name2 = "데코 변형"
        name = "변형"
        Accessibility_Id_1 = Idcomp.clip_menu_resize
        Accessibility_Id_2 = Idcomp.deco_menu_resize
        resize_inst = Resize(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=resize_inst.resize_action)

        except Exception as e:
            name = "resize_action"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    # 크기 변경 액션
    def resize_action(self):
        driver = self.driver
        try:
            Position = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.menu_position)
            Size = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.menu_size)
            Rotation = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.menu_rotation)
            Flip = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.menu_flip)
            Crop = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.menu_crop)

            # 모든 아이디 항목이 존재하는 경우
            if Position and Size and Rotation and Flip and Crop:
                print("5개 항목 다 있는 크기 변경")
                # 아래 코드 실행
                Resize.resize_position(self)
                Resize.resize_size(self)
                Resize.resize_rotation(self)
                Resize.resize_flip(self)
                Resize.resize_crop(self)
                # clipResize1 = [resize_position, resizeSize, resizeRotation, resizeFlip, resizeCrop]
                print("5개의 항목 확인 완료")

            elif not Crop:
                print("반전, 크롭이 없는 크기 변경 (왜곡)")
                Resize.resize_position(self)
                Resize.resize_size(self)
                Resize.resize_rotation(self)
                # clipResize2 = [resize_position, resizeSize, resizeRotation]


            elif not Flip:
                print("반전이 없는 크기 변경 (글자)")
                Resize.resize_position(self)
                Resize.resize_size(self)
                Resize.resize_rotation(self)
                Resize.resize_crop(self)
                # clipResize3 = [resize_position, resizeSize, resizeRotation, resizeCrop]

        except Exception as e:
            name = "resize_action"
            Tester.screenshot(self, name)
            print("크기 조절 > 위치 동작 중 문제 발생", e)

    # 위치
    def resize_position(self):
        driver = self.driver

        Tester.time(driver, 2)

        try:
            Tester.tap(driver, Idcomp.menu_position, "위치 선택")
            KeyFrame.keyFrame_module(self)
            x_ruler_reset = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.transform_x_ruler_reset)
            y_ruler_reset = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.transform_y_ruler_reset)
            print("위치 진입 시 초기화 버튼이 활성화 되어있는지 판별")
            if x_ruler_reset:
                print("x 룰러 초기화 활성화된 상태임")
                x_ruler_reset[0].is_displayed()
                Tester.tap(driver, Idcomp.transform_x_ruler_reset, "x 룰러 초기화 선택")
                Tester.time(driver, 1)
                Tester.long_press_drag(driver, Idcomp.edit_x_ruler, Idcomp.edit_play, 100)
                print("x 룰러 조절")
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.transform_x_ruler_reset, "x 룰러 초기화 선택")
            else:
                print("x 룰러 비활성화된 상태임")
                Tester.long_press_drag(driver, Idcomp.edit_x_ruler, Idcomp.edit_play, 100)
                print("x 룰러 조절")
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.transform_x_ruler_reset, "x 룰러 초기화 선택")

            if y_ruler_reset:
                print("y 룰러 초기화 활성화된 상태임")
                y_ruler_reset[0].is_displayed()
                Tester.tap(driver, Idcomp.transform_y_ruler_reset, "y 룰러 초기화 선택")
                Tester.time(driver, 1)
                Tester.long_press_drag(driver, Idcomp.edit_y_ruler, Idcomp.edit_play, 100)
                print("y 룰러 조절")
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.transform_y_ruler_reset, "y 룰러 초기화 선택")
            else:
                print("y 룰러 비활성화된 상태임")
                Tester.long_press_drag(driver, Idcomp.edit_y_ruler, Idcomp.edit_play, 100)
                print("x 룰러 조절")
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.transform_y_ruler_reset, "x 룰러 초기화 선택")
        except Exception as e:
            name = "resize_position"
            Tester.screenshot(self, name)
            print("크기 조절 > 위치 동작 중 문제 발생", e)

    # 크기
    def resize_size(self):
        driver = self.driver

        Tester.time(driver, 2)

        try:
            # 크기 선택
            Tester.tap(driver, Idcomp.menu_size, "크기 선택")
            # 크기 룰러 확인
            size_ruler_reset = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.transform_size_ruler_reset)
            print("크기 진입 시 초기화 버튼이 활성화 되어있는지 판별")
            if size_ruler_reset:
                print("크기 초기화 활성화된 상태임")
                size_ruler_reset[0].is_displayed()
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.transform_size_ruler_reset, "크기 초기화 선택")
                Tester.time(driver, 1)
                Tester.long_press_drag(driver, Idcomp.edit_size_ruler, Idcomp.edit_play, 100)
                print("크기 룰러 조절")
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.transform_size_ruler_reset, "크기 초기화 선택")
            else:
                print("크기 초기화 비활성화된 상태임")
                Tester.long_press_drag(driver, Idcomp.edit_size_ruler, Idcomp.edit_play, 100)
                print("크기 룰러 조절")
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.transform_size_ruler_reset, "크기 룰러 초기화 선택")
        except Exception as e:
            name = "resize_size"
            Tester.screenshot(self, name)
            print("크기 조절 > 크기 동작 중 문제 발생", e)

    # 회전
    def resize_rotation(self):
        driver = self.driver

        Tester.time(driver, 2)

        try:
            # 회전 선택
            Tester.tap(driver, Idcomp.menu_rotation, "회전 선택")

            for i in range (0, 4):
                Tester.wait_tap(driver, 2, Idcomp.plus_45, None)
            print("+45 4번 선택")
            for i in range(0, 4):
                Tester.wait_tap(driver, 2, Idcomp.minus_45, None)
            print("-45 4번 선택")

            # 회전 룰러 확인
            rotation_ruler_reset = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.transform_rotation_ruler_reset)
            print("회전 진입 시 초기화 버튼이 활성화 되어있는지 판별")
            if rotation_ruler_reset:
                print("회전 초기화 활성화된 상태임")
                rotation_ruler_reset[0].is_displayed()
                Tester.tap(driver, Idcomp.transform_rotation_ruler_reset, "회전 초기화 선택")
                Tester.time(driver, 2)
                Tester.long_press_drag(driver, Idcomp.edit_rotation_ruler, Idcomp.edit_play, 500)
                print("회전 룰러 조절")
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.transform_rotation_ruler_reset, "회전 초기화 선택")
            else:
                print("회전 초기화 비활성화된 상태임")
                Tester.long_press_drag(driver, Idcomp.edit_rotation_ruler, Idcomp.edit_play, 500)
                print("회전 룰러 조절")
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.transform_rotation_ruler_reset, "회전 룰러 초기화 선택")
        except Exception as e:
            name = "resize_rotation"
            Tester.screenshot(self, name)
            print("크기 조절 > 회전 동작 중 문제 발생", e)

    # 반전
    def resize_flip(self):
        driver = self.driver

        Tester.time(driver, 2)

        try:
            # 반전 선택
            Tester.tap(driver, Idcomp.menu_flip, "반전 선택")
            # 반전 항목 확인
            upside_down = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.upside_down)
            switch_sides = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.switch_sides)
            print("위치 진입 시 초기화 버튼이 활성화 되어있는지 판별")
            if upside_down:
                print("상하 반전 활성화된 상태임")
                upside_down[0].is_displayed()
                Tester.tap(driver, Idcomp.upside_down, "상하 반전 off 선택")
                Tester.tap(driver, Idcomp.upside_down, "상하 반전 on 선택")
            else:
                print("상하 반전 비활성화된 상태임")
                Tester.tap(driver, Idcomp.upside_down, "상하 반전 on 선택")
                Tester.tap(driver, Idcomp.upside_down, "상하 반전 off 선택")

            if switch_sides:
                print("좌우 반전 활성화된 상태임")
                switch_sides[0].is_displayed()
                Tester.tap(driver, Idcomp.switch_sides, "좌우 반전 off 선택")
                Tester.tap(driver, Idcomp.switch_sides, "좌우 반전 on 선택")
            else:
                print("좌우 반전 비활성화된 상태임")
                Tester.tap(driver, Idcomp.switch_sides, "좌우 반전 on 선택")
                Tester.tap(driver, Idcomp.switch_sides, "좌우 반전 off 선택")
        except Exception as e:
            name = "resize_flip"
            Tester.screenshot(self, name)
            print("크기 조절 > 반전 동작 중 문제 발생", e)

    # 크롭
    def resize_crop(self):
        driver = self.driver
        Tester.time(driver, 2)
        Tester.tap(driver, Idcomp.menu_crop, "크롭 선택")
        try:
            Tester.long_press_with_offset(driver, Idcomp.crop_left, 6000, 10, 2)
            print("왼쪽 롱프레스 6초간 완료")
            Tester.long_press_with_offset(driver, Idcomp.crop_right, 6000, 10, 2)
            print("오른쪽 롱프레스 6초간 완료")
            Tester.long_press_with_offset(driver, Idcomp.crop_top, 6000, 10, 2)
            print("위 롱프레스 6초간 완료")
            Tester.long_press_with_offset(driver, Idcomp.crop_bottom, 6000, 10, 2)
            print("아래 롱프레스 6초간 완료")
            for i in range(0, 4):
                Tester.wait_tap(driver, 2, Idcomp.undo_button, None)
        except Exception as e:
            name = "resize_crop"
            Tester.screenshot(self, name)
            print("크기 조절 > 크롭 동작 중 문제 발생", e)

# 레이아웃
class Layout:

    def __init__(self, driver):
        self.driver = driver

    def layout_module(self):
        driver = self.driver
        # identify_two 정보
        name = "레이아웃"
        Accessibility_Id_1 = Idcomp.clip_menu_layout
        layout_inst = Layout(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify(driver, name, Accessibility_Id_1, done_id,
                                action=layout_inst.layout_action)
        except Exception as e:
            name = "layout"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def layout_action(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.edit_layout_title_button_0, "첫 번째 레이아웃 제목 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.input_title_cancel_button, "X버튼 선택")
            Tester.tap(driver, Idcomp.edit_layout_title_button_0, "첫 번째 레이아웃 제목 선택")
            Tester.text_input(driver, Idcomp.input_title, text="레이아웃 제목 test")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.input_title_done_button, "V버튼 선택")
            Tester.tap(driver, Idcomp.edit_layout_title_button_0, "첫 번째 레이아웃 제목 선택")
            Tester.text_input(driver, Idcomp.input_title, text="Cinematic 1")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.input_title_done_button, "V버튼 선택")
            Tester.tap(driver, Idcomp.copy, "복사 선택")
            Tester.tap(driver, Idcomp.edit_layout_delete_button_0, "delete 선택")

        except Exception as e:
            name = "layout_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("레이아웃 동작 중 문제 발생", e)

# 배경
class Background:
    def __init__(self, driver):
        self.driver = driver

    # 배경 최종
    def background_Module(self):
        driver = self.driver
        Tester.wait_tap(driver, 5, Idcomp.clip_menu_bg, "배경 진입")

        try:
            clip_background = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.bg_blur)
            print("블러가 있는 항목인지 없는 항목인지 판별")
            if clip_background:
                print("블러 있음")
                # 배경 > 블러가 보이는 경우 해당 아래 코드 실행 (비디오, gif)
                clip_background[0].is_displayed()
                # 아래 코드 실행
                Background.color(self, Idcomp.bg_solid_color)
                Background.gradation(self, Idcomp.bg_gradient)
                Background.pattern(self, Idcomp.bg_pattern)
                Background.blur(self)
                Tester.tap(driver, Idcomp.edit_sub_done, "4개의 항목 확인 완료")
            if not clip_background:
                print("블러 없음")
                # 배경 > 블러가 없는 경우 아래 코드 실행 (사진)
                Background.color(self, Idcomp.bg_solid_color)
                Background.gradation(self, Idcomp.bg_gradient)
                Background.pattern(self, Idcomp.bg_pattern)
                Tester.tap(driver, Idcomp.edit_sub_done, "3개의 항목 확인 완료")

        except Exception as e:
            name = "background_Module"
            Tester.screenshot(self, name)
            print("블러 판별 중 문제 발생", e)

    # 사진 배경
    def picture_background(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.clip_menu_bg, "사진 배경 진입")
        # color = Background.color(self)
        # gradation = Background.gradation(self)
        # pattern = Background.pattern(self)

        Background.color(self, Idcomp.bg_solid_color)
        Background.gradation(self, Idcomp.bg_gradient)
        Background.pattern(self, Idcomp.bg_pattern)
        # pictureBackground = [color, gradation, pattern]
        print("color, gradation, pattern 3가지 항목 실행 완료")

    # 배경 > 색상 더 보기
    def color_palette(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.color_more, "색상 더 보기 선택")
            # colorPalette = [palette, picker, slider]
            Background.palette(self)
            Background.picker(self)
            Background.slider(self)
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.color_solid_done, "palette, picker, slider 3가지 항목 실행 완료 후 완료 선택")
        except Exception as e:
            name = "color_palette"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.color_solid_done, None)
            print("배경 > 색상 더 보기 동작 중 문제 발생", e)

    # 색상
    def color(self, el_id):
        driver = self.driver

        try:
            if el_id is not None:
                Tester.wait_tap(driver, 5, el_id, "색상 선택")
            Tester.tap(driver, *Idcomp.color_id[:1], "색상 1번 선택")
            # 랜덤으로 선택된 항목 클릭
            Tester.long_press_drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button, 300)
            print("색상 드래그")
            Tester.time(driver, 2)
            #색상 룰러 초기화
            Tester.tap(driver, Idcomp.color_alpha_ruler_reset, "색상 룰러 초기화 선택")
            Tester.time(driver, 2)
            Background.color_palette(self)

        except Exception as e:
            name = "color"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("색상 동작 중 문제 발생", e)

    # 색상
    def deco_color(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.deco_menu_color, "색상 선택")
            Tester.tap(driver, *Idcomp.color_id[:1], "색상 1번 선택")
            # 랜덤으로 선택된 항목 클릭
            Tester.long_press_drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button, 300)
            print("색상 드래그")
            Tester.time(driver, 2)
            # 색상 룰러 초기화
            Tester.tap(driver, Idcomp.color_alpha_ruler_reset, "색상 룰러 초기화 선택")
            Tester.time(driver, 2)
            Background.color_palette(self)
            Tester.tap(driver, Idcomp.edit_sub_done, "완료")
        except Exception as e:
            name = "deco_color"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("색상 동작 중 문제 발생", e)

    # 색상
    def deco_label_color(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 5, Idcomp.deco_menu_label_color, "글자 색상 선택")
            Tester.tap(driver, *Idcomp.color_id[:1], "색상 1번 선택")
            # 랜덤으로 선택된 항목 클릭
            Tester.long_press_drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button, 300)
            print("색상 드래그")
            Tester.time(driver, 2)
            # 색상 룰러 초기화
            Tester.tap(driver, Idcomp.color_alpha_ruler_reset, "색상 룰러 초기화 선택")
            Tester.time(driver, 2)
            Background.color_palette(self)
            Tester.tap(driver, Idcomp.edit_sub_done, "완료")
        except Exception as e:
            name = "deco_label_color"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("색상 동작 중 문제 발생", e)

    # 스포이드
    def color_spoid(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.recent_color_spoid_button, "우측 스포이드 선택")
        except Exception as e:
            name = "color_spoid"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("스포이드 동작 중 문제 발생", e)

    # 팔레트
    def palette(self):
        driver = self.driver

        try:
            Tester.wait_tap(driver, 5, Idcomp.palette, "팔레트 선택")

            Tester.time(driver, 2)
            # 팔레트 색상 랜덤 클릭
            for i in range(0, 5):
                random_item = random.choice(Idcomp.palette_id1)  # 첫 번째 리스트 중 랜덤으로 하나 선택
                Tester.wait_tap(driver, 3, random_item, None)
                Tester.time(driver, 1)
                random_item = random.choice(Idcomp.palette_id2)  # 두 번째 리스트 중 랜덤으로 하나 선택
                Tester.wait_tap(driver, 3, random_item, None)
            print("팔레트 상,하 랜덤 클릭 완료")
            Tester.time(driver, 2)
        except Exception as e:
            name = "palette"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.color_solid_done, None)
            print("색상 > 팔레트 부분 정상 동작하지 않음", e)

    # 피커
    def picker(self):
        driver = self.driver
        # todo 스포이드 필요함

        try:
            Tester.wait_tap(driver, 5, Idcomp.picker, "피커 선택")
            # 왼쪽 피커 상, 하 조절
            Tester.long_press_drag(driver, Idcomp.picker_hue, Idcomp.edit_play, 250)
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.picker_hue, Idcomp.palette, 250)
            print("왼쪽 피커 상, 하 조절")
            Tester.time(driver, 2)
            # 중앙 피커 조절
            Tester.long_press_drag(driver, Idcomp.picker_saturation, Idcomp.edit_play, 1000)
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.picker_saturation, Idcomp.palette, 1000)
            print("중앙 피커 조절")
            Tester.time(driver, 2)
            # 오른쪽 피커 상, 하 조절
            Tester.long_press_drag(driver, Idcomp.picker_alpha, Idcomp.edit_play, 250)
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.picker_alpha, Idcomp.slider, 250)
            print("오른쪽 피커 상, 하 조절")
            Tester.time(driver, 2)

        except Exception as e:
            name = "picker"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.color_solid_done, None)
            print("색상 > 피커 부분 정상 동작하지 않음", e)

    # 슬라이더
    def slider(self):
        driver = self.driver

        try:
            Tester.wait_tap(driver, 5, Idcomp.slider, "슬라이더 선택")

            red_ruler_reset = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.red_ruler_reset)
            print("초기화 버튼이 있는지 판별")
            if red_ruler_reset:
                print("초기화 버튼 있음")
                red_ruler_reset[0].is_displayed()
                # R 룰러 조절
                Tester.tap(driver, Idcomp.red_ruler_reset, None)
                Tester.time(driver, 1)
                Tester.long_press_drag(driver, Idcomp.slider_red_ruler, Idcomp.R, 1000)
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.red_ruler_reset, None)
                print("R 룰러 조절 후 초기화")
                # G 룰러 조절
                Tester.tap(driver, Idcomp.green_ruler_reset, None)
                Tester.time(driver, 1)
                Tester.long_press_drag(driver, Idcomp.slider_green_ruler, Idcomp.G, 1000)
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.green_ruler_reset, None)
                print("G 룰러 조절 후 초기화")
                # B 룰러 조절
                Tester.tap(driver, Idcomp.blue_ruler_reset, None)
                Tester.time(driver, 1)
                Tester.long_press_drag(driver, Idcomp.slider_blue_ruler, Idcomp.B, 1000)
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.blue_ruler_reset, None)
                print("B 룰러 조절 후 초기화")
                Tester.time(driver, 2)
            else:
                # 없으면 아래 코드 실행
                print("초기화 버튼 없음")
                Tester.tap(driver, Idcomp.slider, None)
                # R 룰러 조절
                Tester.long_press_drag(driver, Idcomp.slider_red_ruler, Idcomp.R, 1000)
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.red_ruler_reset, "R 룰러 조절 후 초기화")
                # G 룰러 조절
                Tester.long_press_drag(driver, Idcomp.slider_green_ruler, Idcomp.G, 1000)
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.green_ruler_reset, "G 룰러 조절 후 초기화")
                # B 룰러 조절
                Tester.long_press_drag(driver, Idcomp.slider_blue_ruler, Idcomp.B, 1000)
                Tester.time(driver, 1)
                Tester.tap(driver, Idcomp.blue_ruler_reset, "B 룰러 조절 후 초기화")
                Tester.time(driver, 2)
        except Exception as e:
            name = "slider"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.color_solid_done, None)
            print("색상 > 슬라이더 부분 정상 동작하지 않음", e)

    # 그라데이션
    def gradation(self, el_id):
        driver = self.driver

        try:
            Tester.tap(driver, el_id, "그라데이션 선택")
            print("그라데이션")
            Tester.category_check(driver, Idcomp.color_id)
            Tester.drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button)
            print("불투명도 수치 조절")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.color_alpha_ruler_reset, "초기화 선택")
            Tester.tap(driver, el_id, "그라데이션 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.color_more, "그라데이션 더보기(+) 선택")
            # 그라데이션 1번 클릭
            a = Idcomp.color_more_id
            for i in range(0, 5):
                random_item = random.choice(a)  # 위 리스트 중 랜덤으로 하나 선택
                Tester.tap(driver, random_item, None)
            print("그라데이션 랜덤 5회 클릭")
            Tester.tap(driver, Idcomp.color_gradient_done, "그라데이션 완료")

        except Exception as e:
            name = "gradation"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.color_gradient_done, None)
            print("색상 > 그라데이션 부분 정상 동작하지 않음", e)

    # 패턴
    def pattern(self, el_id):
        driver = self.driver

        try:
            Tester.tap(driver, el_id, "패턴 선택")
            pattern = Idcomp.color_id
            print("패턴 리스트")
            Tester.category_check(driver, pattern)
            Tester.drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button)
            print("불투명도 수치 조절")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.color_alpha_ruler_reset, "초기화 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, el_id, "패턴 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.color_more, "패턴 더보기(+) 선택")
            # 패턴 1번 클릭
            a = Idcomp.color_more_id
            for i in range(0, 5):
                random_item = random.choice(a)  # 위 리스트 중 랜덤으로 하나 선택
                Tester.tap(driver, random_item, None)
            print("패턴 랜덤 5회 클릭")
            Tester.tap(driver, Idcomp.color_pattern_done, "패턴 완료")

        except Exception as e:
            name = "pattern"
            Tester.screenshot(self, name)
            print("색상 > 패턴 부분 정상 동작하지 않음", e)

    # 블러
    def blur(self):
        driver = self.driver

        try:
            # 블러 선택
            Tester.tap(driver, Idcomp.bg_blur, "블러 선택")
            # 블러 롱프레스 후 드래그
            Tester.long_press_drag(driver, Idcomp.edit_bg_blur_ruler, Idcomp.edit_play, 100)
            print("블러 롱프레스 후 드래그")
            Tester.time(driver, 2)
            # 초기화 선택
            Tester.tap(driver, Idcomp.bg_blur_ruler_reset, "초기화 선택")
        except Exception as e:
            name = "blur"
            Tester.screenshot(self, name)
            print("색상 > 블러 부분 정상 동작하지 않음", e)

# 음소거
class Mute:
    def __init__(self, driver):
        self.driver = driver

    def mute_module(self):
        driver = self.driver
        try:
            clip_menu_mute = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.clip_menu_mute)

            # 모든 아이디 항목이 존재하는 경우
            if clip_menu_mute :
                print("클립 음소거 확인")
                # 아래 코드 실행
                Mute.mute_action_clip(self)

            elif not clip_menu_mute:
                print("데코 음소거 확인")
                Mute.mute_action_deco(self)

        except Exception as e:
            name = "mute_module"
            Tester.screenshot(self, name)
            print("음소거 없는 항목", e)

    def mute_action_clip(self):
        driver = self.driver
        muteBtn = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.clip_menu_mute)
        try:
            if muteBtn.is_enabled():
                print("클립 음소거가 활성화되었습니다")
                for i in range(0, 2):
                    muteBtn.click()
                    if i == 0:
                        print("음소거 off")  # f-string
                    if i == 1:
                        print("음소거 on")
            else:
                Tester.tap(driver, Idcomp.clip_menu_mute, "음소거가 비활성화되었습니다")
        except Exception as e:
            name = "mute_action_clip"
            Tester.screenshot(self, name)
            print("음소거 아이콘 비활성화 상태", e)

    def mute_action_deco(self):
        driver = self.driver
        muteBtn = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.deco_menu_mute)
        try:
            if muteBtn.is_enabled():
                print("데코 음소거가 활성화되었습니다")
                for i in range(0, 2):
                    muteBtn.click()
                    if i == 0:
                        print("음소거 off")  # f-string
                    if i == 1:
                        print("음소거 on")
            else:
                Tester.tap(driver, Idcomp.clip_menu_mute, "음소거가 비활성화되었습니다")
        except Exception as e:
            name = "mute_action_deco"
            Tester.screenshot(self, name)
            print("음소거 아이콘 비활성화 상태", e)

# 음량
class Volume:

    def __init__(self, driver):
        self.driver = driver

    def volume_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 음량"
        name2 = "데코 음량"
        name = "음량"
        Accessibility_Id_1 = Idcomp.clip_menu_volume
        Accessibility_Id_2 = Idcomp.deco_menu_volume
        volume_inst = Volume(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=volume_inst.volume_action)

        except Exception as e:
            name = "volume_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def volume_action(self):
        driver = self.driver
        try:
            KeyFrame.keyFrame_module(self)
            Tester.long_press_drag(driver, Idcomp.ruler_value, Idcomp.dB, 100)
            print("강도 룰러 드래그")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.edit_value_ruler_reset, "초기화 선택")
            # # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기")
        except Exception as e:
            name = "volume_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done,None)
            print("볼륨 동작 중 문제 발생", e)

# 페이드
class Fade:

    def __init__(self, driver):
        self.driver = driver

    def fade_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 페이드"
        name2 = "데코 페이드"
        name = "페이드"
        Accessibility_Id_1 = Idcomp.clip_menu_fade
        Accessibility_Id_2 = Idcomp.deco_menu_fade
        Fade_inst = Fade(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=Fade_inst.fade_action)

        except Exception as e:
            name = "fade_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def fade_ruler(self):
        driver = self.driver
        try:
            Tester.time(driver, 3)
            Tester.long_press_drag(driver, Idcomp.ruler_value_animation, Idcomp.edit_play, 1000)
            print("페이드 룰러 드래그")

            # # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기")

        except Exception as e:
            name = "fade_ruler"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("페이드 룰러 동작 중 문제 발생", e)

    def fade_action(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.fade_in, "시작 페이드 선택")
            # 페이드 룰러 랜덤 선택
            Fade.fade_ruler(self)
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.animation_ruler_reset, "초기화 선택")
            Tester.time(driver, 1)
            Tester.tap(driver, Idcomp.none, "없음 선택")
            Tester.tap(driver, Idcomp.fade_out, "끝 부분 선택")
            Tester.tap(driver, Idcomp.fade_in, "끝 페이드 선택")
            # 페이드 룰러
            Fade.fade_ruler(self)
            Tester.time(driver, 1)
            Tester.tap(driver, Idcomp.none, "없음 선택")
            # # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기")
            # 완료
        except Exception as e:
            name = "fade_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("페이드 동작 중 문제 발생", e)

# 오디오 효과
class AudioEffect:

    def __init__(self, driver):
        self.driver = driver

    def audio_effect_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 오디오 효과"
        name2 = "데코 오디오 효과"
        name = "오디오 효과"
        Accessibility_Id_1 = Idcomp.clip_menu_audio_effect
        Accessibility_Id_2 = Idcomp.deco_menu_audio_effect
        audioEffect_inst = AudioEffect(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=audioEffect_inst.audio_effect_action)

        except Exception as e:
            print("%s 없는 항목" % name, e)

    def audio_effect_category(self):
        driver = self.driver
        audioEffect_category = [
        Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.content_category_0,
        Idcomp.content_category_1, Idcomp.content_category_2,Idcomp.content_category_3
        ]
        try:
            print("오디오 효과 카테고리")
            Tester.category_check(driver, audioEffect_category)

        except AssertionError as e:
            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.edit_sub_done).click()
            print("오디오 효과 카테고리 부분 정상 동작하지 않음", e)

    def audio_effect_action(self):
        driver = self.driver
        audio_effect_ruler = AudioEffect.audio_effect_ruler
        audio_effect_category = AudioEffect.audio_effect_category
        audio_effect_category(self)
        Tester.tap(driver, Idcomp.content_category_0, "음정 변환 선택")
        Tester.tap(driver, Idcomp.content2_1, "고음 선택")
        audio_effect_ruler(self)

    def audio_effect_ruler(self):
        driver = self.driver

        try:
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.audio_effect_ruler, Idcomp.edit_play, 1000)
            print("오디오 효과 룰러 드래그")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.audio_effect_ruler_reset, "초기화 선택")
            # # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기")
        except Exception as e:
            name = "audio_effect_ruler"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("오디오 효과 룰러 동작 중 문제 발생", e)

# 에코&리버브
class EchoReverb:

    def __init__(self, driver):
        self.driver = driver

    def echo_reverb_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 에코&리버브"
        name2 = "데코 에코&리버브"
        name = "에코&리버브"
        Accessibility_Id_1 = Idcomp.clip_menu_echo_reverb
        Accessibility_Id_2 = Idcomp.deco_menu_echo_reverb
        echoReverb_inst = EchoReverb(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=echoReverb_inst.echo_reverb_action)

        except Exception as e:
            name = "echo_reverb_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def echo_reverb_category(self):
        driver = self.driver
        # 카테고리 변경 필요 시 해당 리스트에서 카테고리 순서 변경
        echoReverb_category = [
        Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.content_category_0,
        Idcomp.content_category_1, Idcomp.content_category_2,
        Idcomp.content_category_3, Idcomp.content_category_4
                                ]
        try:
            print("에코&리버브 카테고리")
            Tester.category_check(driver, echoReverb_category)

        except AssertionError as e:
            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.edit_sub_done).click()
            print("에코&리버브 카테고리 부분 정상 동작하지 않음", e)

    def echo_reverb_action(self):
        driver = self.driver
        # Idcomp의 에코&리버브 카테고리 함수 호출
        EchoReverb.echo_reverb_category(self)
        Tester.tap(driver, Idcomp.content_category_0, "강당 선택")
        Tester.tap(driver, Idcomp.content2_1, "강당1 선택")
        # 에코&리버브 룰러 함수 호출
        EchoReverb.echo_reverb_ruler(self)

    def echo_reverb_ruler(self):
        driver = self.driver

        try:
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.audio_effect_ruler, Idcomp.edit_play, 1000)
            print("에코 & 리버브 룰러 드래그")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.audio_effect_ruler_reset, "초기화 선택")
            # # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기")
        except Exception as e:
            name = "echo_reverb_ruler"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("에코 & 리버브 룰러 동작 중 문제 발생", e)

# 이퀄라이저
class Equalizer:
    def __init__(self, driver):
        self.driver = driver

    def equalizer_module(self):
        driver = self.driver
        equalizer_category = [
            Idcomp.category_Bookmark, Idcomp.category_Recents,
            Idcomp.content_category_0, Idcomp.content_category_1
                                ]
        equalizer_category2 = [
            Idcomp.content02, Idcomp.content2_1, Idcomp.content2_2, Idcomp.content2_3, Idcomp.content2_4,
            Idcomp.content03, Idcomp.content3_1, Idcomp.content3_2, Idcomp.content3_3, Idcomp.content3_4
                                ]
        try:
            Tester.tap(driver, Idcomp.deco_menu_eq, "이퀄라이저 선택")
            Tester.category_check(driver, equalizer_category)
            Tester.category_check(driver, equalizer_category2)
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content_category_0, "튜닝 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.content2_1, "고음 강조 선택")
            Tester.time(driver, 2)
            Tester.long_press_drag(driver, Idcomp.audio_effect_ruler, Idcomp.move_next_clip, 2000)
            Tester.wait_tap(driver, 2, Idcomp.audio_effect_ruler_reset, "초기화 선택")
            Tester.wait_tap(driver, 2, Idcomp.edit_sub_done, "완료 선택")
        except Exception as e:
            name = "equalizer_module"
            Tester.screenshot(self, name)
            # Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("이퀄라이저 동작 중 문제 발생", e)

# 오디오 분리
class AudioDetach:

    def __init__(self, driver):
        self.driver = driver

    def audio_detach_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 오디오 분리"
        name2 = "데코 오디오 분리"
        name = "오디오 분리"
        Accessibility_Id_1 = Idcomp.clip_menu_audio_detach
        Accessibility_Id_2 = Idcomp.deco_menu_audio_detach
        audioDetach_inst = AudioDetach(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=audioDetach_inst.audio_detach_action)

        except Exception as e:
            print("%s 없는 항목" % name, e)

    def audio_detach_action(self):
        pass # 여기에 다시 돌아가는 동작 추가 필요함

# 애니메이션
class Animation:

    def __init__(self, driver):
        self.driver = driver

    def animation_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 애니메이션"
        name2 = "데코 애니메이션"
        name = "애니메이션"
        Accessibility_Id_1 = Idcomp.clip_menu_animation
        Accessibility_Id_2 = Idcomp.deco_menu_animation
        animation_inst = Animation(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=animation_inst.animation_action)

        except Exception as e:
            name = "animation_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def animation_action(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.fade_in, "시작 부분 페이드 선택")
            # 애니메이션 카테고리 체크
            fade_in_out_category = [Idcomp.none, *Idcomp.animation_id]
            print("애니메이션 > 시작 부분 모든 항목")
            Tester.category_check(driver, fade_in_out_category)
            Tester.tap(driver, Idcomp.animation_id_1, "페이드 선택")
            Tester.long_press_drag(driver, Idcomp.animation_duration_ruler, Idcomp.edit_play, 1000)
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.animation_ruler_reset, "초기화")
            Tester.tap(driver, Idcomp.none, "없음 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.overall, "전체")
            Tester.category_check(driver, Idcomp.animation_id_2)
            print("애니메이션 > 전체 모든 항목")
            Tester.tap(driver, Idcomp.none, "없음 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.animation_id_1, "스크롤 왼쪽 선택")
            # 상단 시간 조절
            Tester.long_press_drag(driver, Idcomp.animation_duration_ruler, Idcomp.edit_play, 1000)
            print("상단 시간 조절")
            Tester.time(driver, 1)
            Tester.tap(driver, Idcomp.animation_ruler_reset, "초기화")
            Tester.tap(driver, Idcomp.none, "없음 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.fade_out, "끝 부분")
            # Tester.tap(driver, Idcomp.animation_id_1, "페이드 선택")
            # # 상단 시간 조절
            # Tester.long_press_drag(driver, Idcomp.animation_duration_ruler, Idcomp.edit_play, 1000)
            # print("상단 시간 조절")
            # time.sleep(1)
            # Tester.tap(driver, Idcomp.animation_ruler_reset, "초기화")
            # Tester.tap(driver, Idcomp.none, "없음 선택")
            # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기")
        except Exception as e:
            name = "animation_action"
            Tester.screenshot(self, name)
            print("애니메이션 부분 동작하지 않음", e)

# 특수효과
class Effects:

    def __init__(self, driver):
        self.driver = driver

    # 특수효과 (비디오 클립)
    def effect_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 특수효과"
        name2 = "데코 특수효과"
        name = "특수효과"
        Accessibility_Id_1 = Idcomp.clip_menu_effect
        Accessibility_Id_2 = Idcomp.deco_menu_effect
        effect_inst = Effects(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=effect_inst.effect_action)

        except Exception as e:
            name = "effect_module"
            Tester.screenshot(self, name)
            pass
            print("%s 없는 항목" % name, e)

    def effect_action(self):
        driver = self.driver

        try:
            effect_category = [
                Idcomp.category_Bookmark, Idcomp.category_Recents, *Idcomp.content_category_id[0:5] # *은 리스트 확장 연산자로써 effect_category 포함시킴
            ]
            print("특수효과 카테고리")
            Tester.category_check(driver, effect_category)
            #  나중에 접근성 아이디 들어오면 할 수 있는 내용이라 주석처리
            # content_id_list = [
            #     [f"content_2_{i}" for i in range(0, 11)],
            #     [f"content_3_{i}" for i in range(0, 12)],
            #     [f"content_4_{i}" for i in range(0, 9)],
            #     [f"content_5_{i}" for i in range(0, 6)],
            # ]
            #
            # print("특수효과 모든 항목")
            # for content_id in content_id_list:
            #     for content_id_list in content_id:
            #         while True:
            #             try:
            #                 Tester.category_check(driver, content_id_list)
            #                 break
            #             except Exception:
            #                 print(f"요소를 찾지 못했습니다. 다시 확인합니다. ({content_id_list})")
            #
            #                 # 특정 코드 실행
            #                 Tester.category_check(driver, effect_category)
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 5, Idcomp.content2_1, None)
            Tester.tap(driver, Idcomp.rgb1, "rgb1 선택")
            # 강도 조절
            Tester.long_press_drag(driver, Idcomp.effect_intensity_ruler, Idcomp.edit_play, 1000)
            print("강도 조절")
            Tester.time(driver, 3)
            # 초기화 선택
            Tester.tap(driver, Idcomp.effect_intensity_ruler_reset, "초기화 선택")
            # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기")
        except Exception as e:
            name = "effect_action"
            Tester.screenshot(self, name)
            print("특수효과 액션 동작하지 않음", e)

# 배속
class Speed:

    def __init__(self, driver):
        self.driver = driver

    def speed_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 배속"
        name2 = "데코 배속"
        name = "배속"
        Accessibility_Id_1 = Idcomp.clip_menu_speed
        Accessibility_Id_2 = Idcomp.deco_menu_speed
        speed_inst = Speed(driver)
        done_id = Idcomp.edit_sub_done
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=speed_inst.speed_action)

        except Exception as e:
            name = "speed_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)
    # 배속
    def speed_action(self):
        driver = self.driver
        # 배속 선택
        try:
            Tester.long_press(driver, Idcomp.move_next_frame, 3)
            Tester.tap(driver, Idcomp.move_pre_clip, None)
            # 8배속 적용 시 자꾸 다음 클립으로 넘어가는 버그가 있어서 뺌
            time_list = [
                Idcomp.speed0, Idcomp.speed1, Idcomp.speed2,
                Idcomp.speed3, Idcomp.speed4 #Idcomp.speed5
            ]
            print("배속 리스트 확인")
            Tester.category_check(driver, time_list)
            Tester.time(driver, 2)
            #todo 확인 필요함 자꾸 배속 적용 시 다음 클립으로 넘어가서 생기는 문제 같기도하고 ..
            Tester.wait_tap(driver, 4, Idcomp.speed_ruler_reset, "초기화 선택")
            Tester.long_press_drag(driver, Idcomp.edit_speed_ruler, Idcomp.edit_play, 100)
            print("배속 롱프레스 후 드래그")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.speed_ruler_reset, "초기화 선택")
            # # 전체 적용하기
            # applyToAll(self)
            # print("전체 적용하기 완료")
            Tester.time(driver, 2)
        except Exception as e:
            name = "speed_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("배속 동작 중 문제 발생", e)

# 불투명도
class Opacity:

    def __init__(self, driver):
        self.driver = driver

    def opacity_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 불투명도"
        name2 = "데코 불투명도"
        name = "불투명도"
        Accessibility_Id_1 = Idcomp.clip_menu_opacity
        Accessibility_Id_2 = Idcomp.deco_menu_opacity
        opacity_inst = Opacity(driver)
        done_id = Idcomp.edit_sub_done
        try:
            # 데코, 클립 식별
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=opacity_inst.opacity_action)

        except Exception as e:
            name = "opacity"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def opacity_action(self):
        driver = self.driver
        try:
            KeyFrame.keyFrame_module(self)
            Tester.long_press_drag(driver, Idcomp.edit_value_ruler ,Idcomp.undo_button, 1000)
            time.sleep(2)
            # 초기화
            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.edit_value_ruler_reset).click()
            print("초기화")

        except Exception as e:
            name = "opacity_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("불투명도 동작 중 문제 발생", e)

# 프리즈
class Freeze:
    def __init__(self, driver):
        self.driver = driver

    def freeze_module(self):
        driver = self.driver
        name = "프리즈"
        name1 = "클립 프리즈"
        name2 = "데코 프리즈"
        # Accessibility_Id_1, 2 변수에 할당
        el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.clip_menu_freeze)
        el2 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.deco_menu_freeze)
        try:
            # el1일 경우 아래 내용 실행
            if el1:
                # el1이 화면에 보일 때
                el1[0].is_displayed()
                # el1 선택
                Tester.wait_tap(driver, 3, Idcomp.clip_menu_freeze, "%s 선택" % name1)
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.undo_button, "실행 취소 선택")

            # el2일 경우 아래 내용 실행
            elif el2:
                # el2가 화면에 보일 때
                el2[0].is_displayed()
                # el2 선택
                Tester.wait_tap(driver, 3, Idcomp.deco_menu_freeze, "%s 선택" % name2)
                # 2초 대기
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.undo_button, "%s 완료 선택" % name)
                #todo pip로 이동하는 동작 들어가야함

            else:
                assert False, "%s 없는 항목" % name
        # 판별 자체가 실패할 경우 예외처리
        except Exception as e:
            name = "freeze_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

# 배경 제거
class RemoveBg:
    def __init__(self, driver):
        self.driver = driver

    def remove_bg_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 배경 제거"
        name2 = "데코 배경 제거"
        name = "배경 제거"
        Accessibility_Id_1 = Idcomp.clip_menu_matte_effect
        Accessibility_Id_2 = Idcomp.deco_menu_matte_effect
        removeBg_inst = RemoveBg(driver)
        done_id = Idcomp.edit_sub_done
        try:
            # 데코, 클립 식별
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=removeBg_inst.remove_bg_action)

        except Exception as e:
            name = "removeBg"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def remove_bg_action(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.edit_matte_effect_toggle, "배경 제거 토글 on")
            Tester.long_press_drag(driver, Idcomp.edit_matte_effect_ruler, Idcomp.waveform_type_button, 1000)
            print("민감도 룰러 조절")
            Tester.tap(driver, Idcomp.matte_effect_ruler_reset, "초기화 선택")
            Tester.tap(driver, Idcomp.edit_matte_effect_toggle, "배경 제거 토글 off")
        except Exception as e:
            name = "remove_bg_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("배경 제거 동작 중 문제 발생", e)

# 크로마키
class Chromakey:

    def __init__(self, driver):
        self.driver = driver

    def chromakey_module(self):
        driver = self.driver
        # identify_two 정보
        name1 = "클립 크로마키"
        name2 = "데코 크로마키"
        name = "크로마키"
        Accessibility_Id_1 = Idcomp.clip_menu_chromakey
        Accessibility_Id_2 = Idcomp.deco_menu_chromakey
        chromakey_inst = Chromakey(driver)
        done_id = Idcomp.edit_sub_done
        try:
            # 데코, 클립 식별
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=chromakey_inst.chromakey_action)

        except Exception as e:
            name = "chromakey_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def chromakey_action(self):

        driver = self.driver
        wait = Tester.time(driver, 1)
        try:
            # 포인터 이동
            Tester.long_press_drag(driver, Idcomp.pixel_reader_color, Idcomp.undo_button, 1000) and wait
            Tester.long_press_drag(driver, Idcomp.chromakey_saturation_ruler, Idcomp.saturation, 1000) and wait
            Tester.tap(driver, Idcomp.chromakey_saturation_ruler_reset, None) and wait
            Tester.long_press_drag(driver, Idcomp.chromakey_value_ruler, Idcomp.brightness, 1000) and wait
            Tester.tap(driver, Idcomp.chromakey_value_ruler_reset, None) and wait
            Tester.long_press_drag(driver, Idcomp.chromakey_hue_ruler, Idcomp.hue, 1000) and wait
            Tester.tap(driver, Idcomp.chromakey_hue_ruler_reset, None) and wait
            Tester.long_press_drag(driver, Idcomp.chromakey_saturation_ruler, Idcomp.saturation, 1000) and wait
            Tester.long_press_drag(driver, Idcomp.chromakey_value_ruler, Idcomp.brightness, 1000) and wait
            Tester.long_press_drag(driver, Idcomp.chromakey_hue_ruler, Idcomp.hue, 1000) and wait
            Tester.tap(driver, Idcomp.chromakey_reset, None)
        except Exception as e:
            name = "chromakey_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("크로마키 동작 중 문제 발생", e)

# 블러
class Blur:

    def __init__(self, driver):
        self.driver = driver

    def blur_module(self):
        driver = self.driver
        name = "블러"
        Accessibility_Id = Idcomp.clip_menu_blur
        done_id = Idcomp.edit_sub_done
        blur_inst = Blur(driver)
        try:
            Tester.identify(driver, name, Accessibility_Id, done_id,
                            action=blur_inst.blur_action)
        except Exception as e:
            name = "blur_module"
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

    def blur_action(self):
        driver = self.driver
        try:
            KeyFrame.keyFrame_module(self)
            wait = Tester.time(driver, 1)
            Tester.long_press_drag(driver, Idcomp.blur_ruler, Idcomp.dB, 1000) and wait
            Tester.tap(driver, Idcomp.edit_value_ruler_reset, None)

        except Exception as e:
            name = "blur_action"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("블러 동작 중 문제 발생", e)

# 혼합
class Blend:
    def __init__(self, driver):
        self.driver = driver

    def blend_module(self):
        driver = self.driver
        name = "혼합"
        blend_list = [Idcomp.content00, Idcomp.content01, Idcomp.content1_1, Idcomp.content1_2,
                 Idcomp.content02, Idcomp.content2_1, Idcomp.content03, Idcomp.content3_1,
                 Idcomp.content3_2, Idcomp.content3_3]
        try:
            Tester.tap(driver, Idcomp.deco_menu_blend, "혼합 선택")
            KeyFrame.keyFrame_module(self)
            Tester.category_check(driver, blend_list)
            Tester.tap(driver, Idcomp.content01, "어둡게 하기 선택")
            Tester.time(driver, 3)
            Tester.long_press_drag(driver, Idcomp.edit_blend_opacity_ruler, Idcomp.move_next_clip, 2000)
            Tester.tap(driver, Idcomp.edit_sub_done, "완료 선택")
        except Exception as e:
            print("혼합 동작 중 문제 발생", e)
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)

# 역방향
class Reverse:

    def __init__(self, driver):
        self.driver = driver

    def reverse_module(self):
        driver = self.driver
        name1 = "클립 역방향"
        name2 = "데코 역방향"
        name = "역방향"

        try:
            # Accessibility_Id_1, 2 변수에 할당
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.clip_menu_reverse)
            el2 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.deco_menu_reverse)
            # el1일 경우 아래 내용 실행
            if el1:
                # el1이 화면에 보일 때
                el1[0].is_displayed()
                # el1 선택
                Tester.wait_tap(driver, 3, Idcomp.clip_menu_reverse, "%s 선택" % name1)
                # 2초 대기
                Tester.time(driver, 2)
                Tester.wait_tap(driver, 1000, Idcomp.clip_menu_reverse, "역방향 완료 확인 후 되돌리기")

            # el2일 경우 아래 내용 실행
            elif el2:
                # el2가 화면에 보일 때
                el2[0].is_displayed()
                # el2 선택
                Tester.wait_tap(driver, 3, Idcomp.deco_menu_reverse, "%s 선택" % name2)

                # 2초 대기
                Tester.time(driver, 2)
                Tester.wait_tap(driver, 1000, Idcomp.deco_menu_reverse, "역방향 완료 확인 후 되돌리기")

            # 만약 실패할 경우 name 값 + 없는 항목 문구 출력
            else:
                assert False, "%s 없는 항목" % name
        # 판별 자체가 실패할 경우 예외처리
        except Exception as e:
            Tester.screenshot(self, name)
            print("%s 없는 항목" % name, e)

# 복제
class Duplicate:
    def __init__(self, driver):
        self.driver = driver

    def duplicate_module(self):
        driver = self.driver
        Tester.time(driver, 2)
        name1 = "클립 복제"
        name2 = "데코 복제"
        name = "복제"
        try:
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.clip_menu_duplicate)
            if el1:
                Tester.wait_tap(driver, 10, Idcomp.clip_menu_duplicate, name1)
                Tester.time(driver, 2)
            elif not el1:
                Tester.wait_tap(driver, 10, Idcomp.deco_menu_duplicate, name2)
                Tester.time(driver, 2)
                #todo 데코의 경우 각 동작 새로 추가하는 부분이 필요함
            else:
                assert False, "%s 없는 항목" % name
        except Exception as e:
            print("%s 없는 항목" % name, e)
            Tester.screenshot(self, name)

# PIP로 복제
class PipDuplicate:
    def __init__(self, driver):
        self.driver = driver

    def Pip_duplicate_module(self, action):
        driver = self.driver
        name = "PIP로 복제"
        try:
            Tester.wait_tap(self, 5, Idcomp.clip_menu_duplicate_pip, "PIP로 복제 선택")
            Tester.time(driver, 3)
            Tester.wait_tap(self, 5, Idcomp.edit_done, "완료 선택")
            action()

        # 판별 자체가 실패할 경우 예외처리
        except Exception as e:
            print("PIP로 복제 없는 항목", e)
            Tester.screenshot(self, name)

# 클립, PIP 데코 교체
class ClipReplace:
    def __init__(self, driver):
        self.driver = driver

    def replace_module(self):
        driver = self.driver
        # identify_two 정보
        print("교체 모듈 진입")
        name1 = "클립 교체"
        name2 = "pip 데코 교체"
        name = "교체"
        Accessibility_Id_1 = Idcomp.clip_menu_replace
        Accessibility_Id_2 = Idcomp.deco_menu_replace
        ClipReplace_inst = ClipReplace(driver)
        done_id = None
        Tester.time(driver, 2)
        try:
            Tester.identify_two(driver, name, name1, name2, Accessibility_Id_1, Accessibility_Id_2, done_id,
                                action=ClipReplace_inst.replace_action)

        except Exception as e:
            print("%s 없는 항목" % name, e)
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.replace_cancel, None)

    def replace_action(self):
        driver = self.driver
        name = "교체"
        try:
            Tester.tap(driver, Idcomp.album, "최근 항목 선택")
            Tester.tap(driver, Idcomp.Appium, "에피움 폴더 선택")
            Tester.tap(driver, Idcomp.asset1, "1번 항목 선택")
            element = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.screen_icon_play)
            if element:
                # 아래 코드 실행
                Tester.long_press_drag(driver, Idcomp.timeline, Idcomp.clip_timeline_icon_previ, 1000)
                Tester.long_press_drag(driver, Idcomp.timeline, Idcomp.clip_timeline_icon_end, 1000)
                Tester.long_press(driver, Idcomp.clip_timeline_icon_end, 5000)
                Tester.long_press(driver, Idcomp.clip_timeline_icon_previ, 5000)
                Tester.tap(driver, Idcomp.screen_icon_play, None)
                Tester.tap(driver, Idcomp.replace_done, None)
                Tester.time(driver, 5)
                print("교체 완료")
            elif not element:
                print("교체 완료")

        except Exception as e:
            print("교체 동작 중 문제 발생", e)
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.replace_cancel, None)

    def deco_replace_action(self, ):
        driver = self.driver
        name = "데코 교체"
        Tester.tap(driver, Idcomp.deco_menu_replace, "데코 교체")
        print("bgm, 일반 데코 판별")
        try:
            el1 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.play)
            if el1:
                print("bgm 데코로 확인")
                Tester.wait_tap(driver, 3, Idcomp.cancel, "x버튼 선택")
                Tester.time(driver, 2)
                Tester.tap(driver, Idcomp.content1, "교체 항목 선택")
                Tester.tap(driver, Idcomp.content_add_done, "완료")
                Tester.tap(driver, Idcomp.edit_done, "완료")
            if not el1:
                print("일반 데코로 확인")
                Tester.time(driver, 2)
                el2 = driver.find_elements(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.content01)
                print("콘텐츠 아이디 확인")
                if el2:
                    Tester.wait_tap(driver, 3, Idcomp.content01, "교체 항목 선택")
                    Tester.tap(driver, Idcomp.content_add_done, "완료")
                    Tester.tap(driver, Idcomp.edit_done, "완료")

                if not el2:
                    Tester.wait_tap(driver, 3, Idcomp.content1, "교체 항목 선택")
                    Tester.tap(driver, Idcomp.content_add_done, "완료")
                    Tester.tap(driver, Idcomp.edit_done, "완료")

        except Exception as e:
            print("교체 중 문제 발생", e)
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.edit_done, "완료")

# 파일명 변경
class FileNameChange:
    def __init__(self, driver):
        self.driver = driver

    def file_name_change_module(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.file_name_change, "파일명 선택")
            Tester.text_input(driver, Idcomp.input_title, "appium test")
            Tester.wait_tap(driver, 3, Idcomp.input_title_done_button, "완료 선택")
        except Exception as e:
            name = "file_name_change_module"
            Tester.screenshot(self, name)
            print("파일 이름 변경 동작 중 문제 발생", e)

# 여기로 이동
class MoveToHere:
    def __init__(self, driver):
        self.driver = driver

    def move_to_here_module(self):
        driver = self.driver
        try:
            Tester.long_press(driver, Idcomp.move_next_frame, 1000)
            Tester.tap(driver, Idcomp.deco_menu_move, "여기로 이동 선택")
        except Exception as e:
            name = "moveToHereModule"
            Tester.screenshot(self, name)
            print("여기로 이동 동작 중 문제 발생", e)

# 모션 멈추기
class PauseMotion:
    def __init__(self, driver):
        self.driver = driver

    def pause_motion_module(self):
        driver = self.driver
        try:
            for i in range(0,2):
                Tester.tap(driver, Idcomp.deco_menu_pause, "모션 멈추기 선택")
        except Exception as e:
            name = "pauseMotion"
            Tester.screenshot(driver, name)
            print("모션 멈추기 동작 중 문제 발생", e)

# 트래킹
class Tracking:
    def __init__(self, driver):
        self.driver = driver

    def tracking_module(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.deco_menu_tracking, "트래킹 선택")
            Tester.tap(driver, Idcomp.tracking_start_button, "트래킹하기")
            Tester.wait_tap(driver, 500, Idcomp.until_the_end, "끝까지")
            Tester.tap(driver, Idcomp.tracking_retry_button, "다시 하기 선택")
            Tester.tap(driver, Idcomp.tracking_start_button, "트래킹하기")
            Tester.wait_tap(driver, 500, Idcomp.edit_done, "완료")
            # el1 = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=Idcomp.tracking_add_button)
            # if el1:
            #     Tester.wait_tap(driver, 500, Idcomp.tracking_add_button, "추가 선택")
            #     Tester.time(driver, 5)
            #     Tester.wait_tap(driver, 500, Idcomp.tracking_start_button, "트래킹하기")
            #     Tester.wait_tap(driver, 500, Idcomp.tracking_delete_button, "트래킹 해제")
            # elif el1:
            #     for i in range(0,3):
            #         Tester.tap(driver, Idcomp.move_next_frame, "l> 선택")
            #     Tester.wait_tap(driver, 500, Idcomp.tracking_add_button, "추가 선택")
            #     Tester.time(driver, 5)
            #     Tester.wait_tap(driver, 500, Idcomp.tracking_start_button, "트래킹하기")
            #     Tester.wait_tap(driver, 500, Idcomp.tracking_delete_button, "트래킹 해제")
        except Exception as e:
            print("트래킹 동작 중 문제 발생", e)
            name = "tracking_module"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.edit_done, "완료")

# 부분 설정
class KeyFrame:
    def __init__(self, driver):
        self.driver = driver

    def keyFrame_module(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 3, Idcomp.keyframe_multi_switch, "부분 설정 on")
            for i in range(0,3):
                Tester.tap(driver, Idcomp.move_next_frame, None)
                Tester.tap(driver, Idcomp.move_next_frame, None)
                Tester.tap(driver, Idcomp.add_key_frame_button, None)
            print("키프레임 추가 완료")
            Tester.tap(driver, Idcomp.keyframe_multi_switch, "부분 설정 off")
        except Exception as e:
            name = "keyFrame_module"
            Tester.screenshot(driver, name)
            print("키프레임 동작 중 문제 발생", e)

# 편집
class TextEdit:
    def __init__(self, driver):
        self.driver = driver

    def text_edit_module(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.deco_menu_text, "편집 선택")
            Tester.text_input(driver, Idcomp.edit_input_text_view, "appium test")
            Tester.tap(driver, Idcomp.top_icon_done, "완료 선택")
        except Exception as e:
            name = "text_edit_module"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.top_icon_done, "완료 선택")
            print("편집 동작 중 문제 발생", e)

# 폰트
class Font:
    def __init__(self, driver):
        self.driver = driver

    def font_module(self):
        driver = self.driver
        font_list = [Idcomp.category_Bookmark, Idcomp.category_Recents, Idcomp.category_All, *Idcomp.font_category]
        try:
            Tester.tap(driver, Idcomp.deco_menu_font, "폰트 선택")
            Tester.category_check(driver, font_list)
            Tester.tap(driver, Idcomp.font_category1, "파일 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.top_bar_button1_0, "파일에서 불러오기")
            Tester.wait_tap(driver, 2, Idcomp.cancle, "취소 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.filter_button2_0, "기기에서 불러오기")
            Tester.wait_tap(driver, 2, Idcomp.cancle, "취소 선택")
            Tester.tap(driver, Idcomp.license_button, "저작권 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.faq_close, "닫기")
            Tester.wait_tap(driver, 2, Idcomp.popup_close, "닫기")
            Tester.bookMarkCheck(driver, Idcomp.category_Bookmark, Idcomp.content01, Idcomp.content1, Idcomp.category_All, "폰트")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.edit_done, "완료")
        except Exception as e:
            name = "font_module"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.edit_done, "완료")
            print("폰트 동작 중 문제 발생", e)

# 정렬
class Arrange:
    def __init__(self, driver):
        self.driver = driver

    def arrange_module(self):
        driver = self.driver
        for i in range(0, 2):
            Tester.tap(driver, Idcomp.deco_menu_duplicate, "복제 선택")
        try:
            Tester.tap(driver, Idcomp.deco_menu_arrangement, "정렬 선택")
            for i in range(0, 2):
                Tester.tap(driver, Idcomp.arrangement_fold_button, "폴드 버튼 선택")
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.arrangement_top_button, "맨 위로 선택")
            Tester.wait_tap(driver, 3, Idcomp.own, "1번 선택")
            Tester.long_press_drag(driver, Idcomp.arrangement_handle, Idcomp.arrangement_bottom_button, 2000)
            Tester.tap(driver, Idcomp.arrangement_bottom_button, "맨 아래로 선택")
            Tester.long_press_drag(driver, Idcomp.arrangement_handle, Idcomp.arrangement_fold_button, 2000)
            Tester.wait_tap(driver, 3, Idcomp.arrangement_bottom_button, None)
            Tester.time(driver, 2)
            Tester.wait_tap(driver, 3, Idcomp.arrangement_top_button, None)
            Tester.tap(driver, Idcomp.edit_done, "완료 선택")
        except Exception as e:
            name = "arrange_module"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.edit_done, "예외처리 완료 선택")
            print("정렬 동작 중 문제 발생", e)

# 글자 크기
class TextSize:
    def __init__(self, driver):
        self.driver = driver

    def text_size_module(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.deco_menu_text_size, "글자 크기 선택")
            for i in range(0,2):
                Tester.tap(driver, Idcomp.text_word_select_all, "전체 선택")
                Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.text_chracter_select1, "1번 항목 선택")
            Tester.tap(driver, Idcomp.text_chracter_select3, "3번 항목 선택")
            Tester.long_press_drag(driver, Idcomp.edit_text_size_ruler, Idcomp.edit_play, 2000)
            Tester.tap(driver, Idcomp.edit_done, "완료 선택")

        except Exception as e:
            name = "text_size_module"
            Tester.screenshot(driver, name)
            Tester.tap(driver, Idcomp.edit_done, "완료 선택")
            print("글자 크기 동작 중 문제 발생", e)

# 서식
class TextFormat:
    def __init__(self, driver):
        self.driver = driver

    def text_format_module(self):
        driver = self.driver
        Tester.tap(driver, Idcomp.deco_menu_text_style, "서식 선택")
        funcs = [TextFormat.text_color, TextFormat.text_outline, TextFormat.text_background, TextFormat.text_shadow, TextFormat.text_emphasis]
        Tester.testFuncs(self, funcs, 5, Tester.testFuncsKeyword)
        Tester.tap(driver, Idcomp.edit_sub_done, "완료")

    def text_color(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.text_color_button, "글자 색상 선택")
            Tester.long_press_drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button, 2000)
            Tester.wait_tap(driver, 3, Idcomp.color_alpha_ruler_reset, "초기화 선택")
            Tester.tap(driver, Idcomp.recent_color_spoid_button, "스포이드 선택")
            Tester.long_press_drag(driver, Idcomp.pixel_reader_color, Idcomp.undo_button, 1000)
            Background.color(self, Idcomp.text_solid_color_button)
            Background.gradation(self, Idcomp.text_gradient_color_button)
            Background.pattern(self, Idcomp.bg_pattern_color_button)
        except Exception as e:
            name = "text_color"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("글자 색상 동작 중 문제 발생", e)

    def text_outline(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.text_outline_button, "외곽선 선택")
            Tester.long_press_drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button, 2000)
            print("불투명도 조절")
            Tester.wait_tap(driver, 3, Idcomp.color_alpha_ruler_reset, "초기화 선택")
            Tester.tap(driver, Idcomp.recent_color_spoid_button, "스포이드 선택")
            Tester.long_press_drag(driver, Idcomp.pixel_reader_color, Idcomp.undo_button, 1000)
            Background.color(self, None)
            Tester.long_press_drag(driver, Idcomp.text_outline_width_ruler, Idcomp.text_color_button, 2000)
            print("두께 조절")
            Tester.wait_tap(driver, 3, Idcomp.text_outline_width_ruler_reset, "초기화 선택")
        except Exception as e:
            name = "text_outline"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("글자 외곽선 동작 중 문제 발생", e)

    def text_background(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.text_bg_color_button, "배경 선택")
            Tester.tap(driver, Idcomp.recent_color_spoid_button, "스포이드 선택")
            Tester.long_press_drag(driver, Idcomp.pixel_reader_color, Idcomp.undo_button, 1000)
            Background.color(self, Idcomp.text_bg_solid_color_button)
            Background.gradation(self, Idcomp.text_bg_gradient_color_button)
            Background.pattern(self, Idcomp.text_bg_pattern_color_button)
        except Exception as e:
            name = "text_background"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("글자 배경 동작 중 문제 발생", e)

    def text_shadow(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 3, Idcomp.text_shadow_button, "그림자 선택")
            Tester.long_press_drag(driver, Idcomp.recent_color_alpha_ruler, Idcomp.recent_color_spoid_button, 2000)
            print("불투명도 조절")
            Tester.wait_tap(driver, 3, Idcomp.color_alpha_ruler_reset, "초기화 선택")
            Background.color(self, Idcomp.text_shadow_solid_color_button)
            Tester.wait_tap(driver, 3, Idcomp.text_shadow_angle_button, "각도 선택")

            # # todo 드래그 동작 시 필요한 핸들 접근성 아이디 없음 (동작 안 되는 것 확인 아이디 지정 후 다시 작성하겠습니다)
            # # 클립 좌측 핸들
            # a = driver.tap_xpath(by=MobileBy.XPATH, value='//XCUIElementTypeApplication[@name="VLLO"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther')
            # # 클립 우측 핸들
            # b = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value='270')
            # c = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value='180')
            # d = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value='90')
            # time.sleep(2)
            # # 클립 좌측 핸들 1회 조절
            # TouchAction(driver).long_press(a).wait(2000).move_to(b).release().perform()
            # TouchAction(driver).long_press(a).wait(2000).move_to(c).release().perform()
            # TouchAction(driver).long_press(a).wait(2000).move_to(d).release().perform()
            # time.sleep(2)

        except Exception as e:
            name = "text_shadow"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("글자 그림자 동작 중 문제 발생", e)

    def text_emphasis(self):
        driver = self.driver
        try:
            Tester.wait_tap(driver, 3, Idcomp.text_emphasis_button, "강조 선택")
            Tester.category_check(driver, Idcomp.text_emphasis_list)

        except Exception as e:
            name = "text_emphasis"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("글자 강조 동작 중 문제 발생", e)

# 강도
class TextIntensity:
    def __init__(self, driver):
        self.driver = driver

    def text_intensity_module(self):
        driver = self.driver
        try:
            Tester.tap(driver, Idcomp.deco_menu_intensity, "강도 선택")
            KeyFrame.keyFrame_module(self)
            Tester.long_press_drag(driver, Idcomp.edit_value_ruler, Idcomp.undo_button, 2000)
            Tester.time(driver, 2)
            Tester.tap(driver, Idcomp.edit_value_ruler_reset, "초기화 선택")
        except Exception as e:
            name = "text_intensity_module"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.edit_sub_done, None)
            print("글자 강도 동작 중 문제 발생", e)


    # def text_spacing(self):
    # def text_alignment(self):

# 무음 구간 제거
class SilenceRemoval:
    def __init__(self, driver):
        self.driver = driver

    def silence_removal_module(self):
        driver = self.driver
        try:
            Tester.add_clip(driver, "비디오 클립", Idcomp.category_video)
            Tester.wait_tap(driver, 5, Idcomp.clip_silence_removal, "무음 구간 제거 선택")
            Tester.long_press_drag(driver, Idcomp.sr_volume_control, Idcomp.clip_top_icon_magnet, 2000)
            Tester.time(driver, 3)
            Tester.long_press_drag(driver, Idcomp.sr_min_duration_ruler, Idcomp.sr_button_done, 2000)
            Tester.tap(driver, Idcomp.sr_button_menu_margin, "마진 선택")
            a = Idcomp.sr_button_submenu_default
            b = Idcomp.sr_button_submenu_extra
            c = Idcomp.sr_button_submenu_tight
            margin = [a, b, c]
            Tester.category_check(driver, margin)
            Tester.tap(driver, Idcomp.sr_button_menu_play, "구간 재생")
            for i in range(0,5):
                Tester.tap(driver, Idcomp.sr_button_submenu_next, "구간 재생 - 다음")
            for i in range(0,3):
                Tester.tap(driver, Idcomp.sr_button_submenu_prev, "구간 재생 - 이전")
            Tester.tap(driver, Idcomp.sr_button_done, "완료")
            Tester.wait_tap(driver, 10, Idcomp.undo_button, "실행 취소")
            Tester.time(driver, 3)
            for i in range(1, 11):
                element_id = getattr(Idcomp, f'timeline_clip{i}')
                print(element_id)
                try:
                    element = element_id
                    Tester.wait_tap(driver, 3, element, f"클립 {i}번 선택 완료")
                    break
                except:
                    print(f"클립 {i}번을 찾을 수 없음")



        except Exception as e:
            name = "silence_removal_module"
            Tester.screenshot(self, name)
            Tester.tap(driver, Idcomp.sr_button_done, None)
            print("글자 강도 동작 중 문제 발생", e)

#TODO 전체 적용하기 추후 추가 예정

# # 전체 적용하기
# class applyToAll():
#
#     def applyToAllAction(self):
#         driver = self.driver
#         try:
#             # 해당 아이디가 있는지 찾기
#             select_all = driver.find_elements(by=By.ACCESSIBILITY_ID, value=Idcomp.clip_menu_fade)
#             deselect_all = driver.find_elements(by=By.ACCESSIBILITY_ID, value=Idcomp.deco_menu_fade)
#             fade_action = Fade.fade_action
#
#             if select_all:
#                 # 클립 볼륨이 보이는 경우
#                 select_all[0].is_displayed()
#                 # 아래 코드 실행
#                 select_all[0].click()
#                 print("전체 적용하기 선택")
#                 # 볼륨 액션 실행
#                 fade_action(self)
#
#             elif deselect_all:
#                 # 데코 볼륨이 보이는 경우
#                 deselect_all[0].is_displayed()
#                 # 아래 코드 실행
#                 deselect_all[0].click()
#                 print("전체 적용하기 선택")
#                 # 볼륨 액션 실행
#                 fade_action(self)
#
#             else:
#                 print("전체 적용하기 항목 없음")
#
#         except AssertionError as e:
#             print("Fade 진입, ID 부분 정상 동작하지 않음.", e)
