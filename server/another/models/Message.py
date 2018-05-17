from django.conf import settings
from django.db import models
from sqlalchemy import Column, Integer, String, Text

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'models.User.User')


class MessageManager(models.Manager):

    def inbox_for(self, user):
        """
        Returns all messages that were received by the given user and are not
        marked as deleted.
        """
        return self.filter(
            recipient=user,
            recipient_deleted_at__isnull=True,
        )

    def outbox_for(self, user):
        """
        Returns all messages that were sent by the given user and are not
        marked as deleted.
        """
        return self.filter(
            sender=user,
            sender_deleted_at__isnull=True,
        )

    def trash_for(self, user):
        """
        Returns all messages that were either received or sent by the given
        user and are marked as deleted.
        """
        return self.filter(
            recipient=user,
            recipient_deleted_at__isnull=False,
        ) | self.filter(
            sender=user,
            sender_deleted_at__isnull=False,
        )


class Message():
    NOTIFY = 0
    APPLICATION = 1
    MSG_TYPE = (
        (NOTIFY, 'NOTIFY'),
        (APPLICATION, 'APPLICATION'),
    )

    UNTREATED = 0
    ACCEPT = 1
    REFUSED = 2
    EXPIRED = 3
    MSG_STAT = (
        (UNTREATED, 'UNTREATED'),
        (ACCEPT, 'EXPIRED'),
        (REFUSED, 'REFUSED'),
        (EXPIRED, 'EXPIRED'),
    )
    id = Column(Integer, autoincrement=True, primary_key=True)
    subject = Column(String(140))
    content = Column(Text)
    user_id = Column(String(20), ForeignKey('user.id'))
    sender = models.ForeignKey(AUTH_USER_MODEL, related_name='sent_messages', verbose_name='发送者')
    recipient = models.ForeignKey(AUTH_USER_MODEL, related_name='received_messages', null=True, blank=True, verbose_name='接受者')

    type = models.PositiveSmallIntegerField(choices=MSG_TYPE)
    stat = models.PositiveSmallIntegerField(choices=MSG_STAT, default=UNTREATED)

    sent_at = models.DateTimeField('发送时间', auto_now_add=True, null=True, blank=True)
    read_at = models.DateTimeField('阅读时间', null=True, blank=True)

    sender_deleted_at = models.DateTimeField('发送者删除时间', null=True, blank=True)
    recipient_deleted_at = models.DateTimeField('接受者删除时间', null=True, blank=True)

    objects = MessageManager()

    def new(self):
        """returns whether the recipient has read the message or not"""
        if self.read_at is not None:
            return False
        return True

    def replied(self):
        """returns whether the recipient has written a reply to this message"""
        if self.replied_at is not None:
            return True
        return False

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return ('messages_detail', [self.id])

    get_absolute_url = models.permalink(get_absolute_url)

    # def save(self, **kwargs):
    #     if not self.id:
    #         self.sent_at = timezone.now()
    #     super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['-sent_at']
        verbose_name = '消息'
        verbose_name_plural = '消息'


def inbox_count_for(user):
    """
    returns the number of unread messages for the given user but does not
    mark them seen
    """
    return Message.objects.filter(recipient=user, read_at__isnull=True, recipient_deleted_at__isnull=True).count()