library(tidyverse)

# load data
df <- read_csv("onboard_survey_open_ended.csv")

# reorder columns

col_order <- c("walletwhat", 
               "walletwhat_walletwhy", 
               "wallet_pain", 
               "defiwhat", 
               "defiwhat_defiwhy", 
               "defi_pain", 
               "defi_outcome", 
               "defi_interest", 
               "defi_endgame", 
               "defi_when")

df2 <- df[, col_order]

# Change individual values in "walletwhat" & "defiwhat"

df2$walletwhat[df2$walletwhat == 'coinbasei'] <- 'coinbase'
df2$walletwhat[df2$walletwhat == 'httpswwwmyetherwalletcom'] <- 'myetherwallet'
df2$walletwhat[df2$walletwhat == 'mew'] <- 'myetherwallet'
df2$walletwhat[df2$walletwhat == 'trust'] <- 'trustwallet'

df2$defiwhat[df2$defiwhat == 'uniswapi'] <- 'uniswap'
df2$defiwhat[df2$defiwhat == 'uni'] <- 'uniswap'
df2$defiwhat[df2$defiwhat == 'makerdao'] <- 'maker'
df2$defiwhat[df2$defiwhat == 'compund'] <- 'compound'


# First Wallet tally
df2 %>%
    select(walletwhat) %>%
    group_by(walletwhat) %>%
    tally(sort = TRUE) %>% view()


# First Defi App tally
df2 %>%
    select(defiwhat) %>%
    group_by(defiwhat) %>%
    tally(sort = TRUE) %>% view()


# visualize wallets
df2 %>%
    select(walletwhat, defiwhat) %>%
    group_by(walletwhat) %>%
    tally(sort = TRUE) %>%
    ggplot(aes(x = n, y = reorder(walletwhat, n))) +
    geom_col()

# visualize defi apps used
df2 %>%
    select(walletwhat, defiwhat) %>%
    group_by(walletwhat) %>%
    tally(sort = TRUE) %>%
    ggplot(aes(x = n, y = reorder(walletwhat, n))) +
    geom_col()

# visualize defi when
df2 %>%
    select(defi_when) %>%
    group_by(defi_when) %>%
    tally(sort = TRUE)



