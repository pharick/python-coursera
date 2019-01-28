fin = open("input.txt")

parties = dict()
votes_sum = 0

for line in fin:
    separator_index = line.rfind(" ")
    name = line[:separator_index]
    votes = int(line[separator_index + 1:])
    parties[name] = [votes, None, None]
    votes_sum += votes

quotient = votes_sum / 450

places_sum = 0

for party in parties:
    places = int(parties[party][0] // quotient)
    fraction = parties[party][0] / quotient - parties[party][0] // quotient
    parties[party][1] = places
    parties[party][2] = fraction
    places_sum += places

rest = 450 - places_sum

if rest > 0:
    for party in sorted(sorted(parties, key=lambda party: -parties[party][0]),
                        key=lambda party: -parties[party][2]):
        if rest == 0:
            break
        parties[party][1] += 1
        rest -= 1

for party in parties:
    print(party, parties[party][1])
