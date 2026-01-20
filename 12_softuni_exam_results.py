exam_results = dict()
submissions = dict()

while (command := input()) != "exam finished":
    tokens = command.split("-")
    if tokens[1] == 'banned':
        del exam_results[tokens[0]]
    else:
        name, language, points = command.split("-")
        points = int(points)
        if name not in exam_results.keys():
            exam_results[name] = [{language: int(points)}]
        else:
            language_exists = False
            for idx in range(len(exam_results[name])):
                for lan, score in exam_results[name][idx].items():
                    if language == lan:
                        language_exists = True
                        if points > score:
                            exam_results[name][idx] = points
            if not language_exists:
                exam_results[name].append({language:points})
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for name, results in exam_results.items():
    for index in range(len(results)):
        for crs, pt in results[index].items():
            result_points = pt
            print(f"{name} | {result_points}")

print("Submissions:")
for name, results in submissions.items():
    print(f"{name} - {results}")




