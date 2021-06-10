from marshmallow import Schema, fields


class ConvertSerializer(Schema):
    obsFileList = fields.List(
        fields.Str(),
        required=True,
    )
    obsBucketName = fields.String(required=True)
