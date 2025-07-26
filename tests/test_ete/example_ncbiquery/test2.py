from eGPS4Py import NCBITaxa

if __name__ == "__main__":
    # unittest.main()
    ncbi = NCBITaxa()
    a = ncbi.get_descendant_taxa("hominidae")
    # print(a)
    # print(ncbi.get_common_names(a))
    # print(ncbi.get_topology(a))
    b = ncbi.get_descendant_taxa("homo", intermediate_nodes=True, collapse_subspecies=True)
    # print(ncbi.get_taxid_translator(b))
    #
    print(ncbi.get_common_names(b))
    # ncbi.update_taxonomy_database()