def ckbyr(birth_year): return birth_year and len(birth_year) == 4 and int(birth_year) >= 1920 and int(birth_year) <= 2002
def ckiyr(issue_year): return issue_year and len(issue_year) == 4 and int(issue_year) >= 2010 and int(issue_year) <= 2020
def ckeyr(exp_date): return exp_date and len(exp_date) == 4 and int(exp_date) >= 2020 and int(exp_date) <= 2030
def ckhcl(hair_color): return hair_color and str(hair_color[0]) == "#" and hair_color[1:].isalnum()
def ckecl(eye_color): return eye_color and (eye_color == "amb" or eye_color == "blu" or eye_color == "brn" or eye_color == "gry" or eye_color == "grn" or eye_color == "hzl" or eye_color == "oth")
def ckpid(pid): return pid and len(pid) == 9 and pid.isdigit()
def ckrange(text_string, min, max): return text_string >= min and text_string <= max
def ckhgt(height_string):
    if height_string:
        if height_string[-2:] == "in": return ckrange(int(height_string[:-2]),59,76)
        elif height_string[-2:] == "cm": return ckrange(int(height_string[:-2]),150,193)

input = "aoc2020-python/day4/input.txt"
person = {"byr": "", "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "", "cid": ""}
persons = []
correct_passports_p1 = 0
correct_passports_p2 = 0

with open(input) as blockstream:
    for stream in blockstream:
        person_pieces = stream.split()
        if person_pieces:
            for data_points in person_pieces:    
                data_point = data_points.split(":")
                person[data_point[0]] = data_point[1]
        else:
            persons.append(person)
            person = {"byr": "", "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "", "cid": ""}
persons.append(person)

for pc in persons:
    if pc['byr'] and pc['iyr'] and pc['eyr'] and pc['hgt'] and pc['hcl'] and pc['ecl'] and pc['pid']: correct_passports_p1 += 1
    if ckbyr(pc['byr']) and ckiyr(pc['iyr']) and ckeyr(pc['eyr']) and (ckhgt(pc['hgt'])) and ckhcl(pc['hcl']) and ckecl(pc['ecl']) and ckpid(pc['pid']): correct_passports_p2 += 1

print("P1 Correct passports: " + str(correct_passports_p1))
print("P2 Correct passports: " + str(correct_passports_p2))