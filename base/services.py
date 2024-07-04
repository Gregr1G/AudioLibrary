from django.core.exceptions import ValidationError
import os

def get_audio_upload_file(instance, file):
    return f"books_audio/book_{instance.author.id}/{file}"

def get_book_avatar_upload_file(instance, file):
    return f"books_covers/cover_{instance.author.id}/{file}"

def audio_size_validator(file):
    mb_limit = 1024 * 1024 * 1024

    if file.size > mb_limit:
        raise ValidationError(f"Слишком большой файл.(Максимальный {mb_limit})")

def delete_old_file(path_to_file):
    if os.path.exists(path_to_file):
        os.remove(path_to_file)