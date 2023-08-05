from polly.auth import Polly
from polly import helpers
from polly import constants as const
from polly.omixatlas import OmixAtlas
from polly.errors import paramException
from polly.tracking import Track
from polly import omixatlas_hlpr
from polly.constants import COHORT_SUPPORTED_DATATYPES, COHORT_SUPPORTED_DATASOURCES

import pandas as pd
import plotly.express as px


class Analyze:
    """
    The Analyze class contains functions which can be used to identify cohorts in datasets, \
    perform differential expression and pathway analysis, and execute meta-analysis workflows.\
    Args:
        token (str): Authentication token from polly
    Usage:
        from polly.analyze import Analyze

        analysis = Analyze(token)
    """

    def __init__(self, token=None, env="", default_env="polly") -> None:
        # check if COMPUTE_ENV_VARIABLE present or not
        # if COMPUTE_ENV_VARIABLE, give priority
        env = helpers.get_platform_value_from_env(
            const.COMPUTE_ENV_VARIABLE, default_env, env
        )
        self.session = Polly.get_session(token, env=env)
        self.omixatlas_obj = OmixAtlas()
        self.elastic_url = (
            f"https://api.datalake.discover.{self.session.env}.elucidata.io/elastic/v2"
        )

    @Track.track_decorator
    def identify_cohorts(self, repo_key: str, dataset_id: str) -> pd.DataFrame:
        """
        This function is used to get the cohorts that can be created from samples in a GEO dataset.
        Please note: Currently only Bulk RNASeq datasets from GEO source are supported.
        If results are generated for other datatypes or datasource, they may be inaccurate.
        If you want to use this functionality for any other data type and source,
        please reach out to polly.support@elucidata.io

        If you want to plot a sunburst on specific columns of interest, please use the following code:
        ` import plotly.express as px`
        ` metadata = identify_cohorts(repo_key, dataset_id)`
        ` fig = px.sunburst(metadata, path=['column_1','column_2','column_n'])`
        ` fig.show()`

        Args:
            repo_key (int/str): repo_id or repo_name in str or int format
            dataset_id (str): dataset_id of the GEO dataset. eg. "GSE132270_GPL11154_raw"
        Returns:
            Dataframe showing values of samples across factors/cohorts.

        """
        # param checks
        omixatlas_hlpr.parameter_check_for_dataset_id(dataset_id)
        omixatlas_hlpr.parameter_check_for_repo_id(repo_key)
        repo_key = omixatlas_hlpr.make_repo_id_string(repo_key)

        # Get dataset level metadata and check if datatype is supported
        response_omixatlas = self.omixatlas_obj.omixatlas_summary(repo_key)
        data = response_omixatlas.get("data", "")
        index_name = data.get("indexes", {}).get("files", "")
        if index_name is None:
            raise paramException(
                title="Param Error", detail="Repo entered is not an omixatlas."
            )
        elastic_url = f"{self.elastic_url}/{index_name}/_search"
        query = helpers.elastic_query(index_name, dataset_id)
        metadata = helpers.get_metadata(self, elastic_url, query)
        source_info = metadata.get("_source", "")
        if (source_info["data_type"] not in COHORT_SUPPORTED_DATATYPES) or (
            source_info["dataset_source"] not in COHORT_SUPPORTED_DATASOURCES
        ):
            raise paramException(
                title="Param Error",
                detail="Only Bulk RNA Seq datasets that are from GEO are supported",
            )

        # Get sample level metadata
        col_metadata = self.omixatlas_obj.get_metadata(repo_key, dataset_id, "samples")
        # Index should be sample IDs which are available in geo_accession
        col_metadata = col_metadata.set_index("geo_accession")

        # Remove curated columns and column containing timestamp
        col_metadata = col_metadata.loc[
            :, ~col_metadata.columns.str.contains("curated|time", case=False)
        ]
        # Remove column with cohorts information if it exists
        col_metadata = col_metadata.drop(
            ["sample_characteristics"], axis=1, errors="ignore"
        )
        # Keeps only columns with more than 1 unique value
        col_metadata = col_metadata.loc[:, col_metadata.nunique() > 1]

        # Print a message if there are no unique columns
        if col_metadata.empty:
            print(
                """There is no variation across the sample(s) in the dataset,
             i.e. all metadata is the same. Hence, no cohorts can be created for this dataset.
             The output sunburst will be blank and the output dataframe will be empty.
             Please use `omixatlas.get_metadata("repo_id","dataset_id","table_name")`
             to view the sample-level metadata of a dataset."""
            )

        # Remove columns like sample id etc that has all unique values
        col_metadata = col_metadata.loc[:, col_metadata.nunique() != len(col_metadata)]
        # Fix for 'None entries cannot have not-None children' error in sunburst
        col_metadata = col_metadata.fillna("notgiven")

        # Get list of columns to plot in sunburst, in ascending order of nunique() values
        df = col_metadata
        df = pd.DataFrame(df.nunique()).reset_index()
        df = df.sort_values(by=[0])
        lst = df["index"].to_list()
        print("Factors based on which cohorts can be created for this dataset:", lst)

        #         # if a column contains 'age', bucket into groups
        #         age_col_name = [col for col in col_metadata.columns if "age" in col]
        #         if age_col_name:
        #             # create age ranges and labels
        #             age_bins = [0, 20, 40, 60, 80, 100]
        #             age_labels = ["0-20", "20-40", "40-60", "60-80", "80-100"]

        #             # bin age values into age ranges
        #             array_of_arrays = col_metadata.loc[:, age_col_name].values
        #             array_of_strings = [x[0] for x in array_of_arrays]
        #             col_metadata["age_range"] = pd.cut(
        #                 array_of_strings, bins=age_bins, labels=age_labels
        #             )

        #         # Create dataframe with distribution of factors and number of samples
        #         distribution_df = {"Factor": [], "Cohorts": [], "Number of Samples": []}
        #         if age_col_name:
        #             lst.remove(age_col_name[0])
        #             lst.append("age_range")
        #         for column_name in lst:
        #             unique_values = col_metadata[column_name].unique()
        #             for cohort in unique_values:
        #                 n_samples = len(col_metadata[col_metadata[column_name] == cohort])
        #                 distribution_df["Factor"].append(column_name)
        #                 distribution_df["Cohorts"].append(cohort)
        #                 distribution_df["Number of Samples"].append(n_samples)
        #         distribution_df = pd.DataFrame(distribution_df)
        #         if age_col_name:
        #             distribution_df["Factor"] = distribution_df["Factor"].replace(
        #                 "age_range", age_col_name[0]
        #             )
        #             lst = df["index"].to_list()
        #         print(distribution_df)

        # Plot sunburst
        fig = px.sunburst(col_metadata, path=lst)
        fig.show()
        return col_metadata[lst]
