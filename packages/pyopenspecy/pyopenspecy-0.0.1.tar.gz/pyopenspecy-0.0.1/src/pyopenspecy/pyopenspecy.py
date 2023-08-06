from importlib.resources import files
import pandas as pd
import pyopenspecy
from thefuzz import fuzz


def random_raman_spectrum() -> tuple[pd.DataFrame, dict]:
    metadata = random_raman_metadata()
    df = _raman_data_df()
    return df[df.sample_name == metadata["sample_name"]], metadata


def random_ftir_spectrum() -> tuple[pd.DataFrame, dict]:
    metadata = random_ftir_metadata()
    df = _ftir_data_df()
    return df[df.sample_name == metadata["sample_name"]], metadata


def random_ftir_metadata() -> dict:
    return _metadata_row_to_dict(_ftir_metadata_df().sample(n=1))


def random_raman_metadata() -> dict:
    return _metadata_row_to_dict(_raman_metadata_df().sample(n=1))


def _metadata_row_to_dict(row: pd.DataFrame) -> dict:
    return {
        "sample_name": row.sample_name.iloc[0],
        "spectrum_identity": row.spectrum_identity.iloc[0],
        "spectrum_id": row.spectrum_id.iloc[0],
        "other_information": row.other_information.iloc[0],
    }


def _raman_data_df() -> pd.DataFrame:
    data_filepath = str(files(pyopenspecy) / "data/raman_library.csv")
    df = pd.read_csv(data_filepath)
    _verify_real_df_not_pointer(df)
    return df


def _verify_real_df_not_pointer(df: pd.DataFrame):
    if len(df) < 10:
        raise Exception("Data file pointer detected. Run `git lfs pull`.")


def _ftir_data_df() -> pd.DataFrame:
    metadata_filepath = str(files(pyopenspecy) / "data/ftir_library.csv")
    df = pd.read_csv(metadata_filepath)
    _verify_real_df_not_pointer(df)
    return df


def _raman_metadata_df() -> pd.DataFrame:
    metadata_filepath = str(files(pyopenspecy) / "data/raman_metadata.csv")
    df = pd.read_csv(metadata_filepath)
    _verify_real_df_not_pointer(df)
    return df


def _ftir_metadata_df() -> pd.DataFrame:
    metadata_filepath = str(files(pyopenspecy) / "data/ftir_metadata.csv")
    df = pd.read_csv(metadata_filepath)
    _verify_real_df_not_pointer(df)
    return df


def raman_metadata_by_id(id: int) -> dict:
    df = _raman_metadata_df()
    return _metadata_row_to_dict(df[df.sample_name == id])


def ftir_metadata_by_id(id: int) -> dict:
    df = _ftir_metadata_df()
    return _metadata_row_to_dict(df[df.sample_name == id])


def raman_spectrum_by_id(id: int) -> tuple[pd.DataFrame, dict]:
    df = _raman_data_df()
    return df[df.sample_name == id], raman_metadata_by_id(id)


def ftir_spectrum_by_id(id: int) -> tuple[pd.DataFrame, dict]:
    df = _raman_data_df()
    return df[df.sample_name == id], ftir_metadata_by_id(id)


def fuzzy_search_raman(query, limit):
    return _fuzzy_search_df(_raman_metadata_df(), query, limit)


def fuzzy_search_ftir(query, limit):
    return _fuzzy_search_df(_ftir_metadata_df(), query, limit)


def _fuzzy_search_df(df, query, limit):
    print("Column 'sample_name' contains the id parameter used by pyopenspecy")
    df_meta_scored = df.spectrum_identity.apply(func=lambda s: fuzz.token_set_ratio(query, s))
    indices_of_matched_rows = df.index.isin(df_meta_scored.nlargest(limit).index)
    df_results = df[indices_of_matched_rows]
    df_results.insert(0, 'id', df_results.pop("sample_name"))
    return df_results
