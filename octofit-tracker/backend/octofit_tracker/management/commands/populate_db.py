from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Clear existing data
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            # Teams
            marvel = Team.objects.create(name='marvel', description='Marvel Team')
            dc = Team.objects.create(name='dc', description='DC Team')

            # Users
            ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
            captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='marvel')
            batman = User.objects.create(name='Batman', email='batman@dc.com', team='dc')
            superman = User.objects.create(name='Superman', email='superman@dc.com', team='dc')

            # Activities
            Activity.objects.create(user=ironman, type='run', duration=30, date='2023-01-01')
            Activity.objects.create(user=batman, type='cycle', duration=45, date='2023-01-02')
            Activity.objects.create(user=superman, type='swim', duration=60, date='2023-01-03')
            Activity.objects.create(user=captain, type='walk', duration=20, date='2023-01-04')

            # Leaderboard
            Leaderboard.objects.create(team=marvel, points=150)
            Leaderboard.objects.create(team=dc, points=120)

            # Workouts
            Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
            Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
