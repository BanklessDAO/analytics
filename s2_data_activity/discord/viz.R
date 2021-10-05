# load library ----
library(tidyverse)

# load data ----
new_member <- read_csv("./raw_data/new-member-joins-by-source_290921.csv")
total_member <- read_csv("./raw_data/total-membership-joins_290921.csv")
first_activation <- read_csv("./raw_data/first-day-activation_290921.csv")
next_retention <- read_csv("./raw_data/next-week-retention_290921.csv")
visit_comm <- read_csv("./raw_data/visitors-communicators_290921.csv")
msg_avg <- read_csv("./raw_data/message-avg-msg_290921.csv")

# visualize new_member ----

# pivot longer
# fill by factor
# stacked bar chart
# geom_text
# bankless color scheme

new_member %>%
    rename(
        vanity = "vanity_joins",
        discovery = "discovery_joins",
        time = "interval_start_timestamp"
    ) %>%
    pivot_longer(cols = discovery:vanity, names_to = "channel", values_to = "count") %>%
    ggplot(aes(x = time, y = count, fill = channel)) +
    geom_bar(position = "stack", stat = "identity") +
    geom_text(aes(label = count), position = position_stack(vjust = 0.5), color = "white") +
    theme(
        legend.position = "bottom",
        legend.background = element_rect(fill = "#65737e"),
        legend.text = element_text(color = "white"),
        legend.title = element_text(color = "white"),
        panel.background = element_rect(fill = "#65737e"),
        panel.grid.major = element_line(color = "#65737e"),
        panel.grid.minor = element_line(color = "#65737e"),
        plot.background = element_rect(fill = "#65737e"),
        axis.text.x = element_text(color = "white"),
        axis.text.y = element_text(color = "white"),
        axis.title.x = element_text(color = "white"),
        axis.title.y = element_text(color = "white"),
        title = element_text(color = "white", face = "bold")
    ) +
    scale_fill_manual(values = c("white", "red", "black")) +
    labs(
        title = "How many new members are joining?",
        subtitle = "Where are they coming from?",
        y = "Joins",
        x = ""
    )

# visualize total_member ----

# basic line chart
# bankless color scheme


# visualize first day activation ----

# pivot longer - no need for double y-axis
# two-sided Y-axis
# two lines + bar chart
# one hard coded line (benchmark)
# bankless color scheme

first_activation %>%
    rename(
        time = "interval_start_timestamp",
        new = "new_members",
        talked = "pct_communicated",
        visited = "pct_opened_channels"
    ) %>%
    ggplot(aes(x = time)) +
    geom_bar(aes(y = new, color = "New members"), stat = "identity", fill = "black") +
    geom_line(aes(y = talked*15, color = "% talked (voice or text)"), size = 1.5) +
    geom_line(aes(y = visited*15, color = "% visited more than 3 channels"), size = 1.5) +
    geom_line(y = 480, color = "orange", size = 0.2) +
    scale_y_continuous(
        name = "New Members",
        sec.axis = sec_axis(trans = ~./1500*100, name = "% Activated")
    ) +
    scale_color_manual(values = c("white", "red", "black")) +
    theme(
        legend.position = "bottom",
        legend.background = element_rect(fill = "#65737e"),
        legend.text = element_text(color = "white"),
        legend.title = element_text(color = "white"),
        panel.background = element_rect(fill = "#65737e"),
        panel.grid.major = element_line(color = "#65737e"),
        panel.grid.minor = element_line(color = "#65737e"),
        plot.background = element_rect(fill = "#65737e"),
        axis.text.x = element_text(color = "white"),
        axis.text.y = element_text(color = "white"),
        axis.title.x = element_text(color = "white"),
        axis.title.y = element_text(color = "white"),
        title = element_text(color = "white", face = "bold")
    ) +
    labs(
        title = "How many new members successfully activate on their first day?",
        x = "",
        color = "Legend"
    )

# visualize next week retention ----

# pivot longer - no need for double y-axis
# two-sided Y-axis
# one line + bar chart
# one hard coded line (benchmark)
# bankless color scheme

next_retention %>%
    rename(
        time = "interval_start_timestamp",
        new = "new_members",
        retained = "pct_retained"
    ) %>%
    ggplot(aes(x = time)) +
    geom_bar(aes(y = new, color = "New members"), stat = "identity", fill = "black") +
    geom_line(aes(y = retained*15, color = "Week 1 retention"), size = 1.5) +
    geom_line(y = 320, color = "orange", size = 0.2) +
    scale_y_continuous(
        name = "New Members",
        sec.axis = sec_axis(trans = ~./1500*100, name = "Week 1 retention")
    ) +
    scale_color_manual(values = c("black", "red")) +
    theme(
        legend.position = "bottom",
        legend.background = element_rect(fill = "#65737e"),
        legend.text = element_text(color = "white"),
        legend.title = element_text(color = "white"),
        panel.background = element_rect(fill = "#65737e"),
        panel.grid.major = element_line(color = "#65737e"),
        panel.grid.minor = element_line(color = "#65737e"),
        plot.background = element_rect(fill = "#65737e"),
        axis.text.x = element_text(color = "white"),
        axis.text.y = element_text(color = "white"),
        axis.title.x = element_text(color = "white"),
        axis.title.y = element_text(color = "white"),
        title = element_text(color = "white", face = "bold")
    ) +
    labs(
        title = "How many new members retain the next week?",
        x = "",
        color = "Legend"
    )

# visualize Visitors & Communicators ----

# pivot longer - no need for double y-axis
# two-sided Y-axis
# one line + bar chart
# one hard coded line (benchmark)
# bankless color scheme

visit_comm %>%
    rename(
        time = "interval_start_timestamp",
        comm = "pct_communicated"
    ) %>%
    ggplot(aes(x = time)) +
    geom_bar(aes(y = visitors, color = "Visitors"), stat = "identity", fill = "black") +
    geom_line(aes(y = comm*30, color = "% communicators"), size = 1.5) +
    geom_line(y = 1200, color = "orange", size = 0.2) +
    scale_y_continuous(
        name = "Visitors",
        sec.axis = sec_axis(trans = ~./3000*100, name = "% Communicators")
    ) +
    scale_color_manual(values = c("red", "black")) +
    theme(
        legend.position = "bottom",
        legend.background = element_rect(fill = "#65737e"),
        legend.text = element_text(color = "white"),
        legend.title = element_text(color = "white"),
        panel.background = element_rect(fill = "#65737e"),
        panel.grid.major = element_line(color = "#65737e"),
        panel.grid.minor = element_line(color = "#65737e"),
        plot.background = element_rect(fill = "#65737e"),
        axis.text.x = element_text(color = "white"),
        axis.text.y = element_text(color = "white"),
        axis.title.x = element_text(color = "white"),
        axis.title.y = element_text(color = "white"),
        title = element_text(color = "white", face = "bold")
    ) +
    labs(
        title = "How many members visited and communicated?",
        x = "",
        color = "Legend"
    )

# visualize message avg msg ----

# pivot longer - no need for double y-axis
# two-sided Y-axis
# one line + bar chart
# one hard coded line (benchmark)
# bankless color scheme

msg_avg %>%
    rename(
        time = "interval_start_timestamp",
        per = "messages_per_communicator"
    ) %>%
    ggplot(aes(x = time)) +
    geom_bar(aes(y = messages, color = "Messages sent"), stat = "identity", fill = "black") +
    # conversion between two y-axis (similar to % conversion)
    geom_line(aes(y = per*6000/12, color = "Messages per communicator"), size = 1.5) +
    geom_line(y = 5000, color = "orange", size = 0.2) +
    scale_y_continuous(
        name = "Messages sent",
        sec.axis = sec_axis(trans = ~./6000*12, name = "Message per ommunicator")
    ) +
    scale_color_manual(values = c("red", "black")) +
    theme(
        legend.position = "bottom",
        legend.background = element_rect(fill = "#65737e"),
        legend.text = element_text(color = "white"),
        legend.title = element_text(color = "white"),
        panel.background = element_rect(fill = "#65737e"),
        panel.grid.major = element_line(color = "#65737e"),
        panel.grid.minor = element_line(color = "#65737e"),
        plot.background = element_rect(fill = "#65737e"),
        axis.text.x = element_text(color = "white"),
        axis.text.y = element_text(color = "white"),
        axis.title.x = element_text(color = "white"),
        axis.title.y = element_text(color = "white"),
        title = element_text(color = "white", face = "bold")
    ) +
    labs(
        title = "Message Activity",
        x = "",
        color = "Legend"
    )

