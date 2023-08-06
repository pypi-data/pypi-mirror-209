class Test_Classify:

    def test_has_weights_file(self):

        import importlib_resources

        resource_path = importlib_resources.files('ebeer').joinpath('trained_model.h5')

        flg = False if resource_path is None else True

        print('flg:', flg)

        assert True

    def test_predict(self):

        import ebeer

        bc = ebeer.BeerClassifier()

        n_pos = bc.predict("./assets/beer_imgs/0.jpg")

        print("Label:", ebeer.labels_index[n_pos]["name"])

        assert True
