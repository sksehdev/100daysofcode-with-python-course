import os
import csv
import collections
from typing import List
import pandas as pd
import logbook
import sys


class DataAnalysis:

    def __init__(self, csv_file):
        base_folder = os.path.dirname(__file__)
        self.filename = os.path.join(base_folder, 'data', csv_file)
        self.data = []
        self.Record = collections.namedtuple('Record', 'state, median_household_income, share_unemployed_seasonal,'
                                             'share_population_in_metro_areas,'
                                             'share_population_with_high_school_degree share_non_citizen,'
                                             'share_white_poverty,'
                                             'gini_index, share_non_white, share_voters_voted_trump,'
                                             'hate_crimes_per_100k_splc ,avg_hatecrimes_per_100k_fbi')

    def csv_reader(self):
        with open(self.filename, 'r', encoding='utf-8') as fin:
            reader = csv.DictReader(fin)

            self.data.clear()
            for row in reader:
                if not ("" in row.values()):
                    record = self.parse_row(row)
                    self.data.append(record)
            return self.data

    def parse_row(self, row):
        row['median_household_income'] = int(row['median_household_income'])
        row['share_unemployed_seasonal'] = float(row['share_unemployed_seasonal'])
        row['share_population_in_metro_areas'] = float(row['share_population_in_metro_areas'])
        row['share_population_with_high_school_degree'] = float(row['share_population_with_high_school_degree'])
        row['share_non_citizen'] = float(row['share_non_citizen'])
        row['share_white_poverty'] = float(row['share_white_poverty'])
        row['gini_index'] = float(row['gini_index'])
        row['share_non_white'] = float(row['share_non_white'])
        row['share_voters_voted_trump'] = float(row['share_voters_voted_trump'])
        row['hate_crimes_per_100k_splc'] = float(row['hate_crimes_per_100k_splc'])
        row['avg_hatecrimes_per_100k_fbi'] = float(row['avg_hatecrimes_per_100k_fbi'])

        record = self.Record(
            **row
        )

        return record

    def highest_median_income(self) -> List:
        return sorted(self.csv_reader(), key=lambda x: x.median_household_income, reverse=True)

    def highest_trump_votes(self) -> List:
        return sorted(self.csv_reader(), key=lambda x: x.share_voters_voted_trump, reverse=True)

    def highest_white_poor(self) -> List:
        return sorted(self.csv_reader(), key=lambda x: x.share_white_poverty, reverse=True)

    def highest_avg_hatecrime(self) -> List:
        return sorted(self.csv_reader(), key=lambda x: x.avg_hatecrimes_per_100k_fbi, reverse=True)
