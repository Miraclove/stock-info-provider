import json

import akshare as ak
import pandas as pd


def get_zh_volume_300():
    data_zh_all = ak.stock_zh_a_spot_em().drop(columns=['序号','涨跌额','成交量'])
    data_zh_volume_300 = data_zh_all.sort_values(by='成交额', ascending=False).head(300)
    data_zh_volume_300['成交额'] = round(data_zh_volume_300['成交额']/100000000,3)

    return data_zh_volume_300


if __name__ == '__main__':
    print(get_zh_volume_300())
    # data_header = list(get_zh_volume_300().columns)
    # json_txt = get_zh_volume_300().to_json(orient="records",force_ascii=False)
    # json_list = json.loads(json_txt)
    # json_list = {"data":json_list}
    # print(json_list)

    # data_list_header = list(get_zh_volume_300().columns)
    # header_column = []
    # for header in data_list_header:
    #     header_column.append({"data":header})
    # print(header_column)


    # data = get_zh_volume_300()
    # print(data.values.tolist())
    # data_zh_all = ak.stock_zh_a_spot_em()
    # # 显示所有列
    # pd.set_option('display.max_columns', None)
    # # 显示所有行
    # pd.set_option('display.max_rows', None)
    # # 设置value的显示长度为100，默认为50
    # pd.set_option('max_colwidth', 100)
    #
    # data_zh_volume_300 = data_zh_all.sort_values(by='成交额',ascending=False).head(300)
    # print(data_zh_volume_300)

