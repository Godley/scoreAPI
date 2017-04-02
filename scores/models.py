from django.db import models


# Create your models here.
class Judge(models.Model):
    pass


class Team(models.Model):
    pass


class Competition(models.Model):
    judges = models.ManyToManyField(Judge)
    teams = models.ManyToManyField(Team)


class LineFollowing(Competition):
    pass

class StraightLineSpeed(Competition):
    pass


class MinimalMaze(Competition):
    sensors_used = models.BooleanField()


class Run(models.Model):
    time = models.TimeField()
    completed = models.BooleanField()
    rescues = models.IntegerField()


class MazeRun(Run):
    wall_touches = models.IntegerField()
    abandoned = models.BooleanField()


class StraightLineRun(Run):
    wall_runner = models.BooleanField()


class GolfRun(Run):
    ball_in_hole = models.BooleanField()
    ball_in_sand_hazard = models.BooleanField()
    ball_in_water_hazard = models.BooleanField()
    abandoned = models.BooleanField()

class Obstacle(models.Model):
    name = models.CharField()
    attempted = models.BooleanField()
    rescued = models.BooleanField()
    skipped = models.BooleanField()