# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("wellsfargo", "0012_auto_20180102_1147"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreQualificationRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "locale",
                    models.CharField(
                        choices=[("en_US", "English (US)")],
                        default="en_US",
                        max_length=5,
                        verbose_name="Locale",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "entry_point",
                    models.CharField(
                        choices=[("web", "Web"), ("pos", "Point of Sale")],
                        default="web",
                        max_length=3,
                        verbose_name="Entry Point",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=15, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=20, verbose_name="Last Name"),
                ),
                (
                    "line1",
                    models.CharField(max_length=26, verbose_name="Address Line 1"),
                ),
                ("city", models.CharField(max_length=15, verbose_name="City")),
                (
                    "state",
                    localflavor.us.models.USStateField(
                        max_length=2, verbose_name="State"
                    ),
                ),
                (
                    "postcode",
                    localflavor.us.models.USZipCodeField(
                        max_length=10, verbose_name="Postcode"
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, verbose_name="Phone"
                    ),
                ),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("modified_datetime", models.DateTimeField(auto_now=True)),
                (
                    "credentials",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="prequal_requests",
                        to="wellsfargo.APICredentials",
                        verbose_name="API Credentials",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_datetime", "-id"),
            },
        ),
        migrations.CreateModel(
            name="PreQualificationResponse",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Pre-screen Approved"),
                            ("D", "Pre-screen Not Approved"),
                            ("E", "System Error"),
                            ("M", "Down for Maintenance"),
                        ],
                        max_length=1,
                        verbose_name="Transaction Status",
                    ),
                ),
                ("message", models.TextField(verbose_name="Message")),
                (
                    "offer_indicator",
                    models.CharField(max_length=20, verbose_name="Offer Indicator"),
                ),
                (
                    "credit_limit",
                    models.DecimalField(
                        decimal_places=2, max_digits=12, verbose_name="Credit Limit"
                    ),
                ),
                (
                    "response_id",
                    models.CharField(max_length=8, verbose_name="Unique Response ID"),
                ),
                (
                    "application_url",
                    models.CharField(max_length=200, verbose_name="Application URL"),
                ),
                (
                    "customer_response",
                    models.CharField(
                        choices=[
                            ("", "None"),
                            ("CLOSE", "Offer Closed"),
                            ("YES", "Offer Accepted"),
                            ("NO", "Offer Rejected"),
                        ],
                        default="",
                        max_length=5,
                        verbose_name="Customer Response",
                    ),
                ),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("modified_datetime", models.DateTimeField(auto_now=True)),
                (
                    "request",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="response",
                        to="wellsfargo.PreQualificationRequest",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_datetime", "-id"),
            },
        ),
    ]
