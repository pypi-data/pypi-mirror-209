import pandas as pd
from regbot import signal

df = pd.read_csv('../jupyter/regbot_v39_validation.csv')

y_pred = []
def getSignal(x,y,z):
    #return signal(x,y,z)
    return 1 if signal(x,y,z) > 0.5 else 0

print(df.head())
df = df.sample(frac=1).reset_index(drop=True)
print(df.head())
df = df[df['enter_long'] == 0].tail(1000)
print(df.head())

df['result'] = df.apply(lambda row: getSignal(row['rsi-05'],row['rsi-15'],row['grad-sma-25']), axis=1)

print(df.head())

print(len(df[df['result'] == df['enter_long']]), len(df))
