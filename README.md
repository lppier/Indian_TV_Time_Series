# Indian_TV_Time_Series

In TV advertising, the Gross Rating Point (GRP) metric is one of the primary measures that advertisers use, to determine which TV stations to place their commercials with. With an annual TV advertising market of over US$4 billion, it is of high commercial importance to be able to forecast GRP ratings accurately for India TV stations for all stakeholders.
The objective of this exercise is to demonstrate a suitable Time Series Forecast method that can accurately forecast the GRP TV channel rating data given a limited set of prior data points.

The dataset is the actual GRP weekly metric from an Indian TV channel. A total of 92 weekly data points from 17 Jun 2007 to 15 Mar 2009 is available, of which 72 weekly data points from the beginning will be our training period and 20 weekly data points from 26 Oct 08 onwards is our forecast target, named as the validation period.
The following table summarises the variables in the data used for further processing, what they represent and their data type:

1	**OptimusPrime_Unit7_AsnTS.pdf**	The report for the CA
2	**train.csv, test.csv**	Training data – Data up to 26th Oct 2008, Test data – Data from Nov 2008 – 15 Mar 2009
3	**TimeSeriesRegression.ipynb**	Exploratory analysis 
4	**Arima.ipynb**	Running of auto-ARIMA to choose the best ARIMA values
5	**Time Series.jmp**
	This JMP file contains the analysis for the exponential smoothing and ARIMA modelling. 
6	**Regression_excel folder**	Contains the excel files for regression and dummy variable regression modelling 
7	**Decompositional Methods.ipynb**	Additive and Multiplicative Decompositional Methods
8	**Decompositional_Methods.Rmd**	STL Decompositional Method
9	**Exponential_Smoothing_Try.ipynb**	Some visualizations for exponential smoothing

