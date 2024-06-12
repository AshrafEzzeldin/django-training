from users.models import User
from rest_framework import serializers, validators


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    extra_kwargs = {
        'email': {"required": True,
                  "allow_blank": False,
                  }
    }

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("the passwords don't match.")
        if len(data['password1']) < 9:
            raise serializers.ValidationError("the passwords should be more than 8 chars.")
        return super().validate(data)

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
        )
        user.set_password(validated_data.get("password1"))
        user.save()
        return user
