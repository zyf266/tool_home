from django import forms


#配置sql生成器的输入框
class Sql_Tool(forms.Form):
    status_choices={
        'ygy':'YGY',
        'kyj':'KYJ',
        '0':'空'
    }
    temp=forms.ChoiceField(label='模板选择',choices=status_choices)
    table_name=forms.CharField(label='表名')
    var_column=forms.CharField(label='字符类型字段',required=False)
    int_column=forms.CharField(label='整数类型字段',required=False)
    date_column=forms.CharField(label='日期类型字段',required=False)
    pri_key=forms.CharField(label='主键设置',required=False)
    uni_key=forms.CharField(label='唯一键设置',required=False)
