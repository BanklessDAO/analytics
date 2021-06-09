# load libraries
library(tidyverse)

# load data
df <- read_csv("../raw/daily_tweet_activity_metrics_banklessDAO_20210508_20210608_en.csv")

# Exploratory: Broad
df %>% summary()
df %>% str()
df %>% dim()
df %>% names()

# Exploratory: Date, Tweets Published, Impressions, Engagements

# impressions
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot() +
    geom_area(aes(x = date, y = impressions), fill = "pink") +
    scale_x_date(date_breaks = '1 day') +
    theme_minimal() +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    labs(
        title = "Bankless DAO Twitter Impressions",
        subtitle = "May 8th - June 7th, 2021",
        x = "",
        y = "Impressions",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )
    


# engagements
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot() +
    geom_area(aes(x = date, y = engagements), fill = "light blue") +
    scale_x_date(date_breaks = '1 day') +
    theme_minimal() +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    labs(
        title = "Bankless DAO Twitter Engagements",
        subtitle = "May 8th - June 7th, 2021",
        x = "",
        y = "Engagements",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )


# impressions & engagements
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot(aes(x = impressions, y = engagements)) +
    geom_point() +
    geom_smooth(method = "lm", se = FALSE) +
    theme_minimal() +
    labs(
        title = "Bankless DAO Twitter Metrics (May, 2021)",
        subtitle = "Relationship between Engagement & Impressions",
        x = "Impressions",
        y = "Engagements",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )
    
    

# impressions & engagements with color gradient
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot(aes(x = impressions, y = engagements, color = impressions)) +
    geom_point(size = 4) +
    scale_color_gradientn(colors = c("#00AFBB", "#E7B800", "#FC4E07"))
    
# rectangular binning
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot(aes(x = impressions, y = engagements)) +
    geom_bin2d(bins = 50, color = "white") +
    scale_fill_gradient(low =  "#00AFBB", high = "#FC4E07")+
    theme_minimal()

# Add 2d density estimation
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot(aes(x = impressions, y = engagements)) +
    geom_point(color = "lightgray") +
    geom_density_2d()

# Different geometry and change in gradient color
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot(aes(x = impressions, y = engagements)) +
    geom_point(color = "lightgray") +
    stat_density_2d(aes(fill = ..level..), geom = "polygon") + 
    scale_fill_gradientn(colors = c("#FFEDA0", "#FEB24C", "#F03B20")) +
    theme_minimal() +
    theme(
        legend.position = "none"
    ) +
    labs(
        title = "Bankless DAO Twitter Activity (May, 2021)",
        subtitle = "How most Tweets are performing",
        x = "Impressions",
        y = "Engagements",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )
    
# reshape data (pivot_longer)
# works with geom_line, not geom_col or geom_bar

# y-axis normal scale
df %>% 
    select(1, 3:4) %>%
    rename(
        date = `Date`
    ) %>%
    pivot_longer(!date, names_to = 'variable', values_to = 'number') %>%
    ggplot(aes(x = date, y = number, color = variable)) +
    geom_line(size = 1.2) +
    scale_x_date(date_breaks = '1 day') +
    theme_minimal() +
    theme(
        legend.position = "bottom",
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    labs(
        title = "Bankless DAO Twitter Impressions & Engagements Numbers (May, 2021)",
        subtitle = "Normal Scale (y-axis)",
        y = "Count",
        x = "",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )

# y-axis log-scale
df %>% 
    select(1, 3:4) %>%
    rename(
        date = `Date`
    ) %>%
    pivot_longer(!date, names_to = 'variable', values_to = 'number') %>%
    ggplot(aes(x = date, y = number, color = variable)) +
    geom_line(size = 1.2) +
    scale_x_date(date_breaks = '1 day') +
    # change y-axis to logarithm scale
    scale_y_log10() +
    theme_minimal() +
    theme(
        legend.position = "bottom",
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    labs(
        title = "Bankless DAO Twitter Impressions & Engagements Numbers (May, 2021)",
        subtitle = "Log Scale (y-axis)",
        y = "Count",
        x = "",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )





# remove scientific notation
options(scipen=999)

# See if (number) Tweets published is related to either Impressions or Engagement
df %>%
    select(1:4) %>%
    rename(
        date = Date,
        num = `Tweets published`
    ) %>%
    ggplot(aes(x = num, y = engagements)) +    #change to engagements
    geom_point() +
    geom_smooth(method = "lm")


# engagement only
df %>%
    select(Date, engagements) %>%
    ggplot(aes(x = Date, y = engagements)) +
    geom_area()


# breakdown engagement into sub-components and chart stacked area graph
df %>%
    select(Date, engagements, retweets:`detail expands`, `media views`: `media engagements`) %>%
    pivot_longer(!Date, names_to = "variable", values_to = "count") %>%
    ggplot(aes(x = Date, y = count, fill = variable)) +
    geom_area(stat = "identity", position = "stack") +
    scale_x_date(date_breaks = '1 day') +
    theme_minimal() +
    theme(
        legend.position = "bottom",
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    labs(
        title = "Bankless DAO Twitter Engagement Breakdown",
        subtitle = "May 2021",
        x = "",
        y = "Count",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )
    

    
    
    
    
# marginal distribution with ggplot2 and ggExtra
# impressions and engagements
library(ggExtra)

# basic scatter
p <- df %>%
    select(impressions, engagements) %>%
    ggplot(aes(x = impressions, y = engagements)) +
    geom_point() +
    theme(legend.position = "none")


ggMarginal(p, type = "histogram", size = 10)
ggMarginal(p, type="histogram", fill = "slateblue", xparams = list(  bins=10))
ggMarginal(p, margins = 'x', color="purple", size=4)


# Multi density chart

# basic density plot
df %>%
    select(Date, engagements) %>%
    ggplot(aes(y = engagements)) + 
    geom_density() +
    coord_flip()

# basic histogram

# sample dataframe
data.frame(
    type = c( rep("variable 1", 1000), rep("variable 2", 1000) ),
    value = c( rnorm(1000), rnorm(1000, mean=4) )
)

# impressions & engagement histogram on same axis
df %>%
    select(Date, engagements, impressions) %>%
    pivot_longer(!Date, names_to = "variable", values_to = "count") %>%
    select(variable, count) %>%
    ggplot(aes(x = count, fill = variable)) +
    geom_histogram(color="#e9ecef", alpha=0.6, position = 'identity') +
    scale_fill_manual(values=c("#69b3a2", "#404080"))


# try ggridges next - multiple histograms 
library(ggridges)


df %>%
    select(Date, engagements, retweets:`detail expands`, `media views`: `media engagements`) %>%
    pivot_longer(!Date, names_to = "variable", values_to = "count") %>%
    ggplot(aes(x = count, y = variable, fill = variable)) +
    geom_density_ridges() +
    theme_minimal() +
    theme(
        legend.position = "none"
    ) +
    labs(
        title = "Bankless DAO Twitter Various Engagement Metrics",
        subtitle = "May 2021",
        x = "Count",
        y = "Various Engagement Metrics",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )
    
    
    
    

