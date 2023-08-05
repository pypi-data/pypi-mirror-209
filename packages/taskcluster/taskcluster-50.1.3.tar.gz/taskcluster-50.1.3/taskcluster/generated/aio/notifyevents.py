# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from ...aio.asyncclient import AsyncBaseClient
from ...aio.asyncclient import createApiClient
from ...aio.asyncclient import config
from ...aio.asyncclient import createTemporaryCredentials
from ...aio.asyncclient import createSession
_defaultConfig = config


class NotifyEvents(AsyncBaseClient):
    """
    This pretty much only contains the simple free-form
    message that can be published from this service from a request
    by anybody with the proper scopes.
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-notify/v1/",
    }
    serviceName = 'notify'
    apiVersion = 'v1'

    def notify(self, *args, **kwargs):
        """
        Notification Messages

        An arbitrary message that a taskcluster user
        can trigger if they like.

        The standard one that is published by us watching
        for the completion of tasks is just the task status
        data that we pull from the queue `status()` endpoint
        when we notice a task is complete.

        This exchange takes the following keys:

         * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

         * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
        """

        ref = {
            'exchange': 'notification',
            'name': 'notify',
            'routingKey': [
                {
                    'constant': 'primary',
                    'multipleWords': False,
                    'name': 'routingKeyKind',
                },
                {
                    'multipleWords': True,
                    'name': 'reserved',
                },
            ],
            'schema': 'v1/notification-message.json#',
        }
        return self._makeTopicExchange(ref, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'NotifyEvents']
