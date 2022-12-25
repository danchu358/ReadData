import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io


######################################### Text data 불러와서 가공 및 저장 함수
def cal():

    global df

    with open('C:/Users/21052/Desktop/49TTCLL.csv', 'r') as f:
        df_list = f.readlines()
        # print(df_list)

        opstr = ' '
        for x in df_list:
            opstr += ' ' + x
        # print(opstr)

    df = pd.read_csv(io.StringIO(opstr), sep=",", header=None)
    # print(df)

    df.to_csv('C:/Users/21052/Desktop/OTP_avs_log.csv', encoding='utf-8-sig')
    # df.to_csv('C:/Users/21052/Desktop/OTP_avs_log.csv', index=False, mode='a', encoding='utf-8-sig')

if __name__ == "__main__":
    cal()

df_split = df.iloc[:2, 12:1768]
print(df_split)
df_split2 = df_split.iloc[1, :]
print(df_split2)
df_t = df_split2.transpose()
print(df_t)
df_t.to_csv('C:/Users/21052/Desktop/df_split.csv', encoding='utf-8-sig', index=False)

# df_limit = df.iloc[:2, 10:12]
# print(df_limit)
# plt.plot(df_split)
# df_split2.plot()
# plt.title('title')
# plt.xlabel('xlabel')
# plt.ylabel('ylabel')
# plt.xlim(df_limit[1:,10:11])
# plt.ylim(0, 100)
# plt.show()    