from .models import Year, Climate
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse



class MyModelsTestCase(TestCase):
    def setUp(self):
        self.year1 = Year.objects.create(ID=1, year=2022)
        self.climate1 = Climate.objects.create(year_ID=self.year1, year=2022, month=1, lat="40N",
                                               lon_175_180W=10, lon_170_175W=12, lon_165_170W=8,
                                               lon_160_165W=15, lon_155_160W=20, lon_150_155W=18,
                                               lon_145_150W=25, lon_140_145W=30, lon_135_140W=28,
                                               lon_130_135W=35, created_date=timezone.now())

    def test_year_model(self):
        year1 = Year.objects.get(ID=1)
        self.assertEqual(year1.year, 2022)

    def test_climate_model(self):
        climate1 = Climate.objects.get(year_ID__ID=1)
        self.assertEqual(climate1.year, 2022)
        self.assertEqual(climate1.month, 1)
        self.assertEqual(climate1.lat, "40N")
        self.assertEqual(climate1.lon_175_180W, 10)
        self.assertEqual(climate1.lon_170_175W, 12)
        self.assertEqual(climate1.lon_165_170W, 8)
        self.assertEqual(climate1.lon_160_165W, 15)
        self.assertEqual(climate1.lon_155_160W, 20)
        self.assertEqual(climate1.lon_150_155W, 18)
        self.assertEqual(climate1.lon_145_150W, 25)
        self.assertEqual(climate1.lon_140_145W, 30)
        self.assertEqual(climate1.lon_135_140W, 28)
        self.assertEqual(climate1.lon_130_135W, 35)
        self.assertLess((timezone.now() - climate1.created_date).total_seconds(), 1)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.years_url = reverse('years')
        self.dashboard_url = reverse('dashboard')

        self.year1 = Year.objects.create(ID=121, year=2000)
        self.year2 = Year.objects.create(ID=122, year=2001)

        self.climate1 = Climate.objects.create(year_ID=self.year1, year=2000, month=1, lat='35-40S', lon_175_180W=-99, lon_170_175W=-99, lon_165_170W=-99, lon_160_165W=-99, lon_155_160W=-99, lon_150_155W=-99, lon_145_150W=-99, lon_140_145W=-99, lon_135_140W=-99, lon_130_135W=-99)
        self.climate2 = Climate.objects.create(year_ID=self.year2, year=2001, month=1, lat='35-40S', lon_175_180W=-99, lon_170_175W=-99, lon_165_170W=-99, lon_160_165W=-99, lon_155_160W=-99, lon_150_155W=-99, lon_145_150W=-99, lon_140_145W=-99, lon_135_140W=-99, lon_130_135W=-99)

    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'climatology_stories/index.html')

    def test_years(self):
        response = self.client.get(self.years_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'climatology_stories/years.html')
        self.assertEquals(len(response.context['page_obj'].object_list), 2)

    def test_year_detail(self):
        self.year1 = Year.objects.create(ID=123, year=2000)
        response = self.client.get(reverse('year_detail', args=[self.year1.ID]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'climatology_stories/climate_data.html')
        self.assertEquals(len(response.context['page_obj'].object_list), 0)

    # def test_dashboard(self):
    #     response = self.client.get(self.dashboard_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'climatology_stories/dashboard.html')

    def test_dashboard_post(self):
        data = {'year': '2000', 'month': '1', 'lat': '35-40S', 'year2': '2001', 'month2': '1', 'lat2': '35-40S'}
        response = self.client.post(self.dashboard_url, data=data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'climatology_stories/dashboard.html')
        self.assertEquals(response.context['climate'], self.climate1)
        self.assertEquals(response.context['climate2'], self.climate2)
