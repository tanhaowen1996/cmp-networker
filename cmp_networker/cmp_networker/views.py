from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .authentication import OSAuthentication
from .serializers import BackupPolicy
from .models import Backup
from .filters import BackupFilter
from .settings import OS_REGION_MAWEI, NETWORKER_MW_URL, VCENTER_MW, NETWORKER_CK_URL, VCENTER_CK

from requests import exceptions
import logging
import openstack

logger = logging.getLogger(__package__)


class OSCommonModelMixin:
    update_serializer_class = None

    def get_serializer_class(self):
        return {
            'PUT': self.update_serializer_class
        }.get(self.request.method, self.serializer_class)


class BackupViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
    list： 备份列表

    """
    authentication_classes = (OSAuthentication,)
    filterset_class = BackupFilter
    serializer_class = BackupPolicy
    queryset = Backup.objects.all()
    filter_backends = [DjangoFilterBackend]

    def list(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass


class BackupPolicyViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
    list:
      查看策略列表

    create:
      创建策略

    retrieve:
      获取策略详情列表

    update:
      更新策略名称、描述、备份模式、备份计划、开始时间，间隔时间

    destroy:
      删除策略

    update_server:
      更新策略关联主机

    start_backup:
      立即触发备份策略
    # """

    # authentication_classes = (OSAuthentication,)
    # filterset_class = VolumeFilter
    # update_serializer_class = UpdateVolumeSerializer
    # serializer_class = VolumeSerializer
    # queryset = Volume.objects.all()
    def create(self, request, *args, **kwargs):
        try:
            pass
        except Exception as e:
            pass


class BackupWorkflowViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    pass
