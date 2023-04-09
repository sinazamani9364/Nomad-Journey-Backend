from django.db import models
from accounts.models import User, City
from django.utils.translation import gettext as _


class Announcement(models.Model):
    ONE_TR = 1
    TWO_TR = 2
    THREE_TR = 3
    FOUR_TR = 4
    FIVE_TR = 5
    SIX_TR = 6
    SEVENT_TR = 7
    EIGHT_TR = 8
    NINE_TR = 9
    TEN_TR = 10
    ELEVEN_TR = 11
    TWELVE_TR = 12
    THIRTEEN_TR = 13
    FOURTEEN_TR = 14
    FIFTEEN_TR = 15
    TRAVELERS_COUNT_CHOICES = (
        (ONE_TR, _('1')),
        (TWO_TR, _('2')),
        (THREE_TR, _('3')),
        (FOUR_TR, _('4')),
        (FIVE_TR, _('5')),
        (SIX_TR, _('6')),
        (SEVENT_TR, _('7')),
        (EIGHT_TR, _('8')),
        (NINE_TR, _('9')),
        (TEN_TR, _('10')),
        (ELEVEN_TR, _('11')),
        (TWELVE_TR, _('12')),
        (THIRTEEN_TR, _('13')),
        (FOURTEEN_TR, _('14')),
        (FIFTEEN_TR, _('15'))
    )
    STATUS_CHOICES = (
        ('P', _('Pending')),
        ('A', _('Accepted')),
        ('D', _('Done')),
        ('E', _('Expired'))
    )


    announcer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        related_name='announcer_anc'
    )
    # anc_city = models.ForeignKey(
    #     City,
    #     on_delete=models.DO_NOTHING,
    #     default=None
    # )
    anc_city = models.CharField(max_length=100, null=True, blank=True)
    anc_country = models.CharField(max_length=100, null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    anc_status = models.CharField(choices=STATUS_CHOICES, default='P', max_length=1)
    arrival_date_is_flexible = models.BooleanField(default= False, null=True, blank=True)
    departure_date_is_flexible = models.BooleanField(default= False, null=True, blank=True)
    anc_description = models.TextField(max_length=500, null=True, blank=True)
    anc_timestamp_created = models.DateTimeField(auto_now_add=True)
    travelers_count = models.IntegerField(choices=TRAVELERS_COUNT_CHOICES, null=True, blank=True)
    volunteer_hosts = models.ManyToManyField(
        User, 
        related_name='hosts_anc',
        null=True,blank=True
    )
    main_host = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        default=None,
        related_name='main_host_anc',
        null= True
    )

    def __str__(self):
        return 'This is an announcement with ID ' + str(self.id) + '.'