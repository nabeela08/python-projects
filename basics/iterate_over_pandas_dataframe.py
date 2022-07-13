student_dict = {
    "Students": ["Elena", "Damon", "Caroline", "Stefan"],
    "Score": [78, 86, 68, 59]
}

#looping through dictionaries
# for(key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


#loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    print(row)
    