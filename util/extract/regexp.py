import re

PATTERN = r'^(?P<title>(\d+\.\s+[A-Z].+|[*]{1}.*[*]{1}|#+\s+.+|.+:$))$'

def _regex(text):
    # 정규식으로 title 찾기
    matches = re.finditer(PATTERN, text, re.MULTILINE)

    # title과 content를 분리
    titles = []
    contents = []
    last_pos = 0

    for match in matches:
        title = match.group('title').strip()
        
        # 제목의 길이가 50자를 넘지 않는 경우에만 title로 인식
        if len(title) <= 50:
            titles.append(title)
            
            # content 추출
            content_start = match.end()
            if len(titles) > 1:
                contents.append(text[last_pos:match.start()].strip())
            last_pos = content_start

    # 마지막 content 추가
    contents.append(text[last_pos:].strip())
    return titles, contents