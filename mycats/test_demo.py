"""
데모 프로젝트 테스트
"""

import unittest
import os
import tempfile
from config import *
from advanced_demo import AdvancedReviewProcessor

class TestAdvancedDemo(unittest.TestCase):
    
    def setUp(self):
        self.processor = AdvancedReviewProcessor()
        self.test_dir = tempfile.mkdtemp()
    
    def test_process_single_review(self):
        """단일 리뷰 처리 테스트"""
        test_reviews = [
            {'line_no': 1, 'text': '좋은 제품입니다'},
            {'line_no': 2, 'text': '별로 좋지 않아요'}
        ]
        results = self.processor.process_reviews(test_reviews)
        self.assertEqual(len(results), 2)
        self.assertIn('cleaned', results[0])
        self.assertIn('tokens', results[0])
    
    def test_statistics_generation(self):
        """통계 생성 테스트"""
        test_reviews = [
            {'line_no': 1, 'text': '좋은 제품입니다'},
        ]
        results = self.processor.process_reviews(test_reviews)
        stats = self.processor.generate_statistics(results)
        
        self.assertEqual(stats['total_reviews'], 1)
        self.assertIn('top_words', stats)
        self.assertGreater(len(stats['all_frequencies']), 0)
    
    def test_file_save(self):
        """파일 저장 테스트"""
        test_reviews = [
            {'line_no': 1, 'text': '테스트 문장입니다'},
        ]
        results = self.processor.process_reviews(test_reviews)
        
        output_file = os.path.join(self.test_dir, 'test_output.txt')
        self.processor.save_results(results, output_file)
        
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('테스트', content)

if __name__ == '__main__':
    unittest.main()
