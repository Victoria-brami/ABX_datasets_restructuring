import os.path as osp
import pandas as pd

class TestsConfig:

    """ CHANGE ONLY THESE TWO LINES
    """
    PATH_TO_DATA = '/home/coml/Documents/Victoria/data/'
    DATASET_NAME = 'zerospeech'

    # HUMAN EXPERIMENTS FILE
    CSV_PATH_NAME = osp.join(PATH_TO_DATA, DATASET_NAME, 'annotation_data', DATASET_NAME + '_human_experimental_data.csv')
    CSV_FILE = pd.read_csv(CSV_PATH_NAME)
    # HUMAN_EXP_