#import modules
import os
import csv

input_file = 'election_data.csv'
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')
output_file = 'election_results.txt'
txtpath = os.path.join('..', 'PyPoll', 'election_results.txt')

candidates, total_candidates, candidate_perc, candidate_total, summaries = ([] for i in range(5))


with open(csvpath, 'r+', newline='') as election_data:
    reader = csv.reader(election_data, delimiter=',')
    next(reader)
    number_rows = 0

    for row in reader:
        total_candidates.append(row[2])
        number_rows += 1

sorted_candidates = sorted(total_candidates)

for i in range(number_rows):
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        candidates.append(sorted_candidates[i])

print("\nElection Results")
print("-"*50)
print("Total Votes:", number_rows)
print("-"*50)


for j in range(len(candidates)):
    candidate_count = 0

    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1

    candidate_perc.append(round(candidate_count / number_rows * 100, 1))
    candidate_total.append(candidate_count)


zip = zip(candidates, candidate_perc, candidate_total)

for row in zip:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summaries.append(summary)


for k in range(len(candidate_perc)):
    if candidate_total[k] > candidate_total[k - 1]:
        winner = candidates[k]


print("-" * 40)
print("Winner:", winner)
print("-"*25)
print("\n\n")


with open(txtpath, 'w', newline='') as election_results:
    writer = csv.writer(election_results)

    writer.writerows([
        ["Election Results for: " + input_file],
        ["-"*25],
        ["Total Votes: " + str(number_rows)],
    
    ])
    writer.writerows(summaries)
    writer.writerows([
        ["-"*25],
        ["Winner: " + str(winner)],
    ])


