from pharmpy.tools.modelfit.results import calculate_results


def test_modelfit(load_model_for_test, testdata):
    model = load_model_for_test(testdata / 'nonmem' / 'pheno_real.mod')
    assert model


def test_aggregate(load_model_for_test, testdata):
    model = load_model_for_test(testdata / 'nonmem' / 'pheno.mod')
    res = calculate_results([model, model])
    pe = res.parameter_estimates
    assert len(pe) == 2
    assert list(pe.index) == ['pheno', 'pheno']
    assert list(pe.columns) == ['TVCL', 'TVV', 'IVCL', 'IVV', 'SIGMA_1_1']
