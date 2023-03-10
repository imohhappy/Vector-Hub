# Generated by Django 3.2.16 on 2022-12-20 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentIntent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_intent_id', models.CharField(max_length=225)),
                ('checkout_id', models.CharField(max_length=225)),
                ('created', models.DateTimeField(auto_now=True)),
                ('courses', models.ManyToManyField(to='courses.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('created', models.DateTimeField(auto_now=True)),
                ('payment_intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.paymentintent')),
            ],
        ),
    ]
