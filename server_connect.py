import subprocess, os

class Connect:

    def __init__(self):
        Connect.appium_server(self)
        Connect.WebDriverAgent(self)

    def open_terminal(command):
        subprocess.run(['osascript', '-e', 'tell app "Terminal" to do script "clear"'])
        subprocess.run(['osascript', '-e', f'tell app "Terminal" to do script "{command}" in front window'])

    def appium_server(self):
        appium_server = "appium -p 4724"
        Connect.open_terminal(appium_server)

    def WebDriverAgent(self):
        WebDriverAgent = 'xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=00008110-001274620132801E" test'  # 기기 UDID 변경
        # 디렉토리 이동
        os.chdir('/Users/VIMO/Documents/WebDriverAgent')  # WebDriverAgent 경로 변경
        # 웹 드라이버 실행
        result = subprocess.run(WebDriverAgent, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding='utf-8')
