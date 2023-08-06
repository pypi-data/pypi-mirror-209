# -*- coding: utf-8 -*-

# ****************************************************************
# IDE: PyCharm
# Developed by: JhonyAlexanderGonzal
# Date: 18/05/2023 5:23 p. m.
# Project: cfhl-backend
# Module Name: stats
# ****************************************************************

import base64
from datetime import date
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError as CoreValidationError
from django.utils.translation import gettext_lazy as _
from oasis.models import Stat
from oasis.stats.api.serializers import StatSerializer
from rest_framework import status
from rest_framework.response import Response
from zibanu.django.repository.lib.utils import DocumentGenerator
from zibanu.django.rest_framework.exceptions import APIException
from zibanu.django.rest_framework.exceptions import ValidationError
from zibanu.django.rest_framework.viewsets import ViewSet
from zibanu.django.utils import CodeGenerator
from zibanu.django.utils import Email
from zibanu.django.utils import ErrorMessages


class StatsServices(ViewSet):
    permission_classes = []
    authentication_classes = []

    def list(self, request) -> Response:
        """
        REST Service to get a list of stats
        :param request: request object from HTTP Post.
        :return: response object with status and data
        """

        try:
            qs = Stat.objects.filter(enabled=True)
            serializer = StatSerializer(instance=qs, many=True)
            data_return = serializer.data
            status_return = status.HTTP_200_OK if len(data_return) > 0 else status.HTTP_204_NO_CONTENT
        except Exception as exc:
            raise APIException(ErrorMessages.NOT_CONTROLLED, str(exc),
                               http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status_return, data=data_return)
