from rest_framework import serializers

from task_tracker.models import Task


# class TaskSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=64)
#     description = serializers.CharField(max_length=226)
#     status = serializers.CharField(max_length=2,allow_null=True)
#     priority = serializers.CharField(max_length=2,allow_null=True)
#
#     def create(self, validated_data):
#         return Task(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.status = validated_data.get('status', instance.status)
#         instance.priority = validated_data.get('priority', instance.priority)
#         return instance
#
#     def save(self, validated_data):
#         task = self.create(validated_data)
#         task.save()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority"]
