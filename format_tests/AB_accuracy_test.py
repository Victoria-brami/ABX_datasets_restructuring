import pandas as pd
import numpy as np


def test_accuracy_AB(name):
    data = pd.read_csv(name)
    data = pd.DataFrame(data)

    print(data.head())
    print()

    triplets_ids = [data['tripletid'][0]]
    user_first_ans = [data['first_sound'][0]]
    user_second_ans = [data['second_sound'][0]]
    nbs = [1]

    for i in range(1, len(data['tripletid'])):
        if data['tripletid'][i] == triplets_ids[-1]:
            nbs[-1] += 1
            user_first_ans[-1] += data['first_sound'][i]
            user_second_ans[-1] += data['second_sound'][i]
        else:
            triplets_ids.append(data['tripletid'][i])
            nbs.append(1)
            user_first_ans.append(data['first_sound'][i])
            user_second_ans.append(data['second_sound'][i])

    return triplets_ids, np.array(nbs), np.array(user_first_ans), np.array(user_second_ans)


def select_best_response(triplets_ids, nbs, user_first_ans, user_second_ans):
    resp = []
    normed_first_ans = user_first_ans / nbs
    normed_second_ans = user_second_ans / nbs
    for i in range(len(normed_first_ans)):
        if normed_first_ans[i] > normed_second_ans[i]:
            resp.append('first')
        else:
            resp.append('second')

    data = pd.DataFrame(dict(triplet_id=triplets_ids, user_ans=resp))

    return data



if __name__ == '__main__':

    NAME = '../geomphon-perception-ABX/experiments/pilot_july_2018/data/merged_results_cleaned.csv'
    triplets_ids, nbs, user_first_ans, user_second_ans = test_accuracy_AB(NAME)

    data = select_best_response(triplets_ids, nbs, user_first_ans, user_second_ans)

    print(data)