from collections import Counter


def seq_mining(data, min_ratio, max_len):
    min_freq = min_ratio * len(data)
    patterns = {
        seq[index:index+length+1]
        for seq in data
        for length in range(min(max_len, len(seq)))
        for index in range(len(seq) - length)
    }
    count = Counter(pat for seq in data for pat in patterns if pat in seq)
    return Counter({pat: freq for pat, freq in count.items() if freq >= min_freq})          



    #### 3-level dict comprehension