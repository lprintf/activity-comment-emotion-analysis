from typing import List, Tuple
import pandas
from pandas.core.frame import DataFrame
from jieba import posseg
import jieba

jieba.enable_parallel()  # 开启并行分词
jieba.enable_paddle()  # 加载词性标注模块

def load(path: str) -> list:
    """加载数据

    Args:
        path (str): 数据文件路径

    Returns:
        list: 数据列表
    """
    with open(path, "rd") as fp:
        pandas.read_excel(path)


def dimention_focus(
    sheet: DataFrame,
    span: Tuple[int, int]
) -> DataFrame:
    tmp = sheet[
        sheet.columns[span[0] : span[1]].append(
            sheet.columns[
                2:3
            ]  # append代码非必要，拼接了原始评论，以备不时
        )
    ]
    return tmp[
        tmp[tmp.columns[1]].notnull()
    ]  # 筛选第一个属性非空的行，有些编号非空但得分为空


def split_dimentions(
    sheet: DataFrame,
    span_list: List[Tuple[int, int]] = [
        (5, 8),
        (8, 11),
        (11, 14),
    ],
) -> List[DataFrame]:
    """返回多组列表，包含不同维度评价

    Args:
        sheet (DataFrame): 主列表
        span_list (List[Tuple[int, int]], optional): 列分组规则. Defaults to [ (5, 8), (8, 11), (11, 14), ].

    Returns:
        List[DataFrame]: 根据分组规则分出的多组列表
    """
    return [
        dimention_focus(sheet, span)
        for span in span_list
    ]


def get_stopwords_list(
    filepath: str,
) -> List[str]:
    with open(filepath, "r") as fp:
        return set(
            [w.strip() for w in fp.readlines()]
        )


def seg_sentence(
    sentence: str, stopwords_list: List[str]
):
    stop_flag = [
        "x",
        "c",
        "u",
        "d",
        "p",
        "t",
        "uj",
        "m",
        "f",
        "r",
    ]  # 见https://github.com/fxsjy/jieba，词性标注章节
    if type(sentence)=='float':
        print(sentence)
    sentence_seged = posseg.cut(
        sentence.replace("\n", "")
    )
    outstr = []
    for word, flag in sentence_seged:
        if (
            word not in stopwords_list
            and flag not in stop_flag
        ):
            outstr.append(word)
    return " ".join(outstr)


def generate_train_data(
    sheet: DataFrame, stopwords_list
):
    dimension = sheet.values[:, 0].tolist()
    x = [
        seg_sentence(x, stopwords_list)
        for x in dimension
    ]
    score = sheet.values[:, 1].tolist()
    return x, score
