from django.shortcuts import render
from trocador.duplotubo.forms import Calculo
from trocador.duplotubo.metodo_kern import *
from trocador.duplotubo.models import *
from trocador.duplotubo.forms import *
from trocador.core.models import *
from django.contrib.auth.decorators import login_required

 
def propried_get(Table,temp,temp_w,fluido):
	def trecho(Table,temp):
		query1=Table.objects.filter(temperature__gte=temp)[0] 
		query2=Table.objects.filter(temperature__lte=temp)[len(Table.objects.filter(temperature__lte=temp))-1] 
		temp1=query1.temperature;temp2=query2.temperature
		return query1,query2,temp1,temp2
	for propriedade in fluido.keys():
		try:
			if propriedade=='Viscos_tw':
				query1,query2,temp1,temp2=trecho(Agua,temp_w)
				prop1=eval('query1.Viscos');prop2=eval('query2.Viscos')
			else:
				query1,query2,temp1,temp2=trecho(Agua,temp)
				prop1=eval('query1.%s'%propriedade);prop2=eval('query2.%s'%propriedade)
			fluido[propriedade]=(prop2-prop1)*(temp-temp1)/(temp2-temp1) + prop1 if prop2>prop1 else -(prop1-prop2)*(temp-temp1)/(temp2-temp1) + prop1
		except: pass
	fluido['Pr']=fluido['cp']*fluido['Viscos']/fluido['k']
	return fluidos

def atribut(formulario,dicionario,identificador=''):
	for dado in formulario.cleaned_data.keys():
		if dado.replace(identificador,'') in dicionario.keys():
			dicionario[dado.replace(identificador,'')]=formulario.cleaned_data[dado]
	if 'Annulus' in dicionario.keys():
		dicionario['Diam_int']=dicionario['Diam_int']/1000.0
		dicionario['Diam_ext']=dicionario['Diam_ext']/1000.0
		dicionario['Annulus']=0 if identificador is 'Interno' else 1
	return	dicionario

@login_required
def calculo_duplotubo(request):
	fluidoInterno={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,
	         'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':0,'Liquido':0,'Viscos_tw':0}
	fluidoExterno={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,
	         'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':1,'Liquido':0,'Viscos_tw':0}
	temp_m1=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1'])/2
	temp_m2=(form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/2
	temp_w=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1']+form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/4
	#import pdb; pdb.set_trace()
	exibition = Resultado()
	template_name = 'duplotubo/calculo_duplotubo.html'
	form = Calculo(request.POST or None)

	if form.is_valid():
		if form.cleaned_data['nome_fluido1']=='manual': 
			fiul1=atribut(form.cleaned_data,fluidoInterno,identificador="Interno")

		if form.cleaned_data['nome_fluido2']=='manual': 
			fiul2=atribut(form.cleaned_data,fluidoExterno,identificador='Externo')

		elif form.cleaned_data['nome_fluido2']!='manual' or form.cleaned_data['nome_fluido1']!='manual':
			propried_get(eval(form.cleaned_data['nome_fluido1']),temp_m1,temp_w,fluidoInterno)
			propried_get(eval(form.cleaned_data['nome_fluido2']),temp_m2,temp_w,fluidoExterno)

	context={'form': form}
	if form.is_valid():
		if form.cleaned_data['nome_fluido1']=='manual' and form.cleaned_data['nome_fluido2']!='manual':
			fluido1, fluido2, material = yut(fiul1,
				propried_get(eval(form.cleaned_data['nome_fluido2']),temp_m2,temp_w,fluidoExterno),
				atribut(form.cleaned_data,material))

		if form.cleaned_data['nome_fluido2']=='manual' and form.cleaned_data['nome_fluido1']!='manual':
			fluido1, fluido2, material = yut(
				propried_get(eval(form.cleaned_data['nome_fluido1']),temp_m1,temp_w,fluidoInterno),
				fiul2,
				atribut(form.cleaned_data,material))

		elif form.cleaned_data['nome_fluido1']=='manual' and form.cleaned_data['nome_fluido2']=='manual':
			fluido1, fluido2, material = yut(fiul1,fiul2,atribut(form.cleaned_data,material))
		else:

			fluido1, fluido2, material = yut(
				# Fluido1
				propried_get(eval(form.cleaned_data['nome_fluido1']),temp_m1,temp_w,fluidoInterno),
				# Fluido2
				propried_get(eval(form.cleaned_data['nome_fluido2']),temp_m2,temp_w,fluidoExterno),
				# Material
				atribut(form.cleaned_data,material))

		res = Resultado()
		res.result_fl = fluido1
		res.result_pres = fluido2
		res.result_geral = material
		res.save()

		context = {'form': form,
					'Vazao1':fluido1['Vazao'][0],
					'Vazao2':fluido1['Vazao'][1],
					'Tentr1': fluido1['Temperatura de Entrada'][0],
					'Tentr2': fluido1['Temperatura de Entrada'][1],
					'Tsaid1': fluido1['Temperatura de Saida'][0],
					'Tsaid2': fluido1['Temperatura de Saida'][1],
					'Velocidade_Media_Escoamento1':fluido1['Velocidade Media de Escoamento'][0],
					'Velocidade_Media_Escoamento2':fluido1['Velocidade Media de Escoamento'][1],
					'Numero_Reynolds1':fluido1['Numero de Reynolds'][0],
					'Numero_Reynolds2':fluido1['Numero de Reynolds'][1],
					'Numero_Nusselts1':fluido1['Numero de Nusselts'][0],
					'Numero_Nusselts2':fluido1['Numero de Nusselts'][1],
					'dTlmtd':material['Var. Log. de Temperatura (dTm)'],
					'Coeficiente_Pelicula1':fluido1['Coeficiente de Pelicula (h)'][0],
					'Coeficiente_Pelicula2':fluido1['Coeficiente de Pelicula (h)'][1],

					'DP1':fluido2['DP'][0],
					'DP2':fluido2['DP'][1],
					'DPrb1':fluido2['DPrb'][0],
					'DPrb2':fluido2['DPrb'][1],
					'DP_total1':fluido2['DPtotal'][0],
					'DP_total2':fluido2['DPtotal'][1],
					'Potencia_Bombeamento1': fluido2['Potencia de Bombeamento'][0],
					'Potencia_Bombeamento2': fluido2['Potencia de Bombeamento'][1],
					'DP_Bocais1':fluido2['DPnl (bocais)'][0],
					'DP_Bocais2':fluido2['DPnl (bocais)'][1],

					'Area_Troca_Termica_Total':material['Area de Troca Termica Total'],
					'Calor_Trocado':material['Calor Trocado (Heat Duty)'],
					'Coef_Trans_Calor_Limpo':material['Coef. de Trans. de Calor Limpo (Uc)'],
					'Coef_Trans_Calor_Incrustado':material['Coef. de Trans. de Calor Incrustado (Ud)'],
					'Fator_Limpeza':material['Fator de Limpeza (CF)'],
					'Area_Grampo_Tubular':material['Area por Grampo Tubular'],
					'Numero_Grampos':str(material['Numero de Grampos']),
                    'Excesso_Area':str(material['Excesso de Area (Over-Surface Design)']),
                    }
				
	return render(request, template_name, context)
