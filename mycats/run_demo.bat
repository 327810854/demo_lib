@echo off
setlocal enabledelayedexpansion

echo ========================================
echo 텍스트 전처리 라이브러리 데모
echo ========================================
echo.

REM 1. 의존성 설치
echo 1. 의존성 설치 중...
pip install -r requirements.txt
if errorlevel 1 (
    echo 의존성 설치 실패
    exit /b 1
)
echo ✓ 의존성 설치 완료
echo.

REM 2. 기본 데모 실행
echo 2. 기본 데모 실행 중...
python demo.py
if errorlevel 1 (
    echo 기본 데모 실행 실패
    exit /b 1
)
echo ✓ 기본 데모 완료
echo.

REM 3. 고급 데모 실행
echo 3. 고급 데모 실행 중...
python advanced_demo.py
if errorlevel 1 (
    echo 고급 데모 실행 실패
    exit /b 1
)
echo ✓ 고급 데모 완료
echo.

REM 4. 결과 표시
echo 4. 생성된 결과 파일:
if exist "output" (
    dir output\
    echo.
    echo 결과 미리보기:
    type output\processed_reviews.txt | more
)

echo.
echo ========================================
echo 모든 데모 완료!
echo ========================================
pause
