# library
library(tidyverse)

# load data
# community call # 1 
df <- read_csv("../raw/Bankless DAO Community Call #1.csv")

# community calls 2,3,4
df2 <- read_csv("../raw/Bankless DAO Community Call #2.csv")
df3 <- read_csv("../raw/Bankless DAO Community Call #3.csv")
df4 <- read_csv("../raw/Bankless DAO Community Call #4.csv")

# column names
df %>% names()

# exploratory (rows = 162)
df %>%
    str()

# group by Owner (address) -- 162 distinct addresses 
df %>%
    group_by(Owner) %>%
    tally(sort = TRUE)


# group by ENS name -- 
# 89 missing names
########### ***** Several names had double entries ****** #########
# group by ENS names may not be the best idea
df %>%
    group_by(oktal.eth) %>%
    tally(sort = TRUE) %>%
    view()
    
# match address to name -- 162
df %>%
    group_by(Owner, oktal.eth) %>%
    tally(sort = TRUE)

## ----------- Explore community calls 2, 3, and 4 ------------##

# community call #2
# group by Owner (every address had double-entry, n = 332, when it should be 166)
# saving ONLY distinct addresses into df2a
df2a <- df2 %>%
    group_by(Owner) %>%
    tally(sort = TRUE)

# community call #3
# group by Owner (all addresses are unique, n = 171)
df3 %>%
    group_by(Owner) %>%
    tally(sort = TRUE)


# community call #4
# group by Owner (all addresses are unique, n = 172)

df4 %>%
    group_by(Owner) %>%
    tally(sort = TRUE)

# --- Combine all dataframes into one --- #

# select first two columns from each data frame
# add third column to label community call number (i.e., CC1, CC2, CC3, CC4)
# rbind all dataframes


    