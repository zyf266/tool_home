from contextlib import nullcontext

from django.shortcuts import render

from .form import Sql_Tool
from django import forms


def index(request):
    return render(request, 'index.html')


# Create your views here.
def sql_table_create(request):
    sql_create_table = ""
    if request.method == 'POST':
        forms = Sql_Tool(request.POST)
        if forms.is_valid():
            table_name = forms.cleaned_data['table_name']
            string_fields = forms.cleaned_data['var_column'].split(',')
            # strip()移除字符开头和结尾的所有空白字符
            string_fields = [field.strip() for field in string_fields]

            int_fields = forms.cleaned_data['int_column'].split(',')
            int_fields = [field.strip() for field in int_fields]

            date_fields = forms.cleaned_data['date_column'].split(',')
            date_fields = [field.strip() for field in date_fields]

            primary_key = forms.cleaned_data['pri_key'].split(',')
            primary_key = [pk.strip() for pk in primary_key]

            unique_keys = forms.cleaned_data['uni_key'].split(',')
            unique_keys = [uk.strip() for uk in unique_keys]

            if forms.cleaned_data['temp'] == 'ygy':
                fields = ['`id` bigint(20) NOT NULL AUTO_INCREMENT',
                          '`create_by` varchar(50)',
                          '`update_by` varchar(50)',
                          '`remarks` varchar(50)',
                          '`create_time` datetime',
                          '`update_time` datetime',
                          '`sl_line` varchar(50)',
                          '`sn_line` varchar(50)',
                          '`measurement_curve` varchar(50)',
                          '`measure_date` datetime DEFAULT NULL',
                          '`sample_no` varchar(50) DEFAULT NULL',
                          '`line_id` varchar(50) DEFAULT NULL',
                          '`sample_name` varchar(50) DEFAULT NULL',
                          '`sample_type` varchar(50) DEFAULT NULL',
                          ]
            elif forms.cleaned_data['temp'] == 'kyj':
                fields = ['`id` bigint(20) NOT NULL AUTO_INCREMENT',
                          '`sample_no` varchar(50) DEFAULT NULL',
                          '`sample_time` datetime DEFAULT NULL',
                          '`specimen_date` datetime DEFAULT NULL',
                          '`sample_instar` decimal(16, 6) DEFAULT NULL',
                          '`sample_effective_value` varchar(50) DEFAULT NULL',
                          '`sample_flexural_value` varchar(50) DEFAULT NULL',
                          '`sample_type` varchar(50) DEFAULT NULL COMMENT',
                          '`sample_variety_grade` varchar(50) DEFAULT NULL',
                          '`factory_name` varchar(50) DEFAULT NULL',
                          '`factory_code` varchar(50) DEFAULT NULL',
                          '`dept_id` varchar(50) DEFAULT NULL',
                          '`factory_id` varchar(50) DEFAULT NULL',
                          '`bscode` varchar(50) DEFAULT NULL',
                          'PRIMARY KEY (`id`) USING BTREE',
                          'UNIQUE KEY `kyj` (`sample_no`, `sample_time`, `specimen_date`, `sample_instar`)'
                          ]
            elif forms.cleaned_data['temp'] == '0':
                fields = []

            for field in string_fields:
                if field:
                    fields.append(f"{field} varchar(255)")

            for field in int_fields:
                if field:
                    fields.append(f"{field} int")

            for field in date_fields:
                if field:
                    fields.append(f"{field} datetime")

            if primary_key and primary_key[0]:
                primary_key_str = ", ".join(primary_key)
                fields.append(f"PRIMARY KEY ({primary_key_str})")

            for key in unique_keys:
                if key:
                    fields.append(f"UNIQUE ({key})")

            fields_str = ",\n    ".join(fields)
            sql_create_table = f"CREATE TABLE {table_name} (\n    {fields_str}\n);"
            return render(request, 'sql_create_table.html', {'form': forms, 'sql_create_table': sql_create_table})
        else:
            forms = Sql_Tool()
    else:
        forms = Sql_Tool()
    return render(request, 'sql_create_table.html', {'form': forms})

