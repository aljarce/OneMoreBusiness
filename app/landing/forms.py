from django import forms

class QuestionnaireForm(forms.Form):
    nombre = forms.CharField(label='Nombre completo', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    situacion = forms.ChoiceField(label='Situación actual', choices=[
        ('estudio', 'Estudio'),
        ('estudio_y_trabajo', 'Estudio y trabajo'),
        ('trabajo_medio_tiempo', 'Trabajo a medio tiempo'),
        ('trabajo_tiempo_completo', 'Trabajo a tiempo completo'),
        ('nini', 'No estudio ni trabajo')
    ])
    objetivo = forms.CharField(label='¿Cuál es tu objetivo personal al generar más ingresos y qué cambiaría en tu vida el conseguirlo?', widget=forms.Textarea)
    inversion = forms.ChoiceField(label='¿Cuánto estarías dispuesto a invertir ahora mismo, para generar ingresos con el ecommerce?', choices=[
        ('lt_500', 'Menos de 500 €'),
        ('500-1000', '500 - 1000 €'),
        ('1000-2000', '1000 - 2000 €'),
        ('2000-4000', '2000 - 4000 €'),
        ('gt_4000', 'Más de 4000 €')
    ])
    conseguir = forms.CharField(label='Si cuentas con nuestro acompañamiento durante tres meses, ¿qué te gustaría estar consiguiendo o ganando con tu ecommerce?', widget=forms.Textarea)
    disponibilidad = forms.ChoiceField(label='Si tu situación es aceptada, ¿cuándo estarías disponible para empezar?', choices=[
        ('ahora', 'Ahora mismo'),
        ('2sem', 'En dos semanas'),
        ('1mes', 'En un mes')
    ])
    tlf = forms.CharField(label='Número de teléfono', max_length=20)
