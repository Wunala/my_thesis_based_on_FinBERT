import pandas as pd

# 导入原始文本数据
# df = pd.read_csv('sina_data_30-12.csv')
# # 创建空的Dataframe对象
# result = pd.DataFrame(columns=['data_id', 'day', 'time', 'content', 'sentiment', 'rate'])
# # 遍历文本并进行预测
# for i in range(df.shape[0]):
#     dic = predicts([df['content'][i]])
#     result.loc[i] = [list(dic.keys())[0], list(dic.values())[0][0], list(dic.values())[0][1]]
#
# # 保存到csv文件
# result.to_csv('test_sentiment_results.csv')

df = pd.read_csv('data/sina_data_30-12.csv')
print(len(df))
