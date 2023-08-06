'''
Author: hexu
Date: 2021-10-14 14:54:05
LastEditTime: 2023-05-15 15:45:17
LastEditors: Hexu
Description: 数据集
FilePath: /iw-algo-fx/intelliw/datasets/datasets.py
'''
import json
from typing import List, Tuple, overload
from intelliw.datasets.spliter import get_set_spliter
from intelliw.datasets.datasource_base import DatasetSelector, AbstractDataSource, AbstractDataSourceWriter, \
    DataSourceType as DST, DatasetType, AlgorithmsType
from intelliw.datasets.datasource_empty import EmptyDataSourceWriter
from intelliw.utils.logger import _get_framework_logger
from intelliw.config import config
from intelliw.utils.global_val import gl


logger = _get_framework_logger()


class DataSets:
    def __init__(self, datasource: AbstractDataSource):
        self.datasource = datasource
        self.alldata = []
        self.column_meta = []
        self.model_type = gl.model_type  # 分类/回归/ocr/时间序列/文本分类。。。。。

    def empty_reader(self, dataset_type=DatasetType.TRAIN):
        return self.datasource.reader(page_size=1, offset=0, limit=0, transform_function=None,
                                      dataset_type=dataset_type)

    def reader(self, page_size=10000, offset=0, limit=0, split_transform_function=None):
        return self.datasource.reader(page_size, offset, limit, split_transform_function)

    @overload
    def data_pipeline(self, split_transform_function,
                      alldata_transform_function, feature_process):
        pass

    def data_pipeline(self, *args):
        if config.SOURCE_TYPE == DST.NLP_TYPE:
            return self._nlp_data(config.DATA_SPLIT_MODE)
        elif config.SOURCE_TYPE == DST.CV_TYPE:
            return self._images_data(*self._data_pipeline(*args))
        else:
            if self.model_type == AlgorithmsType.TIME_SERIES:
                args = list(args)
                args.extend([True, True])
            train, validation, test = self._data_pipeline(*args)
            return [train], [validation], [test]

    def read_all_data(self, split_transform_function=None, to_df=False):
        reader = self.reader(config.DATA_SOURCE_READ_SIZE, 0,
                             self.datasource.total(), split_transform_function)
        for idx, content in enumerate(reader):
            if config.SOURCE_TYPE != DST.CV_TYPE:
                if idx == 0:
                    self.column_meta = reader.meta
                    self.alldata = content
                elif 'result' in content and 'result' in self.alldata:
                    self.alldata['result'].extend(content['result'])
            else:
                self.alldata.extend(content)

        if to_df and config.SOURCE_TYPE == DST.CV_TYPE:
            from intelliw.utils.spark_process import Engine
            engine = Engine()
            self.alldata = engine.pd.DataFrame(
                columns=[i['code'] for i in self.column_meta],
                data=self.alldata['result']
            )
        return self.alldata

    def _data_pipeline(self, stf, atf, fp, ignore_dp=False, ignore_split=False):
        # 获取全部数据(切片数据处理， 列选择和数据筛选)
        alldata = self.read_all_data(stf)

        _data_process_args = [
            alldata, atf, fp
        ]
        _get_set_spliter_args = [
            alldata
        ]

        if ignore_dp:
            _data_process_args.append(True)
        if ignore_split:
            _get_set_spliter_args.append(True)

        # 数据处理（时间序列，全局函数和特征工程）
        alldata = self._data_process(*_data_process_args)

        # 数据集切分
        spliter = get_set_spliter(*_get_set_spliter_args)

        # 数据集处理 图片下载/语料下载/数据返回
        return spliter.train_reader(), spliter.validation_reader(), spliter.test_reader()

    def _data_process(self, alldata, atf, fp, do_nothing=False):
        if do_nothing is True:
            pass
        elif config.SOURCE_TYPE == DST.CV_TYPE:
            pass
        elif atf or fp:
            alldata = atf(alldata) if atf else alldata
            alldata = fp(alldata) if fp else alldata
        return alldata

    def _images_data(self, train, val, test):
        tr = self.datasource.download_images(
            train, dataset_type=DatasetType.TRAIN)
        v = self.datasource.download_images(
            val, dataset_type=DatasetType.VALID)
        te = self.datasource.download_images(
            test, dataset_type=DatasetType.TEST)
        return tr, v, te

    def _nlp_data(self, split_mode: int):
        self.datasource.corpora_process(split_mode)
        return [self.datasource()] * 3


class MultipleDataSets:
    def __init__(self) -> None:
        self._total = 0
        self.datasets: List[DataSets] = []
        self.join_type = "no"
        self.model_type = gl.model_type  # 分类/回归/ocr/时间序列/文本分类。。。。。
        self.column_meta = []

    @property
    def total(self):
        return self._total

    @property
    def onlyone(self):
        return self._total == 1

    def add(self, dataset: DataSets):
        self.datasets.append(dataset)
        self._total += 1

    def pop(self, idx=None):
        if idx is not None and isinstance(idx, int):
            return self.datasets.pop(idx)
        else:
            return self.datasets.pop()

    @overload
    def data_pipeline(self, split_transform_function,
                      alldata_transform_function, feature_process):
        pass

    def data_pipeline(self, *args):
        if config.SOURCE_TYPE == DST.NLP_TYPE:
            result = None
            for idx in range(self._total):
                dataset = self.pop(0)
                result = dataset._nlp_data(config.DATA_SPLIT_MODE)
            return result
        elif config.SOURCE_TYPE == DST.CV_TYPE:
            result = None
            for idx in range(self._total):
                dataset = self.pop(0)
                result = dataset._images_data(*dataset._data_pipeline(*args))
            return result
        else:
            # train_set_list, validation_set_list, test_set_list
            trl, vl, tel = [[None] * self._total for _ in range(3)]
            args = list(args) + [True]  # TODO 多数据集暂时不支持特征工程
            if self.model_type == AlgorithmsType.TIME_SERIES:
                args.append(True)
            for idx in range(self._total):
                gl.dataset_idx = idx
                dataset = self.pop(0)
                trl[idx], vl[idx], tel[idx] = dataset._data_pipeline(*args)
                self.column_meta.extend(dataset.column_meta)
            return trl, vl, tel


def get_dataset(cfg) -> Tuple[DataSets, MultipleDataSets]:
    if cfg and isinstance(cfg, str):
        dataset_conf = json.loads(cfg)
    elif config.SOURCE_TYPE == DST.EMPTY:
        dataset_conf = [{"SOURCE_TYPE": DST.EMPTY}]
    else:
        dataset_conf = cfg

    # table, cv, nlp
    mds = MultipleDataSets()
    for cfg in dataset_conf:
        datasource = DatasetSelector.parse(cfg)
        mds.add(DataSets(datasource))
    if mds.onlyone:
        return mds.pop()
    return mds


def get_datasource_writer(cfg: str = None) -> AbstractDataSourceWriter:
    output_datasource_type = 0
    cfg = cfg or config.OUTPUT_DATASET_INFO
    if cfg:
        if isinstance(cfg, str):
            cfg = json.loads(cfg)
        output_datasource_type = cfg['sourceType']
    if output_datasource_type == DST.EMPTY:
        return EmptyDataSourceWriter()
    elif output_datasource_type in (DST.INTELLIV, DST.IW_FACTORY_DATA):
        from intelliw.datasets.dataset_writer import DataSourceWriter
        return DataSourceWriter(output_config=cfg, writer_type=output_datasource_type)
    else:
        err_msg = f"输出数据源设置失败，无效的数据源类型: {output_datasource_type}"
        raise ValueError(err_msg)
