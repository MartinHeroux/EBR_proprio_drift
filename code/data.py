import os
import numpy as np
import pandas as pd


def import_data():
    """Import, parse, clean data for attention experiment 1."""
    sub_numbers = list(range(1,15)) + list(range(16,32))
    sub_id = []
    gender = []
    handedness = []
    age = []

    for sub_num in sub_numbers:
        # Read sub info file
        if sub_num <10:
            sub = 'sub0'
        else:
            sub = 'sub'
        cur_sub = sub + str(sub_num)
        file_path = os.path.join('..','data', cur_sub, cur_sub + '.txt')
        with open(file_path) as f:
            data = f.readlines()
        # Get subject id
        cur_id = data[0].strip().split(':')[1].lstrip()
        sub_id.append(cur_id)
        # Get subject age
        cur_age = int(data[1].strip().split(':')[1])
        age.append(cur_age)
        # Get subject gender
        cur_gender = data[2].strip().split(':')[1].lstrip()
        gender.append(cur_gender)
        # Get subject handedness
        cur_handedness = data[3].strip().split(':')[1].lstrip()
        handedness.append(cur_handedness)

    # Extract spacing and location data
    sp_delay0start = []
    sp_delay0end = []
    sp_delay3start = []
    sp_delay3end = []
    loc_ipsi0start = []
    loc_ipsi0end = []
    loc_ipsi3start = []
    loc_ipsi3end = []
    loc_contra0start = []
    loc_contra0end = []
    loc_contra3start = []
    loc_contra3end = []

    sp_delay0start_mean = []
    sp_delay0end_mean = []
    sp_delay3start_mean = []
    sp_delay3end_mean = []
    loc_ipsi0start_mean = []
    loc_ipsi0end_mean = []
    loc_ipsi3start_mean = []
    loc_ipsi3end_mean = []
    loc_contra0start_mean = []
    loc_contra0end_mean = []
    loc_contra3start_mean = []
    loc_contra3end_mean = []

    for sub_num in sub_numbers:
        # Read sub info file
        if sub_num <10:
            sub = 'sub0'
        else:
            sub = 'sub'
        cur_sub = sub + str(sub_num)
        file_path = os.path.join('..','data', cur_sub, cur_sub + '_data.txt')
        with open(file_path) as f:
            data = f.readlines()
        
        sub_sp_delay0 = []
        sub_sp_delay3 = []
        sub_loc_ipsi0 = []
        sub_loc_ipsi3 = []
        sub_loc_contra0 = []
        sub_loc_contra3 = []

        for line in data:
            if line.strip().split(':')[0] == 'BLOCK':
                cur_block = line.strip().split(':')[1].lstrip()
            elif line.strip().split(':')[0].split('-')[0][:-1] == 'TRIAL':
                pass
            elif line.strip().split(':')[0].split('_')[1] == 'SPACING':
                if cur_block ==  'SPACING DELAY ZERO':
                    sub_sp_delay0.append(int(line.strip().split(':')[1]))
                elif cur_block == 'SPACING DELAY 3MIN':
                    sub_sp_delay3.append(int(line.strip().split(':')[1]))
            elif line.strip().split(':')[0].split('_')[1] == 'LOCATION':
                if cur_block == 'LOCATION CONTRALATERAL DELAY ZERO':
                    sub_loc_contra0.append(float(line.strip().split(':')[1]))
                elif cur_block == 'LOCATION CONTRALATERAL DELAY 3MIN':
                    sub_loc_contra3.append(float(line.strip().split(':')[1]))
                elif cur_block == 'LOCATION IPSILATERAL DELAY ZERO':
                    sub_loc_ipsi0.append(float(line.strip().split(':')[1]))
                elif cur_block == 'LOCATION IPSILATERAL DELAY 3MIN':
                    sub_loc_ipsi3.append(float(line.strip().split(':')[1]))
        
        # SPACING ZERO
        sp_delay0start.append(list(sub_sp_delay0[0:5]))
        sp_delay0end.append(list(sub_sp_delay0[5:10]))
        sp_delay0start_mean.append(np.mean(list(sub_sp_delay0[0:5])))
        sp_delay0end_mean.append(np.mean(list(sub_sp_delay0[5:10])))
        # SPACING 3MIN
        sp_delay3start.append(list(sub_sp_delay3[0:5]))
        sp_delay3end.append(list(sub_sp_delay3[5:10]))
        sp_delay3start_mean.append(np.mean(list(sub_sp_delay3[0:5])))
        sp_delay3end_mean.append(np.mean(list(sub_sp_delay3[5:10])))
        # LOC CONTRAL ZERO
        loc_contra0start.append(list(sub_loc_contra0[0:5]))
        loc_contra0end.append(list(sub_loc_contra0[5:10]))
        loc_contra0start_mean.append(-1*np.mean(list(sub_loc_contra0[0:5])))
        loc_contra0end_mean.append(-1*np.mean(list(sub_loc_contra0[5:10])))
        # LOC CONTRAL 3MIN
        loc_contra3start.append(list(sub_loc_contra3[0:5]))
        loc_contra3end.append(list(sub_loc_contra3[5:10]))
        loc_contra3start_mean.append(-1*np.mean(list(sub_loc_contra3[0:5])))
        loc_contra3end_mean.append(-1*np.mean(list(sub_loc_contra3[5:10])))
        # LOC IPSI ZERO
        loc_ipsi0start.append(list(sub_loc_ipsi0[0:5]))
        loc_ipsi0end.append(list(sub_loc_ipsi0[5:10]))
        loc_ipsi0start_mean.append(np.mean(list(sub_loc_ipsi0[0:5])))
        loc_ipsi0end_mean.append(np.mean(list(sub_loc_ipsi0[5:10])))
        # LOC IPSI 3MIN
        loc_ipsi3start.append(list(sub_loc_ipsi3[0:5]))
        loc_ipsi3end.append(list(sub_loc_ipsi3[5:10]))
        loc_ipsi3start_mean.append(np.mean(list(sub_loc_ipsi3[0:5])))
        loc_ipsi3end_mean.append(np.mean(list(sub_loc_ipsi3[5:10])))

    data = pd.DataFrame({'age': age,
                         'gender': gender,
                         'handedness': handedness,
                         'sp_delay0start': sp_delay0start,
                         'sp_delay0end' : sp_delay0end,
                         'sp_delay3start': sp_delay3start,
                         'sp_delay3end': sp_delay3end,
                         'loc_ipsi0start': loc_ipsi0start,
                         'loc_ipsi0end': loc_ipsi0end,
                         'loc_ipsi3start': loc_ipsi3start,
                         'loc_ipsi3end': loc_ipsi3end,
                         'loc_contra0start': loc_contra0start,
                         'loc_contra0end': loc_contra0end,
                         'loc_contra3start': loc_contra3start,
                         'loc_contra3end': loc_contra3end,
                         'sp_delay0start_mean': sp_delay0start_mean,
                         'sp_delay0end_mean': sp_delay0end_mean,
                         'sp_delay3start_mean': sp_delay3start_mean,
                         'sp_delay3end_mean': sp_delay3end_mean,
                         'loc_ipsi0start_mean': loc_ipsi0start_mean,
                         'loc_ipsi0end_mean': loc_ipsi0end_mean,
                         'loc_ipsi3start_mean': loc_ipsi3start_mean,
                         'loc_ipsi3end_mean': loc_ipsi3end_mean,
                         'loc_contra0start_mean': loc_contra0start_mean,
                         'loc_contra0end_mean': loc_contra0end_mean,
                         'loc_contra3start_mean': loc_contra3start_mean,
                         'loc_contra3end_mean': loc_contra3end_mean},
                          index=sub_id)

    # Convert gender and handedness to category
    data['gender'] = data['gender'].astype('category')
    data['handedness'] = data['handedness'].astype('category')

    return data
