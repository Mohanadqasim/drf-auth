from django.contrib.auth import get_user_model
from .models import Movie
from django.test import TestCase
class MovieTests(TestCase):
    @classmethod
    def setUp(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()
        test_thing = Movie.objects.create(name='flower', owner=testuser1, desc="test desc ...")
        test_thing.save()
    def test_movies_model(self):
        movie = Movie.objects.get(id=1)
        actual_owner= str(movie.owner)
        actual_name = str(movie.name)
        actual_desc = str(movie.desc)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"flower")
        self.assertEqual(actual_desc,"test desc ...")