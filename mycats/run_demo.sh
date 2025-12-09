#!/bin/bash

# 색상 정의
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}텍스트 전처리 라이브러리 데모${NC}"
echo -e "${BLUE}========================================${NC}\n"

# 1. 의존성 설치
echo -e "${BLUE}1. 의존성 설치 중...${NC}"
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo -e "${RED}의존성 설치 실패${NC}"
    exit 1
fi
echo -e "${GREEN}✓ 의존성 설치 완료${NC}\n"

# 2. 기본 데모 실행
echo -e "${BLUE}2. 기본 데모 실행 중...${NC}"
python demo.py
if [ $? -ne 0 ]; then
    echo -e "${RED}기본 데모 실행 실패${NC}"
    exit 1
fi
echo -e "${GREEN}✓ 기본 데모 완료${NC}\n"

# 3. 고급 데모 실행 (옵션)
echo -e "${BLUE}3. 고급 데모 실행 중...${NC}"
python advanced_demo.py
if [ $? -ne 0 ]; then
    echo -e "${RED}고급 데모 실행 실패${NC}"
    exit 1
fi
echo -e "${GREEN}✓ 고급 데모 완료${NC}\n"

# 4. 결과 표시
echo -e "${BLUE}4. 생성된 결과 파일:${NC}"
if [ -d "output" ]; then
    ls -la output/
    echo ""
    echo -e "${BLUE}결과 내용 (첫 20줄):${NC}"
    head -n 20 output/processed_reviews.txt
fi

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}모든 데모 완료!${NC}"
echo -e "${GREEN}========================================${NC}"
