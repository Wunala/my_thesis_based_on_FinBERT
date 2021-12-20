from predict import predicts
import pandas as pd
# 1:pos; 2:neg;
# 导入原始文本数据

df = pd.read_csv('data/Sina_Daily/20211209.csv')
# 创建空的Dataframe对象
result = pd.DataFrame(columns=['data_id', 'day', 'time', 'content', 'if_focus', '0', '1', '2'])
# 遍历文本并进行预测
for i in range(len(df)):  # 实验了400条
    data_id = df['data_id'][i]
    day = df['data_time'][i]
    time = df['timing'][i]
    content = df['content'][i]
    if_focus = df['if_focus'][i]
    dic = predicts([df['content'][i]])
    result.loc[i] = [data_id,
                     day,
                     time,
                     content,
                     if_focus,
                     list(dic.values())[0][0][1],
                     list(dic.values())[0][1][1],
                     list(dic.values())[0][2][1]]

# 保存到csv文件
result.to_csv('Sent_Result/Sina/20211209_sent.csv')



