import pandas as pd

# pandas is for working with data like tables


# series - one dimensional
marks = pd.Series([85, 90, 78])
print(marks)

marks2 = pd.Series([85, 90, 78], index=["jay", "rahul", "amit"])
print(marks2["jay"])


# dataframe - like an excel table
data = {
    "name": ["Jay", "Rahul", "Amit", "Neha", "Priya"],
    "dept": ["IT", "IT", "HR", "HR", "IT"],
    "salary": [50000, 60000, 40000, 50000, 55000],
    "marks": [85, 90, 35, 72, 88],
    "city": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)
print(df)


# reading files
# df = pd.read_csv("students.csv")
# df = pd.read_excel("students.xlsx")
# df = pd.read_json("students.json")


# checking data
print(df.head())
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())


# selecting columns
print(df["name"])
print(df[["name", "salary"]])


# iloc by position, loc by label
print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[0, 2])
print(df.loc[0, "name"])
print(df.loc[0:2, ["name", "salary"]])


# filtering
print(df[df["salary"] > 50000])
print(df[(df["salary"] >= 50000) & (df["dept"] == "IT")])
print(df[(df["salary"] > 55000) | (df["city"] == "Mumbai")])


# sorting
print(df.sort_values("salary"))
print(df.sort_values("salary", ascending=False))
print(df.sort_values(["city", "salary"], ascending=[True, False]))


# add column
df["passed"] = df["marks"] >= 40
df["grade"] = df["marks"].apply(lambda x: "A" if x >= 80 else ("B" if x >= 60 else "F"))
print(df)

# update column
df["salary"] = df["salary"] + 5000

# remove column
df.drop("grade", axis=1, inplace=True)
df.drop("passed", axis=1, inplace=True)

# rename
df.rename(columns={"name": "student_name"}, inplace=True)
print(df.columns)
df.rename(columns={"student_name": "name"}, inplace=True)


# string operations
names = pd.Series(["  jay  ", "RAHUL", "amit"])
print(names.str.strip())
print(names.str.lower())
print(names.str.upper())
print(names.str.contains("r", case=False))


# missing values
data2 = {
    "name": ["Jay", "Rahul", "Amit", "Neha"],
    "age": [21, None, 20, None],
    "salary": [50000, 60000, None, 50000]
}
df2 = pd.DataFrame(data2)

print(df2.isnull())
print(df2.isnull().sum())
print(df2.dropna())

df2["age"] = df2["age"].fillna(0)
df2["salary"] = df2["salary"].fillna(df2["salary"].mean())
print(df2)


# duplicates
data3 = {"name": ["Jay", "Rahul", "Jay"], "marks": [85, 90, 85]}
df3 = pd.DataFrame(data3)
df3.drop_duplicates(inplace=True)
df3 = df3.reset_index(drop=True)
print(df3)


# groupby
print(df.groupby("dept")["salary"].mean())
print(df.groupby("dept")["salary"].agg(["mean", "min", "max"]))
print(df.groupby(["city", "dept"])["salary"].mean())
print(df["dept"].value_counts())

# stats
print(df["salary"].sum())
print(df["salary"].mean())
print(df["salary"].min())
print(df["salary"].max())
print(df["salary"].median())


# concat - stack two dataframes
df_a = pd.DataFrame({"name": ["Jay", "Rahul"], "salary": [50000, 60000]})
df_b = pd.DataFrame({"name": ["Amit", "Neha"], "salary": [40000, 50000]})
combined = pd.concat([df_a, df_b], ignore_index=True)
print(combined)


# merge - like sql join
emp = pd.DataFrame({"emp_id": [1, 2, 3], "name": ["Jay", "Rahul", "Amit"], "dept_id": [10, 10, 20]})
dept = pd.DataFrame({"dept_id": [10, 20], "dept_name": ["IT", "HR"]})
result = pd.merge(emp, dept, on="dept_id")
print(result)


# export
combined.to_csv("output.csv", index=False)
combined.to_json("output.json", orient="records")
print("saved")

import os
os.remove("output.csv")
os.remove("output.json")
