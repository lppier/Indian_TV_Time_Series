library(ggplot2) 
library(forecast)

# Read CSV into R
setwd("/Users/davidleonardi/Projects/Indian_TV_Time_Series")
curDir <- getwd()

df <- read.csv(file="./data/ActualRatings_weeklyGRP.csv", header=TRUE, sep=",", stringsAsFactors=FALSE)

df$GRPRatingsDate <- as.Date(sapply(df$GRPRatingsDate, function(x) strsplit(x, " ")[[1]][1]), "%d-%B-%Y")

ggplot(data=df, aes(x=GRPRatingsDate, y=GRP)) +
  geom_line()+
  geom_point()+
  labs(title="Weekly Ratings 2007 - 2009", y="GRP", x="GRP Ratings Date")

df_train <- df[which(df$GRPRatingsDate <= "2008-10-26"),]
df_test <- df[which(df$GRPRatingsDate > "2008-10-26"),]

head(df_train, 5)
head(df_test, 5)

timeseries_train = df_train$GRP

ts_train = ts(timeseries_train, frequency = 12)
decompose_train = decompose(ts_train, "multiplicative")

plot(as.ts(decompose_train$seasonal))
plot(as.ts(decompose_train$trend))
plot(as.ts(decompose_train$random))
plot(decompose_train)
