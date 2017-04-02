from django.db import models


# Create your models here.
class Judge(models.Model):
    pass


class Team(models.Model):
    pass


class Competition(models.Model):
    judges = models.ManyToManyField(Judge)
    teams = models.ManyToManyField(Team)


class Entry(models.Model):
    team = models.ForeignKey(Team)


class LineFollowing(Entry):
    pass


class StraightLineSpeed(Entry):
    pass

class Golf(Entry):
    pass


class Bowling(Entry):
    pass


class ObstacleCourse(Entry):
    pass


class MinimalMaze(Entry):
    sensors_used = models.BooleanField()


class Run(models.Model):
    time = models.TimeField()
    completed = models.BooleanField()
    rescues = models.IntegerField()


class MazeRun(Run):
    entry = models.ForeignKey(MinimalMaze)
    wall_touches = models.IntegerField()
    abandoned = models.BooleanField()


class StraightLineRun(Run):
    entry = models.ForeignKey(StraightLineSpeed)
    wall_runner = models.BooleanField()


class GolfRun(Run):
    entry = models.ForeignKey(Golf)
    ball_in_hole = models.BooleanField()
    ball_in_sand_hazard = models.BooleanField()
    ball_in_water_hazard = models.BooleanField()
    abandoned = models.BooleanField()


class BowlRun(models.Model):
    entry = models.ForeignKey(Bowling)
    pins_bowl_one = models.IntegerField()
    pins_bowl_two = models.IntegerField()
    foul = models.BooleanField()
    time = models.TimeField()


class Obstacle(models.Model):
    entry = models.ForeignKey(ObstacleCourse)
    name = models.CharField(max_length=20)
    attempted = models.BooleanField()
    rescued = models.BooleanField()
    skipped = models.BooleanField()


class LineFollowRun(Run):
    entry = models.ForeignKey(LineFollowing)