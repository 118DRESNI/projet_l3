import math

def conv_volt2ppm(ADC):
	ADCO2		=ADC[0]
	ADCO		=ADC[1]
	ADCNTC		=ADC[2]
	ADCQEPAS	=ADC[3]

	#convert vco2 to ppm 
	A=(ADCO2+0.044)/0.438490649
	PPMCO2=math.exp(A)
    #convert vco to ppm
	Ro_clean_air_factor=0.7
	Vcc=5000 #supply voltage
	RL=10000 #load résistance
	Rs = RL * (1024 - ADCO) / ADCO
	mV = ADCO * (Vcc / 1024)
	Ro = ((Vcc - mV) * RL) / (mV * Ro_clean_air_factor) #Ro = calibration factor for measurement in clean air.
	ratio=Rs/Ro
	#convert equation from sensitivity curve co
	a=ratio/22.073
	b=-1/0.66666
	PPMCO=a**b
	#valeurs bidon
	PPMNTC		=-1
	PPMQEPAS	=-1

	PPM = []
	PPM[0]=PPMCO2
	PPM[1]=PPMCO
	PPM[2]=PPMNTC
	PPM[3]=PPMQEPAS
	return(PPM)

