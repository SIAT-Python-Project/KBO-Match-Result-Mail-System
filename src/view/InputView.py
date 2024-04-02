from utils.Mail import Mail

kbo_teams = ['NC', 'SSG', '롯데', '삼성', '키움', '두산', 'LG', '한화', 'KT', 'KIA']
team_result_info = {'1': 'recent_match_info', '2': 'today_match_info', '3': 'recent_match_news'}
rank_info = {'1': 'team_rank', '2': 'players_rank'}


def inputSettingValue():
    info = dict()
    info['email'] = inputMail()
    info['team'] = inputTeam()
    info['rank'] = inputRanking()

    return info

def inputMail():
    print('------------------------------')
    print("받으실 메일을 적어주십시요.")
    email = input('>>>')
    print('------------------------------')
    print("받으실 메일의 비밀번호를 적어주십시요.")
    passwd = input('>>>')

    try:
        mail = Mail(email, passwd)
        mail.send_test()
        return {"email": email, "passwd": passwd}
    except Exception as e:
        print(f'[ERROR] {e}')
        return inputMail()

def inputTeam():
    team = dict()

    team['teams'] = inputTeamName()
    team['result'] = inputTeamResult()

    return team

def inputTeamName():
    print('------------------------------')
    for team in kbo_teams:
        print(team)
    print('원하는 구단들을 ,기준으로 입력해주세요.')
    print('ex) NC,KT,한화')
    teams = set(input(">>>").split(','))
    try:
        for team in teams:
            if team not in kbo_teams:
                raise Exception('올바른 팀 이름을 입력해주세요')
            
        return list(teams)
    except Exception as e:
        print(f'[ERROR] {e}')
        return inputTeamName()
    
def inputTeamResult():
    print('------------------------------')
    print('1. 최근 경기 기록 및 박스 스코어')
    print('2. 오늘 경기 일정')
    print('3. 최근 경기 뉴스')
    print('받고 싶은 정보를 ,기준으로 입력해주세요.')
    print('ex) 1,2')

    team_input = input('>>>')

    results = set(team_input.split(','))

    if team_input == '':
        results = set()

    try:
        team_results = []

        for result in results:
            if result not in team_result_info:
                raise Exception('올바른 숫자 형식을 입력해주세요')

            team_results.append(team_result_info[result])

        return team_results

    except Exception as e:
        print(f'[ERROR] {e}')
        return inputTeamResult()
    

def inputRanking():
    print('------------------------------')
    print('1. 구단 순위')
    print('2. 선수별 순위')
    print('받고 싶은 정보를 ,기준으로 입력해주세요.')
    print('ex) 1,2')

    ranking_input = input('>>>')

    results = set(ranking_input.split(','))

    if ranking_input == '':
        results = set()

    try:
        rank_results = []

        for result in results:
            if result not in rank_info:
                raise Exception('올바른 숫자 형식을 입력해주세요')

            rank_results.append(rank_info[result])

        return rank_results

    except Exception as e:
        print(f'[ERROR] {e}')
        return inputRanking()