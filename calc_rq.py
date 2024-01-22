#!/usr/bin/env python3

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Calculate RQ test results')
    parser.add_argument('file_name', type=str, help='Path to the file to be read')
    return parser.parse_args()

def get_score(cat):
    p,n = cat['pos'],cat['neg'] 
    pos = sum([answers[i-1] for i in p])
    neg = sum([answers[i-1] for i in n])
    return pos, neg, pos-neg

categories = {
    'emotion regulation':{
        'pos':[13,25,26,56],
        'neg':[2,7,23,31]
    },
    'impulse control':{
        'pos':[4,15,42,47],
        'neg':[11,36,38,55]
    },
    'optimism':{
        'pos':[18,27,32,53],
        'neg':[3,33,39,43]
    },
    'causal analysis':{
        'pos':[12,19,21,48],
        'neg':[1,41,44,52]
    },
    'empthy':{
        'pos':[10,34,37,46],
        'neg':[24,30,50,54]
    },
    'self-efficacy ':{
        'pos':[5,28,29,49],
        'neg':[9,17,20,22]
    },
    'reaching out':{
        'pos':[6,8,14,40],
        'neg':[16,35,45,51]
    }
}

if __name__ == '__main__':
    args    = get_args()
    num_qs  = 56
    answers = [int(l.strip()) for l in open(args.file_name, 'r')]
    if len(answers) != num_qs:
        print(f'go back and answer all {num_qs} questions in {args.file_name}')

    all_nums = set()
    for cat in categories:
        all_nums |= (
            set(categories[cat]['neg']) |
            set(categories[cat]['pos'])
        )
        (p,n,t) = get_score(categories[cat])
        print( '{}'.format(cat))
        print(f'  positive: {p}')
        print(f'  negitive: {n}')
        print(f'  total:    {t}')
    assert len(all_nums) == num_qs

