"""
데모 프로젝트 설정
"""

import os

# 프로젝트 루트 경로
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# 출력 디렉토리
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')

# 입력 데이터
INPUT_FILE = os.path.join(PROJECT_ROOT, 'reviews.txt')

# 로그 설정
LOG_FILE = os.path.join(OUTPUT_DIR, 'process.log')

# 민감한 단어 목록
SENSITIVE_WORDS = [
    '별로다', '지루하다', '재미없다', '별로', '싫어',
    '욕설', '나쁜말', '저주', '비속어',
    'terrible', 'bad', 'awful', 'waste', 'worst'
]

# 토크나이저 설정
TOKENIZER_CONFIG = {
    'remove_stopwords': True,
    'top_n': 10,  # 상위 N 개 단어
}

# 정리기 설정
CLEANER_CONFIG = {
    'lowercase': True,
    'remove_punctuation': True,
    'remove_numbers': False,
    'remove_extra_spaces': True,
}

# 필터 설정
FILTER_CONFIG = {
    'replacement_char': '*',
}

if __name__ == '__main__':
    print(f"프로젝트 루트: {PROJECT_ROOT}")
    print(f"출력 디렉토리: {OUTPUT_DIR}")
    print(f"입력 파일: {INPUT_FILE}")
