# load library ----
library(tidyverse)

# load data ----
p1 <- read_csv("./raw_data/snapshot-report-12389500.csv")
p2 <- read_csv("./raw_data/snapshot-report-12381760.csv")
p3 <- read_csv("./raw_data/snapshot-report-12414778.csv")
p4 <- read_csv("./raw_data/snapshot-report-12597085.csv")
p5 <- read_csv("./raw_data/snapshot-report-12655510.csv")
p6 <- read_csv("./raw_data/snapshot-report-12742069.csv")
p7 <- read_csv("./raw_data/snapshot-report-12822029.csv")
p8 <- read_csv("./raw_data/snapshot-report-12921898.csv")
p9 <- read_csv("./raw_data/snapshot-report-13238616.csv")
p10 <- read_csv("./raw_data/snapshot-report-13239761.csv")

# data wrangling ----

# select two columns needed (address, balance $BANK)
# add column proposal number
# add column proposal full name
# save as new data frame
# join into one data frame

df1 <- p1 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 1",
        name = "Approve the Bankless DAO Genesis Proposal"
    )

df2 <- p2 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 2",
        name = "What charity should CMS Holdings donate 100k towards"
    )

df3 <- p3 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 3",
        name = "Badge Distribution for Second Airdrop"
    )


df4 <- p4 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 4",
        name = "Reward Season 0 Active Members"
    )


df5 <- p5 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 5",
        name = "Bankless DAO Season 1"
    )


df6 <- p6 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 6",
        name = "BanklessDAO Season 1 Grants Committee Ratification"
    )

df7 <- p7 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 7",
        name = "BED Index Logo Contest"
    )

df8 <- p8 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 8",
        name = "Request for funds for Notion's ongoing subscription"
    )


df9 <- p9 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 9",
        name = "Transfer ownership of the treasury multisig wallet from the genesis team to the DAO"
    )


df10 <- p10 %>%
    select(address, balance) %>%
    mutate(
        num = "proposal 10",
        name = "Bankless DAO Season 2"
    )

# combine new data frames ----

new <- rbind(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10) 

# visualize ----

# specify factor order (proposal #'s)
library(forcats)

# manually arranging factors - num
# note: move "proposal 10" to the end
# them apply newly arranged factor levels to column of interest
new$num <- fct_relevel(new$num, c("proposal 1", "proposal 2", "proposal 3", "proposal 4", "proposal 5", 
                       "proposal 6", "proposal 7", "proposal 8", "proposal 9", "proposal 10"))


# manually arrange factors - name
# then apply newly arranged factor levels to column of interest
new$name <- fct_relevel(new$name, c("Approve the Bankless DAO Genesis Proposal",
                        "What charity should CMS Holdings donate 100k towards",
                        "Badge Distribution for Second Airdrop",
                        "Reward Season 0 Active Members",
                        "Bankless DAO Season 1",
                        "BanklessDAO Season 1 Grants Committee Ratification",
                        "BED Index Logo Contest",
                        "Request for funds for Notion's ongoing subscription",
                        "Transfer ownership of the treasury multisig wallet from the genesis team to the DAO",
                        "Bankless DAO Season 2"))

# visualize num addresses vote ----

new %>%
    count(name) %>%
    ggplot(aes(x = n, y = name, fill = name)) +
    geom_col() +
    geom_text(aes(label = n), hjust = -0.2, color = "white") +
    theme(
        legend.position = "none",
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
    scale_y_discrete(limits = rev(levels(new$name))) +
    scale_fill_manual(values = c("#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2", 
                                 "#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2")) +
    labs(
        title = "Member Participation in Snapshot Votes",
        subtitle = "Season 0 - Season 1",
        y = "",
        x = "Number of Addresses"
    )
    
    
# visualize BANK balance vote ----

new %>%
    group_by(name) %>%
    summarize(sum = sum(balance)) %>%
    ggplot(aes(x = sum, y = name, fill = name)) +
    geom_col() +
    geom_text(aes(label = sprintf("%0.0f", round(sum, digits = 2))), hjust = 1, color = "#65737e") +
    theme(
        legend.position = "none",
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
    scale_y_discrete(limits = rev(levels(new$name))) +
    scale_x_continuous(labels = scales::comma) +
    scale_fill_manual(values = c("#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2", 
                                 "#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2", "#ffb2b2")) +
    labs(
        title = "BANK Allocated to Snapshot Votes",
        subtitle = "Season 0 - Season 1",
        y = "",
        x = "Amount of BANK"
    )

# get rid of scientific notation
options(scipen=999)

# visualize governance participation ----

gov_partcipation <- new %>%
    count(address, sort = TRUE) %>%
    count(n)

gov_partcipation %>%
    ggplot(aes(x = n, y = nn)) +
    geom_col(aes(fill = as.factor(n))) +
    geom_text(aes(label = nn), vjust = -0.5, color = "white") +
    scale_x_continuous(breaks=seq(1,10, 1)) +
    scale_fill_manual(values = c("#b20000", "#e50000", "#ff0000", "#ff4c4c", "#ff6666",
                                 "#ff7f7f", "#ff9999", "#ffb2b2", "#ffcccc", "#ffe5e5")) +
    theme(
        legend.position = "none",
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
        title = "Participation in Governance",
        subtitle = "Snapshot Proposals 1-10",
        x = "Proposals",
        y = "Number of Addresses"
    )

