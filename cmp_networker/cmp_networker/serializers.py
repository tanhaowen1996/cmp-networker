from rest_framework import serializers
from .models import Backup, BackupPolicy, BackupWorkflow, Job, \
    OpenstackMsg, PolicyGroup, Server, VmHost, VmMachine, Volume


class BackupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Backup
        fields = '__all__'


class BackupPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = BackupPolicy
        fields = '__all__'


class BackupWorkflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = BackupWorkflow
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class OpenstackMsgSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpenstackMsg
        fields = '__all__'


class PolicyGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolicyGroup
        fields = '__all__'


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'


class VmHostSerializer(serializers.ModelSerializer):

    class Meta:
        model = VmHost
        fields = '__all__'


class VmMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = VmMachine
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volume
        fields = '__all__'
