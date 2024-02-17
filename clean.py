#!/usr/bin/python3
"""
Script to clean dataset
"""
import pandas as pd
import numpy as np


df = pd.read_csv('archive/houses_for_sale.csv')

df['selling price'] = df['selling price'].replace(
        'Price not communicated',
        np.nan
        )
