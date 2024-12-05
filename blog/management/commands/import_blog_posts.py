import csv
from django.core.management.base import BaseCommand, CommandError
from blog.models import BlogPost
from django.utils.termcolors import colorize

class Command(BaseCommand):
    help = 'Import blog posts from a CSV file'

    def add_arguments(self, parser):
        
        parser.add_argument(
            'csv_file',
            type=str,
            help='The path to the CSV file containing blog posts data'
        )

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        try:
            with open(csv_file_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                   
                    blog_post = BlogPost(
                        title=row['title'],
                        content=row['content'],
                        country=row['country']
                    )
                    blog_post.save()

                    
                    self.stdout.write(colorize(f"Successfully imported: {row['title']}", fg='green'))
        except FileNotFoundError:
            raise CommandError(f"The file {csv_file_path} does not exist.")
        except KeyError as e:
            raise CommandError(f"Missing column in CSV: {e}")
        except Exception as e:
            raise CommandError(f"An error occurred: {e}")