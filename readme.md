# 情感分析实验--商品活动对用户评价的影响



## log

### bert训练日志
训练10epoch，在第一个epoch之后模型验证集准确率和f1_score稳定在96%,可完全拟合训练集。
```
current loss: 1.170670509338379          current acc: 0.375
current loss: 0.4180063917046756         current acc: 0.8563432835820896
train loss:  0.31530060880228966         train acc: 0.8929257977700884
valid loss:  0.13135706215492776         valid acc: 0.9534482758620689   f1_score: 0.9543918918918919
current loss: 0.12304583191871643        current acc: 0.9375
current loss: 0.117590182164304          current acc: 0.9614427860696517
train loss:  0.11163032512134798         train acc: 0.9638600538254517
valid loss:  0.14193103687737035         valid acc: 0.9551724137931035   f1_score: 0.956081081081081
current loss: 0.03256088122725487        current acc: 1.0
current loss: 0.08909222928214058        current acc: 0.9692164179104478
train loss:  0.08804479440491349         train acc: 0.9705882352941176
valid loss:  0.16134737392988158         valid acc: 0.95         f1_score: 0.9510135135135135
current loss: 0.05174955725669861        current acc: 1.0
current loss: 0.06331128770003643        current acc: 0.9813432835820896
train loss:  0.06903063927125758         train acc: 0.9794309880815071
valid loss:  0.14477129596461719         valid acc: 0.9551724137931035   f1_score: 0.956081081081081
current loss: 0.09667693078517914        current acc: 0.9375
current loss: 0.056246270904020956       current acc: 0.9822761194029851
train loss:  0.05393473562738784         train acc: 0.9828911956939639
valid loss:  0.13748340917486898         valid acc: 0.9534482758620689   f1_score: 0.9543918918918919
current loss: 0.016206348314881325       current acc: 1.0
current loss: 0.04467292703150665        current acc: 0.9866293532338308
train loss:  0.04505255851077567         train acc: 0.986159169550173
valid loss:  0.13555608230416435         valid acc: 0.9672413793103448   f1_score: 0.9679054054054054
current loss: 0.010042335838079453       current acc: 1.0
current loss: 0.039162815988656896       current acc: 0.9891169154228856
train loss:  0.03648228664593942         train acc: 0.9900038446751249
valid loss:  0.15814639139618422         valid acc: 0.9534482758620689   f1_score: 0.9543918918918919
current loss: 0.0047212401404976845      current acc: 1.0
current loss: 0.026916217958943833       current acc: 0.9909825870646766
train loss:  0.03649442173480599         train acc: 0.9888504421376394
valid loss:  0.12972805343687888         valid acc: 0.9603448275862069   f1_score: 0.9611486486486487
current loss: 0.003555796341970563       current acc: 1.0
current loss: 0.02835105172652677        current acc: 0.9916044776119403
train loss:  0.03126445593936597         train acc: 0.9903883121876201
valid loss:  0.1542410595945045          valid acc: 0.9637931034482758   f1_score: 0.964527027027027
current loss: 0.0024404041469097137      current acc: 1.0
current loss: 0.027175129096450014       current acc: 0.9900497512437811
train loss:  0.028298824624889786        train acc: 0.9898116109188774
valid loss:  0.12965496264341464         valid acc: 0.9672413793103448   f1_score: 0.9679054054054054
```


## past

情况有变，重写所有数据预处理和预测打分模块。

```
## 流程

1. 爬数据： [all_comment](raw/all_comment(1).rar)；
2. 预处理1： 根据月份划分数据； [8月前](raw/细致处理后文件/text_8月前。。%20.csv), [8月后](raw/细致处理后文件/text_8月后（处理后）%20(1).csv)；
3. 预处理2： [提取8月前评论](raw/评论预处理程序/评论数据预处理_v2.ipynb)后人工标注；得到[数据集1](raw/训练文件/数据集/数据集1.xlsx)
   1. 情感分析： 在[数据集1](raw/训练文件/数据集/数据集1.xlsx)上训练贝叶斯模型，然后用该模型对[数据集2](raw/训练文件/数据集/数据集2.xlsx)进行预测，得到[结果](raw/分商品_v2(1)(1).xlsx)。

## 数据集描述

[数据集1](raw/训练文件/数据集/数据集1.xlsx)，第2019行开始是差评数据，同时包含八月前后数据。

## 思路

   1. 对 数据集1 进行规范处理得到 [for_modeling]((data/for_modeling.xlsx))；
   2. 加载后划分为90%的训练集，和10%的测试集；
   3. 使用多项式朴素贝叶斯算法在训练集上，针对不同维度训练模型，在测试集上进行测试得到模型准确度。（使用提取特征时使用二元词袋表述句子）
   4. 使用训练好的模型对全部数据进行情感分析，得到更多标注好的数据方便进一步统计分析。

# 后续工作

   1. 数据范围增加到4个月 all_comment;
   2. 使用逻辑回归和SVM，随机森林进行情感分析;
```