import os 

def get_paired_samples(folder='data/raw-reads'):
    lst = os.listdir(folder)
    global_dict = {}
    for file in lst:
        file_lst = file.split("_")
        if file_lst[0] not in global_dict:
            global_dict[file_lst[0]] = {'r1': None,
                                    'r2': None}
        if file_lst[1] == '1.fastq':
            global_dict[file_lst[0]]['r1'] = os.path.join(folder,file)
        if file_lst[1] == '2.fastq':
            global_dict[file_lst[0]]['r2'] = os.path.join(folder,file)
    return global_dict

# paired_samples = get_paired_samples()
# SAMPLES = list(paired_samples.keys())
# print(paired_samples)