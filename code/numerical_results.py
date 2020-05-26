from scipy.stats import t
import pandas as pd
from collections import namedtuple
import os


def write_numerical_results(data):

    file_path = os.path.join('..', 'numerical_results', 'numerical_results.txt')
    with open(file_path, 'w') as file:
        file.write('-' * 22 + '\n')
    with open(file_path, 'a') as file:
        file.write('Horizontal drift study' + '\n')
        file.write('-' * 22 + '\n\n')
        cond = 'CONDITION'
        m = 'MEAN'
        ninetynine = '99%CI'
        file.write(f'{cond:<35} {m:>10} {ninetynine:^20}\n')

    sp0min = ['sp_delay0start_mean', 'sp_delay0end_mean', 'sp0diff']
    sp3min = ['sp_delay3start_mean', 'sp_delay3end_mean', 'sp3diff']
    calc_write_results(data, sp0min, sp3min, file_path)

    loc_ipsi0min = ['loc_ipsi0start_mean', 'loc_ipsi0end_mean', 'loc_ipsi0diff']
    loc_ipsi3min = ['loc_ipsi3start_mean', 'loc_ipsi3end_mean', 'loc_ipsi3diff']
    calc_write_results(data, loc_ipsi0min, loc_ipsi3min, file_path)

    loc_contra0min = ['loc_contra0start_mean', 'loc_contra0end_mean', 'loc_contra0diff']
    loc_contra3min = ['loc_contra3start_mean', 'loc_contra3end_mean', 'loc_contra3diff']
    calc_write_results(data, loc_contra0min, loc_contra3min, file_path)


def calc_write_results(data, zero, three, filename):

    zero_start = data[zero[0]].values
    zero_end = data[zero[1]].values
    zero_diff = [b - a for a, b in zip(zero_start, zero_end)]

    zero_results = list()
    zero_results.append(outcomes(zero_start))
    zero_results.append(outcomes(zero_end))
    zero_results.append(outcomes(zero_diff))

    three_start = data[three[0]].values
    three_end = data[three[1]].values
    three_diff = [b - a for a, b in zip(three_start, three_end)]

    three_results = list()
    three_results.append(outcomes(three_start))
    three_results.append(outcomes(three_end))
    three_results.append(outcomes(three_diff))

    three_zero = [b - a for a, b in zip(zero_diff, three_diff)]
    three_zero_results = outcomes(three_zero)

    write_results(zero, zero_results, filename)
    write_results(three, three_results, filename)
    n = three[2] + '-' + zero[2]
    write_results([n], [three_zero_results], filename)


def outcomes(values):
    Results = namedtuple('Results', 'mean upper_99 lower_99')
    vals = pd.Series(values)
    t_val = t.ppf([0.995], len(vals))
    output = Results(mean=vals.mean(),
                     upper_99=float(vals.mean() + (vals.sem() * t_val)),
                     lower_99=float(vals.mean() - (vals.sem() * t_val)))
    return output


def write_results(names, results, filename):
    with open(filename, 'a') as file:
        for name, result in zip(names, results):
            file.write(f'{name:<35} {result.mean:>10.2f} '
                       f'{result.lower_99:>8.2f} to '
                       f'{result.upper_99:<8.2f}\n')

