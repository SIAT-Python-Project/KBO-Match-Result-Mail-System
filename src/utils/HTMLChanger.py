def to_HTML(data: dict) -> str:
    html = ''

    html += to_HTML_team_info(data['team_info'])

    html += to_HTML_rank(data['ranking_info'])

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
    html = ''

    if 'team_rank' in data:
        html += to_HTML_team_rank(data['team_rank'])

    if 'players_rank' in data:
        html += to_HTML_player_rank(data['players_rank'])

    return html

def to_HTML_team_rank(data: list[object]) -> str:
    return ''

def to_HTML_player_rank(data: dict) -> str:
    return ''