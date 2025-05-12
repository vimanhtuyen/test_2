from django.contrib.auth import get_user_model

User = get_user_model()
username = 'vimanhtuyen'
email = 'vimanhtuyen@gmail.com'
password = 'Q1w2e3@#'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superuser created!")
else:
    print("⚠️ Superuser already exists.")
