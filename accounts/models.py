from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from kabaramadalapeste import models as game_models
from kabaramadalapeste.conf import settings as game_settings

from enum import Enum
import logging
logger = logging.getLogger(__file__)

# Create your models here.


class Gender(Enum):
    Man = 'Man'
    Woman = 'Woman'


class Member(AbstractUser):
    is_participant = models.BooleanField(default=True)

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username


class Participant(models.Model):
    class CantResetStartIsland(Exception):
        pass

    class ParticipantIsNotOnIsland(Exception):
        pass

    class ProprtiesAreNotEnough(Exception):
        pass

    member = models.OneToOneField(Member, related_name='participant', on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    city = models.CharField(max_length=40)
    document = models.ImageField(upload_to='documents/')
    gender = models.CharField(max_length=10, default=Gender.Man, choices=[(tag.value, tag.name) for tag in Gender])
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    is_activated = models.BooleanField(default=False)

    currently_at_island = models.ForeignKey('kabaramadalapeste.Island',
                                            on_delete=models.SET_NULL,
                                            related_name="current_participants",
                                            null=True)

    def __str__(self):
        return str(self.member)

    @property
    def sekke(self):
        """
        Warning changes on this property wont be applied if you want to make changes use get_safe_sekke
        """
        return self.properties.get(property_type=game_settings.GAME_SEKKE)

    def get_safe_sekke(self):
        return self.properties.select_for_update().get(property_type=game_settings.GAME_SEKKE)

    def init_pis(self):
        if game_models.ParticipantIslandStatus.objects.filter(participant=self).count():
            logger.info('Participant currently has some PIS. We cant init again.')
            return
        # TODO: handle random Treasure assignment
        # TODO: handle random question assignment
        for island in game_models.Island.objects.all():
            game_models.ParticipantIslandStatus.objects.create(
                participant=self,
                island=island,
            )

    def init_properties(self):
        if self.properties.count():
            logger.info('Participant currently has some properties. We cant init again.')
            return
        for property_type, amount in game_settings.GAME_PARTICIPANT_INITIAL_PROPERTIES.items():
            if amount > 0:
                self.properties.create(
                    participant=self,
                    property_type=property_type,
                    amount=amount
                )
            else:
                logger.warning('Property could not be negative we continue setting other properties')

    def set_start_island(self, dest_island):
        if self.currently_at_island:
            raise Participant.CantResetStartIsland
        with transaction.atomic():
            dest_pis = game_models.ParticipantIslandStatus.objects.get(
                participant=self,
                island=dest_island
            )
            dest_pis.currently_in = True
            dest_pis.did_reach = True
            dest_pis.reached_at = timezone.now()
            dest_pis.save()

            self.currently_at_island = dest_island
            self.save()

    def move(self, dest_island, is_free=False):
        if not self.currently_at_island:
            raise Participant.ParticipantIsNotOnIsland
        if not self.currently_at_island.is_neighbor_with(dest_island):
            raise game_models.Island.IslandsNotConnected

        if not is_free and self.sekke.amount < game_settings.GAME_MOVE_PRICE:
            raise Participant.ProprtiesAreNotEnough

        with transaction.atomic():
            if not is_free:
                safe_sekke = self.get_safe_sekke()
                safe_sekke.amount -= game_settings.GAME_MOVE_PRICE
                safe_sekke.save()

            src_pis = game_models.ParticipantIslandStatus.objects.get(
                participant=self,
                island=self.currently_at_island
            )
            src_pis.currently_in = False
            src_pis.currently_anchored = False
            src_pis.save()

            dest_pis = game_models.ParticipantIslandStatus.objects.get(
                participant=self,
                island=dest_island
            )

            dest_pis.currently_in = True
            dest_pis.did_reach = True
            dest_pis.reached_at = timezone.now()
            dest_pis.save()

            self.currently_at_island = dest_island
            self.save()

    def put_anchor_on_current_island(self):
        if not self.currently_at_island:
            raise Participant.ParticipantIsNotOnIsland
        if self.sekke.amount < game_settings.GAME_PUT_ANCHOR_PRICE:
            raise Participant.ProprtiesAreNotEnough

        current_pis = game_models.ParticipantIslandStatus.objects.get(
            participant=self,
            island=self.currently_at_island
        )
        with transaction.atomic():
            current_pis.currently_anchored = True
            current_pis.last_anchored_at = timezone.now()
            current_pis.save()

            safe_sekke = self.get_safe_sekke()
            safe_sekke.amount -= game_settings.GAME_PUT_ANCHOR_PRICE
            safe_sekke.save()


class Judge(models.Model):
    member = models.OneToOneField(Member, related_name='judge', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.member)


class PaymentAttempt(models.Model):
    participant = models.ForeignKey(Participant, related_name='payment_attempts', on_delete=models.CASCADE)
    red_id = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    authority = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    request_datetime = models.DateTimeField(auto_now_add=True)
    verify_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'PaymentAttempt object (' + str(self.pk) + ') (' + str(self.participant) + ')'
