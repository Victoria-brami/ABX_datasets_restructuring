import unittest
import pandas as pd
import os.path as osp
import numpy as np

PATH_TO_DATA_FOLDER = '/home/coml/Documents/Victoria/data'

CSV_PATH_NAME = osp.join(PATH_TO_DATA_FOLDER, 'cogsci-2019/annotation_data/cogsci-2019_stimuli.csv')
CSV_FILE = pd.read_csv(CSV_PATH_NAME)
CSV_FILE = pd.DataFrame(CSV_FILE)


def is_not_a_wav_file(arg):
    print('{} is not a WAV file'.format(arg))


def is_not_a_float(arg):
    print('{} is not a float'.format(arg))


def is_not_a_string(arg):
    print('{} is not a string'.format(arg))


class TestStimuliCSVFileFormat(unittest.TestCase):

    # 1) test file name format: must have the form '<dataset_name>_stimuli.csv'
    def test_csv_name_suffix(self):
        csv_name = CSV_PATH_NAME.split('/')[-1]
        # must finish by '_stimuli.csv'
        self.assertEqual(csv_name.split('_')[-1], 'stimuli.csv')
        # At most one '_' in csv name, separating dataset name and stimuli
        self.assertEqual(len(csv_name.split('_')), 2)

    # 2) Test csv name prefix (same as the folder)
    def test_csv_name_prefix(self):
        csv_name = CSV_PATH_NAME.split('/')[-1]
        dataset_name = CSV_PATH_NAME.split('/')[-3]
        csv_name_prefix = csv_name.split('_')[0]
        print('names', dataset_name, csv_name_prefix)
        self.assertEqual(dataset_name, csv_name_prefix)

    # 3) test keys list
    def test_key_contents(self):
        self.assertTrue(len(CSV_FILE.keys()[1:]) == 12)
        for key in CSV_FILE.keys()[1:]:
            self.assertIn(key, ['index', '#file_source', '#file_extract', 'onset', 'offset', '#phone',
                                'context', 'language', 'speaker', 'prev_phone', 'next_phone', 'dataset'])

    # 4) test each key format

    # 4) a) test index format on random indexes
    # def test_index_format(self):
    #     random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
    #     for i in random_indexes:
    #         print(type(CSV_FILE['index'][i]))
    #         self.assertTrue(type(CSV_FILE['index'][i]) == int)
    # with self.assertRaises(TypeError):
    #     is_not_a_float(CSV_FILE['index'][i])

    # 4) b) test #file format on random indexes
    # def test_stimuli_filename_format(self):
    #     random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
    #     for i in random_indexes:
    #         # is a wav file
    #         self.assertTrue(CSV_FILE['#file'][i].split('.')[-1] == 'wav')
    #         with self.assertRaises(TypeError):
    #             is_not_a_wav_file(CSV_FILE['#file'][i])

    # 4) c) test onset and offset format (offset superior to onset)
    def test_onset_and_offset_format(self):
        random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(CSV_FILE['onset'][i], float)
            self.assertIsInstance(CSV_FILE['offset'][i], float)
            self.assertLess(CSV_FILE['onset'][i], CSV_FILE['offset'][i])

    # 4) d) test context format (str, 'NA' or 'S_D')

    # 4) e) test language format (str, two capital letters)
    def test_language_format(self):
        random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(CSV_FILE['language'][i], str)
            self.assertTrue(CSV_FILE['language'][i].isupper())
            self.assertTrue(len(CSV_FILE['language'][i]) == 2)

    # 4) f) test speaker format
    def test_speaker_format(self):
        random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(CSV_FILE['speaker'][i], str)
            # with self.assertRaises(TypeError):
            #     is_not_a_string(CSV_FILE['speaker'][i])

    # 4) g) test prev phone format (type str and IPA alphabet)
    def test_prev_phone_format(self):
        random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(CSV_FILE['prev_phone'][i], str)

    # 4) h) test next phone format(type str and IPA alphabet)
    def test_next_phone_format(self):
        random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(CSV_FILE['next_phone'][i], str)

    # 4) i) test dataset key format (same name as the csv prefix and folder prefix)
    def test_dataset_key_format(self):
        random_indexes = np.random.randint(0, CSV_FILE.count()[0], 10)
        dataset_name = CSV_PATH_NAME.split('/')[-3]
        for i in random_indexes:
            self.assertTrue(CSV_FILE['dataset'][i] == dataset_name)


if __name__ == '__main__':
    unittest.main()
