def part1(filename):
    import re
    with open(filename) as f:
        f = f.read().split('\n\n')
    count = 0
    # passports = []
    for i in f:
        passport = {}
        i = i.split()
        for j in i:
            j = j.split(':')
            passport[j[0]] = j[1]
        if 'cid' not in passport.keys():
            passport['cid'] = ''
        # passports.append(passport)
        i = passport.keys()
        if 'byr' in i and 'iyr' in i and 'eyr' in i and 'hgt' in i and 'hcl' in i and 'ecl' in i and 'pid' in i:# and 'cid' in i:
            if re.search('^[0-9]{4}$',passport['byr']):
                byr = int(passport['byr'])
                if byr < 1920 or byr > 2002:
                    print("Failed byr:",byr)
                    continue
            else:
                    print("Failed byr:",byr)
                    continue

            if re.search('^[0-9]{4}$',passport['iyr']):
                iyr = int(passport['iyr'])
                if iyr < 2010 or iyr > 2020:
                    print('Failed iyr:',iyr)
                    continue
            else:
                print('Failed iyr:',iyr)
                continue

            if re.search('^[0-9]{4}$',passport['eyr']):
                eyr = int(passport['eyr'])
                if eyr < 2020 or eyr > 2030:
                    print('Failed eyr:',eyr)
                    continue
            else:
                print('Failed eyr:',eyr)
                continue

            hgt = passport['hgt']
            try:
                hgtnum = int(hgt[:-2])
            except:
                print("Failed hgt to int:",hgt)
                continue
            if hgt[-2:] == 'cm' and (hgtnum < 150 or hgtnum > 192):
                print("Failed cm height:",hgt)
                continue
            elif hgt[-2:] == 'in' and (hgtnum < 59 or hgtnum > 76):
                print("Failed in height:",hgt)
                continue

            if not re.search('^#[0-9a-f]{6}$',passport['hcl']):
                print("Failed hcl:",passport['hcl'])
                continue

            if passport['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
                print("Failed ecl:",passport['ecl'])
                continue

            if not re.search('^[0-9]{9}$',passport['pid']):
                print("Failed pid:",passport['pid'])
                continue
            
            print('Valid:',passport)
            count += 1
    print(count)

part1('input.txt')