import os
import sys

# 把 LJH/ossing
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSSING_ROOT = os.path.join(ROOT, "ossing")
if OSSING_ROOT not in sys.path:
    sys.path.insert(0, OSSING_ROOT)

from ossing import TextCleaner, SensitiveWordFilter, Tokenizer

class ReviewProcessor:
    """리뷰 처리 파이프라인"""
    
    def __init__(self):
        # 각 구성 요소 초기화
        self.cleaner = TextCleaner(
            lowercase=True,
            remove_punctuation=True,
            remove_numbers=False,
            remove_extra_spaces=True
        )
        
        self.filter = SensitiveWordFilter(replacement_char='*')
        # 민감한 단어 목록 로드
        self.filter.load_from_list([
            '별로다', '지루하다', '재미없다', '별로', '싫어',
            'terrible', 'bad', 'awful', 'waste'
        ])
        
        self.tokenizer = Tokenizer()
    
    def process_single(self, text):
        """단일 리뷰 처리"""
        # 1단계: 정리
        cleaned = self.cleaner.clean(text)
        
        # 2단계: 민감한 단어 필터링
        filtered = self.filter.filter(cleaned)
        
        # 3단계: 토크나이징
        tokens = self.tokenizer.tokenize(filtered, remove_stopwords=True)
        
        # 4단계: 단어 빈도 통계
        freq = self.tokenizer.get_word_frequency(
            filtered, 
            remove_stopwords=True, 
            top_n=5
        )
        
        return {
            'original': text,
            'cleaned': cleaned,
            'filtered': filtered,
            'tokens': tokens,
            'word_freq': freq,
            'has_sensitive': self.filter.has_sensitive_words(text),
            'sensitive_words': self.filter.get_sensitive_words(text)
        }
    
    def process_batch(self, texts):
        """일괄 리뷰 처리"""
        return [self.process_single(text) for text in texts]
    
    def generate_report(self, reviews):
        """처리 보고서 생성"""
        report = {
            'total_reviews': len(reviews),
            'reviews_with_sensitive': sum(
                1 for r in reviews if r['has_sensitive']
            ),
            'all_words': [],
            'all_frequencies': {}
        }
        
        # 모든 단어 빈도 요약
        for review in reviews:
            for word, freq in review['word_freq']:
                if word in report['all_frequencies']:
                    report['all_frequencies'][word] += freq
                else:
                    report['all_frequencies'][word] = freq
            report['all_words'].extend(review['tokens'])
        
        # 단어 빈도 정렬
        sorted_freq = sorted(
            report['all_frequencies'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        report['top_words'] = sorted_freq
        
        return report


def main():
    """메인 프로그램"""
    
    # 처리기 생성
    processor = ReviewProcessor()
    
    # 샘플 데이터: 사용자 리뷰
    sample_reviews = [
        "이 음식점 정말 좋아요. 음식도 맛있고 서비스도 훌륭해요.",
        "  환경이 좋습니다!!! 하지만 음식은    별로입니다.",
        "오늘 여기 왔는데, terrible 경험이었어요. 너무 별로였어요.",
        "친구 추천으로 왔는데 나쁜 점도 있지만 괜찮아요.",
        "지루하다, 다시는 안 올 거예요! 이곳은 끔찍했어요."
    ]
    
    print("=" * 70)
    print("텍스트 전처리 라이브러리 데모 - 사용자 리뷰 처리 시스템")
    print("=" * 70)
    print()
    
    # 단일 리뷰 처리 예시
    print("【예시 1: 단일 리뷰 처리】")
    print("-" * 70)
    result = processor.process_single(sample_reviews[0])
    print(f"원본: {result['original']}")
    print(f"정리됨: {result['cleaned']}")
    print(f"필터링됨: {result['filtered']}")
    print(f"토크나이징: {result['tokens']}")
    print(f"단어 빈도 (상위 5개): {result['word_freq']}")
    print(f"민감한 단어 포함: {result['has_sensitive']}")
    if result['sensitive_words']:
        print(f"민감한 단어: {result['sensitive_words']}")
    print()
    
    # 모든 리뷰 처리
    print("【예시 2: 일괄 리뷰 처리】")
    print("-" * 70)
    results = processor.process_batch(sample_reviews)
    
    for i, result in enumerate(results, 1):
        print(f"\n리뷰 #{i}:")
        print(f"  원본: {result['original']}")
        print(f"  필터링됨: {result['filtered']}")
        print(f"  단어 수: {len(result['tokens'])}")
        print(f"  민감한 단어: {result['sensitive_words'] if result['sensitive_words'] else '없음'}")
    print()
    
    # 통계 보고서 생성
    print("【예시 3: 통계 보고서】")
    print("-" * 70)
    report = processor.generate_report(results)
    
    print(f"총 리뷰 수: {report['total_reviews']}")
    print(f"민감한 단어 포함 리뷰 수: {report['reviews_with_sensitive']}")
    print(f"총 단어 수: {len(report['all_words'])}")
    print(f"고유 단어 수: {len(report['all_frequencies'])}")
    print()
    print("고빈도 단어 (상위 10개):")
    for word, freq in report['top_words']:
        print(f"  - {word}: {freq}")
    print()
    
    # 결과를 파일에 저장
    print("【예시 4: 결과 저장】")
    print("-" * 70)
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 처리 결과 저장
    with open(os.path.join(output_dir, 'processed_reviews.txt'), 'w', encoding='utf-8') as f:
        for i, result in enumerate(results, 1):
            f.write(f"【리뷰 #{i}】\n")
            f.write(f"원본: {result['original']}\n")
            f.write(f"필터링됨: {result['filtered']}\n")
            f.write(f"민감한 단어: {result['sensitive_words']}\n")
            f.write(f"단어 빈도: {result['word_freq']}\n")
            f.write("-" * 70 + "\n\n")
    
    print(f"✓ 처리 결과가 {output_dir}/processed_reviews.txt 에 저장되었습니다")
    
    # 통계 보고서 저장
    with open(os.path.join(output_dir, 'report.txt'), 'w', encoding='utf-8') as f:
        f.write("텍스트 처리 통계 보고서\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"총 리뷰 수: {report['total_reviews']}\n")
        f.write(f"민감한 단어 포함 리뷰 수: {report['reviews_with_sensitive']}\n")
        f.write(f"총 단어 수: {len(report['all_words'])}\n")
        f.write(f"고유 단어 수: {len(report['all_frequencies'])}\n\n")
        f.write("고빈도 단어 (상위 10개):\n")
        for word, freq in report['top_words']:
            f.write(f"  {word}: {freq}\n")
    
    print(f"✓ 통계 보고서가 {output_dir}/report.txt 에 저장되었습니다")
    print()
    print("데모가 완료되었습니다!")


if __name__ == '__main__':
    main()
