# Generated by Django 4.1.3 on 2023-12-19 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcreageType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Acreage Type',
                'verbose_name_plural': 'Acreage Types',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attention_line1', models.CharField(blank=True, max_length=128)),
                ('attention_line2', models.CharField(blank=True, max_length=128)),
                ('address_line1', models.CharField(max_length=128)),
                ('address_line2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=40)),
                ('originalLessee', models.CharField(max_length=40)),
                ('agreementDate', models.DateField()),
                ('effectiveDate', models.DateField()),
                ('term', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AgreementStage',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
                ('index', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Agreement Stage',
                'verbose_name_plural': 'Agreement Stages',
            },
        ),
        migrations.CreateModel(
            name='AgreementStatus',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Agreement Status',
                'verbose_name_plural': 'Agreement Statuses',
            },
        ),
        migrations.CreateModel(
            name='AgreementType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Agreement Type',
                'verbose_name_plural': 'Agreement Types',
            },
        ),
        migrations.CreateModel(
            name='BackupWithholdingType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Backup Withholding Type',
                'verbose_name_plural': 'Backup Withholding Types',
            },
        ),
        migrations.CreateModel(
            name='BusinessAssociateType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Business Associate Type',
                'verbose_name_plural': 'Business Associate Types',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=4)),
                ('abbreviation', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('update_date', models.DateField()),
                ('hidden', models.BooleanField(default=False)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=50)),
                ('update_date', models.DateField()),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'County',
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Entity Type',
                'verbose_name_plural': 'Entity Types',
            },
        ),
        migrations.CreateModel(
            name='LandDivision',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Land Division',
                'verbose_name_plural': 'Land Divisions',
            },
        ),
        migrations.CreateModel(
            name='Landowner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('ssn', models.CharField(max_length=11, verbose_name='Social Security Number')),
                ('backupWithholding', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('address', models.ManyToManyField(to='landman.address')),
                ('backupWithholdingType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.backupwithholdingtype')),
                ('entity_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.entitytype')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgressDateStatus',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Project Progress Date Status',
                'verbose_name_plural': 'Project Progress Date Statuses',
            },
        ),
        migrations.CreateModel(
            name='ProjectProgressDateType',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Project Progress Date Type',
                'verbose_name_plural': 'Project Progress Date Types',
            },
        ),
        migrations.CreateModel(
            name='ProjectStage',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
                ('index', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Project Stage',
                'verbose_name_plural': 'Project Stages',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Project Status',
                'verbose_name_plural': 'Project Statuses',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Project Type',
                'verbose_name_plural': 'Project Types',
            },
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Subject Type',
                'verbose_name_plural': 'Subject Types',
            },
        ),
        migrations.CreateModel(
            name='SurveyType',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Survey Type',
                'verbose_name_plural': 'Survey Types',
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Task Status',
                'verbose_name_plural': 'Task Statuses',
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Task Type',
                'verbose_name_plural': 'Task Types',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='WellStatus',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Well Status',
                'verbose_name_plural': 'Well Statuses',
            },
        ),
        migrations.CreateModel(
            name='WorkingList',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('agreements', models.ManyToManyField(blank=True, to='landman.agreement')),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
                ('longitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.wellstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('effDateFrom', models.DateField(blank=True, verbose_name='Effective Date From')),
                ('effDateTo', models.DateField(blank=True, verbose_name='Effective Date To')),
                ('dueDate', models.DateField(blank=True, verbose_name='Due Date')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.taskstatus')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.tasktype')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=6)),
                ('abbreviation', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('update_date', models.DateField()),
                ('hidden', models.BooleanField(default=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.country')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.surveytype')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgressDate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('due_date', models.DateField(verbose_name='Due Date')),
                ('completed_date', models.DateField(verbose_name='Completed Date')),
                ('update_date', models.DateTimeField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.projectprogressdatestatus')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.projectprogressdatetype')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('contacts', models.ManyToManyField(blank=True, to='landman.landowner')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.country')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.county')),
                ('cross_references', models.ManyToManyField(blank=True, to='landman.project')),
                ('progress_dates', models.ManyToManyField(blank=True, to='landman.projectprogressdate')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.projectstage')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.state')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.projectstatus')),
                ('tasks', models.ManyToManyField(blank=True, to='landman.task')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.projecttype')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('update_date', models.DateTimeField()),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JeffersonianLegalHeader',
            fields=[
                ('acreage', models.DecimalField(blank=True, decimal_places=6, max_digits=13, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('townshipNum', models.IntegerField()),
                ('townshipDir', models.CharField(choices=[('N', 'North'), ('S', 'South')], default='N', max_length=10)),
                ('rangeNum', models.IntegerField()),
                ('rangeDir', models.CharField(choices=[('E', 'East'), ('W', 'West')], default='E', max_length=10)),
                ('section', models.IntegerField()),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='legal_segments', to='landman.agreement')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.country')),
                ('county', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.PROTECT, to='landman.county')),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.PROTECT, to='landman.state')),
                ('surveyType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.surveytype')),
            ],
            options={
                'verbose_name': 'Jeffersonian Legal Segment',
                'verbose_name_plural': 'Jeffersonian Legal Segments',
            },
        ),
        migrations.CreateModel(
            name='HistoricalWell',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
                ('longitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.wellstatus')),
            ],
            options={
                'verbose_name': 'historical well',
                'verbose_name_plural': 'historical wells',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(max_length=254)),
                ('effDateFrom', models.DateField(blank=True, verbose_name='Effective Date From')),
                ('effDateTo', models.DateField(blank=True, verbose_name='Effective Date To')),
                ('dueDate', models.DateField(blank=True, verbose_name='Due Date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.taskstatus')),
                ('type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.tasktype')),
            ],
            options={
                'verbose_name': 'historical task',
                'verbose_name_plural': 'historical tasks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('country', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.country')),
                ('county', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.county')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('stage', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.projectstage')),
                ('state', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.state')),
                ('status', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.projectstatus')),
                ('type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.projecttype')),
            ],
            options={
                'verbose_name': 'historical project',
                'verbose_name_plural': 'historical projects',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalJeffersonianLegalHeader',
            fields=[
                ('acreage', models.DecimalField(blank=True, decimal_places=6, max_digits=13, null=True)),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('townshipNum', models.IntegerField()),
                ('townshipDir', models.CharField(choices=[('N', 'North'), ('S', 'South')], default='N', max_length=10)),
                ('rangeNum', models.IntegerField()),
                ('rangeDir', models.CharField(choices=[('E', 'East'), ('W', 'West')], default='E', max_length=10)),
                ('section', models.IntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('agreement', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.agreement')),
                ('country', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.country')),
                ('county', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='state', chained_model_field='state', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.county')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='country', chained_model_field='country', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.state')),
                ('surveyType', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.surveytype')),
            ],
            options={
                'verbose_name': 'historical Jeffersonian Legal Segment',
                'verbose_name_plural': 'historical Jeffersonian Legal Segments',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAgreement',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=40)),
                ('originalLessee', models.CharField(max_length=40)),
                ('agreementDate', models.DateField()),
                ('effectiveDate', models.DateField()),
                ('term', models.IntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('landDivision', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.landdivision')),
                ('rights', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.right')),
                ('stage', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.agreementstage')),
                ('status', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.agreementstatus')),
                ('type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.agreementtype')),
            ],
            options={
                'verbose_name': 'historical agreement',
                'verbose_name_plural': 'historical agreements',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAcreage',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('agreement', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.agreement')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.acreagetype')),
                ('unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='landman.unit')),
            ],
            options={
                'verbose_name': 'historical acreage',
                'verbose_name_plural': 'historical acreages',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.state'),
        ),
        migrations.AddField(
            model_name='county',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agreementtype',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='agreement_types', to='landman.subjecttype'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='landDivision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.landdivision'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='related',
            field=models.ManyToManyField(blank=True, to='landman.agreement'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='rights',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.right'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.agreementstage'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.agreementstatus'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.agreementtype'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='wells',
            field=models.ManyToManyField(blank=True, to='landman.well'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.state'),
        ),
        migrations.CreateModel(
            name='Acreage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('agreement', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='acreage', to='landman.agreement')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.acreagetype')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landman.unit')),
            ],
        ),
    ]
