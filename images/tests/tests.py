from django.test import TestCase
from ..models import *
# Create your tests here.

class ImageTestCase(TestCase):

    # set up method
    def setUp(self):
        self.loc =Location(name='Nairobi')
        self.loc.save_loc()
        self.new= Picture(name='My Picture', description='Photo taken by me', category='food', location='nairobi',image='default.jpg')
        self.new.save_pic()


    def test_instance(self):
        self.assertTrue(isinstance(self.new,Picture))

    def test_save_method(self):
        self.new.save_pic()
        pics=Picture.objects.all()
        self.assertTrue(len(pics) > 0)


    def test_delete_method(self):
        self.new.delete_pic()
        pics=Picture.objects.all()
        self.assertTrue(len(pics) < 0)



class Location(TestCase):
    def setUp(self):
        self.nimo = Editor(first_name='Nimo', last_name='Maina', email='nimo@example.com', phone_number='0712345678')
        self.nimo.save_editor()

        # Create a new tag and save it
        self.new_tag= tags(name='testing')
        self.new_tag.save()

        self.new_article=Article(title = 'Test Article',post='This is a random test Post',editor = self.nimo)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news=Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_dae(self):
        test_date = '2019-02-25'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
