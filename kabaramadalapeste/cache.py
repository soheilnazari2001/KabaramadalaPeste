from kabaramadalapeste.models import Participant
from django.utils import timezone


class ParticipantsDataCache:
    data = {}
    last_calculated = None
    seconds_between = 60

    @classmethod
    def calc_data(cls):
        data = {}
        for par in Participant.objects.filter(is_activated=True, document_status='Verified'):
            data[par.pk] = {
                'username': par.member.username,
                # 'picture': par.profile_url,  # TODO: uncomment here
                'island_id': par.currently_at_island.island_id if par.currently_at_island else None
            }
        return data

    @classmethod
    def get_data(cls):
        if cls.last_calculated is None or (timezone.now() - cls.last_calculated).seconds > cls.seconds_between:
            cls.data = cls.calc_data()
            cls.last_calculated = timezone.now()
        return cls.data
