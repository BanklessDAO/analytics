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

# select Owner (public address) and Claim Date from each dataframe

# Claim Date: 5/14/2021
c1 <- df %>%
    select(Owner, `Claim Date`)

# see c2
df2 %>%
    select(ID, Owner, `Claim Date`) %>%
    group_by(ID, Owner)

# Claim Date: 5/21/2021
c2 <- df2a %>%
    mutate(
        `Claim Date` = "5/21/2021"
    ) %>%
    select(1,3)

# Claim Date: 5/28/2021
c3 <- df3 %>%
    select(Owner, `Claim Date`)


# Claim Date: 6/4/2021
c4 <- df4 %>%
    select(Owner, `Claim Date`)


# rbind all dataframes

combine <- rbind(c1, c2, c3, c4)


#------- Wrangle and Visualize Combined Data Frame ---------#

# Number of Poaps Claimed by Addresses
combine %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    rename(
        public_address = Owner,
        poaps_claimed = n
    ) %>%
    group_by(poaps_claimed) %>%
    tally(sort = TRUE) %>%
    rename(
        num_addresses = n
    ) %>%
    arrange(poaps_claimed) %>%
    ggplot(aes(x = poaps_claimed, y = num_addresses, fill = 'red')) +
    geom_col() +
    geom_text(aes(label = num_addresses), vjust = -0.50) +
    theme_minimal() +
    theme(legend.position = "none") +
    labs(
        title = "Bankless DAO Engagement",
        subtitle = "Community Calls #1-4",
        x = "Number of POAPs claimed",
        y = "Number of Addresses",
        caption = "Data: poap.gallery | Analytics: @paulapivat"
    )

# Number of POAPs claimed by Date

main_dates <- c("5/14/2021", "5/21/2021", "5/28/2021", "6/4/2021")


combine %>%
    group_by(`Claim Date`) %>%
    tally(sort = TRUE) %>%
    arrange(`Claim Date`) %>%
    rename(
        poaps_claimed = n,
        Date = `Claim Date`
    ) %>%
    ggplot(aes(x = Date,  y = poaps_claimed, fill = ifelse(Date %in% main_dates, 'red', 'black'))) +
    geom_col() +
    theme_minimal() +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position = "none"
    )





    