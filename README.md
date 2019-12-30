# opsschool4-coding

Given the input: https://github.com/ops-school/opsschool4-coding/blob/master/hw.json Which contains names paired with their ages, and the bucket ranges (age ranges).

for example: {“ppl_names”: { “arie”: 35, “david”: 99}, “buckets”: [11, 22, 40]} 0-11, 11-22, 22-40, 40-100

And turn the input in to a YAML: 22-40: arie 40-100: david

Notes:

condition to enter the bucket is being equal or larger than the lower number and smaller of the higher number.
you can assume that the lowest limit for age is 0 and the highest is the maximum age +1.
Plan:

import the json file to python
sort the list by the ages
calculate the higher limit - what's the maximum age and add 1 to limit
create the buckets and name them
sort the names into the buckets created
turn the output into YAML file
done
