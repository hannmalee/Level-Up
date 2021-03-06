from django.db import models

class Game(models.Model):
    name = models.CharField( max_length=100)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    skill_level = models.IntegerField()
    maker = models.CharField(max_length=50)

    def __str__(self):
        return self.name