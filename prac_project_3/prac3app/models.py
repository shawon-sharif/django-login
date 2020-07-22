from django.db import models

# Create your models here.


class Player(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+" "+ self.last_name+ " "+ self.position

class PlayerDetails(models.Model):
    athlate=models.ForeignKey(Player,on_delete=models.CASCADE)
    club=models.CharField(max_length=50)
    release_money=models.IntegerField()
    join_date=models.DateField()

    rating=(
    (1," 95+ "),
    (2," 90+"),
    (3," 85+"),
    (4," 80+")
    )
    fifa_rating=models.IntegerField(choices=rating)


    def __str__(self):
        return self.athlate+ self.club + str(self.release_money)+str(self.join_date) + str(self.fifa_rating)
