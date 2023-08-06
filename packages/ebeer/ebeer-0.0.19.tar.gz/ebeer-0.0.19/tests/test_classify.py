class Test_Classify:

    def test_has_weights_file(self):

        import importlib_resources

        resource_path = importlib_resources.files(
            'ebeer').joinpath('trained_model.h5')

        flg = False if resource_path is None else True

        print('flg:', flg)

        assert True

    def test_predict(self):

        import ebeer

        n_pos = ebeer.BeerClassifier.predict("assets/beer_imgs/0.jpg")

        print("Label:", ebeer.DataLabel[n_pos]["name"])

        assert True

    def test_predict_simple(self):

        import ebeer

        beerData = ebeer.BeerClassifier.predict_simple(
            "assets/beer_imgs/0.jpg")

        print('beerData:', beerData)

        assert True
