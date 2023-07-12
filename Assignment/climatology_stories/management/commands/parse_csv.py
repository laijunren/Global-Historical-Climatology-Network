import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from climatology_stories.models import Climate, Year

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Climate.objects.all().delete()
        Year.objects.all().delete()
        print("tables dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/climatology_stories/data/Year_and_ID.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                year = Year.objects.create(
                ID = int(row[0]),
                year = int(row[1]),
                )
                year.save()

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/climatology_stories/data/ghcn-m-v1.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                year_temp = row[0]
                print(year_temp)
                year_obj = Year.objects.filter(year = year_temp).first()
                print(year_obj.ID)

                climate = Climate.objects.create(
                year_ID = year_obj,
                year = int(row[0]),
                month = int(row[1]),
                lat = row[2],
                lon_175_180W = int(row[3]),
                lon_170_175W = int(row[4]),
                lon_165_170W = int(row[5]),
                lon_160_165W = int(row[6]),
                lon_155_160W = int(row[7]),
                lon_150_155W = int(row[8]),
                lon_145_150W = int(row[9]),
                lon_140_145W = int(row[10]),
                lon_135_140W = int(row[11]),
                lon_130_135W = int(row[12]),
                )
<<<<<<< HEAD
                climate.save()
=======
                climate.save()
>>>>>>> 3f7018cbe34ff8381eaf6496cb53f0305b2b6bfe
