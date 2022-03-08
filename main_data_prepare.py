import pandas as pd
from pandas import DataFrame
from main_tools import deduplicate
from dateutil.parser import parse

def get_comments(x):
    result = []

    for y in eval(x[1]).values():
        for z in y:
            result.append((z["referenceTime"], z["score"], z["content"]))
    return result

def get_comments_(x):
    result = []
    for y in eval(x[1]):
        result.append((y["referenceTime"], y["score"], y["content"]))
    return result

def prepare_data(comment_activity_sheet:DataFrame):
    comment=comment_activity_sheet.copy(deep=True)
    product_comment=comment[['活动时间','product_comments']].apply(get_comments,axis=1)
    poor_comment=comment[['活动时间','poor_comment']].apply(get_comments_,axis=1)
    middle_comment=comment[['活动时间','middle_comment']].apply(get_comments_,axis=1)
    good_comment=comment[['活动时间','good_comment']].apply(get_comments_,axis=1)
    deduplicate_comment=(poor_comment+middle_comment+good_comment+product_comment).map(deduplicate)
    comment["评论明细"] = deduplicate_comment

    thin_comment = comment[['productId','评论明细','活动时间']]

    thin_comment['活动前评论'] = thin_comment.apply(lambda x: [c for c in x['评论明细'] if parse(c[0]) < x['活动时间']], axis=1)
    thin_comment['活动后评论'] = thin_comment.apply(lambda x: [c for c in x['评论明细'] if parse(c[0]) > x['活动时间']], axis=1)
    data4train=[]
    for value in thin_comment.values:
        for __comment in value[3]:
            data4train.append([value[0], value[2], __comment[0], __comment[2], '活动前', __comment[1]])
        for __comment in value[4]:
            data4train.append([value[0], value[2], __comment[0], __comment[2], '活动后', __comment[1]])

    data4train_sheet = pd.DataFrame(data4train, columns=['productId', '活动时间', '评论时间', '评论内容', '类型', '评分'])
    return data4train_sheet