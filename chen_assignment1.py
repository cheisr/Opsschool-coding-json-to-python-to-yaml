if __name__ == '__main__':

    import json
    import operator
    import yaml


with open('hw.json') as myfile:
        data = myfile.read()

parsed_json = json.loads(data)
print(parsed_json)

ppl_ages_dict = parsed_json["ppl_ages"]
age_buckets_list = parsed_json["buckets"]

print("ages dict: ", ppl_ages_dict)
print("buckets list: ", age_buckets_list)

max_age = max(ppl_ages_dict.items(), key=operator.itemgetter(1))[1]
max_age += 1
print("max age: ", max_age)

age_buckets_list += [0, max_age]
age_buckets_list.sort()
print("buckets list: ", age_buckets_list)

buckets_counter = len(age_buckets_list)
print(age_buckets_list, buckets_counter)

keystring = "{0} - {1}"
result = {}

for i in range(1, buckets_counter):
    values_list = []
    dictkey = keystring.format(age_buckets_list[i-1], age_buckets_list[i])
    for name in ppl_ages_dict:
        if age_buckets_list[i-1] <= ppl_ages_dict[name] < age_buckets_list[i]:
            values_list.append('' + name)
    result[dictkey] = values_list

with open('result', 'w') as yaml_file:
    yaml.dump(result, yaml_file, default_flow_style=False, allow_unicode=True)
    print("yaml output: ", result)