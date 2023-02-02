import re


def check_tls(address):
    abba_re = re.compile(r'(.)(?!\1)(.)\2\1')
    # using '|'.join() instead of ''.join() so separate hypernets aren't joined together
    hypernets = '|'.join(re.findall(r'\[(.*?)]', address))
    if abba_re.findall(hypernets):
        return False
    return bool(abba_re.findall(address))


def check_ssl(address):
    non_hypernets = '|'.join(re.findall(r'(?:^|])(.*?)(?:\[|$)', address))
    hypernets = '|'.join(re.findall(r'\[(.*?)]', address))
    aba_bab_re = re.compile(r'(?=(.)(?!\1|\|)(.)\1)', re.VERBOSE)
    aba = set(aba_bab_re.findall(non_hypernets))
    bab = {(a, b) for b, a in aba_bab_re.findall(hypernets)}
    return bool(aba & bab)


def solution(inp):
    part1 = 0
    part2 = 0
    for line in inp.splitlines():
        if check_tls(line):
            part1 += 1
        if check_ssl(line):
            part2 += 1
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
