from solution import rna_ify


def test_rna_ify():
    assert rna_ify("TTTT") == "UUUU"
    assert rna_ify("GCAT") == "GCAU"
    assert rna_ify("GACCGCCGCC") == "GACCGCCGCC"
