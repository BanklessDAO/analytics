# library
library(tidyverse)

# load raw data

df <- read_csv("../raw/guild-total-membership.csv") 
df1 <- read_csv("../raw/guild-retention.csv")
df2 <- read_csv("../raw/guild-communicators.csv")
df3 <- read_csv("../raw/guild-voice-activity.csv")
df4 <- read_csv("../raw/popular-text-channels.csv")

# guild total membership
df %>%
    ggplot(aes(x = interval_start_timestamp, y = total_membership)) +
    geom_col()

# guild retention (new members)
df1 %>%
    ggplot(aes(x = interval_start_timestamp, y = new_members)) +
    geom_col()

# guild visitors / communicators (pct)
df2 %>%
    ggplot(aes(x = interval_start_timestamp, y = pct_communicated)) +
    geom_col()

# guild voice activity (speaking minutes)
df3 %>%
    ggplot(aes(x = interval_start_timestamp, y = speaking_minutes)) +
    geom_col()

# popular text channels (SINGLE DATE time-stamp)
df4 %>%
    select(channel_name, messages) %>%
    ggplot(aes(x = messages, y = reorder(channel_name, messages))) +
    geom_col()

