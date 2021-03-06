# -*- coding: utf-8 -*-
# vim:tabstop=4:expandtab:sw=4:softtabstop=4

import logging

from django.core.management.base import BaseCommand
from subscription.models import UserSubscription

logger = logging.getLogger('subscription')

class Command(BaseCommand):
    help='Expires the subscriptions by inactivating them. Should run at least once a day from cron!'

    def handle(self,*args,**kwargs):
        UserSubscription.active_objects.unsubscribe_expired()
