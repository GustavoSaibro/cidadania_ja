from django.db import models

class Party(models.Model):
    party_id = models.IntegerField(primary_key=True, db_index=True, null=False, default=-1)
    party_name = models.CharField(max_length=200)
    party_initials = models.CharField(max_length=20)
    
    def __str__(self):
        return self.party_name
class Candidate(models.Model):
    candidate_id = models.IntegerField(primary_key=True, db_index=True, null=False, default=-1)
    candidate_name = models.CharField(max_length=200)
    candidate_party = models.ForeignKey(Party, null=True, on_delete=models.SET_NULL )
    # candidate_document = models.CharField(max_length=11)
    candidate_email = models.EmailField(max_length=200)
    candidate_spent_daily = models.FloatField()
    candidate_spent_monthly = models.FloatField()
    candidate_spent_total = models.FloatField()

    def __str__(self):
        return self.candidate_name