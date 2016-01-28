import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import math

loansData = pd.read_csv('loansData_clean.csv')
loansData['IR_TF'] = map(lambda x: 0 if x < .12 else 1, loansData['Interest.Rate.Clean'])
loansData['Intercept'] = 1
indVars = ['Intercept', 'FICO.Score', 'Amount.Funded.By.Investors']

def main():

	logit = sm.Logit(loansData['IR_TF'], loansData[indVars])
	result = logit.fit()
	coeff = result.params
	
	def logisticfunction():
		pv = (1/(1+math.e**(coeff['Intercept'] + (coeff['FICO.Score'] * input('Enter FICO Score: ')) 
		+ (coeff['Amount.Funded.By.Investors'] * input('Enter Amount Funded: ')))))	
		return pv
	
	def pred():
		pt = logisticfunction()
		if pt > .7: 
			print('Approved')
		else:
			print('Rejected')
	
	pred()
	
if __name__ == "__main__":
    main()











