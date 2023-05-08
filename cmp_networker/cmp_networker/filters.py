from django_filters import (
    FilterSet,
    CharFilter)
from .models import Backup, BackupPolicy, BackupWorkflow, Job, \
    OpenstackMsg, PolicyGroup, Server, VmHost, VmMachine, Volume


class BackupFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    tenant_id = CharFilter(field_name='tenant_id', lookup_expr='icontains')
    tenant_name = CharFilter(field_name='tenant_name', lookup_expr='icontains')
    strategy_server = CharFilter(field_name='strategy_server', lookup_expr='icontains')
    region = CharFilter(field_name='region', lookup_expr='icontains')
    server_id = CharFilter(field_name='region', lookup_expr='icontains')
    server_name = CharFilter(field_name='region', lookup_expr='icontains')

    class Meta:
        mode = Backup
        filter = ('name', 'id', 'tenant_id', 'tenant_name', 'region', 'strategy_server', 'server_id', 'server_name')


class BackupPolicyFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    tenant_id = CharFilter(field_name='tenant_id', lookup_expr='icontains')
    tenant_name = CharFilter(field_name='tenant_name', lookup_expr='icontains')
    region = CharFilter(field_name='region', lookup_expr='icontains')

    class Meta:
        mode = BackupPolicy
        filter = ('name', 'id', 'tenant_id', 'tenant_name', 'region')


class BackupWorkflowFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    policy_id = CharFilter(field_name='policy_id', lookup_expr='icontains')
    status = CharFilter(field_name="status", lookup_expr='icontains')

    class Meta:
        mode = BackupWorkflow
        filter = ('name', 'id', 'policy_id', 'status')


class JobFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    backup_id = CharFilter(field_name='backup_id', lookup_expr='icontains')
    server_id = CharFilter(field_name='protocol', lookup_expr='icontains')

    class Meta:
        mode = Job
        filter = ('backup_id', 'id', 'server_id')


class OpenstackMsgFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    object_id = CharFilter(field_name='object_id', lookup_expr='icontains')
    region = CharFilter(field_name='region', lookup_expr='icontains')

    class Meta:
        mode = OpenstackMsg
        filter = ('object_id', 'id', 'region')


class PolicyGroupFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    bp_id = CharFilter(field_name='bp_id', lookup_expr='icontains')
    tenant_id = CharFilter(field_name="tenant_id", lookup_expr='icontains')

    class Meta:
        mode = PolicyGroup
        filter = ('name', 'id', 'bp_id', 'tenant_id')


class ServerFilter(FilterSet):
    server_id = CharFilter(field_name='server_id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    tenant_id = CharFilter(field_name='tenant_id', lookup_expr='icontains')

    class Meta:
        mode = Server
        filter = ('name', 'server_id', 'tenant_id')


class VmHostFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    region = CharFilter(field_name='region', lookup_expr='icontains')
    cluster_id = CharFilter(field_name="cluster_id", lookup_expr='icontains')

    class Meta:
        mode = VmHost
        filter = ('name', 'id', 'region', 'cluster_id')


class VmMachineFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    region = CharFilter(field_name='region', lookup_expr='icontains')
    host_id = CharFilter(field_name="host_id", lookup_expr='icontains')

    class Meta:
        mode = VmMachine
        filter = ('name', 'id', 'region', 'host_id')


class VolumeFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    server_id = CharFilter(field_name='server_id', lookup_expr='icontains')

    class Meta:
        mode = Volume
        filter = ('name', 'id', 'server_id')
