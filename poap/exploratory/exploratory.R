# library
library(tidyverse)

# load data
# community call # 1 
df <- read_csv("../raw/Bankless DAO Community Call #1.csv")

# community calls 2,3,4,5,6
df2 <- read_csv("../raw/Bankless DAO Community Call #2.csv")
df3 <- read_csv("../raw/Bankless DAO Community Call #3.csv")
df4 <- read_csv("../raw/Bankless DAO Community Call #4.csv")
df5 <- read_csv("../raw/Bankless DAO Community Call #5.csv")
df6 <- read_csv("../raw/Bankless DAO Community Call #6.csv")
df7 <- read_csv("../raw/BDAO Community Call #7.csv")

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

# --------------------- Combine all dataframes into one ----------------------- #

# select Owner (public address) and Claim Date from each dataframe

# Claim Date: 5/14/2021
c1 <- df %>%
    select(Owner, `Claim Date`) %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE)

# Claim Date: 5/21/2021
# note: n column shows duplicates (n = 2) - eliminated via group_by
c2 <- df2 %>%
    select(Owner, `Claim Date`) %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE)


# Claim Date: 5/28/2021
c3 <- df3 %>%
    select(Owner, `Claim Date`) %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) 


# Claim Date: 6/4/2021
c4 <- df4 %>%
    select(Owner, `Claim Date`) %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE)

# Claim Date: 6/11/2021
c5 <- df5 %>%
    select(Owner, `Claim Date`) %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE)

# Claim Date: 6/18/2021
c6 <- df6 %>%
    select(Owner, `Claim Date`) %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE)


# Claim Date: 6/25/2021
c7 <- df7 %>%
    select(Owner, `Claim Date`) %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE)


#------Before Combine, do another group_by without `Claim Date` to eliminate any potential duplicates -----#

# n = 162
c1 %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    view()

# n = 166
c2 %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    view()

# n = 171
c3 %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    view()

# n = 172
c4 %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    view()

# n = 286
c5 %>% 
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    view()

# n = 246
c6 %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    view()

# n = 223
c7 %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    view()

#------ Group by WITH `Claim Date` to check the same address claimed more than once per call -----#

# n = 162
c1 %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) %>%
    view()

# n = 166
c2 %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) %>%
    view()

# n = 171
c3 %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) %>%
    view()

# n = 172
c4 %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) %>%
    view()


# n = 286
c5 %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) %>%
    view()

# n = 246
c6 %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) %>%
    view()

# n = 223
c7 %>%
    group_by(Owner, `Claim Date`) %>%
    tally(sort = TRUE) %>%
    view()

# rbind all dataframes

combine_wk4 <- rbind(c1, c2, c3, c4)

combine_wk5 <- rbind(c1, c2, c3, c4, c5)

combine_wk6 <- rbind(c1, c2, c3, c4, c5, c6)

combine_wk7 <- rbind(c1, c2, c3, c4, c5, c6, c7)

# NOTE numbers can change because the pool is not fixed
# every community call could be someone's first POAP claim
# the it's someone's second call out of the (current) total of only 6 calls
# and it's someone's third call out of 6 and so forth
# with every new call, the previous call could've also been someone's last POAP claim (they didn't claim the most recent one)


combine_wk4 %>%
    group_by(Owner) %>%
    count(sort = TRUE) %>%
    view()


combine_wk5 %>%
    group_by(Owner) %>%
    count(sort = TRUE) %>%
    view()

combine_wk6 %>%
    group_by(Owner) %>%
    count(sort = TRUE) %>%
    view()

#------- Wrangle and Visualize Combined Data Frame ---------#

# Number of Poaps Claimed by Addresses
combine_wk7 %>%      # change weekly
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
        title = "Bankless DAO Community Call Engagement",
        subtitle = "Order by Number of POAPs claimed",
        x = "Number of POAPs claimed",
        y = "Number of Addresses",
        caption = "Data: poap.gallery | Analytics: @paulapivat"
    )

# Number of POAPs claimed by Date

main_dates <- c("5/14/2021", "5/21/2021", "5/28/2021", "6/4/2021")

main_dates_wk5 <- c("5/14/2021", "5/21/2021", "5/28/2021", "6/4/2021", "6/11/2021")

main_dates_wk6 <- c("5/14/2021", "5/21/2021", "5/28/2021", "6/4/2021", "6/11/2021", "6/18/2021")

main_dates_wk7 <- c("5/14/2021", "5/21/2021", "5/28/2021", "6/4/2021", "6/11/2021", "6/18/2021", "6/25/2021")



# Fix Date Ordering so that 6/11/2021 is the most recent date


combine_wk7 %>%      # change weekly
    # change Claim Date from Char to Date
    mutate(
        Date = as.Date(`Claim Date`, "%m/%d/%Y")
    ) %>% 
    group_by(Date) %>%
    tally() %>% 
    rename(
        poaps_claimed = n
    ) %>%
    # change main_dates_x every week
    ggplot(aes(x = Date, y = poaps_claimed, fill = ifelse(Date %in% as.Date(main_dates_wk7, "%m/%d/%Y"), 'red', 'green'))) +  
    geom_col() +
    scale_x_date(date_breaks = '2 day') +
    geom_text(aes(label = poaps_claimed), vjust = -0.50) +
    theme_minimal() +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position = "none"
    ) +
    labs(
        title = "Bankless DAO Community Call Engagement",
        subtitle = "POAPs claimed by Date",
        x = "",
        y = 'Number of POAPs Claimed',
        caption = "Data: poap.gallery | Analytics: @paulapivat"
    )
    
    
    
    
    
    

########### HOLD: Waiting to be Deleted ###########


# group_by address
combine %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    ungroup() %>%
    group_by(n) %>%
    tally(sort = TRUE) %>%
    ungroup()

# separate categories into group
# see how many addresses are contained
# step 1: pivot wider,
# step 2: save as combine2
# step 3: split out columns 1,2,3,4
# step 4: use %in% to check if addresses in one column of combine2 are contained in another column

combine2 <- combine %>%
    group_by(Owner) %>%
    tally(sort = TRUE) %>%
    ungroup() %>%
    mutate(
        nn = 1
    ) %>%
    pivot_wider(names_from = n, values_from = nn)


# step 3: split out columns 1,2,3,4

combine2$Owner[1:54] %>% view()   # 4 -- 54

combine2$Owner[55:104] %>% view() # 3 -- 50

combine2$Owner[105:175] %>% view() # 2 -- 71

combine2$Owner[176:338] %>% view() # 1 -- 163

# Save vector to a variable
one <- combine2$Owner[176:338]
one2 <- combine2$Owner[176:338]

# all TRUE
one %in% one2


two <- combine2$Owner[105:175]

# True (should be in two)
'0xc3464cff62431e7bc561fd46fae981206a6220a5' %in% two

# True (should be in one)
'0x94adb25a1e5232bd69ffc9c16d728372c3b8730c' %in% one

# What's in two *should* be in one
# But is NOT
'0xc3464cff62431e7bc561fd46fae981206a6220a5' %in% one

# group_by collapses instances where we'd expect to see an address 2,3 or 4 into ONE address
# after group_by, there won't be overlap between the groupings (those with one vs two POAPs)
# to test '%in%' we must use the original columns df, df2, df3, df4

# CC1 -> CC2   163 - 71, expect TRUE: 71, FALSE: 92

# Fundamental Problem -> Some People Claims CC1 *after* CC2 had started (v. late claimers)
# SOLUTION: Arrange in Desc by `Claim Date`, then artificially create bins based on dates


# OR Occam's Razor, see discrepancy between those with 3 POAP vs 4 POAPs
# WHO has FOUR CCs, but NOT THREE CCs POAPs



table_count <- combine %>%
    count(Owner) %>%
    rename(
        num_appear = n
    )

# DO a Table Join

left_join(table_count, combine, by = 'Owner') 




four <- combine2$Owner[1:54]   # -- appear four times

three <- combine2$Owner[55:104] # -- should appear 50 times


four %in% combine$Owner # checks out 54 true
three %in% combine$Owner # checks out 50 true
two %in% combine$Owner # checks out 71 true
one %in% combine$Owner # checks out 163

three %in% four

combine %>%
    arrange(desc(`Claim Date`)) %>% 
    
    combine %>%
    group_by(Owner) %>%
    count()

# Fundamental Problem -> Some People Claims CC1 *after* CC2 had started (v. late claimers)
# re-create c1-4, with ID, then count




# What does add up is POAPs claimed by Date adds up to combine of n = 671

one_two <- c1$Owner %in% c2$Owner

length(one_two[one_two==FALSE])  #95

sum(one_two) # another way to count
table(one_two)["FALSE"] # another way to count




# step 4: use %in% to check if addresses in one column of combine2 are contained in another column

# CC1 -> CC2   163 - 71, expect TRUE: 71, FALSE: 92
combine2$Owner[176:338] %in% combine2$Owner[105:175]


combine2$Owner[1:54] %in% combine2$Owner[1:54]

combine2$Owner[1:54] %in% combine2$Owner[55:104] 

combine2$Owner[55:104] %in% combine2$Owner[105:175]


    