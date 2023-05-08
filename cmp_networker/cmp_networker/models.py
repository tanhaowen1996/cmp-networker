from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Backup(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name=_('backup id')
    )
    name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    tenant_id = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    tenant_name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    region = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    server_id = models.CharField(
        max_length=128,
    )
    server_name = models.CharField(
        max_length=128,
    )
    strategy_server = models.CharField(
        max_length=128,
    )
    size = models.IntegerField(
        null=True,
        blank=True,
    )
    unit = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    vm_info = models.CharField(
        max_length=2048,
        null=True,
        blank=True,
    )
    type = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time')
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time')
    )

    class Meta:
        indexes = (BrinIndex(fields=['updated_time', 'created_time']),)


class BackupPolicy(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('backup policy id')
    )
    name = models.CharField(
        max_length=128,
    )
    region = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    tenant_id = models.CharField(
        max_length=28,
        null=True,
        blank=True,
    )
    tenant_name = models.CharField(
        max_length=28,
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=4096,
        null=True,
        blank=True,
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time')
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time')
    )

    class Meta:
        indexes = (BrinIndex(fields=['updated_time', 'created_time']),)


class BackupWorkflow(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('backup workflow id')
    )
    name = models.CharField(
        max_length=128,
    )
    policy_id = models.UUIDField(
        null=True,
        blank=True,
    )
    schedule_activities = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    schedule_period = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    start_time = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    start_interval = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=4096,
        null=True,
        blank=True,
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time')
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time')
    )

    class Meta:
        indexes = (BrinIndex(fields=['updated_time', 'created_time']),)


class Job(models.Model):
    id = models.UUIDField(
        primary_key=True,
        verbose_name=_('job id')
    )
    type = models.CharField(
        max_length=128,
    )
    state = models.CharField(
        max_length=128,
    )
    stopped = models.CharField(
        max_length=128,
    )
    completion_status = models.CharField(
        max_length=64,
    )
    start_time = models.DateTimeField(
        verbose_name=_('start time')
    )
    end_time = models.DateTimeField(
        verbose_name=_('end time')
    )
    bp_id = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    backup_id = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    server_id = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=256,
    )
    manual_or_time = models.CharField(
        max_length=256,
    )
    hypervisor_id = models.CharField(
        max_length=128,
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time')
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time')
    )

    class Meta:
        indexes = (BrinIndex(fields=['updated_time', 'created_time']),)


class OpenstackMsg(models.Model):
    id = models.CharField(
        max_length=128,
        primary_key=True,
    )
    event_type = models.CharField(
        max_length=128,
    )
    display_name = models.CharField(
        max_length=256,
    )
    object_id = models.CharField(
        max_length=128,
    )
    region = models.CharField(
        max_length=128,
    )
    updated_time = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time')
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time')
    )

    class Meta:
        indexes = (BrinIndex(fields=['updated_time', 'created_time']),)


class PolicyGroup(models.Model):
    id = models.CharField(
        max_length=128,
        primary_key=True,
    )
    name = models.CharField(
        max_length=128,
    )
    bp_id = models.CharField(
        max_length=128,
    )
    tenant_id = models.CharField(
        max_length=128,
    )
    servers = models.CharField(
        max_length=4096,
    )


class Server(models.Model):
    server_id = models.CharField(
        max_length=128,
        primary_key=True,
    )
    hypervisor_id = models.CharField(
        max_length=128,
    )
    name = models.CharField(
        max_length=128,
    )
    disks = models.CharField(
        max_length=2048,
    )
    son_list = models.CharField(
        max_length=2048,
    )
    remove = models.IntegerField(
        default=0
    )
    image_id = models.CharField(
        max_length=128,
    )
    flavor_id = models.CharField(
        max_length=128,
    )
    version = models.CharField(
        max_length=16,
    )
    tenant_id = models.CharField(
        max_length=128,
    )


class VmHost(models.Model):
    id = models.CharField(
        max_length=128,
        primary_key=True,
    )
    name = models.CharField(
        max_length=256,
    )
    region = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    cluster_id = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    power_state = models.CharField(
        max_length=64,
    )
    maintenance = models.IntegerField(
        null=True,
    )
    boot_time = models.DateTimeField(
        null=True
    )


class VmMachine(models.Model):
    id = models.CharField(
        max_length=128,
        primary_key=True,
    )
    name = models.CharField(
        max_length=256,
    )
    region = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    host_id = models.CharField(
        max_length=128,
    )
    power_state = models.CharField(
        max_length=64,
    )


class Volume(models.Model):
    id = models.CharField(
        max_length=128,
        primary_key=True,
    )
    server_id = models.CharField(
        max_length=128,
    )
    device = models.CharField(
        max_length=256,
    )
    name = models.CharField(
        max_length=256,
    )
    key = models.IntegerField(
        null=True
    )
    volume_name_vc = models.CharField(
        max_length=256,
    )
    size = models.IntegerField(
        null=True,
    )
    volume_type = models.CharField(
        max_length=64,
    )
