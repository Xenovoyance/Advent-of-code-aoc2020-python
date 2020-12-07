run_env = "prod" ## test or prod
if run_env == "test":
    input = "aoc2020-python/day4/test.txt"
else:
    input = "aoc2020-python/day4/input.txt"

person = {"byr": "", "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "", "cid": ""}
persons = []

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

def checkheight(height_string):
    validated = False
    if person_to_check['hgt']:
        if person_to_check['hgt'][-2:] == "in":
            if int(person_to_check['hgt'][:-2]) >= 59 and int(person_to_check['hgt'][:-2]) <= 76:
                validated = True
        elif person_to_check['hgt'][-2:] == "cm":
            if int(person_to_check['hgt'][:-2]) >= 150 and int(person_to_check['hgt'][:-2]) <= 193:
                validated = True
    return validated

def checkhaircolor(hair_color):
    validated = False
    if hair_color:
        if str(hair_color[0]) == "#":
            if hair_color[1:].isalnum():
                validated = True
    return validated

def checkeyecolor(eye_color):
    validated = False
    if eye_color:
        if eye_color == "amb" or eye_color == "blu" or eye_color == "brn" or eye_color == "gry" or eye_color == "grn" or eye_color == "hzl" or eye_color == "oth":
            validated = True
    return validated

def checkpid(pid):
    validated = False
    if pid:
        if len(pid) == 9 and pid.isdigit():
            validated = True
    return validated

# Part 1
correct_passports = 0
for person_to_check in persons:
    if person_to_check['byr']:
        if person_to_check['iyr']:
            if person_to_check['eyr']:
                if person_to_check['hgt']:
                    if person_to_check['hcl']:
                        if person_to_check['ecl']:
                            if person_to_check['pid']:
                                correct_passports += 1

print("P1 Correct passports: " + str(correct_passports))

# Part 2
correct_passports = 0
for person_to_check in persons:
    if person_to_check['byr'] and len(person_to_check['byr']) == 4 and int(person_to_check['byr']) >= 1920 and int(person_to_check['byr']) <= 2002:
        if person_to_check['iyr'] and len(person_to_check['iyr']) == 4 and int(person_to_check['iyr']) >= 2010 and int(person_to_check['iyr']) <= 2020:
            if person_to_check['eyr'] and len(person_to_check['eyr']) == 4 and int(person_to_check['eyr']) >= 2020 and int(person_to_check['eyr']) <= 2030:
                if (checkheight(person_to_check['hgt'])):
                    if checkhaircolor(person_to_check['hcl']):
                        if checkeyecolor(person_to_check['ecl']):
                            if checkpid(person_to_check['pid']):
                                correct_passports += 1

print("P2 Correct passports: " + str(correct_passports))