
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# 결측치를 평균으로 채우기
def fill_na_mean(df, columns):
    for column in columns:
        df[column] = df[column].fillna(df[column].mean())
    return df

# 결측치를 중앙값으로 채우기
def fill_na_median(df, columns):
    for column in columns:
        df[column] = df[column].fillna(df[column].median())
    return df

# 결측치를 최빈값으로 채우기
def fill_na_mode(df, columns):
    for column in columns:
        df[column] = df[column].fillna(df[column].mode()[0])
    return df

# 특정 칼럼 스케일링 (표준화)
def standardize(df, columns):
    scaler = StandardScaler()
    for column in columns:
        df[column] = scaler.fit_transform(df[column].values.reshape(-1, 1))
    return df

# 특정 칼럼 스케일링 (정규화)
def normalize(df, columns):
    scaler = MinMaxScaler()
    for column in columns:
        df[column] = scaler.fit_transform(df[column].values.reshape(-1, 1))
    return df

# 데이터프레임의 칼럼을 원-핫 인코딩
def one_hot_encode(df, columns):
    return pd.get_dummies(df, columns=columns)

# 데이터를 학습용 데이터와 테스트용 데이터로 나누기
def split_data(df, test_size=0.2, random_state=42):
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)
    return train, test

# 데이터프레임의 정보를 출력
def print_info(df):
    print("Data shape: ", df.shape)
    print("Missing values: ", df.isnull().sum())
    print("Data types:\n", df.dtypes)

