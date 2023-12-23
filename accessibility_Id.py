# kevin - 접근성 아이디 모아둔 파일/ 접근성 아이디 변경, 카테고리 순서 변경 시 해당 파일에서만 변겅
# from appium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import random
# from selenium.webdriver.common.by import By
class Idcomp:
    #========================== 메인 화면에 필요한 아이디 =======================================
    # 배너
    BannerMenu = "VLStartViewController_BannerMenu"
    # 새 프로젝트 버튼
    new_project = "VLStartViewController_CreateBewButton"
    # 팝업 상단 x
    popup_close = "popup_close"
    # 메인 설정
    SettingButton = "VLStartViewController_TopContainer_SettingButton"
    # 유튜브 플레이어가 있는지 확인
    Youtubeplayer = "YouTube 동영상 플레이어"
    # 도움말
    help = "도움말"
    # 저작권
    license = "license"
    # 질문 선택 질문들은 아래에 추후에 업데이트하도록 하겠습니다
    question1 = "무료체험/구독은 자동으로 갱신되나요?"
    # FAQ 취소 버튼
    faq_close = "audio common icon close"
    # 녹화 중 터치 포인트 활성화
    show_touch = "setting_show_touch"
    # 도움말 > 카테고리 일반
    basic = "일반"
    # 문의하기
    contact_us = "문의하기"
    # 평가 및 리뷰하기
    review = "평가 및 리뷰하기"
    # 팝업 -> 삭제
    alert_0 = "alert_0"
    # 팝업 -> 취소
    alert_1 = "alert_1"
    # 추가 화면에서 다음으로 버튼
    icon_next = "album bottom icon next off"
    # 프로젝트 생성하기 버튼
    create_project = "프로젝트 생성하기"
    # 메인 화면의 스토어 버튼
    main_store = "main_store"
    # 배너 오른쪽 이미지
    bannerRightSideImage = "bannerRightSideImage"
    # 상점 도움말
    store_help = "store_help"
    # 도움말 완료
    help_done = "help_done"
    # 이용약관 선택
    terms_of_use = "store_terms_of_use"
    # 개인 정보 정책
    privacy_policy = "store_privacy_policy"
    # 프로젝트 썸네일 fill, fit
    fill_icon = "VLStartViewController_TopContainer_ScaleButton"
    # 프로젝트 정렬 오름차순
    project_sort_up = "main icon align up"
    # 프로젝트 정렬 내림차순
    project_sort_down = "main icon align down"
    # 프로젝트 생성한 날짜
    project_created = "popup_created"
    # 이름 선택
    project_name = "popup_name"
    # 마지막으로 열어본 날짜
    project_opened = "popup_opened"

    # 프로젝트 메뉴 버튼(···)
    project_edit_buttom = "project_edit_buttom"
    # 프로젝트1 메뉴 버튼(···)
    project_edit_buttom1 = "project_edit_buttom_0"
    # 프로젝트2 메뉴 버튼(···)
    project_edit_buttom2 = "project_edit_buttom_1"
    # 프로젝트3 메뉴 버튼(···)
    project_edit_buttom3 = "project_edit_buttom_2"
    # 프로젝트4 메뉴 버튼(···)
    project_edit_buttom4 = "project_edit_buttom_3"
    # 프로젝트5 메뉴 버튼(···)
    project_edit_buttom5 = "project_edit_buttom_4"

    # 프로젝트 분류 색상 빨강색
    popup_tag_red = "popup_tag_red"
    # 프로젝트 분류 색상 노랑색
    popup_tag_yellow = "popup_tag_yellow"
    # 프로젝트 분류 색상 초록색
    popup_tag_green = "popup_tag_green"
    # 프로젝트 분류 색상 파란색
    popup_tag_blue = "popup_tag_blue"
    # 프로젝트 분류 색상 보라색
    popup_tag_purple = "popup_tag_purple"

    # 프로젝트 목록 선택, 취소
    project_select_button = "start_project_select_button"
    # 모두 선택
    project_select_all_button = "VLStartViewController_ProjectEditContainer_ProjectSelectAllButton"
    # 모두 선택 후 삭제
    ProjectDeleteButton = "VLStartViewController_ProjectEditContainer_ProjectDeleteButton"
    # 왼쪽 상단 내 프로젝트
    start_my_project_button = "start_my_project_button"

    # 왼쪽 상단 내 프로젝트 이후 빨강색
    popup_red = "popup_red"
    # 왼쪽 상단 내 프로젝트 이후 노랑색
    popup_yellow = "popup_yellow"
    # 왼쪽 상단 내 프로젝트 이후 초록색
    popup_green = "popup_green"
    # 왼쪽 상단 내 프로젝트 이후 파랑색
    popup_blue = "popup_blue"
    # 왼쪽 상단 내 프로젝트 이후 보라색
    popup_purple = "popup_purple"
    # 왼쪽 상단 내 프로젝트 이후 내 프로젝트
    popup_all = "popup_all"

    # 최근 삭제된 항목
    popup_recycle_bin = "popup_recycle_bin"
    # X버튼 선택
    common_bottom_icon_close = "common bottom icon close"
    # 선택 > 모두 선택
    select_all = "모두 선택"
    # 선택 > 선택 해제
    deselect_all = "선택 해제"
    # 선택 > 복원
    restore = "복원"
    # 영구 삭제
    delete_permanently = "영구 삭제"
    # 프로젝트 공유하기
    project_share = "popup_share_project"
    # 이름 변경
    popup_rename = "popup_rename"
    # 이름 변경 > x버튼
    input_title_cancel_button = "input_title_cancel_button"
    # 이름 변경 > V버튼
    input_title_done_button = "input_title_done_button"
    # text field 찾기
    input_title = "input_title"
    # 프로젝트 메뉴 > 복제
    popup_duplicate = "popup_duplicate"
    # 프로젝트 메뉴 > 삭제
    popup_delete = "popup_delete"
    # 삭제
    delete = "삭제"
    # 닫기
    close = "닫기"
    # 스토어 닫기
    premium_icon_close = "premium icon close"

    #=================================== 새 프로젝트 진입 후 부터 사용하는 아이디 ======================================
    # 빈 장면 넣기
    insert_blank = "album_bottom_icon_Insert Blank"
    # 전체
    category_all = "asset_category_all"
    # 비디오 / GIF 만들기
    create_new_button = "VLStartViewController_CreateBewButton"
    # 카메라
    camera = "album_bottom_icon_camera"
    # 사진 촬영
    photo_capture = "PhotoCapture"
    # 사진 사용
    use_photo = "사진 사용"
    # 파일
    file = "album_bottom_icon_file"
    # 취소
    cancle = "취소"
    # 앨범
    album = "album"
    # Appium 폴더
    Appium = "Appium"
    # 추가 이름의 앨범
    add = "추가"
    # 비디오 카테고리
    category_video = "asset_category_video"
    # GIF 카테고리
    category_gif = "asset_category_gif"
    # 사진 카테고리
    category_photo = "asset_category_photo"

    # 미디어 스톡
    media_stock = "media_stock"

    # 추가 화면에서 클립
    # 에셋1
    asset1 = "asset_1_0"
    # 에셋2
    asset2 = "asset_2_0"
    # 에셋3
    asset3 = "asset_3_0"

    # 미디어 선택하기 에셋
    asset_1 = "asset_1_1"
    # 가운데 클립 목록에서 전체 보기
    asset_expand = "asset_expand_1_0"
    # 우측 상단 체크 해제
    check_box = "main icon check box"
    # 프리뷰 닫기
    preview_close = "compose_preview_close"
    # 하단 목록에서 클립 전체 보기
    asset_selected = "asset_selected_0"

    content_expand0 = "content_expand00"

    # 하단 목록에서 클립 삭제
    # 하단 목록에서 1번 클립 삭제
    selected_delete_1 = "asset_selected_delete_0"
    # 하단 목록에서 2번 클립 삭제
    selected_delete_2 = "asset_selected_delete_1"
    # 하단 목록에서 3번 클립 삭제
    selected_delete_3 = "asset_selected_delete_2"
    # 하단 목록에서 4번 클립 삭제
    selected_delete_4 = "asset_selected_delete_3"
    # 하단 목록에서 5번 클립 삭제
    selected_delete_5 = "asset_selected_delete_4"

    # 하단 목록에 5번 아이디
    asset_selected_4 = "asset_selected_4"

    # 스톡
    stoke = "VLLO 스톡"

    # 1번 콘텐츠
    content1 = "content_0_0"
    # 2번 콘텐츠
    content2 = "content_0_1"
    # 3번 콘텐츠
    content3 = "content_0_2"
    # 4번 콘텐츠
    content4 = "content_0_3"
    # 5번 콘텐츠
    content5 = "content_0_4"

    # 저작권 확인하기
    copyright_check = "저작권 확인하기"

    # 프로젝트 추가 하단
    asset_selected_0 = "asset_selected_0"
    asset_selected_1 = "asset_selected_1"
    asset_selected_2 = "asset_selected_2"

    content00 = "content_0_0"
    # 1번 콘텐츠
    content01 = "content_1_0"
    # 2번 콘텐츠
    content02 = "content_2_0"
    # 3번 콘텐츠
    content03 = "content_3_0"
    # 4번 콘텐츠
    content04 = "content_4_0"
    # 5번 콘텐츠
    content05 = "content_5_0"

    # 콘텐츠
    content1_1 = "content_1_1"
    content1_2 = "content_1_2"
    content1_3 = "content_1_3"
    content1_4 = "content_1_4"

    content2_1 = "content_2_1"
    content2_2 = "content_2_2"
    content2_3 = "content_2_3"
    content2_4 = "content_2_4"

    content3_1 = "content_3_1"
    content3_2 = "content_3_2"
    content3_3 = "content_3_3"
    content3_4 = "content_3_4"


    # 프로젝트
    project = "프로젝트"

    # 프로젝트 선택
    # 1번 프로젝트
    project1 = "project_0"
    # 2번 프로젝트
    project2 = "project_1"
    # 3번 프로젝트
    project3 = "project_2"
    # 4번 프로젝트
    project4 = "project_3"

    # PIP 이미지
    pip_image = "edit_add_image_button"
    # PIP GIF
    pip_gif = "edit_add_gif_button"
    # PIP 비디오
    pip_video = "edit_add_video_button"

    # l< 버튼
    move_pre_clip = "move_pre_clip"

    # >l 선택
    move_next_clip = "move_next_clip"

    # l> 선택
    move_next_frame = "move_next_frame"

    # <l 선택
    move_pre_frame = "move_pre_frame"

    # 실행 취소
    undo_button = "edit_undo_button"

    # 재실행
    redo_button = "edit_redo_button"

    # +버튼
    add_button = "edit_clip_add_button"

    # 타임라인 클립
    # 1번 클립
    timeline_clip1 = "timeline_clip_0"
    # 2번 클립
    timeline_clip2 = "timeline_clip_1"
    # 3번 클립
    timeline_clip3 = "timeline_clip_2"
    # 4번 클립
    timeline_clip4 = "timeline_clip_3"
    # 5번 클립
    timeline_clip5 = "timeline_clip_4"
    timeline_clip6 = "timeline_clip_5"
    timeline_clip7 = "timeline_clip_6"
    timeline_clip8 = "timeline_clip_7"
    timeline_clip9 = "timeline_clip_8"
    timeline_clip10 = "timeline_clip_9"
    timeline_clip11 = "timeline_clip_10"


    # text box 선택
    project_title = "project_title"

    # 첫 장면
    first_screen = "첫 장면"
    # 4 : 3
    screen4_3 = "4 : 3"
    # 4 : 5
    screen4_5 = "4 : 5"
    # 1 : 1
    screen1_1 = "1 : 1"
    # 16 : 9
    screen16_9 = "16 : 9"
    # 9 : 16
    screen9_16 = "9 : 16"
    # 1.85 : 1
    screen185_1 = "1.85 : 1"
    # 2 : 1
    screen2_1 = "2 : 1"
    # 2.35 : 1
    screen235_1 = "2.35 : 1"

    # 화면 비율 리스트
    project_setting_category1 = [first_screen, screen4_3, screen4_5, screen1_1,
                                screen16_9, screen9_16, screen185_1, screen2_1, screen235_1]

    # 혼합 룰러
    edit_blend_opacity_ruler = "edit_blend_opacity_ruler_collection_view"

    # 강도 룰러
    add_filter_strength_ruler = "add_filter_strength_ruler_collection_view"

    # 하단 완료
    done_button = "bottom_bar_done_button"

    # 끼움
    fit = "끼움"
    # 채움
    fill = "채움"
    # 가운데
    center = "가운데"

    # 영상 배치 리스트
    project_setting_category2 = [fit, fill, center]

    #프로젝트 생성
    create_project = "button_create_project"

    # 필터+
    filter_plus = "top_bar_filter_button"

    # 전체 보기
    View_all = "tag_filter_full_mode_toggle"

    # 필터 - 완료
    filter_done = "tag_filter_done_button"

    # BGM 정렬
    sort_button = "top_bar_sort_button"

    # BGM 정렬 - 최신 순
    bgm_lastest = "popup_lastest"

    # BGM 정렬 - 재생 시간 짧은 순
    bgm_shortest = "popup_shortest"

    # BGM 정렬 - 재생 시간 긴 순
    bgm_longest = "popup_longest"

    # BGM 정렬 - 기본 값
    popup_none = "popup_none"

    # X버튼 선택
    add_cancel = "bottom_bar_cancel_button"

    # BGM 저작권
    license_button = "top_bar_license_button"

    # 파일에서 가져오기
    top_bar_button1_0 = "top_bar_import_button_1"
    top_bar_button1_1 = "top_bar_filter_button_1"
    # 비디오에서 추출하기
    filter_button2_0 = "top_bar_import_button_2"
    top_bar_button2_1 = "top_bar_filter_button_2"
    # 교체 앨범 선택(없으면 앨범 생성 필요함)
    replace_album = "교체"

    # 완료
    done = "done"
    # 팝업 완료
    popup_done = "popup_done"
    # 배속 완료
    speed_done = "edit_speed_done"

    # 트랜지션 완료
    transition_edit_done = "transition_edit_done"

    # 하단 음원 우측 핸들 (>)
    end_time = "end_time"

    # 하단 음원 좌측 핸들 (<)
    start_time = "start_time"

    # 음원 선택
    sound_1 = "sound_0"
    sound_2 = "sound_1"
    sound_3 = "sound_2"
    sound_4 = "sound_3"

    # 재생 / 일시 정지
    play = "play"

    # 배너 유튜브 링크 재생
    bannerplay = "재생"

    # 창 닫기
    cancel = "cancel"

    # 음원 파일 삭제 버튼
    sound_delete_1 = "sound_delete_0"
    sound_delete_2 = "sound_delete_1"
    sound_delete_3 = "sound_delete_2"
    sound_delete_4 = "sound_delete_3"

    # 삭제 버튼 선택
    delete_button_0_0 = "content_select_delete_button_0_0"

    # 좌측 북마크
    bookmark_button = "sound_select_bookmark_button"

    # 텍스트 편집
    sound_select_title = "sound_select_edit_title_button"

    # 이미지 변경
    clip_icon_replace = "clip icon replace"

    # 썸네일 선택
    thumbnail_select1 = "thumbnail_select_0"
    thumbnail_select2 = "thumbnail_select_1"
    thumbnail_select3 = "thumbnail_select_2"
    thumbnail_select4 = "thumbnail_select_3"

    # 파일 text field 찾기
    file_text_field = "태그 검색 또는 생성"

    # 텍스트 옆 +
    add_tag_0 = "add_tag_0_0"

    # 하단 테그 삭제
    tag_delete_button = "selected_sound_tag_delete_button_0"

    # 태그 추가 버튼
    add_tag_button = "sound_select_add_tag_button"

    # 검색 기록 삭제
    add_tag_clear = "add_tag_clear"

    # 검색창 선택
    category_Search = "content_category_Search"

    # 검색 후
    search_searchbar = "content_search_searchbar"

    # 배경음악 완료
    content_add_done = "bottom_bar_done_button"

    # 효과음
    sound_effect_button = "edit_add_sound_effect_button"

    # 음성 녹음
    voice_recording_button = "edit_add_voice_recording_button"

    # 녹음 완료
    voice_add_done = "voice_add_done"

    # 녹음 시작
    voice_recording = "voice icon recording"

    # 녹음 중지
    voice_recording_stop = "voice icon recording stop"

    # 파일명
    file_name_change = "파일명"

    # 녹음 파일명
    file_name = "파일명 :"

    # 녹음 듣기
    voice_recording_play = "듣기"

    # 녹음 정지
    voice_recording_pause = "정지"

    # 녹음 다시 듣기
    voice_recording_replay = "다시 듣기"

    # 녹음 여기로 이동
    voice_recording_move_here = "여기로 이동"

    # 글자 선택
    add_text_button = "edit_add_text_button"

    # 펜 선택
    palette_tool_pen = "palette_tool_pen_base"

    # 그리기 완료
    done1 = "완료"

    # 보정
    adjustment = "보정"

    # 보정 메뉴
    menu_filter_adjust = "deco_menu_filter_adjust"

    # 보정 밝기
    adjustment_brightness_button = "edit_filter_adjustment_brightness_button"
    # 보정 대조
    adjustment_contrast_button = "edit_filter_adjustment_contrast_button"
    # 보정 채도
    adjustment_saturation_button = "edit_filter_adjustment_saturation_button"
    # 보정 생동감
    adjustment_vibrance_button = "edit_filter_adjustment_vibrance_button"
    # 보정 온도
    adjustment_temperature_button = "edit_filter_adjustment_temperature_button"
    # 보정 틴트
    adjustment_tint_button = "edit_filter_adjustment_tint_button"
    # 보정 색조
    adjustment_hue_button = "edit_filter_adjustment_hue_button"
    # 보정 그림자
    adjustment_shadow_button = "edit_filter_adjustment_shadow_button"
    # 보정 하이라이트
    adjustment_highlight_button = "edit_filter_adjustment_highlight_button"
    # 보정 선명도
    adjustment_sharpness_button = "edit_filter_adjustment_sharpness_button"
    # 보정 강도
    adjustment_intensity_button = "edit_filter_adjustment_intensity_button"

    # 보정 룰러 값 조절 5.00
    ruler_value_5 = "edit_filter_adjustment_ruler_value_5.00"
    # 보정 룰러 값 조절 95.00
    ruler_value_95 = "edit_filter_adjustment_ruler_value_text_95.00"

    # 트랜지션 시간 조절 1.00
    transition_ruler_value_1 = "transition_duration_ruler_value_1.00"

    # 음량 강도 룰러 0.90
    edit_ruler_value_90 = "edit_value_ruler_value_0.90"

    # 오디오 이펙트 룰러
    audio_effect_ruler = "edit_audio_effect_intensity_ruler_collection_view"

    # 강도 룰러
    ruler_value = "edit_value_ruler"

    # 강도
    dB = "강도"

    # 페이드 상단 룰러
    ruler_value_animation = "edit_animation_duration_ruler"

    # 애니메이션 조절
    animation_duration_ruler = "edit_animation_duration_ruler"

    # 애니메이션 없음
    animation_none = "none"

    # 애니메이션에서 사용하는 아이디
    animation_id = [f"animation_{i}" for i in list(range(0, 16, 1))]
    animation_id_1 = "animation_1"
    animation_id_2 = [f"animation_{i}" for i in list(range(0, 12, 1))]
    # 팔레트에서 사용하는 아이디
    palette_id1 = [f"color_palette{i}_2" for i in list(range(0, 7, 1))]
    palette_id2 = [f"color_palette_category_{i}" for i in list(range(0, 11, 1))]

    # color_를 사용하는 아이디
    color_id = [f"color_{i}" for i in list(range(1, 10, 1))]

    # color_more_를 사용하는 아이디
    color_more_id = [f"color_more_{i}" for i in list(range(1, 16, 1))]

    # 특수효과애서 사용하는 콘텐츠 아이디
    content2_id = [f"content_2_{i}" for i in list(range(0, 11, 1))]
    content3_id = [f"content_3_{i}" for i in list(range(0, 12, 1))]
    content4_id = [f"content_4_{i}" for i in list(range(0, 9, 1))]
    content5_id = [f"content_4_{i}" for i in list(range(0, 6, 1))]

    # 오디오 이펙트 강도 조절
    audio_effect_ruler_value_60 = "edit_audio_effect_intensity_ruler_value_60.00"

    # 텍스트 강도 조절
    ruler_value_text_5 = "add_filter_strength_ruler_value_text_0.50"

    # 페이드 상단 수치 조절
    ruler_value_animation_15 = "edit_animation_duration_ruler_value_1.50"

    # 오디오 이펙트 상단 수치 조절
    ruler_value_audio_effect_5 = "edit_audio_effect_intensity_ruler_value_5.00"

    # def volumeRuler(self):
    #     a = [f"edit_value_ruler_value_{i:.2f}" for i in range(0.1, 1, 0.1)]
    #     random_item = random.choice(a)
    #     print(random_item, "볼륨 랜덤 선택 완료")

    # 강도 룰러
    edit_value_ruler = "edit_value_ruler_collection_view"

    # 회전 수치 조절
    transform_rotation_ruler_value_5 = "edit_transform_rotation_ruler_value_5.00"

    # 색상 불투명도 룰러
    recent_color_alpha_ruler = "recent_color_alpha_ruler_collection_view"

    # 색상 불투명도
    color_alpha_ruler_value_95 = "recent_color_alpha_ruler_value_0.95"

    # 블러 수치 조절
    bg_blur_ruler_value_05 = "edit_bg_blur_ruler_value_0.05"

    # 블러 룰러
    edit_bg_blur_ruler = "edit_bg_blur_ruler_collection_view"

    # 크기 조절
    transform_size_ruler_value_09 = "edit_transform_size_ruler_value_0.90"

    # 애니메이션 조절
    animation_duration_ruler_value_05 = "edit_animation_duration_ruler_value_0.50"

    # 위치 x값
    transform_x_ruler_value_text_45 = "edit_transform_x_ruler_value_text_0.45"

    # 위치 y값
    transform_y_ruler_value_text_45 = "edit_transform_y_ruler_value_text_0.45"

    # 오디오 분리
    deco_menu_audio_detach = "deco_menu_audio_detach"

    # 프로젝트 설정 버튼
    top_icon_setting = "editor top icon setting"

    # 상단 V버튼
    top_icon_done = "common top icon done"

    # 상단 튜토리얼
    top_icon_tutorial = "editor top icon tutorial"

    # 문의 > 튜토리얼
    tutorial = "tutorial"

    # 유튜브
    youtube = "share icon youtube"
    # 인스타
    instagram = "share icon instagram"
    # 페이스북
    facebook = "share icon facebook"

    # 튜토리얼 카테고리
    tutorial_category = [f"short_cut_{i}" for i in list(range(0, 27, 1))]

    # #배속
    tutorial_speed = "#배속"
    # 저작군
    tutorial_license = "저작권"
    # 키보드 단축키
    tutorial_keyboard = "키보드 단축키"

    # 재생 / 정지
    edit_play = "edit_play"

    editor_setting = "editor_top_icon_setting"

    # 전체 화면으로 보기
    screen_icon_full = "editor_screen_icon_full"

    # 10초 이후로 이동
    icon_skip_next = "fullscreen icon skip next"
    # 10초 이전으로 이동
    icon_skip_previous = "fullscreen icon skip previous"

    # 배속
    speed_full_screen = "speed_full_screen"

    # 0.5x
    full_screen_speed_0_5 = "full_screen_speed_0_5"
    # 1x
    full_screen_speed_1 = "full_screen_speed_1"
    # 1.5x
    full_screen_speed_1_5 = "full_screen_speed_1_5"
    # 2x
    full_screen_speed_2 = "full_screen_speed_2"

    # 데코 편집 메뉴 색상
    deco_menu_color = "deco_menu_color"

    # 색상 선택
    color_1 = "color_0"
    color_2 = "color_1"
    color_3 = "color_2"
    color_4 = "color_3"
    color_5 = "color_4"

    # 에코 & 리버브
    deco_menu_echo_reverb = "deco_menu_echo_reverb"

    # 보정 리셋
    adjustment_ruler_reset = "edit_filter_adjustment_ruler_reset"

    # 보정 초기화
    adjustment_reset_button = "edit_filter_adjustment_reset_button"

    # 필터 초기화
    strength_ruler_reset = "add_filter_strength_ruler_reset"

    # 강도 초기화
    intensity_ruler_reset = "add_distort_intensity_ruler_reset"

    # 트랜지션 초기화
    transition_ruler_reset = "transition_duration_ruler_reset"

    # 최근 사용 초기화
    content_recent_reset = "content_recent_reset"

    # 음량 강도 초기화
    edit_value_ruler_reset = "edit_value_ruler_reset"

    # 애니메이션 룰러 초기화
    animation_ruler_reset = "edit_animation_duration_ruler_reset"

    # 오디오 이펙트 룰러 초기화
    audio_effect_ruler_reset = "edit_audio_effect_intensity_ruler_reset"

    # 색상 초기화
    color_alpha_ruler_reset = "recent_color_alpha_ruler_reset"

    # 블러 초기화
    bg_blur_ruler_reset = "edit_bg_blur_ruler_reset"

    # 시간 초기화
    duration_ruler_reset = "edit_duration_ruler_reset"

    # x값 초기화
    transform_x_ruler_reset = "edit_transform_x_ruler_reset"

    # y값 초기화
    transform_y_ruler_reset = "edit_transform_y_ruler_reset"

    # 크기 초기화
    transform_size_ruler_reset = "edit_transform_size_ruler_reset"

    # 회전 초기화
    transform_rotation_ruler_reset = "edit_transform_rotation_ruler_reset"

    # 이퀄라이저 선택
    deco_menu_eq = "deco_menu_eq"

    # 내 필터 메뉴
    deco_menu_save = "deco_menu_save"

    # 크기 선택
    deco_transform_menu_size = "deco_transform_menu_size"

    # 삭제 동작
    select_delete_button1 = "content_select_delete_button_2_0"

    # 페이드
    clip_menu_fade = "clip_menu_fade"

    # 시작 페이드
    fade_in = "animation_0"

    # 끝 부분
    fade_out = "끝 부분"

    # 없음
    none = "없음"

    # 무음 구간 제거
    clip_silence_removal = "clip_menu_silence_removal"
    # 무음 구간 제거 핸들
    sr_volume_control = "sr_volume_control"
    # 무음 구간 제거 룰러
    sr_min_duration_ruler = "sr_min_duration_ruler_collection_view"
    # 무음 구간 제거 완료 버튼
    sr_button_done = "sr_button_done"
    # 무음 구간 제거 마진
    sr_button_menu_margin = "sr_button_menu_margin"
    # 마진 - 타이트
    sr_button_submenu_tight = "sr_button_submenu_tight"
    # 마진 - 기본
    sr_button_submenu_default = "sr_button_submenu_default"
    # 마진 - 여유
    sr_button_submenu_extra = "sr_button_submenu_extra"
    # 구간 재생
    sr_button_menu_play = "sr_button_menu_play"
    # 다음으로
    sr_button_submenu_next = "sr_button_submenu_next"
    # 이전으로
    sr_button_submenu_prev = "sr_button_submenu_prev"

    # 애니메이션에서 사용하는 아이디
    content_category_id = [f"content_category_{i}" for i in list(range(0, 20, 1))]

    # 카테고리 (쓰이는 부분이 많아서 특정할 수 없음)
    content_category_0 = "content_category_0"
    content_category_1 = "content_category_1"
    content_category_2 = "content_category_2"
    content_category_3 = "content_category_3"
    content_category_4 = "content_category_4"
    content_category_5 = "content_category_5"
    content_category_6 = "content_category_6"
    content_category_7 = "content_category_7"
    content_category_8 = "content_category_8"
    content_category_9 = "content_category_9"
    content_category_10 = "content_category_10"
    content_category_11 = "content_category_11"
    content_category_12 = "content_category_12"
    content_category_13 = "content_category_13"
    content_category_14 = "content_category_14"
    content_category_15 = "content_category_15"

    # 미디어 모드
    mediamode_fit = "edit common icon mediamode fit"
    mediamode_fil = "edit common icon mediamode fil"
    mediamode_cen = "edit common icon mediamode cen"

    # 원
    oval = "원"
    # 사각형
    rectangle = "사각형"

    # 강도 조절
    distort_intensity_ruler = "add_distort_intensity_ruler_collection_view"

    # 전체 화면 재생 / 일시 정지
    play_full_screen = "play_full_screen"

    # 전체 화면 캡쳐
    capture_full_screen = "capture_full_screen"

    # 전체 화면 닫기
    exit_full_screen = "exit_full_screen"

    # 웨이브폼 옵션 열기 / 닫기
    waveform_type_button = "filter_waveform_type_button"

    # 웨이브폼 옵션 왼쪽으로 넘기기
    waveform_type_arrow_left = "filter_waveform_type_arrow_left"

    # 웨이브폼 옵션 오른쪽으로 넘기기
    waveform_type_arrow_right = "filter_waveform_type_arrow_right"

    # 말풍선 뷰 옵션 열기 / 닫기
    deco_type_button = "filter_deco_type_button"

    # 말풍선 옵션 왼쪽으로 넘기기
    deco_type_arrow_left = "filter_deco_type_arrow_left"

    # 말풍선 옵션 오른쪽으로 넘기기
    deco_type_arrow_right = "filter_deco_type_arrow_right"

    # 스토리보드
    story_board_button = "edit_story_board_button"

    # 스토리보드 닫기
    storyboard_cancel = "storyboard_cancel"

    # 스토리보드 미리보기 on / off
    storyboard_expand = "storyboard_expand"

    # 스토리보드 복제
    storybard_duplicate = "storybard_duplicate"

    # 스토리보드 삭제
    storyboard_delete = "storyboard_delete"

    # 스토리보드 클립 선택
    storyboard_1 = "storyboard_0"
    storyboard_2 = "storyboard_1"
    storyboard_3 = "storyboard_2"
    storyboard_4 = "storyboard_3"
    storyboard_5 = "storyboard_4"

    # 스토리보드 완료
    storyboard_done = "storyboard_done"

    # 상단 눈 아이콘 on / off
    clip_top_icon_eye = "clip top icon eye"

    # 상단 그리드 아이콘 on / off
    clip_top_icon_grid = "clip top icon grid"

    # 상단 자석 아이콘 on / off
    clip_top_icon_magnet = "clip top icon magnet"

    # 처음부터
    from_the_start = "처음부터"

    # 여기부터
    from_now = "여기부터"

    # 분할
    split = "분할"

    # 여기까지
    until_now = "여기까지"

    # 끝까지
    until_the_end = "끝까지"

    crop_left = "deco_crop_left"
    crop_right = "deco_crop_right"
    crop_top = "deco_crop_top"
    crop_bottom = "deco_crop_bottom"


    # 클립 크기 변경 핸들
    overlay_resize = "overlay_resize"
    # 클립 회전 핸들
    overlay_rotate = "overlay_rotate"
    # 클립 크롭 버튼 위
    overlay_top_crop = "overlay_top_crop"
    # 클립 크롭 버튼 아래
    overlay_bottom_crop = "overlay_bottom_crop"
    # 클립 크롭 버튼 오른쪽
    overlay_right_crop = "clip_screen_edit_handle_icon_right.png"
    # 클립 크롭 버튼 왼쪽
    overlay_left_crop = "overlay_left_crop"
    # 클립 삭제 핸들
    overlay_delete = "overlay_delete"

    # 클립 좌측 핸들
    move_start_time_view = "move_start_time_view"

    # 클립 우측 핸들
    move_end_time_view = "move_end_time_view"

    # 클립 트랜지션
    timeline_clip_transition_1 = "timeline_clip_transition_0"
    timeline_clip_transition_2 = "timeline_clip_transition_1"
    timeline_clip_transition_3 = "timeline_clip_transition_2"
    timeline_clip_transition_4 = "timeline_clip_transition_3"
    timeline_clip_transition_5 = "timeline_clip_transition_4"

    # 정렬 핸들
    arrangement_handle = "editor_arrangement_icon_handle.png"

    # 정렬 1번
    own = "1"
    arrangement_bottom_button = "edit_arrangement_bottom_button"
    arrangement_top_button = "edit_arrangement_top_button"

    # 맨 앞으로
    move_to_start = "맨 앞으로"

    # 왼쪽으로 이동
    move_to_left = "왼쪽으로 이동"

    # 오른쪽으로 이동
    move_to_right = "오른쪽으로 이동"

    # 맨 뒤로
    move_to_end = "맨 뒤로"

    # 클립 음소거 on / off
    clip_menu_mute = "clip_menu_mute"

    # 음량
    clip_menu_volume = "clip_menu_volume"

    # 데코 음소거 on / off
    deco_menu_mute = "deco_menu_mute"

    # 음량
    deco_menu_volume = "deco_menu_volume"

    # 데코 페이드 선택
    deco_menu_fade = "deco_menu_fade"

    # 데코 오디오 효과
    deco_menu_audio_effect = "deco_menu_audio_effect"

    # 클립 에코 & 리버브
    clip_menu_echo_reverb = "clip_menu_echo_reverb"

    # 클립 오디오 효과
    clip_menu_audio_effect = "clip_menu_audio_effect"

    # 클립 오디오 분리
    clip_menu_audio_detach = "clip_menu_audio_detach"

    # 클립 배경
    clip_menu_bg = "clip_menu_bg"

    # 배경 블러
    bg_blur = "bg_blur"

    # 배경 색상
    bg_solid_color = "bg_solid_color"

    # 색상 더보기
    color_more = "color_more"

    # 팔레트 선택
    palette = "palette"

    # 배경 스포이드
    spoid_button = "more_color_spoid_button"

    # 팔레트 색상
    color_palette_1 = "color_palette0_0"
    color_palette_2 = "color_palette1_0"
    # color_palette_3 = "color_palette0_0"
    # color_palette_4 = "color_palette0_0"
    # color_palette_5 = "color_palette0_0"

    # 하단 팔레트 색상
    color_palette_category_1 = "color_palette_category_1"
    color_palette_category_2 = "color_palette_category_2"

    # 피커
    picker = "picker"

    # 피커 왼쪽
    picker_hue = "color_picker_hue"

    # 피커 중앙
    picker_saturation = "color_picker_saturation"

    # 피커 오른쪽
    picker_alpha = "color_picker_alpha"

    # 슬라이더 레드 룰러
    slider_red_ruler = "color_slider_red_ruler_collection_view"

    # 슬라이더 RBG
    R = "R"
    G = "G"
    B = "B"

    # 슬라이더 그린 룰러
    slider_green_ruler = "color_slider_green_ruler_collection_view"

    # 슬라이더 룰러 리셋
    red_ruler_reset = "color_slider_red_ruler_reset"
    green_ruler_reset = "color_slider_green_ruler_reset"
    blue_ruler_reset = "color_slider_blue_ruler_reset"

    # 크기변경 하단 메뉴 / 위치 크기 회전 반전 크롭 순
    menu_position = "deco_transform_menu_position"
    menu_size = "deco_transform_menu_size"
    menu_rotation = "deco_transform_menu_rotation"
    menu_flip = "deco_transform_menu_flip"
    menu_crop = "deco_transform_menu_crop"

    # 위치 룰러
    x = 'X'
    edit_x_ruler = "edit_transform_x_ruler"
    y = "Y"
    edit_y_ruler = "edit_transform_y_ruler"

    # 슬라이더 블루 룰러
    slider_blue_ruler = "color_slider_blue_ruler_collection_view"

    # 크기 룰
    edit_size_ruler = "edit_transform_size_ruler"
    # 회전 룰러
    edit_rotation_ruler = "edit_transform_rotation_ruler"

    # 슬라이더
    slider = "slider"

    # 색상 완료
    color_solid_done = "color_solid_done"

    # 그라데이션
    bg_gradient = "bg_gradient"

    # 우측 스포이드
    recent_color_spoid_button = "recent_color_spoid_button"

    # 그라데이션
    color_more_1 = "color_more_1"

    # 그라데이션 완료
    color_gradient_done = "color_gradient_done"

    # 배경 패턴
    bg_pattern = "bg_pattern"

    # 패턴 완료
    color_pattern_done = "color_pattern_done"

    # 시간
    clip_menu_duration = "clip_menu_duration"

    # 시간 항목 리스트
    deco_duration_list = [f"deco_duration_{i}" for i in list(range(0, 5, 1))]

    # 크기 변경
    clip_menu_resize = "clip_menu_resize"

    # 회전
    transform_menu_rotation = "deco_transform_menu_rotation"

    # -45° 선택
    minus_45 = "-45°"
    # +45° 선택
    plus_45 = "+45°"

    # 반전 선택
    deco_transform_menu_flip = "deco_transform_menu_flip"

    # 상하 반전
    upside_down = "상하 반전"

    # 좌우 반전
    switch_sides = "좌우 반전"

    # 레이아웃 선택
    clip_menu_layout = "clip_menu_layout"

    # 첫 번째 레이아웃 제목
    edit_layout_title_button_0 = "edit_layout_title_button_0"

    # 복사
    copy = "copy"

    # 레이아웃 삭제
    edit_layout_delete_button_0 = "edit_layout_delete_button_0"

    # 애니메이션 선택
    clip_menu_animation = "clip_menu_animation"

    # 애니메이션 전체
    overall = "전체"

    # 특수효과
    clip_menu_effect = "clip_menu_effect"

    # "RGB1"
    rgb1 = "RGB1"

    # 애니메이션 강도 조절
    effect_intensity_ruler_value_45 = "edit_effect_intensity_ruler_value_0.45"

    # 애니메이션 강도 룰러
    effect_intensity_ruler = "edit_effect_intensity_ruler"

    # 강도 초기화
    effect_intensity_ruler_reset = "edit_effect_intensity_ruler_reset"

    # 값 조절
    effect_value_ruler_value_10 = "edit_effect_value_ruler_value_10.00"

    # 값 초기화
    effect_value_ruler_reset = "edit_effect_value_ruler_reset"

    # 배속 선택
    clip_menu_speed = "clip_menu_speed"

    # 0.2x
    speed0 = "speed_0_2"
    # 0.5x
    speed1 = "speed_0_5"
    # 1x
    speed2 = "speed_1"
    # 2x
    speed3 = "speed_2"
    # 4x
    speed4 = "speed_4"
    # 8x
    speed5 = "speed_8"

    # 배속 룰러
    edit_speed_ruler = "edit_speed_ruler_collection_view"

    # 시간 룰러
    edit_duration_ruler = "edit_duration_ruler_collection_view"

    # 배속 룰러 초기화
    speed_ruler_reset = "edit_speed_ruler_reset"

    # 불투명도
    clip_menu_opacity = "clip_menu_opacity"

    # 프리즈
    clip_menu_freeze = "clip_menu_freeze"

    # 배경 제거
    clip_menu_matte_effect = "clip_menu_matte_effect"

    # 배경 제거 토근 on / off
    edit_matte_effect_toggle = "edit_matte_effect_toggle"

    # 민감도 룰러
    edit_matte_effect_ruler = "edit_matte_effect_sensitivity_ruler_collection_view"

    # 민감도 초기화
    matte_effect_ruler_reset = "edit_matte_effect_sensitivity_ruler_reset"

    # 웨이브폼 필터
    waveform_type_button = "filter_waveform_type_button"

    # 크로마키 포인터
    pixel_reader_color = "pixel_reader_color_preview"

    # 크로마키 채도 룰러
    chromakey_saturation_ruler = "edit_chromakey_saturation_ruler_collection_view"

    # 크로마키 채도 초기화
    chromakey_saturation_ruler_reset = "edit_chromakey_saturation_ruler_reset"

    # 채도
    saturation = "채도"

    # 크로마키 밝기 룰러
    chromakey_value_ruler = "edit_chromakey_value_ruler_collection_view"

    # 크로마키 밝기 초기화
    chromakey_value_ruler_reset = "edit_chromakey_value_ruler_reset"

    # 밝기
    brightness = "밝기"

    # 크로마키 색조 룰러
    chromakey_hue_ruler = "edit_chromakey_hue_ruler"

    # 크로마키 색조 초기화
    chromakey_hue_ruler_reset = "edit_chromakey_hue_ruler_reset"

    # 색조
    hue = "색조"

    # 크로마키
    clip_menu_chromakey = "clip_menu_chromakey"

    # 채도 조절
    chromakey_saturation_ruler_value_01 = "edit_chromakey_saturation_ruler_value_0.15"

    # 채도 초기화
    chromakey_saturation_ruler_reset = "edit_chromakey_saturation_ruler_reset"

    # 밝기 조절
    chromakey_value_ruler_value_01 = "edit_chromakey_value_ruler_value_0.15"

    # 밝기 초기화
    chromakey_value_ruler_reset = "edit_chromakey_value_ruler_reset"

    # 색조 조절
    chromakey_hue_ruler_value_15 = "edit_chromakey_hue_ruler_value_0.15"

    # 색조 초기화
    chromakey_hue_ruler_reset = "edit_chromakey_hue_ruler_reset"

    # 크로마키 스포이드
    chromakey_spoid = "chromakey_spoid"

    # 크로마키 초기화
    chromakey_reset = "chromakey_reset"

    # 블러 선택
    clip_menu_blur = "clip_menu_blur"

    # 블러 룰러
    blur_ruler = "edit_value_ruler_collection_view"

    # PIP 복제
    clip_menu_duplicate_pip = "clip_menu_duplicate_pip"

    # 복제
    clip_menu_duplicate = "clip_menu_duplicate"

    # 키프레임 on / off
    keyframe_multi_switch = "keyframe_multi_switch"

    # 키프레임 추가
    add_key_frame_button = "edit_add_key_frame_button"

    # 색상
    text_solid_color_button = "text_solid_color_button"

    # 서식 그라데이션
    text_gradient_color_button = "text_gradient_color_button"

    # 서식 외곽선
    text_outline_button = "text_outline_button"

    # 서식 두께 룰러
    text_outline_width_ruler = "edit_text_outline_width_ruler_collection_view"
    text_outline_width_ruler_reset = "edit_text_outline_width_ruler_reset"

    #서식 배경, 그라데이션, 배경
    text_bg_solid_color_button = "text_bg_solid_color_button"
    text_bg_gradient_color_button = "text_bg_gradient_color_button"
    text_bg_pattern_color_button = "text_bg_pattern_color_button"

    # 패턴
    bg_pattern_color_button = "bg_pattern_color_button"

    # 글자 색상
    deco_menu_label_color = "deco_menu_label_color"

    # 크기 변경
    deco_menu_resize = "deco_menu_resize"

    # 위치 x값 조절
    transform_x_ruler_value_45 = "edit_transform_x_ruler_value_0.45"

    # 위치 y값 조절
    transform_y_ruler_value_45 = "edit_transform_y_ruler_value_0.45"

    # 크롭
    deco_transform_menu_crop = "deco_transform_menu_crop"

    # 애니메이션
    deco_menu_animation = "deco_menu_animation"

    # 특수효과
    deco_menu_effect = "deco_menu_effect"

    # 배속
    deco_menu_speed = "deco_menu_speed"

    # 불투명도
    deco_menu_opacity = "deco_menu_opacity"

    # 프리즈
    deco_menu_freeze = "deco_menu_freeze"

    # 비디오
    video = "비디오"
    video2 = "video"

    # GIF
    gif = "GIF"

    # 프로젝트
    project = "project"

    # 자막
    caption = "caption"

    # 배경 제거
    deco_menu_matte_effect = "deco_menu_matte_effect"

    # 크로마키
    deco_menu_chromakey = "deco_menu_chromakey"

    # 정렬
    deco_menu_arrangement = "deco_menu_arrangement"

    # fold up / down
    arrangement_fold_button = "edit_arrangement_fold_button"

    # 맨 아래로
    bottom = "맨 아래로"

    # 맨 위로
    top = "맨 위로"

    # 혼합
    deco_menu_blend = "deco_menu_blend"

    # 혼합 불투명도
    blend_opacity_ruler_value_90 = "edit_blend_opacity_ruler_value_0.90"

    # 블랜딩 초기화
    blend_opacity_ruler_reset = "edit_blend_opacity_ruler_reset"

    # 폰트
    deco_menu_font = "deco_menu_font"

    # 글자 크기
    deco_menu_text_size = "deco_menu_text_size"

    # 글자 크기 룰러
    edit_text_size_ruler = "edit_text_size_ruler_collection_view"

    # 글자 부분 설정 전체 선택
    text_word_select_all = "text_word_select_0_0"
    # 글자 부분 설정 개별
    text_chracter_select1 = "text_chracter_select_0_1"
    text_chracter_select2 = "text_chracter_select_0_2"
    text_chracter_select3 = "text_chracter_select_0_3"

    # 크기 조절
    text_size_ruler_value_330 = "edit_text_size_ruler_value_330.00"

    # 첫 번째 어절
    text_chracter_select_1 = "text_chracter_select_0_1"
    text_chracter_select_2 = "text_chracter_select_0_2"
    text_chracter_select_3 = "text_chracter_select_0_3"
    text_chracter_select_4 = "text_chracter_select_0_4"
    text_chracter_select_5 = "text_chracter_select_0_5"

    # 어절 선택 해제
    text_common_edit_style_partial = "text common edit style partial"

    # 글자 크기
    deco_menu_caption_text_size = "deco_menu_caption_text_size"

    # 크기 조절
    caption_size_ruler_value_20 = "edit_caption_size_ruler_value_20.00"

    # 크기 룰러 초기화
    caption_size_ruler_reset = "edit_caption_size_ruler_reset"

    # 글자 편집
    deco_menu_text = "deco_menu_text"

    # 글자 입력 텍스트 필드
    edit_input_text_view = "edit_input_text_view"

    # 서식
    deco_menu_text_style = "deco_menu_text_style"

    # 글자 색상
    text_color_button = "text_text_color_button"

    # 배경색
    text_bg_color_button = "text_bg_color_button"

    # 그림자
    text_shadow_button = "text_shadow_button"

    text_shadow_solid_color_button = "text_shadow_solid_color_button"

    # 각도
    text_shadow_angle_button = "text_shadow_angle_button"

    # 흐림 정도
    text_shadow_blur_radius_button = "text_shadow_blur_radius_button"

    # 흐림 룰러 조절
    text_shadow_blur_radius_ruler_value_1 = "edit_text_shadow_blur_radius_ruler_value_1.00"

    # 강조
    text_emphasis_button = "text_emphasis_button"

    # 기울기 on / off
    text_emphasis_italic_button = "text_emphasis_italic_button"

    # 굵기 on / off
    text_emphasis_bold_button = "text_emphasis_bold_button"

    # 밑줄 on / off
    text_emphasis_underline_button = "text_emphasis_underline_button"

    # 취소선 on / off
    text_emphasis_strike_through_button = "text_emphasis_strike_through_button"

    text_emphasis_list = [text_emphasis_italic_button, text_emphasis_bold_button,
                          text_emphasis_underline_button, text_emphasis_strike_through_button]
    # 간격
    text_spacing_button = "text_spacing_button"

    # 교체
    deco_menu_replace = "deco_menu_replace"
    clip_menu_replace = "clip_menu_replace"

    # X 버튼
    replace_cancel = "replace_cancel"

    # ◁l 1프레임 앞으로 선택
    clip_timeline_icon_previ = "editor cliptimeline icon previ"

    # ▷l 1프레임 뒤로 선택
    clip_timeline_icon_end = "editor cliptimeline icon end n"

    # 재생
    screen_icon_play = "editor screen icon play"

    # 정지
    screen_icon_pause = "editor screen icon pause"

    # 교체 타임라인
    timeline = "timeline"

    # 교체 완료
    replace_done = "replace_done"

    # 강도
    deco_menu_intensity = "deco_menu_intensity"

    # 강도 수치
    value_ruler_value_50 = "edit_value_ruler_value_0.50"

    # 모양
    deco_menu_mosaic_shape = "deco_menu_mosaic_shape"

    # 페더
    deco_menu_feather = "deco_menu_feather"

    # 페더 강도 조절
    edit_value_ruler_value_20 = "edit_value_ruler_value_0.20"

    # 반전 on /off
    deco_menu_invert = "deco_menu_invert"

    # 트래킹
    deco_menu_tracking = "deco_menu_tracking"

    # 트래킹하기
    tracking_start_button = "edit_tracking_start_button"

    # 다시하기
    tracking_retry_button = "edit_tracking_retry_button"

    # 트래킹 추가
    tracking_add_button = "edit_tracking_add_button"

    # 트래킹 해제
    tracking_delete_button = "edit_tracking_delete_button"

    # 역방향 on / off
    clip_menu_reverse = "clip_menu_reverse"
    deco_menu_reverse = "deco_menu_reverse"

    # 모션 멈추기 on / off
    deco_menu_pause = "deco_menu_pause"

    # 여기로 이동
    deco_menu_move = "deco_menu_move"

    # 복제
    deco_menu_duplicate = "deco_menu_duplicate"

    # 전체 적용하기
    menu_apply_to_all = "menu_apply_to_all"

    # 취소 선택
    deco_apply_cancel = "deco_apply_cancel"

    # 클립2 선택
    apply_0 = "apply_0"

    # 전체 적용하기 확인
    deco_apply_done = "deco_apply_done"

    # 테두리
    deco_stroke_menu_color = "deco_stroke_menu_color"

    # 선 테두리
    deco_menu_stroke = "deco_menu_stroke"

    # 두께
    deco_stroke_menu_width = "deco_stroke_menu_width"

    # 두께 룰러 조절
    text_size_ruler_value_24 = "edit_text_size_ruler_value_2.40"

    # 두께 초기화
    text_size_ruler_reset = "edit_text_size_ruler_reset"

    # 선 끝
    deco_stroke_menu_edge = "deco_stroke_menu_edge"

    # 선 끝 1번 항목
    stroke_type_edge_butt = "stroke_type_edge_butt"

    # 선 끝 2번 항목
    stroke_type_edge_round = "stroke_type_edge_round"

    # 선 끝 3번 항목
    stroke_type_edge_square = "stroke_type_edge_square"

    # 선 종류
    deco_stroke_menu_dash = "deco_stroke_menu_dash"

    # 선 종류 1번 항목
    stroke_type_dash_line = "stroke_type_dash_line"

    # 선 종류 2번 항목
    stroke_type_dash_dot1 = "stroke_type_dash_dot1"

    # 선 종류 3번 항목
    stroke_type_dash_dot2 = "stroke_type_dash_dot2"

    # 앞머리
    deco_stroke_menu_start_point = "deco_stroke_menu_start_point"

    # 앞머리 1번 항목
    start_point_none = "start_point_none"

    # 앞머리 2번 항목
    start_point_circle = "start_point_circle"

    # 앞머리 3번 항목
    start_point_square = "start_point_square"

    # 앞머리 4번 항목
    start_point_diamond = "start_point_diamond"

    # 앞머리 5번 항목
    start_point_arrow_fill = "start_point_arrow_fill"

    # 앞머리 6번 항목
    start_point_arrow_fill_round = "start_point_arrow_fill_round"

    # 앞머리 7번 항목
    start_point_arrow_stroke = "start_point_arrow_stroke"

    # 앞머리 8번 항목
    start_point_arrow_stroke_round = "start_point_arrow_stroke_round"

    # 앞머리 9번 항목
    start_point_flipped_arrow_fill = "start_point_flipped_arrow_fill"

    # 앞머리 10번 항목
    start_point_flipped_arrow_fill_round = "start_point_flipped_arrow_fill_round"

    # 뒷머리
    deco_stroke_menu_end_point = "deco_stroke_menu_end_point"

    # 앞머리 1번 항목
    end_point_none = "end_point_none"

    # 앞머리 2번 항목
    end_point_circle = "end_point_circle"

    # 앞머리 3번 항목
    end_point_square = "end_point_square"

    # 앞머리 4번 항목
    end_point_diamond = "end_point_diamond"

    # 앞머리 5번 항목
    end_point_arrow_fill = "end_point_arrow_fill"

    # 앞머리 6번 항목
    end_point_arrow_fill_round = "end_point_arrow_fill_round"

    # 앞머리 7번 항목
    end_point_arrow_stroke = "end_point_arrow_stroke"

    # 앞머리 8번 항목
    end_point_arrow_stroke_round = "end_point_arrow_stroke_round"

    # 앞머리 9번 항목
    end_point_flipped_arrow_fill = "end_point_flipped_arrow_fill"

    # 앞머리 10번 항목
    end_point_flipped_arrow_fill_round = "end_point_flipped_arrow_fill_round"

    # 테두리 배치
    deco_stroke_menu_align = "deco_stroke_menu_align"

    # 테두리 1번 항목
    stroke_type_align_center = "stroke_type_align_center"

    # 테두리 2번 항목
    stroke_type_align_inner = "stroke_type_align_inner"

    # 테두리 3번 항목
    stroke_type_align_outer = "stroke_type_align_outer"

    # 왜곡 선곡
    add_distort_button = "edit_add_distort_button"

    # fold
    fold = "content_expand"

    # BGM 진입
    add_bgm_button = "edit_add_bgm_button"

    # 모션 스티커
    add_sticker_button = "edit_add_sticker_button"
    vllo_button = "sticker_add_vllo_button"
    giphy_button = "sticker_add_giphy_button"

    giphy_bookmark_button = "giphy_select_bookmark_button"
    giphy_recents_button = "giphy_select_recents_button"
    giphy_trending_button = "giphy_select_trending_button"
    giphy_search_button = "giphy_select_search_button"
    giphy_search_back_button = "giphy_select_search_back_button"
    # 프레임 선택
    add_frame_button = "edit_add_frame_button"
    # 템플릿 선택
    add_template_button = "edit_add_template_button"
    # 그리기 & 도형 선택
    add_shape_button = "edit_add_shape_button"

    # giphy 저작권
    giphy_license_button = "giphy_select_license_button"

    # 라벨 진입
    add_label_button = "edit_add_label_button"
    # 자막 진입
    add_caption_button = "edit_add_caption_button"
    # 필터 진입
    add_filter_button = "edit_add_filter_button"
    # 특수효과 진입
    add_effect_button = "edit_add_effect_button"
    # 추출하기
    top_icon_export = "editor_top_icon_export"

    resolution = "해상도"

    resolution_4k = "resolution_4k"
    resolution_QHD = "resolution_best"
    resolution_high = "resolution_high"
    resolution_medium = "resolution_medium"
    resolution_low = "resolution_low"
    resolution_category = [resolution_4k, resolution_QHD, resolution_high,
                           resolution_medium, resolution_low]

    framerate = "프레임레이트"
    framerate1 = "framerate_18"
    framerate2 = "framerate_24"
    framerate3 = "framerate_25"
    framerate4 = "framerate_30"
    framerate5 = "framerate_48"
    framerate6 = "framerate_50"
    framerate7 = "framerate_60"
    framerate_category = [framerate1, framerate2, framerate3,
                          framerate4, framerate5, framerate6,
                          framerate7]

    iButton1 = "추가 정보"
    h264 = "codec_h_264"
    h265 = "codec_h_265"
    iButton2 = "alarm_info"
    alarm_on = "alarm_on"
    alarm_off = "alarm_off"

    export_button = "export_button"
    share_icon_done_line = "share_icon_done_line"
    share_top_icon_home = "share top icon home"
    ## 공통으로 쓰이는 카테고리-------------------------------------------------------------
    # 전체
    category_All = "content_category_All"
    # 파일 선택
    category_Files = "content_category_Files"
    # NEW
    category_New = "content_category_New"
    # 북마크
    category_Bookmark = "content_category_Bookmark"
    # 최근 사용
    category_Recents = "content_category_Recents"

    midea_stock_1 = "content_category_pkg_media_stock_intro"
    midea_stock_2 = "content_category_pkg_media_stock_outro"
    midea_stock_3 = "content_category_pkg_media_stock_transition"
    midea_stock_4 = "content_category_pkg_media_stock_background"
    midea_stock_5 = "content_category_pkg_media_stock_frame"
    midea_stock_6 = "content_category_pkg_media_stock_glitter"
    midea_stock_7 = "content_category_pkg_media_stock_gradient"
    midea_stock_8 = "content_category_pkg_media_stock_season"
    midea_stock_9 = "content_category_pkg_media_stock_countdown"
    midea_stock_10 = "content_category_pkg_media_stock_game"
    midea_stock_11 = "content_category_pkg_media_stock_scifi"
    # 스톡 카테고리
    midea_stock_category = [midea_stock_1, midea_stock_2, midea_stock_3,
                            midea_stock_4, midea_stock_5, midea_stock_6,
                            midea_stock_7, midea_stock_8, midea_stock_9,
                            midea_stock_10, midea_stock_11]
    ## 오디오 - 배경음악 카테고리-------------------------------------------------------------
    # 아이튠즈
    category_iTunes = "content_category_iTunes"
    bgm_category1 = "content_category_pkg_bgm_daily"
    bgm_category2 = "content_category_pkg_bgm_vlog"
    bgm_category3 = "content_category_pkg_bgm_cafe"
    bgm_category4 = "content_category_pkg_bgm_kid_and_pet"
    bgm_category5 = "content_category_pkg_bgm_travel"
    bgm_category6 = "content_category_pkg_bgm_love"
    bgm_category7 = "content_category_pkg_bgm_wedding_and_propose"
    bgm_category8 = "content_category_pkg_bgm_entertainment"
    bgm_category9 = "content_category_pkg_bgm_advertisement"
    bgm_category10 = "content_category_pkg_bgm_cinematic"
    bgm_category11 = "content_category_pkg_bgm_game"
    bgm_category12 = "content_category_pkg_bgm_season"
    bgm_category13 = "content_category_pkg_bgm_beauty_and_fashion"
    bgm_category14 = "content_category_pkg_bgm_party_and_club"
    bgm_category = [bgm_category1, bgm_category2, bgm_category3,
                    bgm_category4, bgm_category5, bgm_category6,
                    bgm_category7, bgm_category8, bgm_category9,
                    bgm_category10, bgm_category11, bgm_category12,
                    bgm_category13, bgm_category14]
    ## 오디오 - 효과음 카테고리-------------------------------------------------------------

    bgm_category1 = "content_category_pkg_sound_fx_life_sounds"
    bgm_category2 = "content_category_pkg_sound_fx_effect"
    bgm_category3 = "content_category_pkg_sound_fx_human"
    bgm_category4 = "content_category_pkg_sound_fx_animal"
    bgm_category5 = "content_category_pkg_sound_fx_nature"
    bgm_category6 = "content_category_pkg_sound_fx_cartoon"
    bgm_category7 = "content_category_pkg_sound_fx_clap_and_spectator"
    bgm_category8 = "content_category_pkg_sound_fx_footsteps"
    bgm_category9 = "content_category_pkg_sound_fx_bell_and_siren"
    bgm_category10 = "content_category_pkg_sound_fx_instrument"
    bgm_category11 = "content_category_pkg_sound_fx_action_and_horror"
    bgm_category12 = "content_category_pkg_sound_fx_weapon_and_war"
    bgm_category13 = "content_category_pkg_sound_fx_transportation"

    soundEffect_category = [bgm_category1, bgm_category2, bgm_category3,
                            bgm_category4, bgm_category5, bgm_category6,
                            bgm_category7, bgm_category8, bgm_category9,
                            bgm_category10, bgm_category11, bgm_category12,
                            bgm_category13]
    ## 그래픽 - 모션 스티커 카테고리-------------------------------------------------------------
    sticker_category1 = "content_category_pkg_sticker_basic"
    sticker_category2 = "content_category_pkg_sticker_shape"
    sticker_category3 = "content_category_pkg_sticker_line"
    sticker_category4 = "content_category_pkg_sticker_type"
    sticker_category5 = "content_category_pkg_sticker_123"
    sticker_category6 = "content_category_pkg_sticker_memo"
    sticker_category7 = "content_category_pkg_sticker_speechbubble"
    sticker_category8 = "content_category_pkg_sticker_sns"
    sticker_category9 = "content_category_pkg_sticker_effect"
    sticker_category10 = "content_category_pkg_sticker_pointing"
    sticker_category11 = "content_category_pkg_sticker_emotion"
    sticker_category12 = "content_category_pkg_sticker_rating"
    sticker_category13 = "content_category_pkg_sticker_fashion"
    sticker_category14 = "content_category_pkg_sticker_diary"
    sticker_category15 = "content_category_pkg_sticker_travel"
    sticker_category16 = "content_category_pkg_sticker_love"
    sticker_category17 = "content_category_pkg_sticker_food"
    sticker_category18 = "content_category_pkg_sticker_season"
    sticker_category19 = "content_category_pkg_sticker_cute"
    sticker_category20 = "content_category_pkg_sticker_fun"
    sticker_category21 = "content_category_pkg_sticker_sketch"

    sticker_category = [sticker_category1, sticker_category2, sticker_category3, sticker_category4,
                        sticker_category5, sticker_category6, sticker_category7, sticker_category8,
                        sticker_category9, sticker_category10, sticker_category11, sticker_category12,
                        sticker_category13, sticker_category14, sticker_category15, sticker_category16,
                        sticker_category17, sticker_category18, sticker_category19, sticker_category20,
                        sticker_category21]
    ## 그래픽 - 프레임 카테고리---------------------------------------------------------
    frame_category1 = "content_category_pkg_frame_basic"
    frame_category2 = "content_category_pkg_frame_line"
    frame_category3 = "content_category_pkg_frame_film"
    frame_category4 = "content_category_pkg_frame_vlog"
    frame_category5 = "content_category_pkg_frame_fashion"
    frame_category6 = "content_category_pkg_frame_daily"
    frame_category7 = "content_category_pkg_frame_season"
    frame_category = [frame_category1, frame_category2, frame_category3,
                      frame_category4, frame_category5, frame_category6,
                      frame_category7]
    ## 그래픽 - 템플릿 카테고리----------------------------------------------------------
    template_category1 = "content_category_pkg_template_fun"
    template_category2 = "content_category_pkg_template_twinkle"
    template_category3 = "content_category_pkg_template_love"
    template_category4 = "content_category_pkg_template_film"
    template_category5 = "content_category_pkg_template_season"
    template_category6 = "content_category_pkg_template_festival"
    template_category = [template_category1, template_category2, template_category3,
                         template_category4, template_category5, template_category6]
    ## 그래픽 - 도형 카테고리------------------------------------------------------------
    # 그리기 & 도형 선택
    category_pkg_shape_drawing_line = "content_category_pkg_shape_drawing_line"
    # 도형 선택
    category_pkg_shape_shape = "content_category_pkg_shape_shape"

    ## 글자 - 글자 카테고리-------------------------------------------------------------
    text_category1 = "content_category_pkg_text_basic"
    text_category2 = "content_category_pkg_text_caption"
    text_category3 = "content_category_pkg_text_intro"
    text_category4 = "content_category_pkg_text_Thumbnail"
    text_category5 = "content_category_pkg_text_vlog"
    text_category6 = "content_category_pkg_text_fashion_beauty"
    text_category7 = "content_category_pkg_text_season"
    text_category8 = "content_category_pkg_text_emotion"
    text_category = [text_category1, text_category2, text_category3,
                     text_category4, text_category5, text_category6,
                     text_category7, text_category8]
    ## 글자 - 라벨 카테고리-------------------------------------------------------------
    # 노트 선택
    label_category1 = "content_category_pkg_label_note"
    label_category2 = "content_category_pkg_label_tag"
    label_category3 = "content_category_pkg_label_title"
    label_category4 = "content_category_pkg_label_bubble"
    label_category5 = "content_category_pkg_label_shape"
    label_category6 = "content_category_pkg_label_sns"
    label_category7 = "content_category_pkg_label_pcphone"
    label_category8 = "content_category_pkg_label_season"
    label_category = [label_category1, label_category2, label_category3,
                      label_category4, label_category5, label_category6,
                      label_category7, label_category8]
    ## 글자 - 자막 카테고리-------------------------------------------------------------
    caption_category1 = "content_category_pkg_caption_basic"
    caption_category2 = "content_category_pkg_caption_vlog"
    caption_category3 = "content_category_pkg_caption_diary"
    caption_category4 = "content_category_pkg_caption_fashion"
    caption_category5 = "content_category_pkg_caption_love"
    caption_category6 = "content_category_pkg_caption_beauty"
    caption_category7 = "content_category_pkg_caption_cute"
    caption_category8 = "content_category_pkg_caption_season"
    caption_category9 = "content_category_pkg_caption_name"
    caption_category10 = "content_category_pkg_caption_sns"
    caption_category = [label_category1, label_category2, label_category3,
                        label_category4, label_category5, label_category6,
                        label_category7, label_category8, label_category8,
                        label_category8, label_category8]
    ## 폰트 카테고리
    font_category1 = "content_category_pkg_user_created"
    font_category2 = "content_category_pkg_font_basic"
    font_category3 = "content_category_en"
    font_category4 = "content_category_ko"
    font_category5 = "content_category_ja"
    font_category6 = "content_category_th"
    font_category7 = "content_category_zh-tw"
    font_category = [font_category1, font_category2, font_category3,
                     font_category4, font_category5, font_category6,
                     font_category7]
    # 필터 카테고리
    ## 폰트 카테고리
    filter_category1 = "content_category_1"
    filter_category2 = "content_category_2"
    filter_category3 = "content_category_3"
    filter_category4 = "content_category_4"
    filter_category5 = "content_category_5"
    filter_category6 = "content_category_6"
    filter_category7 = "content_category_7"
    filter_category8 = "content_category_8"
    filter_category9 = "content_category_9"
    filter_category10 = "content_category_10"
    filter_category11 = "content_category_11"
    filter_category12 = "content_category_12"
    filter_category13 = "content_category_13"
    filter_category14 = "content_category_14"
    filter_category15 = "content_category_15"
    filter_category16 = "content_category_16"
    filter_category17 = "content_category_17"
    filter_category = [filter_category1, filter_category2, filter_category3,
                       filter_category4, filter_category5, filter_category6,
                       filter_category7, filter_category8, filter_category9,
                       filter_category10, filter_category11, filter_category12,
                       filter_category13, filter_category14, filter_category15,
                       filter_category16, filter_category17]
    ## 효과 - 특수효과 카테고리-------------------------------------------------------------
    effect_category1 = "content_category_pkg_effect_basic"
    effect_category2 = "content_category_pkg_effect_color"
    effect_category3 = "content_category_pkg_effect_retro"
    effect_category4 = "content_category_pkg_effect_glitch"
    effect_category5 =  "content_category_pkg_effect_light"
    effect_category6 = "content_category_pkg_effect_lens"
    effect_category7 = "content_category_pkg_effect_motion"
    effect_category8 = "content_category_pkg_effect_split"
    effect_category = [effect_category1, effect_category2, effect_category3,
                       effect_category4, effect_category5, effect_category6,
                       effect_category7, effect_category8]
    ##효과 - 왜곡
    distort_category1 = "distort_blur_button"
    distort_category2 = "distort_pixellate_button"
    distort_category3 = "distort_zoom_button"
    distort_category4 = "distort_fish_eye_button"
    distort_category5 = "distort_twirl_button"

    distort_category = [distort_category1, distort_category2, distort_category3,
                        distort_category4, distort_category5]

    timeline_clip_transition = ["timeline_clip_transition_" + str(i) for i in range(115)]

    # 추출 상단
    export_category = [video2, gif, project, caption]

    # 오디오 타임라인
    bottom_audio = "bottom_audio"
    # 그래픽 타임라인
    bottom_graphic = "bottom_graphic"

    # 글자 타임라인
    bottom_text = "bottom_text"
    # PIP 타임라인
    bottom_pip = "bottom_pip"
    # 필터 타임라인
    bottom_effect = "bottom_effect"

    # 백그라운드 블로 활성화 시 필요한 아이디
    activate_vllo = "com.darinsoft.vimo"
    # self.driver.activate_app(~)

    # 뒤로 가기
    icon_back = "common top icon back"

    # 완료
    edit_done = "edit_done"

    # 완료2
    edit_sub_done = "edit_sub_done"

# 해당 클래스의 아이디 모두 리스트에 추가
#variable_list
variable_list = []
for key, value in Idcomp.__dict__.items():
    if not key.startswith("__") and not callable(value):
        variable_list.append(key)