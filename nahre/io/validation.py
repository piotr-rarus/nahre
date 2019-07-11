from lazy_property import LazyProperty
import numpy as np
import pandas as pd

from . import base


class Validator(base.DataSet):
    """
    This class is responsible for:
    - loading validation records from .csv file;
    - calculating validation errors abs(test_x - pred_x) for every value
    - aggregating statistic from whole batch validation: avg, min, max, std...

    Returns
    -------
    Validator
        Validation set instance with pandas data frame loaded from csv.
    """

    def __init__(self, path):
        """
        Creates new ValidationSet instance.

        Parameters
        ----------
        path : str
            Path to csv file. Place your values column-wise.
            Records are denoted by rows.

        """

        super().__init__(path)

    @LazyProperty
    def records(self):
        return pd.read_csv(self.PATH, index_col='file')

    def validate(self, preds):
        """
        Validates batch against giver prediction set.

        Parameters
        ----------
        preds : dict
            Key - record ID (e.g. filename); value - dictionary of pred values.

        Returns
        -------
        pd.DataFrame
            Validation result for each record and aggregated stats.
        """

        validated = {}

        for filename, pred in preds.items():
            if filename in self.records.index:
                validated[filename] = {}
                test = self.records.loc[filename]
                for k, pv in pred.items():

                    tv = test[k]
                    dk = abs(tv - pv)

                    validated[filename]['pred_' + k] = pv
                    validated[filename]['test_' + k] = tv
                    validated[filename]['d_' + k] = dk

        validated = pd.DataFrame.from_dict(validated, orient='index')
        return validated

    def aggregate(self, validation):
        """
        Aggregates stats from validation result.

        Parameters
        ----------
        validation : pd.DataFrame
            Validation results for each record.

        Returns
        -------
        pd.DataFrame
            Aggregated statistics from batch validation.
            This includes:
            - avg
            - avg_sqr
            - min
            - max
            - std
            - var
        """

        stats = {}
        for k in validation.axes[0]:
            if k.startswith('d_'):
                values = validation.loc[k].values

                stats[k] = {}
                stats[k]['avg'] = np.average(values)
                stats[k]['arg_sqr'] = np.average(values ** 2)
                stats[k]['min'] = np.min(values)
                stats[k]['max'] = np.max(values)
                stats[k]['std'] = np.std(values)
                stats[k]['var'] = np.var(values)

        return pd.DataFrame.from_dict(stats)
