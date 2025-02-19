# Generated by Django 3.2.4 on 2021-07-01 14:30

from django.db import migrations, models
import django.db.models.deletion
import external_services.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0049_auto_20210701_1730'),
        ('external_services', '0013_auto_20210414_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkservice',
            name='destination_region',
            field=models.PositiveSmallIntegerField(choices=[(0, 'DESTINATION_INTERNAL_PRIVACY_NOTICE'), (1, 'DESTINATION_ORGANIZATION_PRIVACY_NOTICE'), (3, 'DESTINATION_EEA_PRIVACY_NOTICE'), (5, 'DESTINATION_PRIVACYSHIELD_PRIVACY_NOTICE'), (6, 'DESTINATION_GLOBAL_PRIVACY_NOTICE')], default=6, help_text='SERVICE_DESTINATION_REGION_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='linkservice',
            name='enabled',
            field=models.BooleanField(default=True, help_text='SERVICE_ENABLED_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='linkservice',
            name='menu_icon_class',
            field=models.CharField(default='globe', help_text='SERVICE_MENU_ICON_HELPTEXT', max_length=32),
        ),
        migrations.AlterField(
            model_name='linkservice',
            name='menu_label',
            field=models.CharField(help_text='SERVICE_MENU_LABEL_HELPTEXT', max_length=255),
        ),
        migrations.AlterField(
            model_name='linkservice',
            name='privacy_notice_url',
            field=models.CharField(blank=True, help_text='SERVICE_PRIVACY_NOTICE_URL_HELPTEXT', max_length=512),
        ),
        migrations.AlterField(
            model_name='linkservice',
            name='url',
            field=models.CharField(help_text='SERVICE_URL', max_length=256),
        ),
        migrations.AlterField(
            model_name='ltiservice',
            name='access_settings',
            field=models.IntegerField(choices=[(0, 'LTI_SERVICE_ANONYMOUS_NO_API'), (5, 'LTI_SERVICE_PUBLIC_NO_API'), (10, 'LTI_SERVICE_PUBLIC_YES_API')], default=0, help_text='LTI_SERVICE_ACCESS_SETTINGS_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='ltiservice',
            name='consumer_key',
            field=models.CharField(help_text='LTI_SERVICE_CONSUMER_KEY_HELPTEXT', max_length=128),
        ),
        migrations.AlterField(
            model_name='ltiservice',
            name='consumer_secret',
            field=models.CharField(help_text='LTI_SERVICE_CONSUMER_SECRET_HELPTEXT', max_length=128),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='access',
            field=models.IntegerField(choices=[(0, 'MENU_ITEM_ACCESS_ALL'), (5, 'MENU_ITEM_ACCESS_ASSISTANTS_AND_TEACHERS'), (10, 'MENU_ITEM_ACCESS_TEACHERS')], default=0),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='course_instance',
            field=models.ForeignKey(help_text='MENU_ITEM_COURSE_INSTANCE_HELPTEXT', on_delete=django.db.models.deletion.CASCADE, related_name='ext_services', to='course.courseinstance'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_group_label',
            field=models.CharField(blank=True, help_text='MENU_ITEM_MENU_GROUP_LABEL_HELPTEXT', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_icon_class',
            field=models.CharField(blank=True, help_text='MENU_ITEM_MENU_ICON_CLASS_HELPTEXT', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_label',
            field=models.CharField(blank=True, help_text='MENU_ITEM_MENU_LINK_LABEL_HELPTEXT', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_url',
            field=models.CharField(blank=True, help_text='MENU_ITEM_MENU_URL_HELPTEXT', max_length=256, null=True, validators=[external_services.models.validate_no_domain]),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_weight',
            field=models.IntegerField(default=0, help_text='MENU_ITEM_MENU_WEIGHT_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='service',
            field=models.ForeignKey(blank=True, help_text='MENU_ITEM_SERVICE_HELPTEXT', null=True, on_delete=django.db.models.deletion.CASCADE, to='external_services.linkservice'),
        ),
    ]
