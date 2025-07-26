import pandas as pd


def get_HGNC_human_gene_df():
    """
    Get complete human gene information from HGNC database.
    
    This function reads the local HGNC complete human gene dataset Excel file
    and returns a pandas DataFrame with all gene information.
    
    Parameters:
        None
        
    Returns:
        pandas.DataFrame: DataFrame containing complete HGNC human gene information
        
    Example:
        >>> df = get_HGNC_human_gene_df()
        >>> print(df.columns)
        Index(['hgnc_id', 'symbol', 'name', ...], dtype='object')
        
    Note:
        Make sure the hgnc_complete_set.xlsx file exists at the specified path
    """
    path = r"C:\Users\yudal\Documents\project\geneNamesGetter\hgnc_complete_set.xlsx"
    df = pd.read_excel(path)
    return df


if __name__ == "__main__":
    # Test code: get gene dataframe and filter specific genes
    df1 = get_HGNC_human_gene_df()
    # First set of test gene IDs
    target = {'HGNC:7556', 'HGNC:7555', 'HGNC:7559', 'HGNC:7553'}
    # Second set of test gene IDs (overwrites the first set)
    target = {'HGNC:2514', 'HGNC:6207'}
    # Filter target genes and print results
    result = df1[df1['hgnc_id'].isin(target)]
    print(result)