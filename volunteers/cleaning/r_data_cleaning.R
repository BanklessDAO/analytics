library(tidyverse)
library(data.table)

df <- read_csv("./volunteer.csv")

df %>%
    names()

df2 <- df %>%
    rename(role = `What role(s) are you volunteering for?`)


# using data.table to split out column with multiple words
df3 <- setDT(tstrsplit(as.character(df2$role), " ", fixed=TRUE))[]
