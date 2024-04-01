# KBO-Match-Result-Mail-System
KBO 경기 결과를 메일로 알려주는 프로젝트 입니다.

## 주요 기능
- 원하는 구단별 경기 기록을 받아볼 수 있습니다.
  - 원하는 정보만 받아볼 수 있습니다.
  - 1. 전날 경기 기록 및 박스 스코어 (성민)  
    2. 오늘 경기 일정  (성민)
    3. 이닝 별 정보  (창민)
    4. 전날 경기 뉴스  (창민)
- 전날 구단별 순위 및 선수 순위를 받아볼 수 있습니다.
  - 1. 구단 순위  (창민)
    2. 선수별 순위{(타자:타율별, 안타, 홈런, 타점, 주루), (투수: 평균자책점, 승리, 삼진)}  (희권)
- 매일 오전8시 결과를 메일로 알려준다(경기가 있는 날)
- 모든 기능은 파일로 만든다(파일이름: ex)24.04.01_경기기록)



### 폴더
- .env 
- src
  - webdriver
    - crawling
        - Y_Game
        - T_Game
        - Inning_info
        - News
        - Team_score
        - Player_score
        - ...
    - MyWebDriver.py
  - utils
    - SleepTime.py
  - fileIO
  - main.py

## 사용 언어
- Python: 3.11.8

### 사용 라이브러리



