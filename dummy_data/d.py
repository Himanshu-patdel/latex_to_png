import base64

# Given byte data
image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00d\x00\x00\x00d\x08\x02\x00\x00\x00\xff\x80\x02\x03\x00\x00\x00\xe6IDATx\x9c\xed\xd0A\t\x00 \x00\xc0@\xb5\x7fg\xad\xe0^"\xdc%\x18\x9b{pk\xbd\x0e\xf8\x89Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\x81Y\xc1\x01\x8a^\x01\xc7\xf1\x84\x1az\x00\x00\x00\x00IEND\xaeB`\x82'

# Encode bytes to Base64
base64_encoded_image = base64.b64encode(image_bytes).decode('utf-8')

print(base64_encoded_image)
{
    "image_data": "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAA5klEQVR4nO3QQQkAIADAQLV/Z63gXiLcJRibe3BrvQ74iVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZgVmBWYFZwQGKXgHH8YQaegAAAABJRU5ErkJggg=="
}
