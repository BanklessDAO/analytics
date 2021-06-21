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

# ----------- Exploratory DAO WIDE  ----------------#

# NOTE: At the moment, unclear how to interpret total membership in relation to new_members, vistors, pct_retained,
# so we'll explore each variable separately


# Try compare Total Membership & Speaking Minutes
df %>%
    left_join(df3, by = "interval_start_timestamp") %>%
    pivot_longer(!interval_start_timestamp, names_to = "category", values_to = "count") %>%
    ggplot(aes(x = interval_start_timestamp, y = count, fill = category)) +
    geom_bar(position = "dodge", stat = "identity")


# Try Total membership, New members, Visitors
df %>%
    left_join(df1, by = "interval_start_timestamp") %>%
    left_join(df2, by = "interval_start_timestamp") %>%
    select(interval_start_timestamp, total_membership, visitors, new_members) %>%
    pivot_longer(!interval_start_timestamp, names_to = "category", values_to = "count") %>%
    ggplot(aes(x = interval_start_timestamp, y = count, fill = category)) +
    geom_bar(position = "fill", stat = "identity")


df1
df2
df3


# ----------- Exploratory DISCORD CHANNELS ----------------#

# unable to print out Emojis

# Top 30 Discord Channels by Messages
# note: arrange before slice
# note: duplicate - "general", one is in archive
# note: By Date: 2021-06-08

df4 %>%
    select(channel_name, messages) %>%
    # note: arrange before slice
    arrange(desc(messages)) %>%
    slice(1:30) %>%
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
    # note: arrange before slice
    arrange(desc(readers)) %>% 
    slice(1:30) %>% 
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

# Top 30 Discord Channels by Chatters
df4 %>%
    select(channel_name, chatters) %>%
    # note: arrange before slice
    arrange(desc(chatters)) %>% 
    slice(1:30) %>% 
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


# ----------------- Parking Lot ----------------- #




# ----------------- APPENDIX -------------------- #

# Try modern text features tidyverse
emojis <- "👩🏾‍💻🔥📊"

p <- ggplot() + 
    geom_label(
        aes(x = 0, y = 0, label = emojis), 
        family = "Apple Color Emoji"
    )

preview_devices(p, "emoji")


