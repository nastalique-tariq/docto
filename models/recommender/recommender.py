import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=93)


def Convert(string):
    li = list(string.split(","))
    return li


def Convert_to_list(string):
    strr = str(string)
    li = list(strr.split(","))
    return li


doctors = pd.read_csv("final_doc_data2.csv")
doctors['Disease-treated'] = doctors['Disease-treated'].apply(Convert)
doctors["City"] = doctors["City"].apply(Convert_to_list)
doctors["Specialization"] = doctors["Specialization"].apply(Convert_to_list)
doctors["Cost"] = doctors["Cost"].apply(Convert_to_list)
doctors['Tags'] = + doctors['Specialization'] + doctors['Disease-treated'] + doctors['City'] + doctors['Cost']

new_df2 = doctors[['Doctor id', 'Doctor Name', 'Specialization', 'Disease-treated', 'City', 'Cost', 'Tags']]
new_df2['Tags'] = new_df2['Tags'].apply(lambda x: " ".join(x))
new_df2['Tags'] = new_df2['Tags'].apply(lambda x: x.lower())

vectors = cv.fit_transform(new_df2['Tags']).toarray()

similarity = cosine_similarity(vectors)


def recommend(doctor):
    doctor_index = new_df2[new_df2['Doctor Name'] == doctor]
    if len(doctor_index) == 0:
        return []
    doctor_index = doctor_index.index[0]

    distances = similarity[doctor_index]
    doctor_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    res = [new_df2.iloc[i[0]].to_dict() for i in doctor_list]

    for i in doctor_list:
        print(new_df2.iloc[i[0]][1])

    return res


def recommend_doctor(disease):
    i = 0
    found = False
    for row in new_df2['Disease-treated']:
        if disease in row:
            found = True
            break
        i += 1
    if not found:
        return []
    distances = similarity[new_df2.index[i]]
    doctor_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    res = [new_df2.iloc[i[0]].to_dict() for i in doctor_list]
    for i in doctor_list:
        print(new_df2.iloc[i[0]][1])
    return res
