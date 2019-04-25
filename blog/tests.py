from django.test import TestCase
from .models import Entry
# Create your tests here.




class EntryModelTest(TestCase):
    # The rest of our model code
    class Meta:
        verbose_name_plural = "entries"

##case 1
    def test_string_representation(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)
##case 2
    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")
##case 3

class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
