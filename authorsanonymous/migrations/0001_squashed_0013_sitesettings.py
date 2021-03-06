# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-25 08:33
from __future__ import unicode_literals

import authorsanonymous.models
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    replaces = [('authorsanonymous', '0001_initial'), ('authorsanonymous', '0002_auto_20180105_0507'), ('authorsanonymous', '0003_fancypage_header_icon'), ('authorsanonymous', '0004_auto_20180105_1242'), ('authorsanonymous', '0005_auto_20180105_1244'), ('authorsanonymous', '0006_auto_20180105_2256'), ('authorsanonymous', '0007_sitecopy'), ('authorsanonymous', '0008_auto_20180105_2305'), ('authorsanonymous', '0009_auto_20180105_2308'), ('authorsanonymous', '0010_metadata'), ('authorsanonymous', '0011_add_body_background'), ('authorsanonymous', '0012_more_contact_details'), ('authorsanonymous', '0013_sitesettings')]

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', authorsanonymous.models.StreamField([])),
                ('header_body', wagtail.core.fields.RichTextField(default='', verbose_name='Text')),
                ('header_text', models.CharField(default='', max_length=255, verbose_name='Title')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('body_background', models.ForeignKey(blank=True, help_text="Background image for this page. If not set, the background image in the <a href='/admin/settings/authorsanonymous/sitecopy/'>site copy</a> will be used instead.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FancyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', authorsanonymous.models.StreamField([])),
                ('header_body', wagtail.core.fields.RichTextField(verbose_name='Text')),
                ('header_text', models.CharField(max_length=255, verbose_name='Title')),
                ('header_icon', authorsanonymous.models.ChoiceField(help_text="See <a href='http://fontawesome.io/icons/'>Font Awesome</a> for the list of available icons.", max_length=40, verbose_name='Icon')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('body_background', models.ForeignKey(blank=True, help_text="Background image for this page. If not set, the background image in the <a href='/admin/settings/authorsanonymous/sitecopy/'>site copy</a> will be used instead.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('email_public', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=20)),
                ('instagram_handle', models.CharField(blank=True, max_length=20)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
                ('goodreads_url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteCopy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(default='Authors Anonymous', help_text='The title shown at the very top of content pages.', max_length=255)),
                ('copyright', models.CharField(default='Your Name Here', help_text='Copyright statement in the footer', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
                ('contact_body', wagtail.core.fields.RichTextField(default='')),
                ('contact_title', models.CharField(default='Get in touch', max_length=50)),
                ('body_background', models.ForeignKey(blank=True, help_text='Default background image for all pages', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtraAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', authorsanonymous.models.ChoiceField(help_text="See <a href='http://fontawesome.io/icons/'>Font Awesome</a> for the list of available icons.", max_length=40, verbose_name='Icon')),
                ('text', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('setting', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_accounts', to='authorsanonymous.ContactDetails')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_analytics_id', models.CharField(max_length=20)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
