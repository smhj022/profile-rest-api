from rest_framework import serializers

# serializer is a feature from django from a rest framework that allows you to/
# easily convert data inputs into python objects and vice versa.


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing over view """

    name = serializers.CharField(max_length=10)
