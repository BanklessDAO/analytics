# load libraries
library(tidyverse)
library(lubridate) # reformat timestamp for tweet metrics analysis

# load daily tweet data (numeric)
df <- read_csv("../raw/daily_tweet_activity_metrics_banklessDAO_20210508_20210608_en.csv")
df2 <- read_csv("../raw/daily_tweet_activity_metrics_banklessDAO_20210605_20210703_en.csv")

# load tweet activity metrics (string)
df3 <- read_csv("../raw/tweet_activity_metrics_banklessDAO_20210605_20210703_en.csv")
df4 <- read_csv("../raw/tweet_activity_metrics_banklessDAO_20210508_20210608_en.csv")


# Exploratory: Broad
df %>% summary()
df %>% str()
df %>% dim()
df %>% names()

# Exploratory: Date, Tweets Published, Impressions, Engagements

# impressions [check] May 8th - June 7th 2021
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
    


# engagements [check]
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


# impressions & engagements [check]
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

# Different geometry and change in gradient color [check]
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

# y-axis normal scale [check]
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

# y-axis log-scale [check]
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


# breakdown engagement into sub-components and chart stacked area graph [check]
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


# try ggridges next - multiple histograms [check]
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
    
########----------------------- June 5th, 2021 / June 7th - July 2nd, 2021 -----------------------#########

### NOTE: remove Last Three Rows from last month's data to prevent overlap with New raw data - slice off June 5 - 7th
df1a <- df %>%
    slice(1:28)


# RBIND df1a + df2 to combine datasets with no overlapping dates
# Use newer version of June 5-7

df2a <- rbind(df1a, df2)

# impressions May 8th - July 2nd, 2021
df2a %>%
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
        subtitle = "May 8th - July 2nd, 2021",
        x = "",
        y = "Impressions",
        caption = "Data: Twitter, @frogmonkee | Analytics: @paulapivat"
    )
    

# engagements May 8th - July 2nd, 2021
df2a %>%
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
        subtitle = "May 8th - July 2th, 2021",
        x = "",
        y = "Engagements",
        caption = "Data: Twitter, @frogmonkee | Analytics: @paulapivat"
    )


# impressions & engagements Relationship May 8th - July 2nd, 2021
df2a %>%
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
        title = "Bankless DAO Twitter Metrics (May - June, 2021)",
        subtitle = "Relationship between Engagement & Impressions",
        x = "Impressions",
        y = "Engagements",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )

# How Most Tweets are Performing (June, 2021),
# Different geometry and change in gradient color
# NOTE: df2 NOT df2a

df2 %>%
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
        title = "Bankless DAO Twitter Activity",
        subtitle = "How most Tweets are performing from June 5th - July 2nd",
        x = "Impressions",
        y = "Engagements",
        caption = "Data: Twitter, @frogmonkee | Analytics: @paulapivat"
    )

# breakdown engagement into sub-components and chart stacked area graph May 8th - July 2nd, 2021
df2a %>%
    # engagement = function of (retweets, replies, likes, user profile clicks, url clicks, hashtags, detail expands, media view, media engagements)
    select(Date, retweets:`detail expands`, `media views`: `media engagements`) %>%
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
        subtitle = "May 8th - July 2nd 2021",
        x = "",
        y = "Count",
        caption = "Data: Twitter, @frogmonkee | Analytics: @paulapivat"
    )


# breakdown engagement with side-by-side bar charts for easier comparisons
df2a %>%
    # engagement = function of (retweets, replies, likes, user profile clicks, url clicks, hashtags, detail expands, media view, media engagements)
    select(Date, retweets:`detail expands`, `media views`: `media engagements`) %>%
    pivot_longer(!Date, names_to = "variable", values_to = "count") %>%
    ggplot(aes(x = Date, y = count, fill = variable)) +
    geom_col(position = "fill") +
    scale_x_date(date_breaks = '1 day') +
    theme_minimal() +
    theme(
        legend.position = "bottom",
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    labs(
        title = "Bankless DAO Twitter Engagement Breakdown (Percentage)",
        subtitle = "May 8th - July 2nd 2021",
        x = "",
        y = "Percentage",
        caption = "Data: Twitter, @frogmonkee | Analytics: @paulapivat"
    )




# try ggridges next - multiple histograms [check]
library(ggridges)


df2a %>%
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
        subtitle = "May - June 2021",
        x = "Count",
        y = "Various Engagement Metrics",
        caption = "Data: Twitter | Analytics: @paulapivat"
    )

###--------------------- How much is Daily Engagement correlated with Number of Daily Tweets? ---------------------###
### ~ 0.70 correlation !!!

cor(df2a$`Tweets published`, df2a$engagements)


###--------------------- Explore Tweets from Days with >1000 Engagement--------------------###

# NOTE: Dates with highest Engagement (> 1000) - NOT counting first 2 days (May 8 - 9)
# May - 28, 14, 12, 11, 10, 29, 17, 30, 18
# June - 4, 2, 1, 24, 9, 12, 11, 10, 13, 5

# Reformat TimeStamp to YYYY-MM-DD (remove hour/mins)
# Then can filter by Dates with highest Engagements

# Need to RBIND df3 and df4 - while avoiding overlap (same as above)
may <- df4 %>%
    slice(11:234) 

df5 <- rbind(df3, may) 

# FILTER for specific dates with highest overall engagement
# May - 28, 14, 12, 11, 10, 29, 17, 30, 18
# June - 4, 2, 1, 24, 9, 12, 11, 10, 13, 5
# NOTE: save as separate CSV for additional analyses
df5 %>%
    select(`Tweet permalink`,`Tweet text`, time, impressions, engagements, `engagement rate`) %>%
    mutate(
        date = as.Date(time)
    ) %>% 
    filter(date == as.Date("2021-05-28") | 
           date == as.Date("2021-05-14") |
           date == as.Date("2021-05-12") |
           date == as.Date("2021-05-11") |
           date == as.Date("2021-05-10") |
           date == as.Date("2021-05-29") |
           date == as.Date("2021-05-17") |
           date == as.Date("2021-05-30") |
           date == as.Date("2021-05-18") |
           date == as.Date("2021-06-04") |
           date == as.Date("2021-06-02") |
           date == as.Date("2021-06-01") |
           date == as.Date("2021-06-24") |
           date == as.Date("2021-06-09") |
           date == as.Date("2021-06-12") |
           date == as.Date("2021-06-11") |
           date == as.Date("2021-06-10") |
           date == as.Date("2021-06-13") |
           date == as.Date("2021-06-05")) %>%
    write_csv("tweets_on_days_with_highest_engagement.csv")
