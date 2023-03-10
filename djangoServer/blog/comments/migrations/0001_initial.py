# Generated by Django 4.1.3 on 2022-11-30 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_users', '0001_initial'),
        ('exrc_posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_id', models.TextField(null=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exrc_posts.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_users.bloguser')),
            ],
            options={
                'db_table': 'blog_comments',
            },
        ),
    ]
