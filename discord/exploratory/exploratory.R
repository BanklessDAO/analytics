# library
library(tidyverse)

# new library for emoji
install.packages("emojifont")
library(emojifont)

# NOTE: UNABLE TO DISPLAY EMOJIs.
library(ggtext)
# install.packages("emo") ‘emo’ is not available (for R version 4.0.2)
remotes::install_github("hadley/emo")
library(emo)

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
# arrange in descending order by number of messages

# ----------- DISCORD CHANNELS ----------------#

# unable to print out Emojis

# Top 30 Discord Channels by Messages
# note: duplicate - "general", one is in archive
# note: By Date: 2021-06-08


df4 %>%
    select(channel_name, messages) %>%
    slice(1:30) %>% 
    arrange(desc(messages)) %>% 
    ggplot(aes(x = messages, y = reorder(channel_name, messages), fill = channel_name)) +
    geom_col() +
    geom_text(aes(label = messages), hjust = -0.1) +
    theme_minimal() +
    theme(
        legend.position = "none"
    ) +
    labs(
        title = "Top 30 Discord Channels by Messages",
        subtitle = "Bankless DAO (by June 8th)",
        caption = "Data: BanklessDAO | @frogmonkee | Analytics: @paulapivat",
        y = "Channels",
        x = "Number of Messages"
    )


# Top 30 Discord Channels by Readers
df4 %>%
    select(channel_name, readers) %>%
    slice(1:30) %>% 
    arrange(desc(readers)) %>% 
    ggplot(aes(x = readers, y = reorder(channel_name, readers), fill = channel_name)) +
    geom_col() +
    geom_text(aes(label = readers), hjust = -0.1) +
    theme_minimal() +
    theme(
        legend.position = "none"
    ) +
    labs(
        title = "Top 30 Discord Channels by Readers",
        subtitle = "Bankless DAO (by June 8th)",
        caption = "Data: BanklessDAO | @frogmonkee | Analytics: @paulapivat",
        y = "Channels",
        x = "Number of Readers"
    )


df4 %>%
    select(channel_name, chatters) %>%
    slice(1:30) %>% 
    arrange(desc(chatters)) %>% 
    ggplot(aes(x = chatters, y = reorder(channel_name, chatters), fill = channel_name)) +
    geom_col() +
    geom_text(aes(label = chatters), hjust = -0.1) +
    theme_minimal() +
    theme(
        legend.position = "none"
    ) +
    labs(
        title = "Top 30 Discord Channels by Chatters",
        subtitle = "Bankless DAO (by June 8th)",
        caption = "Data: BanklessDAO | @frogmonkee | Analytics: @paulapivat",
        y = "Channels",
        x = "Number of Chatters"
    )


# ----------------- APPENDIX ----------------- #

# Try modern text features tidyverse
emojis <- "👩🏾‍💻🔥📊"

p <- ggplot() + 
    geom_label(
        aes(x = 0, y = 0, label = emojis), 
        family = "Apple Color Emoji"
    )

preview_devices(p, "emoji")


