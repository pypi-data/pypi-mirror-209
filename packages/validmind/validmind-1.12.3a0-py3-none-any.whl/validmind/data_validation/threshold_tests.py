"""
Threshold based tests
"""

from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from dataclasses import dataclass
from pandas_profiling.config import Settings
from pandas_profiling.model.typeset import ProfilingTypeSet
from scipy import stats

from ..vm_models import (
    Dataset,
    TestResult,
    Figure,
    ThresholdTest,
    ResultSummary,
    ResultTable,
    ResultTableMetadata,
)


@dataclass
class ClassImbalance(ThresholdTest):
    """
    The class imbalance test measures the disparity between the majority
    class and the minority class in the target column.
    """

    category = "data_quality"
    name = "class_imbalance"
    required_context = ["dataset"]
    default_params = {"min_percent_threshold": 0.2}

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The class imbalance test returns results like these:
        [{"values": {"0": 0.798, "1": 0.202}, "column": "Exited", "passed": true}]

        So we build a table with 2 rows, one for each class.
        """

        results_table = []
        result = results[0]
        for class_name, class_percent in result.values.items():
            results_table.append(
                {
                    "Class": f'{class_name} ({"Negative" if class_name == "0" or class_name == 0 else "Positive"})',
                    "Percentage of Rows (%)": class_percent * 100,
                }
            )

        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(
                        title=f"Class Imbalance Results for Column {self.dataset.target_column}"
                    ),
                )
            ]
        )

    def run(self):
        # Can only run this test if we have a Dataset object
        if not isinstance(self.dataset, Dataset):
            raise ValueError("ClassImbalance requires a validmind Dataset object")

        if self.dataset.target_column is None:
            print("Skipping class_imbalance test because no target column is defined")
            return

        target_column = self.dataset.target_column
        imbalance_percentages = self.df[target_column].value_counts(normalize=True)

        # Does the minority class represent more than our threshold?
        passed = imbalance_percentages.min() > self.params["min_percent_threshold"]
        results = [
            TestResult(
                column=target_column,
                passed=passed,
                values=imbalance_percentages.to_dict(),
            )
        ]

        return self.cache_results(results, passed=passed)


@dataclass
class Duplicates(ThresholdTest):
    """
    The duplicates test measures the number of duplicate rows found in
    the dataset. If a primary key column is specified, the dataset is
    checked for duplicate primary keys as well.
    """

    category = "data_quality"
    name = "duplicates"
    required_context = ["dataset"]
    default_params = {"min_threshold": 1}

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The duplicates test returns results like these:
        [{"values": {"n_duplicates": 0, "p_duplicates": 0.0}, "passed": true}]

        So we build a table with 1 row and show number of duplicates and percentage of duplicates.
        """
        result = results[0]
        results_table = [
            {
                "Number of Duplicates": result.values["n_duplicates"],
                "Percentage of Duplicates (%)": result.values["p_duplicates"] * 100,
                "Pass/Fail": "Pass" if result.passed else "Fail",
            }
        ]
        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(
                        title="Duplicate Rows Results for Dataset"
                    ),
                )
            ]
        )

    def run(self):
        rows = self.df.shape[0]

        n_duplicates = len(self.df[self.df.duplicated(keep=False)])
        p_duplicates = n_duplicates / rows
        passed = n_duplicates < self.params["min_threshold"]

        results = [
            TestResult(
                passed=passed,
                values={"n_duplicates": n_duplicates, "p_duplicates": p_duplicates},
            )
        ]

        # Additionally, run duplicates test on fields that are primary keys
        primary_keys = []
        for field in self.dataset.fields:
            if field.get("type_options", None) and field.get("type_options").get(
                "primary_key", False
            ):
                primary_keys.append(field["id"])

        for col in primary_keys:
            col_n_duplicates = len(self.df[self.df[col].duplicated(keep=False)])
            col_p_duplicates = col_n_duplicates / rows
            col_passed = col_n_duplicates < self.params["min_threshold"]
            results.append(
                TestResult(
                    column=col,
                    passed=col_passed,
                    values={
                        "n_duplicates": col_n_duplicates,
                        "p_duplicates": col_p_duplicates,
                    },
                )
            )

        return self.cache_results(results, passed=all([r.passed for r in results]))


@dataclass
class HighCardinality(ThresholdTest):
    """
    The high cardinality test measures the number of unique
    values found in categorical columns.
    """

    category = "data_quality"
    name = "cardinality"
    required_context = ["dataset"]
    default_params = {
        "num_threshold": 100,
        "percent_threshold": 0.1,
        "threshold_type": "percent",  # or "num"
    }

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The high cardinality test returns results like these:
        [{"values": {"n_distinct": 0, "p_distinct": 0.0}, "column": "Exited", "passed": true}]
        """
        results_table = [
            {
                "Column": result.column,
                "Number of Distinct Values": result.values["n_distinct"],
                "Percentage of Distinct Values (%)": result.values["p_distinct"] * 100,
                "Pass/Fail": "Pass" if result.passed else "Fail",
            }
            for result in results
        ]
        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(
                        title="High Cardinality Results for Dataset"
                    ),
                )
            ]
        )

    def run(self):
        typeset = ProfilingTypeSet(Settings())
        dataset_types = typeset.infer_type(self.df)

        results = []
        rows = self.df.shape[0]

        num_threshold = self.params["num_threshold"]
        if self.params["threshold_type"] == "percent":
            num_threshold = int(self.params["percent_threshold"] * rows)

        for col in self.df.columns:
            # Only calculate high cardinality for categorical columns
            if str(dataset_types[col]) != "Categorical":
                continue

            n_distinct = self.df[col].nunique()
            p_distinct = n_distinct / rows

            passed = n_distinct < num_threshold

            results.append(
                TestResult(
                    column=col,
                    passed=passed,
                    values={
                        "n_distinct": n_distinct,
                        "p_distinct": p_distinct,
                    },
                )
            )

        return self.cache_results(results, passed=all([r.passed for r in results]))


@dataclass
class HighPearsonCorrelation(ThresholdTest):
    """
    Test that the pairwise Pearson correlation coefficients between the
    features in the dataset do not exceed a specified threshold.
    """

    category = "data_quality"
    name = "pearson_correlation"
    required_context = ["dataset"]
    default_params = {"max_threshold": 0.3}

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The high pearson correlation test returns results like these:
        [{"values": {"correlations": [{"column": "NumOfProducts", "correlation": -0.3044645622389459}]}, "column": "Balance", "passed": false}]
        """
        results_table = [
            {
                "Columns": f'({result.column}, {result.values["correlations"][0]["column"]})',
                "Coefficient": result.values["correlations"][0]["correlation"],
                "Pass/Fail": "Pass" if result.passed else "Fail",
            }
            for result in results
        ]
        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(
                        title="High Pearson Correlation Results for Dataset"
                    ),
                )
            ]
        )

    def run(self):
        corr = self.df.corr(numeric_only=True)
        cols = corr.columns

        # Matrix of True/False where True means the correlation is above the threshold
        # Fill diagonal with False since all diagonal values are 1
        bool_index = abs(corr.values) >= self.params["max_threshold"]
        np.fill_diagonal(bool_index, False)

        # Simple cache to avoid a->b and b->a correlation entries
        correlation_mapping_cache = {}

        def cache_hit(from_field, to_field):
            correlation_keys = [from_field, to_field]
            correlation_keys.sort()
            cache_key = "-".join(correlation_keys)

            if cache_key in correlation_mapping_cache:
                return True

            correlation_mapping_cache[cache_key] = True
            return False

        def corr_items(from_field, to_fields):
            return [
                {
                    "column": to_field,
                    "correlation": corr.loc[from_field, to_field],
                }
                for to_field in to_fields
                if cache_hit(from_field, to_field) is False
            ]

        res = {
            col: corr_items(col, cols[bool_index[i]].values.tolist())
            for i, col in enumerate(cols)
            if any(bool_index[i])
        }

        # Cleanup keys with no values
        res = {k: v for k, v in res.items() if len(v) > 0}
        passed = len(res) == 0

        results = [
            TestResult(
                column=col,
                values={"correlations": correlations},
                passed=False,
            )
            for col, correlations in res.items()
        ]

        return self.cache_results(results, passed=passed)


@dataclass
class MissingValues(ThresholdTest):
    """
    Test that the number of missing values in the dataset across all features
    is less than a threshold
    """

    category = "data_quality"
    name = "missing"
    required_context = ["dataset"]
    default_params = {"min_threshold": 1}

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The missing values test returns results like these:
        [{"values": {"n_missing": 0, "p_missing": 0.0}, "column": "Exited", "passed": true}]
        """
        results_table = [
            {
                "Column": result.column,
                "Number of Missing Values": result.values["n_missing"],
                "Percentage of Missing Values (%)": result.values["p_missing"] * 100,
                "Pass/Fail": "Pass" if result.passed else "Fail",
            }
            for result in results
        ]
        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(
                        title="Missing Values Results for Dataset"
                    ),
                )
            ]
        )

    def run(self):
        rows = self.df.shape[0]

        missing = self.df.isna().sum()
        results = [
            TestResult(
                column=col,
                passed=missing[col] < self.params["min_threshold"],
                values={"n_missing": missing[col], "p_missing": missing[col] / rows},
            )
            for col in missing.index
        ]

        return self.cache_results(results, passed=all([r.passed for r in results]))


@dataclass
class Skewness(ThresholdTest):
    """
    The skewness test measures the extent to which a distribution of
    values differs from a normal distribution. A positive skew describes
    a longer tail of values in the right and a negative skew describes a
    longer tail of values in the left.
    """

    category = "data_quality"
    name = "skewness"
    required_context = ["dataset"]
    default_params = {"max_threshold": 1}

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The skewness test returns results like these:
        [{"values": {"skewness": 1.0}, "column": "NumOfProducts", "passed": false}]
        """
        results_table = [
            {
                "Column": result.column,
                "Skewness": result.values["skewness"],
                "Pass/Fail": "Pass" if result.passed else "Fail",
            }
            for result in results
        ]
        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(title="Skewness Results for Dataset"),
                )
            ]
        )

    def run(self):
        typeset = ProfilingTypeSet(Settings())
        dataset_types = typeset.infer_type(self.df)

        skewness = self.df.skew(numeric_only=True)
        passed = all(abs(skewness) < self.params["max_threshold"])
        results = []

        for col in skewness.index:
            # Only calculate skewness for numerical columns
            if str(dataset_types[col]) != "Numeric":
                continue

            col_skewness = skewness[col]
            results.append(
                TestResult(
                    column=col,
                    passed=abs(col_skewness) < self.params["max_threshold"],
                    values={
                        "skewness": col_skewness,
                    },
                )
            )

        return self.cache_results(results, passed=passed)


@dataclass
class UniqueRows(ThresholdTest):
    """
    Test that the number of unique rows is greater than a threshold
    """

    category = "data_quality"
    name = "unique"
    required_context = ["dataset"]
    default_params = {"min_percent_threshold": 1}

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The unique rows test returns results like these:
        [{"values": {"n_unique": 10000, "p_unique": 1.0}, "column": "Exited", "passed": true}]
        """
        results_table = [
            {
                "Column": result.column,
                "Number of Unique Values": result.values["n_unique"],
                "Percentage of Unique Values (%)": result.values["p_unique"] * 100,
                "Pass/Fail": "Pass" if result.passed else "Fail",
            }
            for result in results
        ]
        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(
                        title="Unique Rows Results for Dataset"
                    ),
                )
            ]
        )

    def run(self):
        rows = self.df.shape[0]

        unique_rows = self.df.nunique()
        results = [
            TestResult(
                column=col,
                passed=(unique_rows[col] / rows) < self.params["min_percent_threshold"],
                values={
                    "n_unique": unique_rows[col],
                    "p_unique": unique_rows[col] / rows,
                },
            )
            for col in unique_rows.index
        ]

        return self.cache_results(results, passed=all([r.passed for r in results]))


@dataclass
class TooManyZeroValues(ThresholdTest):
    """
    The zeros test finds columns that have too many zero values.
    """

    category = "data_quality"
    name = "zeros"
    required_context = ["dataset"]
    default_params = {"max_percent_threshold": 0.03}

    def summary(self, results: List[TestResult], all_passed: bool):
        """
        The zeros test returns results like these:
        [{"values": {"n_zeros": 10000, "p_zeros": 1.0}, "column": "Exited", "passed": true}]
        """
        results_table = [
            {
                "Column": result.column,
                "Number of Zero Values": result.values["n_zeros"],
                "Percentage of Zero Values (%)": result.values["p_zeros"] * 100,
                "Pass/Fail": "Pass" if result.passed else "Fail",
            }
            for result in results
        ]
        return ResultSummary(
            results=[
                ResultTable(
                    data=results_table,
                    metadata=ResultTableMetadata(title="Zeros Results for Dataset"),
                )
            ]
        )

    def run(self):
        rows = self.df.shape[0]
        typeset = ProfilingTypeSet(Settings())
        dataset_types = typeset.infer_type(self.df)
        results = []

        for col in self.df.columns:
            # Only calculate zeros for numerical columns
            if str(dataset_types[col]) != "Numeric":
                continue

            value_counts = self.df[col].value_counts()

            if 0 not in value_counts.index:
                continue

            n_zeros = value_counts[0]
            p_zeros = n_zeros / rows

            results.append(
                TestResult(
                    column=col,
                    passed=p_zeros < self.params["max_percent_threshold"],
                    values={
                        "n_zeros": n_zeros,
                        "p_zeros": p_zeros,
                    },
                )
            )

        return self.cache_results(results, passed=all([r.passed for r in results]))


@dataclass
class TimeSeriesOutliers(ThresholdTest):
    """
    Test that find outliers for time series data using the z-score method
    """

    category = "data_quality"
    name = "time_series_outliers"
    required_context = ["dataset"]
    default_params = {"zscore_threshold": 3}

    def run(self):
        # Check if the index of dataframe is datetime
        is_datetime = pd.api.types.is_datetime64_any_dtype(self.df.index)
        if not is_datetime:
            raise ValueError("Dataset must be provided with datetime index")

        # Validate threshold paremeter
        if "zscore_threshold" not in self.params:
            raise ValueError("zscore_threshold must be provided in params")
        zscore_threshold = self.params["zscore_threshold"]

        temp_df = self.df.copy()
        temp_df = temp_df.dropna()
        typeset = ProfilingTypeSet(Settings())
        dataset_types = typeset.infer_type(temp_df)
        test_results = []
        test_figures = []
        num_features_columns = [
            k for k, v in dataset_types.items() if str(v) == "Numeric"
        ]

        outliers_table = self._identify_outliers(
            temp_df[num_features_columns], zscore_threshold
        )
        fig = self._plot_outliers(temp_df, outliers_table)
        passed = outliers_table.empty

        if not outliers_table.empty:
            outliers_table["Date"] = outliers_table["Date"].astype(str)

        test_results.append(
            TestResult(
                test_name="outliers",
                passed=passed,
                values=outliers_table.to_dict(orient="list"),
            )
        )
        test_figures.append(
            Figure(
                for_object=self,
                key=self.name,
                figure=fig,
            )
        )

        return self.cache_results(test_results, passed=passed, figures=test_figures)

    def _identify_outliers(self, df, threshold):
        """
        Identifies and returns outliers in a pandas DataFrame using the z-score method.

        Args:
        df (pandas.DataFrame): A pandas DataFrame containing the data to be analyzed.
        threshold (float): The absolute value of the z-score above which a value is considered an outlier.

        Returns:
        pandas.DataFrame: A DataFrame containing the variables, z-scores, threshold, and dates of the identified outliers.

        Example:
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]})
        threshold = 2.5
        outliers = _identify_outliers(df, threshold)
        """
        z_scores = pd.DataFrame(stats.zscore(df), index=df.index, columns=df.columns)
        outliers = z_scores[(z_scores > threshold).any(axis=1)]
        outlier_table = []
        for idx, row in outliers.iterrows():
            for col in df.columns:
                if abs(row[col]) > threshold:
                    outlier_table.append(
                        {
                            "Variable": col,
                            "z-score": row[col],
                            "Threshold": threshold,
                            "Date": idx,
                        }
                    )
        return pd.DataFrame(outlier_table)

    def _plot_outliers(self, df, outliers_table):
        """
        Plots time series with identified outliers.

        Args:
            df (pandas.DataFrame): Input data with time series.
            outliers_table (pandas.DataFrame): DataFrame with identified outliers.

        Returns:
            matplotlib.figure.Figure: A matplotlib figure object with subplots for each variable.
        """
        sns.set(style="darkgrid")
        n_variables = len(df.columns)
        fig, axes = plt.subplots(n_variables, 1, sharex=True)

        for i, col in enumerate(df.columns):
            sns.lineplot(data=df, x=df.index, y=col, ax=axes[i], label=col)

            if not outliers_table.empty:
                variable_outliers = outliers_table[outliers_table["Variable"] == col]
                for idx, row in variable_outliers.iterrows():
                    date = row["Date"]
                    outlier_value = df.loc[date, col]
                    axes[i].scatter(
                        date,
                        outlier_value,
                        marker="o",
                        s=100,
                        c="red",
                        label="Outlier" if idx == 0 else "",
                    )

            axes[i].legend()
            axes[i].set_ylabel(col, weight="bold", fontsize=16)
            axes[i].set_title(
                f"Time Series with Outliers for {col}", weight="bold", fontsize=16
            )

        plt.xlabel("Date", weight="bold", fontsize=16)
        plt.tight_layout()

        # Do this if you want to prevent the figure from being displayed
        plt.close("all")
        return fig


@dataclass
class TimeSeriesMissingValues(ThresholdTest):
    """
    Test that the number of missing values is less than a threshold
    """

    category = "data_quality"
    name = "time_series_missing_values"
    required_context = ["dataset"]
    default_params = {"min_threshold": 1}

    def run(self):
        # Check if the index of dataframe is datetime
        is_datetime = pd.api.types.is_datetime64_any_dtype(self.df.index)
        if not is_datetime:
            raise ValueError("Dataset must be provided with datetime index")

        # Validate threshold paremeter
        if "min_threshold" not in self.params:
            raise ValueError("min_threshold must be provided in params")
        min_threshold = self.params["min_threshold"]

        rows = self.df.shape[0]
        missing = self.df.isna().sum()
        test_results = [
            TestResult(
                column=col,
                passed=missing[col] < min_threshold,
                values={"n_missing": missing[col], "p_missing": missing[col] / rows},
            )
            for col in missing.index
        ]

        fig_barplot = self._barplot(self.df, rotation=45, font_size=16)
        fig_heatmap = self._heatmap(self.df)
        test_figures = []
        if fig_barplot is not None:
            test_figures.append(
                Figure(
                    for_object=self,
                    key=f"{self.name}:barplot",
                    figure=fig_barplot,
                    metadata={"type": "barplot"},
                )
            )
            test_figures.append(
                Figure(
                    for_object=self,
                    key=f"{self.name}:heatmap",
                    figure=fig_heatmap,
                    metadata={"type": "heatmap"},
                )
            )

        return self.cache_results(
            test_results,
            passed=all([r.passed for r in test_results]),
            figures=test_figures,
        )

    def _barplot(
        self, df: pd.DataFrame, rotation: int = 45, font_size: int = 18
    ) -> plt.Figure:
        """
        Generate a bar plot of missing values in a pandas DataFrame.

        Args:
        df (pandas.DataFrame): The input DataFrame to plot the missing values of.
        rotation (int): The rotation angle for x-axis labels. Default is 45.
        font_size (int): The font size for x-axis and y-axis labels. Default is 18.

        Returns:
        matplotlib.figure.Figure: A matplotlib figure object containing the bar plot.
        """
        # Create a bar plot using seaborn library
        missing_values = df.isnull().sum()
        if sum(missing_values.values) != 0:
            with plt.style.context("seaborn"):
                fig, ax = plt.subplots()
                sns.barplot(
                    data=missing_values,
                    x=missing_values.index,
                    y=missing_values.values,
                    ax=ax,
                )
                ax.set_xticklabels(
                    labels=missing_values.index, rotation=rotation, fontsize=font_size
                )
                plt.yticks(rotation=45, fontsize=font_size)
                ax.set_ylabel(
                    "Number of Missing Values", weight="bold", fontsize=font_size
                )
                ax.set_xlabel("Variables (Columns)", weight="bold", fontsize=font_size)
                ax.set_title(
                    "Total Number of Missing Values per Variable",
                    weight="bold",
                    fontsize=font_size + 2,
                )
        else:
            fig = None

        return fig

    def _heatmap(self, df):
        """
        Plots a heatmap to visualize missing values in a dataframe with actual years on the x-axis.

        Args:
        df (pandas.DataFrame): The input dataframe to visualize.

        Returns:
        matplotlib.figure.Figure: A matplotlib figure object representing the heatmap plot.

        Raises:
        None
        """
        # Create a boolean mask for missing values
        missing_mask = df.isnull()
        # Set seaborn plot style
        sns.set(style="darkgrid")
        fig, ax = plt.subplots()

        # Plot the heatmap
        sns.heatmap(
            missing_mask.T, cmap="viridis", cbar=False, xticklabels=False, ax=ax
        )

        # Add actual years on the x-axis
        years = df.index.year.unique()
        xticks = [
            df.index.get_loc(df.index[df.index.year == year][0]) for year in years
        ]
        plt.xticks(xticks, years, rotation=45, fontsize=18)
        plt.yticks(rotation=45, fontsize=18)
        plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))
        ax.set_xlabel("Rows (Years)", weight="bold", fontsize=18)
        ax.set_ylabel("Variables (Columns)", weight="bold", fontsize=18)
        ax.set_title(
            "Missing Values Heatmap with Actual Years in Rows",
            weight="bold",
            fontsize=20,
        )
        # Do this if you want to prevent the figure from being displayed
        plt.close("all")

        return fig


@dataclass
class TimeSeriesFrequency(ThresholdTest):
    """
    Test that detect frequencies in the data
    """

    category = "data_quality"
    name = "time_series_frequency"
    required_context = ["dataset"]

    def run(self):
        # Check if the index of dataframe is datetime
        is_datetime = pd.api.types.is_datetime64_any_dtype(self.df.index)
        if not is_datetime:
            raise ValueError("Dataset must be provided with datetime index")

        freq_df = self._identify_frequencies(self.df)
        n_frequencies = len(freq_df["Frequency"].unique())
        test_results = [
            TestResult(
                passed=n_frequencies == 1,
                values=freq_df.to_dict(orient="list"),
            )
        ]
        fig_frequency = self._frequency_plot(self.df)
        test_figures = []
        test_figures.append(
            Figure(
                for_object=self,
                key=f"{self.name}:frequencyplot",
                figure=fig_frequency,
                metadata={"type": "frequencyplot"},
            )
        )
        return self.cache_results(
            test_results,
            passed=all([r.passed for r in test_results]),
            figures=test_figures,
        )

    def _identify_frequencies(self, df):
        """
        Identify the frequency of each series in the DataFrame.

        :param df: Time-series DataFrame
        :return: DataFrame with two columns: 'Variable' and 'Frequency'
        """
        frequencies = []
        freq_dict = {
            "S": "Second",
            "T": "Minute",
            "min": "Minute",
            "H": "Hourly",
            "D": "Daily",
            "B": "Business day",
            "W": "Weekly",
            "MS": "Monthly",
            "M": "Monthly",
            "Q": "Quarterly",
            "A": "Yearly",
            "Y": "Yearly",
        }

        for column in df.columns:
            series = df[column].dropna()
            if not series.empty:
                freq = pd.infer_freq(series.index)
                label = freq_dict[freq] if freq in freq_dict.keys() else freq
            else:
                label = None

            frequencies.append({"Variable": column, "Frequency": label})

        freq_df = pd.DataFrame(frequencies)

        return freq_df

    def _frequency_plot(self, df):
        """
        Creates a frequency plot of time differences between consecutive entries in a DataFrame index.

        Args:
        df (pandas.DataFrame): The input DataFrame.

        Returns:
        A matplotlib Figure object representing the frequency plot of time differences.
        """

        # Calculate the time differences between consecutive entries
        time_diff = df.index.to_series().diff().dropna()

        # Convert the time differences to a suitable unit (e.g., days)
        time_diff_days = time_diff.dt.total_seconds() / (60 * 60 * 24)

        # Create a DataFrame with the time differences
        time_diff_df = pd.DataFrame({"Time Differences (Days)": time_diff_days})
        fig, ax = plt.subplots()
        # Plot the frequency distribution of the time differences
        sns.histplot(
            data=time_diff_df, x="Time Differences (Days)", bins=50, kde=False, ax=ax
        )

        plt.yticks(rotation=45, fontsize=18)
        ax.set_ylabel("Frequency", weight="bold", fontsize=18)
        ax.set_xlabel("Time Differences (Days)", weight="bold", fontsize=18)
        ax.set_title(
            "Frequency",
            weight="bold",
            fontsize=20,
        )

        # Do this if you want to prevent the figure from being displayed
        plt.close("all")

        return fig
