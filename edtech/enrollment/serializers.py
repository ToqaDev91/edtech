from rest_framework import serializers

class JSONFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        if not value.name.endswith('.json'):
            raise serializers.ValidationError("Only .json files are allowed.")

        if value.content_type not in ['application/json', 'text/plain']:
            raise serializers.ValidationError("Invalid file type.")
        try:
            import json
            content = value.read()
            json.loads(content)
            value.seek(0)
        except json.JSONDecodeError:
            raise serializers.ValidationError("File content is not valid JSON.")
        
        return value