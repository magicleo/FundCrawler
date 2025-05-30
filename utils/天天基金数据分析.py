#!/usr/bin/env python
# coding: utf-8

# 晨星
# https://www.morningstar.cn/#/fund/003309
# 天天基金(APP比网页分析维度多)
# https://fundf10.eastmoney.com/jbgk_005159.html
#同花顺（APP比网页内容多）
#https://fund.10jqka.com.cn/012943/index.html


import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)

# 显示所有行
pd.set_option('display.max_rows', None)

# 显示所有内容（不换行）
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


df=pd.read_csv('/ymt-ai/liuxl/FundCrawler/result.csv')



df.columns



for col in [
  '资产规模(亿)',
    '一个月回报', '三个月回报', '六个月回报', '今年以来回报', '一年回报', '二年回报（年化）',
       '三年回报（年化）', '五年回报（年化）', '十年回报（年化）', '回报(一年)', '标准差(一年)', '最大回撤(一年)',
       '下行风险(一年)', '晨星风险(一年)', '夏普比例(一年)', '卡玛比率(一年)', '索提诺比率(一年)',
       '阿尔法系数(一年)', '贝塔系数(一年)', 'R平方(一年)', '月度胜率(一年)', '涨势捕获率(一年)',
       '跌势捕获率(一年)', '回报(三年)', '标准差(三年)', '最大回撤(三年)', '下行风险(三年)', '晨星风险(三年)',
       '夏普比例(三年)', '卡玛比率(三年)', '索提诺比率(三年)', '阿尔法系数(三年)', '贝塔系数(三年)', 'R平方(三年)',
       '月度胜率(三年)', '涨势捕获率(三年)', '跌势捕获率(三年)', '标准差(三年%)', '标准差(五年%)',
       '标准差(十年%)', '夏普比率(三年)', '夏普比率(五年)', '夏普比率(十年)', '阿尔法系数(相对于基准指数%)',
       '贝塔系数(相对于基准指数)', 'R平方(相对于基准指数)'
]:
    df[col] = pd.to_numeric(df[col], errors='coerce')



df = df.fillna(0)

pdf = df.groupby("基金类型").size().reset_index(name='cnt')
pdf.sort_values(by='cnt',ascending=False).head(15)


# # 找纯债型基金

df[
(df['一个月回报']>0.3)
&(df['三个月回报']>0.9)
&(df['一年回报']>3)
&(df['二年回报（年化）']>3)
&(df['三年回报（年化）']>3)
&(df["基金类型"].str.contains("债券")) 
&(~df["基金类型"].str.contains("长债|混合")) 
&(df['最大回撤(一年)']>-2)
&(df['最大回撤(三年)']>-3)
&(df['资产规模(亿)']>4)
].sort_values(by='夏普比例(一年)',ascending=False)


# # 含混合型

# In[141]:


df[
(df['一个月回报']>0.3)
&(df['三个月回报']>0.9)
&(df['六个月回报']>1.8)
&(df['一年回报']>4)
&(df['二年回报（年化）']>4)
&(df['三年回报（年化）']>4)
&(df["基金类型"].str.contains("债券|偏债")) 
&(~df["基金类型"].str.contains("长债")) 
&(df['最大回撤(一年)']>-2.5)
&(df['最大回撤(三年)']>-5)
&(df['资产规模(亿)']>4)

].shape


# In[142]:


df[
(df['一个月回报']>0.3)
&(df['三个月回报']>0.9)
&(df['六个月回报']>1.8)
&(df['一年回报']>4)
&(df['二年回报（年化）']>4)
&(df['三年回报（年化）']>4)
&(df["基金类型"].str.contains("债券|偏债")) 
&(~df["基金类型"].str.contains("长债")) 
&(df['最大回撤(一年)']>-2.5)
&(df['最大回撤(三年)']>-5)
&(df['资产规模(亿)']>4)
].sort_values(by='夏普比例(一年)',ascending=False)


# In[114]:


# 按照年化3.6%以上债基，筛选
# 月度超过0.3, 3月超过0.9，6个月超过1.8，1年超过3.6，成立年限超过3年
df[
(df['一个月回报']>0.3)
&(df['三个月回报']>0.9)
&(df['六个月回报']>1.8)
&(df['一年回报']>4)
&(df['二年回报（年化）']>4)
&(df['三年回报（年化）']>4)
].sort_values(by='夏普比率(三年)',ascending=False)

df[df['基金代码']=='010430']







