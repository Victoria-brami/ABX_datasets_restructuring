import unittest

import numpy as np

from format_tests.tests_configuration import TestsConfig

PATH_TO_DATA_FOLDER = '/home/coml/Documents/Victoria/data'
cfg = TestsConfig()


# CSV_PATH_NAME = osp.join(PATH_TO_DATA_FOLDER, 'cogsci-2019/annotation_data/cogsci-2019_human_experimental_data.csv')
# CSV_FILE = pd.read_csv(CSV_PATH_NAME)
# CSV_FILE = pd.DataFrame(CSV_FILE)


class TestHumanCSVFileFormat(unittest.TestCase):

    # 1) test file name format: must have the form '<dataset_name>_stimuli.csv'
    def test_csv_name_suffix(self):
        csv_name = cfg.CSV_PATH_NAME.split('/')[-1]
        # must finish by '_human_experiments_data.csv'
        self.assertTrue(csv_name.endswith('_human_experimental_data.csv'))
        # At most one '_' in csv name, separating dataset name and stimuli
        self.assertEqual(len(csv_name.split('_')), 4)

    # 2) Test csv name prefix (same as the folder)
    def test_csv_name_prefix(self):
        csv_name = cfg.CSV_PATH_NAME.split('/')[-1]
        dataset_name = cfg.CSV_PATH_NAME.split('/')[-3]
        csv_name_prefix = csv_name.split('_')[0]
        self.assertEqual(dataset_name, csv_name_prefix)

    # 3) Test key list
    def test_key_contents(self):

        # self.assertTrue(len(cfg.CSV_FILE.keys()[1:]) == 23)
        for key in cfg.CSV_FILE.keys():
            if key == 'Unnamed: 0' or key == 'Unnamed: 0.1':
                continue
            self.assertIn(key, ['subject_id', 'subject_language', 'triplet_id', 'TGT_item', 'OTH_item',
                                'X_item', 'TGT_first', 'user_ans', 'bin_user_ans', 'speaker_TGT', 'speaker_OTH',
                                'speaker_X', 'language_TGT', 'language_OTH', 'language_X',
                                'phone_TGT', 'phone_OTH', 'phone_X',
                                'context', 'prev_phone', 'next_phone', 'dataset'])

    # 4) Test each column format
    # 4) a) Test subject_id format
    def test_subject_id_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['subject_id'][i], str)

    # 4) b) Test subject_language format
    def test_subject_language_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['subject_language'][i], str)
            self.assertTrue(cfg.CSV_FILE['subject_language'][i].isupper())
            self.assertTrue(len(cfg.CSV_FILE['subject_language'][i]) == 2)

    # 4) c) Test triplet_id format
    def test_triplet_id_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['triplet_id'][i], str)
            self.assertTrue(cfg.CSV_FILE['triplet_id'][i].startswith('triplet_'))

    # 4) d) Test TGT_item format
    def test_TGT_item_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['TGT_item'][i], str)
            self.assertTrue(cfg.CSV_FILE['TGT_item'][i].endswith('.wav'))

    # 4) e) Test OTH_item format
    def test_OTH_item_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['OTH_item'][i], str)
            self.assertTrue(cfg.CSV_FILE['OTH_item'][i].endswith('.wav'))

    # 4) f) Test X_item format
    def test_X_item_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['X_item'][i], str)
            self.assertTrue(cfg.CSV_FILE['X_item'][i].endswith('.wav'))

    # 4) g) Test corr_ans format
    def test_corr_ans_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIn(cfg.CSV_FILE['TGT_first'][i], [True, False])

    # 4) h) Test user_ans format
    def test_user_ans_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIn(cfg.CSV_FILE['user_ans'][i], range(-3, 4))

    # 4) i) Test bin_user_ans format
    def test_bin_user_ans_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIn(cfg.CSV_FILE['bin_user_ans'][i], [-1, 1])

    # 4) j) Test speaker_TGT format
    def test_speaker_TGT_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['speaker_TGT'][i], str)

    # 4) k) Test speaker_OTH format
    def test_speaker_OTH_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['speaker_OTH'][i], str)

    # 4) l) Test speaker_X format
    def test_speaker_X_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['speaker_X'][i], str)

    # 4) m) Test language_TGT format
    def test_language_TGT_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['language_TGT'][i], str)
            self.assertTrue(cfg.CSV_FILE['language_TGT'][i].isupper())
            self.assertTrue(len(cfg.CSV_FILE['language_TGT'][i]) == 2)

    # 4) n) Test language_OTH format
    def test_language_OTH_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['language_OTH'][i], str)
            self.assertTrue(cfg.CSV_FILE['language_OTH'][i].isupper())
            self.assertTrue(len(cfg.CSV_FILE['language_OTH'][i]) == 2)

            # 4) o) Test language_X format ?

    # 4) p) Test phone_TGT format (not in capital letter, IPA alphabet)
    def test_phone_TGT_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['phone_TGT'][i], str)
            self.assertTrue(cfg.CSV_FILE['phone_TGT'][i].islower())

    # 4) q) Test phone_OTH format (not in capital letter, IPA alphabet)
    def test_phone_OTH_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['phone_OTH'][i], str)
            self.assertTrue(cfg.CSV_FILE['phone_OTH'][i].islower())

    # 4) r) Test phone_X format (not in capital letter, IPA alphabet)
    def test_phone_X_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['phone_X'][i], str)
            self.assertTrue(cfg.CSV_FILE['phone_X'][i].islower())

    # 4) s) Test context format
    def test_context_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['context'][i], str)

    # 4) t) Test prev_phone format
    def test_prev_phone_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['prev_phone'][i], str)
            self.assertTrue(cfg.CSV_FILE['prev_phone'][i].islower())

    # 4) u) Test next_phone format
    def test_next_phone_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        for i in random_indexes:
            self.assertIsInstance(cfg.CSV_FILE['next_phone'][i], str)
            self.assertTrue(cfg.CSV_FILE['next_phone'][i].islower())

    # 4) v) Test dataset format
    def test_dataset_key_format(self):
        random_indexes = np.random.randint(0, cfg.CSV_FILE.count()[0], 10)
        dataset_name = cfg.CSV_PATH_NAME.split('/')[-3]
        for i in random_indexes:
            self.assertEqual(cfg.CSV_FILE['dataset'][i], dataset_name)


def customize_test(list_of_tests):
    suite_of_tests = unittest.TestSuite()
    for thing_to_test in list_of_tests:
        suite_of_tests.addTest(TestHumanCSVFileFormat(thing_to_test))
    return suite_of_tests


if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(customize_test(['test_csv_name_prefix', 'test_language_TGT_format', 'test_dataset_key_format']))
