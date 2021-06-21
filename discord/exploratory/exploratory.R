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

# 1 combine doa-wide data individually, then plot together
# 2 combine three channel plots together
# 3 list all major channels, create a vector of those names, filter by vector
# 4 plot all variables for the top-10 channels: readers, chatters, messages
# TBD -- do this later -- (Top: Research, Legal, Design, AV, Translator, Marketing, Writer's, Education, Developer, Analytics, Ops, Treasury)

# 1. research-general   Research Guild
# 2. general-legal          Legal Guild
# 3. design                    Design Guild
# 4. av-general              AV Guild
# 5. translation-general   Translator’s Guild
# 6. marketing-general    Marketing Guild
# 7. writer-general           Writer’s Guild
# 8. values                       Education Guild
# 9. onboard                    Education Guild
# 9. dev-guild                   Developer’s Guild
# 10. analytics                  Analytics Guild
# 11. ops-general             OPS Guild
# 12. treasury                   Treasury Guild


# NOTE: At the moment, unclear how to interpret total membership in relation to new_members, visitors, pct_retained,
# so we'll explore each variable separately


df %>%
    left_join(df1, by = "interval_start_timestamp") %>%
    left_join(df2, by = "interval_start_timestamp") %>%
    left_join(df3, by = "interval_start_timestamp") %>%
    select(interval_start_timestamp, total_membership, new_members, visitors, speaking_minutes) %>%
    pivot_longer(!interval_start_timestamp, names_to = "category", values_to = "count") %>%
    ggplot(aes(x = interval_start_timestamp, y = count, color = category)) +
    geom_line(size = 2) +
    theme_minimal() +
    theme(
        legend.position = "bottom"
    ) +
    labs(
        title = "Bankless DAO discord at-a-glance",
        subtitle = "May, 2021",
        x = "",
        y = "",
        caption = "Data: Bankless DAO | @frogmonkee | Analytics: @paulapivat"
    )







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


# Compare Total Membership & Speaking Minutes
df %>%
    left_join(df3, by = "interval_start_timestamp") %>%
    pivot_longer(!interval_start_timestamp, names_to = "category", values_to = "count") %>%
    ggplot(aes(x = interval_start_timestamp, y = count, fill = category)) +
    geom_bar(position = "dodge", stat = "identity")


# Compare Total membership, New members, Visitors
df %>%
    left_join(df1, by = "interval_start_timestamp") %>%
    left_join(df2, by = "interval_start_timestamp") %>%
    select(interval_start_timestamp, total_membership, visitors, new_members) %>%
    pivot_longer(!interval_start_timestamp, names_to = "category", values_to = "count") %>%
    ggplot(aes(x = interval_start_timestamp, y = count, fill = category)) +
    geom_bar(position = "fill", stat = "identity")



# ----------------- APPENDIX -------------------- #

# Try modern text features tidyverse
emojis <- "👩🏾‍💻🔥📊"

p <- ggplot() + 
    geom_label(
        aes(x = 0, y = 0, label = emojis), 
        family = "Apple Color Emoji"
    )

preview_devices(p, "emoji")


