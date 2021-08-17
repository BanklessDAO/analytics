library(dplyr) #data manipulation and query 
library(dbplyr) #use dplyr in databases
library(magrittr)# piping function %>% 
library(igraph) #network analysis 
library(psych) #statistical analysis
library(janitor) #data cleaning
library(DBI) #query public bigquery dataset
library(odbc)
library(bigrquery)

### NOTE: If not set up with a google cloud service account will need to query public bigquery dataset. 

con <- dbConnect(
  bigrquery::bigquery(),
  project = "publicdata",
  dataset = "crypto_ethereum"
)

#> <Big
source("BANK_token_transfers/helper_functions/get_network_stats.R") #helper functions for network analysis. This should be in your working directory or full path.

sql <- "SELECT from_address, to_address, value, transaction_hash, block_timestamp, block_number
FROM `bigquery-public-data.crypto_ethereum.token_transfers` 
WHERE token_address = '0x2d94aa3e47d9d5024503ca8491fce9a2fb4da198'"
# create pointer table to query bigquery to pull BANK token transfers
bank_token_transfers <-  tbl(con, "crypto_ethereum.token_transfers") #will need to authenticate with google cred
bank_token_transfers <- dbGetQuery(con, sql)

#query data and convert to igraph object for network analysis. data is in memory
token_transfer_graph <- bank_token_transfers %>%
  select(from_address, to_address, value) %>%
  igraph::graph_from_data_frame()


# apply helper function
df <- get_node_stats(token_transfer_graph)
df$address <- rownames(df) #create col name based on row names. 

#conduct cluster analysis on network 
uttg <- as.undirected(token_transfer_graph)
clusters <- igraph::cluster_louvain(uttg)

#assign clusters to col variable in df
df$clusters <- clusters$membership

#get values of total sent and total received
edge_df <- igraph::as_long_data_frame(token_transfer_graph)
`colnames<-`(edge_df, c("from","to", "bank_value", "sending_address", "receiving_address")) -> edge_df
edge_df$bank_value <- round(as.numeric(edge_df$bank_value), 2)

total_sent <- edge_df %>%
  select(sending_address, bank_value) %>%
  group_by(sending_address) %>%
  summarise("total_bank_sent" = sum(bank_value))
total_received <- edge_df %>%
  select(receiving_address, bank_value) %>%
  group_by(receiving_address) %>%
  summarise("total_bank_received" = sum(bank_value))

# df <- left_join(df,total_received, b = c("address" = "receiving_address")) %>%
#   left_join(total_sent, b = c("address" = "sending_address")) %>%
#   mutate("token_transfer_ratio" = df$out_degree-df$in_degree) %>%
#   mutate("token_value_ratio" = df$total_bank_sent-df$total_bank_received)

df <- left_join(df,total_received, b = c("address" = "receiving_address")) %>%
  left_join(total_sent, b = c("address" = "sending_address"))

df <- clean_names(df)

write.csv(df, "BANK_token_transfers/data/BANK_token_transfer_network_health.csv")
