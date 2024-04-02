def to_HTML(data: dict) -> str:
    html = '<html>'

    html += add_head()
    html += add_body(data)

    html += '</html>'

    return html

def add_head():
    html = '<head>'


    html += '</head>'

    return html

def add_body(data):
    html = '<body>'

    html += to_HTML_team_info(data['team_info'])

    html += to_HTML_rank(data['ranking_info'])

    html += '</body>'

    return html

def to_HTML_team_info(data: dict) -> str:
    html = ''
    if 'recent_match_info' in data:
        html += to_HTML_recent_match(data['recent_match_info'])

    if 'today_match_info' in data:
        html += to_HTML_today_match(data['today_match_info'])
    
    if 'recent_match_news' in data:
        html += to_HTML_recent_match_news(data['recent_match_news'])

    return html

def to_HTML_recent_match(data: list[object]) -> str:
    return ''

def to_HTML_today_match(data: list[object]) -> str:
    return ''

def to_HTML_recent_match_news(data: list[object]) -> str:
    return ''
    
def to_HTML_rank(data: dict) -> str:
    html = '<div id="rank">'

    if 'team_rank' in data:
        html += to_HTML_team_rank(data['team_rank'])

    if 'players_rank' in data:
        html += to_HTML_player_rank(data['players_rank'])

    html += '</div>'

    return html

def to_HTML_team_rank(data: list[object]) -> str:
    return ''

def to_HTML_player_rank(data: dict) -> str:
    hitters = data['hitter']
    pitchers = data['pitcher']

    html = '<div id="player-rank">'
    
    html += to_HTML_hitter(hitters)

    html += '</div>'

    return html

def to_HTML_hitter(data: dict):
    html = '<div>'
    html += '<div>타자</div>'
    html += to_HTML_hitter_AVG(data['AVG'])
    html += to_HTML_hitter_H(data['H'])
    html += to_HTML_hitter_HR(data['HR'])
    html += to_HTML_hitter_RBI(data['RBI'])
    html += to_HTML_hitter_SB(data['SB'])


    html += '</div>'

    return html

def to_HTML_hitter_AVG(data) -> str:
    html = \
"""
<div class='table-name'>타율</div>
<table>
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    <tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getAvg())

    html += '</html>'

    return html

def to_HTML_hitter_H(data) -> str:
    html = \
"""
<div class='table-name'>안타</div>
<table>
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    <tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getHit())

    html += '</html>'

    return html

def to_HTML_hitter_HR(data) -> str:
    html = \
"""
<div class='table-name'>홈런</div>
<table>
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    <tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getHomeRun())

    html += '</html>'

    return html

def to_HTML_hitter_RBI(data) -> str:
    html = \
"""
<div class='table-name'>타점</div>
<table>
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    <tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getRunBattedIn())

    html += '</html>'

    return html

def to_HTML_hitter_SB(data) -> str:
    html = \
"""
<div class='table-name'>주루</div>
<table>
    <tr>
        <th>순위</th>
        <th>이름</th>
        <th>소속</th>
        <th>정보</th>
    <tr>
"""
    for i, player in enumerate(data):
        html += player.toHTML(i+1, player.getStolenBase())

    html += '</html>'

    return html