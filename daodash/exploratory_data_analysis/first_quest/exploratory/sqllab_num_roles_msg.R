# load libraries
library(tidyverse)

# load data ----
df <- read_csv("sqllab_num_roles_msg.csv")
df2 <- read_csv("time_firstquest_complete.csv")

# turn num_roles into categorical variables
# create categorical variable by converting dbl to chr
# note -content_count in reoder to reverse bars
df %>%
    mutate(
        num_roles_bin = as.character(num_roles)
    ) %>%
    filter(content_count > 100) %>%
    ggplot(aes(x = reorder(username, -content_count), y = content_count, fill = num_roles_bin)) +
    geom_col() +
    theme_minimal() +
    theme(
        legend.position = "bottom",
        axis.text.x = element_text(angle = 45, hjust = 1),
        panel.grid.major = element_line(colour = "white"),
        panel.grid.minor = element_line(colour = "white")
    ) +
    labs(
        title = "Members with over 100 Messages Sent",
        fill = "Number of First Quest Tags",
        y = "Number of Messages Sent",
        x = "Discord Handle",
        caption = "Data: DAO Dash | Viz: @paul_apivat"
    )
    


# Facet Wrap view
df %>%
    mutate(
        num_roles_bin = as.character(num_roles)
    ) %>%
    filter(content_count > 100) %>%
    ggplot(aes(x = reorder(username, num_roles_bin), y = content_count, fill = num_roles_bin)) +
    geom_col() +
    facet_wrap(~ num_roles_bin) +
    theme_minimal() +
    theme(
        legend.position = "bottom",
        axis.text.x = element_text(angle = 90, hjust = 1),
        panel.grid.major = element_line(colour = "white"),
        panel.grid.minor = element_line(colour = "white")
    ) +
    labs(
        title = "Members with over 100 Messages Sent",
        subtitle = "Segmented by Number of First Quest Tags",
        fill = "Number of First Quest Tags",
        y = "Number of Messages Sent",
        x = "Discord Handle",
        caption = "Data: DAO Dash | Viz: @paul_apivat"
    )

# Run correlation between num_roles and content_count
# correlation 0.07 95-CI: 0.02 - 0.12
# low correlation
cor.test(df$num_roles, df$content_count, method = c("pearson"))


# % of new members obtaining First Quest Complete ----

# Example ----

# example: create data

value1 <- abs(rnorm(26))*2
data <- data.frame(
    x=LETTERS[1:26], 
    value1=value1, 
    value2=value1+1+rnorm(26, sd=1) 
)

# lollipop chart with First Quest data ----
# May, June, July -- November
df2 %>%
    filter(month < 8) %>%
    ggplot() +
    geom_segment(aes(x=username, xend=username, y=month, yend=activated_at_month), color="grey") +
    geom_point(aes(x=username, y=month), color=rgb(0.2,0.7,0.1,0.5), size=3) +
    geom_point(aes(x=username, y=activated_at_month), color=rgb(0.7,0.2,0.1,0.5), size=3) +
    scale_y_continuous(breaks = seq(1,11, by = 1)) +
    coord_flip() +
    theme_minimal() +
    theme(
        panel.grid.major = element_line(colour = "white"),
        panel.grid.minor = element_line(colour = "white")
    ) +
    labs(
        title = "New Members Obtaining 'First Quest Complete'.",
        subtitle = "Discord Joins: May, June, July",
        x = "Discord Handle",
        y = "Month",
        caption = "Data: DAO Dash | Viz: @paul_apivat"
    )

# Aug, Sept, Oct -- November
df2 %>%
    filter(month > 7) %>%
    ggplot() +
    geom_segment(aes(x=username, xend=username, y=month, yend=activated_at_month), color="grey") +
    geom_point(aes(x=username, y=month), color=rgb(0.2,0.7,0.1,0.5), size=3) +
    geom_point(aes(x=username, y=activated_at_month), color=rgb(0.7,0.2,0.1,0.5), size=3) +
    scale_y_continuous(breaks = seq(1,11, by = 1)) +
    coord_flip() +
    theme_minimal() +
    theme(
        panel.grid.major = element_line(colour = "white"),
        panel.grid.minor = element_line(colour = "white")
    ) +
    labs(
        title = "New Members Obtaining 'First Quest Complete'.",
        subtitle = "Discord Joins: Aug, Sept, Oct",
        x = "Discord Handle",
        y = "Month",
        caption = "Data: DAO Dash | Viz: @paul_apivat"
    )


