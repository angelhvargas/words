from WordsProcessor import WordsProcessor


class TestWordsProcessor:

    def test_can_instantiate_words_processor(self):
        """test if WordsProcessor class does exists
        or can be instantiate"""
        words_processor = WordsProcessor
        pass

    def test_can_read_file_to_process(self):
        """ test if an existing file can be read and
        loaded for processing"""
        words_processor = WordsProcessor("./test.txt")
        pass
