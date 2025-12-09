"""
고급 데모: 파일 입출력, 로깅, 향상된 분석
"""

import os
import logging
from datetime import datetime
from config import *
from ossing import TextCleaner, SensitiveWordFilter, Tokenizer

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AdvancedReviewProcessor:
    """고급 리뷰 처리기"""
    
    def __init__(self):
        self.cleaner = TextCleaner(**CLEANER_CONFIG)
        self.filter = SensitiveWordFilter(**FILTER_CONFIG)
        self.filter.load_from_list(SENSITIVE_WORDS)
        self.tokenizer = Tokenizer()
        
        logger.info("리뷰 처리기 초기화 완료")
    
    def process_file(self, input_file):
        """파일에서 리뷰 읽기 및 처리"""
        reviews = []
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                for line_no, line in enumerate(f, 1):
                    text = line.strip()
                    if text:
                        reviews.append({
                            'line_no': line_no,
                            'text': text
                        })
                        logger.debug(f"라인 {line_no} 읽음: {text[:50]}...")
        except FileNotFoundError:
            logger.error(f"파일을 찾을 수 없습니다: {input_file}")
            return []
        except Exception as e:
            logger.error(f"파일 읽기 오류: {e}")
            return []
        
        logger.info(f"총 {len(reviews)}개 리뷰 로드됨")
        return reviews
    
    def process_reviews(self, reviews):
        """리뷰 목록 처리"""
        results = []
        for review in reviews:
            result = {
                'line_no': review['line_no'],
                'original': review['text'],
                'cleaned': self.cleaner.clean(review['text']),
            }
            
            result['filtered'] = self.filter.filter(result['cleaned'])
            result['has_sensitive'] = self.filter.has_sensitive_words(result['original'])
            result['sensitive_words'] = self.filter.get_sensitive_words(result['original'])
            result['tokens'] = self.tokenizer.tokenize(
                result['filtered'], 
                remove_stopwords=True
            )
            result['word_freq'] = self.tokenizer.get_word_frequency(
                result['filtered'],
                remove_stopwords=True,
                top_n=5
            )
            
            results.append(result)
            logger.debug(f"리뷰 #{review['line_no']} 처리 완료")
        
        return results
    
    def generate_statistics(self, results):
        """통계 생성"""
        stats = {
            'total_reviews': len(results),
            'reviews_with_sensitive': sum(1 for r in results if r['has_sensitive']),
            'avg_tokens': 0,
            'all_words': [],
            'all_frequencies': {},
        }
        
        # 모든 단어 빈도 수집
        for result in results:
            stats['all_words'].extend(result['tokens'])
            for word, freq in result['word_freq']:
                stats['all_frequencies'][word] = stats['all_frequencies'].get(word, 0) + freq
        
        # 평균 토큰 수
        if results:
            stats['avg_tokens'] = len(stats['all_words']) / len(results)
        
        # 상위 10개 단어
        stats['top_words'] = sorted(
            stats['all_frequencies'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        
        # 민감한 단어 통계
        stats['sensitive_word_freq'] = {}
        for result in results:
            for word in result['sensitive_words']:
                stats['sensitive_word_freq'][word] = \
                    stats['sensitive_word_freq'].get(word, 0) + 1
        
        logger.info(f"통계 생성 완료 - 총 {stats['total_reviews']}개 리뷰 분석됨")
        return stats
    
    def save_results(self, results, output_file):
        """결과를 파일에 저장"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("리뷰 처리 결과\n")
                f.write("=" * 80 + "\n\n")
                f.write(f"생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for result in results:
                    f.write(f"【리뷰 #{result['line_no']}】\n")
                    f.write(f"원본:\n  {result['original']}\n\n")
                    f.write(f"정리됨:\n  {result['cleaned']}\n\n")
                    f.write(f"필터링됨:\n  {result['filtered']}\n\n")
                    f.write(f"토크나이징:\n  {', '.join(result['tokens'])}\n\n")
                    f.write(f"단어 빈도:\n")
                    for word, freq in result['word_freq']:
                        f.write(f"  - {word}: {freq}\n")
                    if result['sensitive_words']:
                        f.write(f"민감한 단어: {', '.join(result['sensitive_words'])}\n")
                    f.write("-" * 80 + "\n\n")
            
            logger.info(f"결과 저장 완료: {output_file}")
        except Exception as e:
            logger.error(f"결과 저장 오류: {e}")
    
    def save_statistics(self, stats, output_file):
        """통계를 파일에 저장"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("텍스트 처리 통계 보고서\n")
                f.write("=" * 80 + "\n\n")
                f.write(f"생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("【기본 통계】\n")
                f.write(f"총 리뷰 수: {stats['total_reviews']}\n")
                f.write(f"민감한 단어 포함 리뷰 수: {stats['reviews_with_sensitive']}\n")
                f.write(f"총 단어 수: {len(stats['all_words'])}\n")
                f.write(f"고유 단어 수: {len(stats['all_frequencies'])}\n")
                f.write(f"평균 토큰 수: {stats['avg_tokens']:.2f}\n\n")
                
                f.write("【고빈도 단어 (상위 10개)】\n")
                for i, (word, freq) in enumerate(stats['top_words'], 1):
                    f.write(f"{i}. {word}: {freq}\n")
                f.write("\n")
                
                if stats['sensitive_word_freq']:
                    f.write("【민감한 단어 빈도】\n")
                    for word, freq in sorted(
                        stats['sensitive_word_freq'].items(),
                        key=lambda x: x[1],
                        reverse=True
                    ):
                        f.write(f"- {word}: {freq}회\n")
                    f.write("\n")
            
            logger.info(f"통계 저장 완료: {output_file}")
        except Exception as e:
            logger.error(f"통계 저장 오류: {e}")


def main():
    """메인 함수"""
    logger.info("=" * 80)
    logger.info("고급 리뷰 처리 데모 시작")
    logger.info("=" * 80)
    
    # 출력 디렉토리 생성
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 처리기 초기화
    processor = AdvancedReviewProcessor()
    
    # 파일에서 리뷰 읽기
    reviews = processor.process_file(INPUT_FILE)
    
    if not reviews:
        logger.warning("처리할 리뷰가 없습니다")
        return
    
    # 리뷰 처리
    results = processor.process_reviews(reviews)
    
    # 통계 생성
    stats = processor.generate_statistics(results)
    
    # 결과 저장
    output_file = os.path.join(OUTPUT_DIR, 'advanced_results.txt')
    processor.save_results(results, output_file)
    
    # 통계 저장
    stats_file = os.path.join(OUTPUT_DIR, 'advanced_report.txt')
    processor.save_statistics(stats, stats_file)
    
    # 콘솔에 요약 출력
    print("\n" + "=" * 80)
    print("처리 완료!")
    print("=" * 80)
    print(f"총 리뷰 수: {stats['total_reviews']}")
    print(f"민감한 단어 포함: {stats['reviews_with_sensitive']}")
    print(f"고유 단어 수: {len(stats['all_frequencies'])}")
    print(f"\n고빈도 단어 (상위 5개):")
    for word, freq in stats['top_words'][:5]:
        print(f"  - {word}: {freq}")
    print(f"\n결과 파일:")
    print(f"  ✓ {output_file}")
    print(f"  ✓ {stats_file}")
    print("=" * 80)
    
    logger.info("고급 리뷰 처리 데모 완료")


if __name__ == '__main__':
    main()
