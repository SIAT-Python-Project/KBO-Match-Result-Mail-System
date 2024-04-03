def to_HTML(data: dict) -> str:
    html = '<html>'

    html += add_head()
    html += add_body(data)

    html += '</html>'

    return html

def add_head() -> str:
    html = '<head>'

    html += \
"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>야구다 야구!</title>
    <style>
        .type-label {
            font-size: 20px;
            font-weight: bold;
        }

        .player-rank-table,
        .team-rank-table,
        .recent-match-table,
        .next-match-table {
            text-align: center;
            margin-bottom: 15px;
            width: 95%;
        }

        .table-name,
        .li-name {
            font-size: 17px;
            font-weight: bold;
        }

        a {
            text-decoration: none;
        }

        .pitcher-table,
        .hitter-table,
        .team-rank-table,
        .match {
            width: 95%;
        }

        table,
        th,
        td {
            border: 1px solid black;
            border-collapse: collapse;
        }

        th {
            background: black;
            color: white;
            font-weight: bold;
        }

        .pitcher-tables,
        .hitter-tables {
            margin-bottom: 20px;
            flex-grow: 1;
            display: flex;
            align-items: center;
            flex-direction: column;
        }

        #player-rank {
            display: flex;
        }

        .container {
            flex-grow: 1;
        }

        body {
            display: flex;
        }


        .match-info {
            display: flex;
            flex-direction: row;
        }

        .match {
            flex-grow: 1;
        }
    </style>
"""

    html += '</head>'

    return html

def add_body(data: dict) -> str:
    html = '<body>'

    html += to_HTML_team_info(data['team_info'])

    html += to_HTML_rank(data['ranking_info'])

    html += '</body>'

    return html

def to_HTML_team_info(data: dict) -> str:
    html = '<div id="info" class="container">'

    if 'recent_match_info' in data or 'today_match_info' in data:
        html += '<fieldset class="match-info">'
        html += '<legend class="type-label">경기 결과</legend>'

        if 'recent_match_info' in data:
            html += to_HTML_recent_match(data['recent_match_info'])

        if 'today_match_info' in data:
            html += to_HTML_today_match(data['today_match_info'])

        html += '</fieldset>'
    
    if 'recent_match_news' in data:
        html += to_HTML_recent_match_news(data['recent_match_news'])

    return html

def to_HTML_recent_match(data: list[object]) -> str:
    html = \
"""
            <div class="match recent-match">
                <div class="table-name">최근 경기</div>
                <table class="recent-match-table">
                    <tr>
                        <th>날짜</th>
                        <th>팀1</th>
                        <th>결과</th>
                        <th>팀2</th>
                    </tr>
"""
    for match in data:
        html += match.toHTML()

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_today_match(data: list[object]) -> str:
    html = \
"""
            <div class="match next-match">
                <div class="table-name">다음 경기</div>
                <table class="next-match-table">
                    <tr>
                        <th>날짜</th>
                        <th>팀1</th>
                        <th>팀2</th>
                        <th>구장</th>
                        <th>시작시간</th>
                    </tr>
"""
    for match in data:
        html += match.toHTML()

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_recent_match_news(data: dict) -> str:
    html = \
"""
        <fieldset class="team-news">
            <legend class="type-label">팀 뉴스</legend>
            <ul>
"""
    for key in data:
        html += '<li>'
        html += f'<div class="li-name">{key}</div>'

        if len(data[key]) > 0:
            html += '<ul>'

            for news in data[key]:
                html += news.toHTML()

            html += '</ul>'
            
        html += '</li>'

    html += '</ul>'
    html += '</fieldset>'

    return html
    
def to_HTML_rank(data: dict) -> str:

    html = '<div id="rank">'

    if 'team_rank' in data:
        html += to_HTML_team_rank(data['team_rank'])

    if 'players_rank' in data:
        html += to_HTML_player_rank(data['players_rank'])

    html += '</div>'

    return html

def to_HTML_team_rank(data: list[object]) -> str:
    html = \
"""
        <div id="team-rank">
            <fieldset class="team-table">
                <legend class="type-label">팀 순위</legend>
                <table class="team-rank-table">
                    <tr>
                        <th>순위</th>
                        <th>팀명</th>
                        <th>경기</th>
                        <th>승</th>
                        <th>패</th>
                        <th>무</th>
                        <th>승률</th>
                        <th>게임차</th>
                        <th>최근10경기</th>
                        <th>연속</th>
                    </tr>
"""
    for team in data:
        html += team.toHTML()

    html += '</table>'
    html += '</fieldset>'
    html += '</div>'

    return html

def to_HTML_player_rank(data: dict) -> str:
    hitters = data['hitter']
    pitchers = data['pitcher']

    html = '<div id="player-rank">'
    
    html += to_HTML_hitter(hitters)
    html += to_HTML_pitcher(pitchers)

    html += '</div>'

    return html

def to_HTML_pitcher(data: dict) -> str:
    html = '<fieldset class="pitcher-tables">'
    html += '<legend class="type-label">투수</legend>'
    html += to_HTML_pitcher_AVG(data['AVG'])
    html += to_HTML_pitcher_S(data['W'])
    html += to_HTML_pitcher_SO(data['SO'])

    html += '</fieldset>'

    return html

def to_HTML_pitcher_AVG(data) -> str:
    html = \
"""
<div class="pitcher-table">
<div class="table-name">평균자책점</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getEarnedRunsAverage())

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_pitcher_S(data) -> str:
    html = \
"""
<div class="pitcher-table">
<div class="table-name">승리</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getWin())

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_pitcher_SO(data) -> str:
    html = \
"""
<div class="pitcher-table">
<div class="table-name">삼진</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getStrikeOuts())

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_hitter(data: dict) -> str:
    html = '<fieldset class="hitter-tables">'
    html += '<legend class="type-label">타자</legend>'
    html += to_HTML_hitter_AVG(data['AVG'])
    html += to_HTML_hitter_H(data['H'])
    html += to_HTML_hitter_HR(data['HR'])
    html += to_HTML_hitter_RBI(data['RBI'])
    html += to_HTML_hitter_SB(data['SB'])


    html += '</fieldset>'

    return html

def to_HTML_hitter_AVG(data) -> str:
    html = \
"""
<div class="hitter-table">
<div class="table-name">타율</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getAvg())

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_hitter_H(data) -> str:
    html = \
"""
<div class="hitter-table">
<div class="table-name">안타</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getHit())

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_hitter_HR(data) -> str:
    html = \
"""
<div class="hitter-table">
<div class="table-name">홈런</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getHomeRun())

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_hitter_RBI(data) -> str:
    html = \
"""
<div class="hitter-table">
<div class="table-name">타점</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getRunBattedIn())

    html += '</table>'
    html += '</div>'

    return html

def to_HTML_hitter_SB(data) -> str:
    html = \
"""
<div class="hitter-table">
<div class="table-name">주루</div>
<table class="player-rank-table">
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    </tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getStolenBase())

    html += '</table>'
    html += '</div>'

    return html