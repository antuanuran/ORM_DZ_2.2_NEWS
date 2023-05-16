import json
from django.core.management import BaseCommand
from articles.models import Article, Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('articles.json', 'r', encoding='utf-8') as file:
            all_articles = json.load(file)

        for article in all_articles:
            if article['model'] == 'articles.article':
                Article.objects.create(title=article['fields']['title'], text=article['fields']['text'], image=article['fields']['image'], published_at=article['fields']['published_at'])

            else:
                Tag.objects.create(name=article['fields']['name1'])
                Tag.objects.create(name=article['fields']['name2'])
                Tag.objects.create(name=article['fields']['name3'])
                Tag.objects.create(name=article['fields']['name4'])




