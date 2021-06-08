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
    geom_area(aes(x = date, y = impressions), fill = "pink")


# engagements
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot() +
    geom_area(aes(x = date, y = engagements), fill = "light blue")


# impressions & engagements
df %>%
    select(1:4) %>%
    rename(
        num_tweets = `Tweets published`,
        date = `Date`
    ) %>%
    ggplot(aes(x = impressions, y = engagements)) +
    geom_point() +
    geom_smooth(method = "lm")

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
    scale_fill_gradientn(colors = c("#FFEDA0", "#FEB24C", "#F03B20"))
    
# reshape data (pivot_longer)
# works with geom_line, not geom_col or geom_bar

df %>% 
    select(1, 3:4) %>%
    rename(
        date = `Date`
    ) %>%
    pivot_longer(!date, names_to = 'variable', values_to = 'number') %>%
    ggplot(aes(x = date, y = number, color = variable)) +
    geom_line() +
    # change y-axis to logarithm scale
    scale_y_log10()

# remove scientific notation
options(scipen=999)

