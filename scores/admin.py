from django.contrib import admin
from scores.models import Competition, Judge, Run, LineFollowing, StraightLineSpeed, MinimalMaze, MazeRun, StraightLineRun, GolfRun, BowlRun, Obstacle, Bowling, ObstacleCourse, LineFollowRun
# Register your models here.

class RunInline(admin.StackedInline):
    model = Run


class MazeRunInline(admin.StackedInline):
    model = MazeRun


class StraightLineInline(admin.StackedInline):
    model =StraightLineRun


class GolfRunInline(admin.StackedInline):
    model = GolfRun


class BowlRunInline(admin.StackedInline):
    model = BowlRun


class ObstacleInline(admin.StackedInline):
    model = Obstacle


class LineFollowInline(admin.StackedInline):
    model = LineFollowRun


class LineFollowAdmin(admin.ModelAdmin):
    inlines = [LineFollowInline]


class StraightLineAdmin(admin.ModelAdmin):
    inlines = [StraightLineInline]


class MinimalMazeAdmin(admin.ModelAdmin):
    inlines = [MazeRunInline]


class BowlingAdmin(admin.ModelAdmin):
    inlines = [BowlRunInline]



admin.site.register(Competition)
admin.site.register(Judge)
admin.site.register(LineFollowing, LineFollowAdmin)
admin.site.register(StraightLineSpeed, StraightLineAdmin)
admin.site.register(MinimalMaze, MinimalMazeAdmin)
admin.site.register(Bowling, BowlingAdmin)