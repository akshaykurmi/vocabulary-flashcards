from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)


class Deck(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class FlashCard(models.Model):
    word = models.CharField(max_length=50)
    definition = models.CharField(max_length=300)
    sample_sentence = models.CharField(max_length=300)
    mnemonic = models.CharField(max_length=300)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
