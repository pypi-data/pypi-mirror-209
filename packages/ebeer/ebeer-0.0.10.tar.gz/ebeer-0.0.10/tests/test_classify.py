
class Test_Classify:

    def test_predict(self):

        from ebeer.beer_classifier import BeerClassifier
        from ebeer.label_index import labels_index

        bc = BeerClassifier()

        n_pos = bc.predict("./assets/beer_imgs/0.jpg")

        print("n_pos:", n_pos, " - label:",
              labels_index[n_pos]["name"], "\n\n")

        assert True
