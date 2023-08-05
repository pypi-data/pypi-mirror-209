
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# 결측치를 평균으로 채우는 함수
def fill_mean(df, cols):
    for col in cols:
        df[col] = df[col].fillna(df[col].mean())
    return df

# 결측치를 중앙값으로 채우는 함수
def fill_median(df, cols):
    for col in cols:
        df[col] = df[col].fillna(df[col].median())
    return df

# 결측치를 최빈값으로 채우는 함수
def fill_mode(df, cols):
    for col in cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

# 특정 칼럼을 표준화하는 함수
def standard(df, cols):
    scaler = StandardScaler()
    for col in cols:
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))
    return df

# 특정 칼럼을 정규화하는 함수
def normalize(df, cols):
    scaler = MinMaxScaler()
    for col in cols:
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))
    return df

# 데이터프레임 정보 출력 함수
def info(df):
    print("Data shape: ", df.shape)
    print("Missing values: ", df.isnull().sum())
    print("Data types:\n", df.dtypes)
