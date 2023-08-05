# Author: Salyl Bhagwat, Gammath Works
# Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = 'Salyl Bhagwat'
__copyright__ = 'Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works'

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import (mean_squared_error, r2_score, make_scorer)
from sklearn.model_selection import (TimeSeriesSplit, GridSearchCV)
from sklearn.preprocessing import (StandardScaler, minmax_scale)
from matplotlib import pyplot as plt

try:
    from gammath_spot import gammath_mi_scores as gmis
except:
    import gammath_mi_scores as gmis

try:
    from gammath_spot import gammath_lpep as lpep
except:
    import gammath_lpep as lpep

try:
    from gammath_spot import gammath_utils as gut
except:
    import gammath_utils as gut

try:
    from gammath_spot import gammath_tc as gtc
except:
    import gammath_tc as gtc

#This is experimental and a WIP.

def main():
    tsymbol = sys.argv[1]
    mtdpy, mtd5y = gut.get_min_trading_days()
    path = Path(f'tickers/{tsymbol}')
    df = pd.read_csv(path / f'{tsymbol}_history.csv')
    df_len=len(df)

    prices = df.Close
    prices = df.Close.truncate(before=(df_len-mtdpy)).reset_index().drop('index', axis=1).Close
    prices_len = len(prices)

    gscores = pd.read_csv(path / f'{tsymbol}_micro_gscores.csv', index_col='Unnamed: 0')
    gscores_scaled = gscores.drop('Date', axis=1).apply(minmax_scale)
    print(gscores_scaled)

#    tss = TimeSeriesSplit(n_splits=mtdpy)
#    tss.split(gscores)



if __name__ == '__main__':
    main()
