from django.db import models


class Candidate(models.Model):
    # candidate_id = models.IntegerField(primary_key=True, db_index=True)
    candidate_name = models.CharField(max_length=200)
    candidate_party = models.CharField(max_length=20)
    # candidate_document = models.CharField(max_length=11)
    candidate_email = models.EmailField(max_length=200)
    candidate_spent_daily = models.FloatField()
    candidate_spent_monthly = models.FloatField()
    candidate_spent_total = models.FloatField()

    def __str__(self):
        return self.candidate_name