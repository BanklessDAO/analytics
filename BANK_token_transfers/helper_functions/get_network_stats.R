library(igraph)
library(data.table)
library(purrr)
library(DT)


### --------To use these functions the following inputs are needed.  -------####
#read in igraph/graph. This is example dataset 
## The c arg must be a igraph object. can also use graph_from_() from other graph structures
##Creates a list of dataframes contain node statistics, centrality measures,..
##...This information can then be used in predictive models and...
##...further explore visually or testing distrubitions.
#many of these functions become far more useful when multiple time points of node id and edges is collected over time.

  get_node_stats <- function(c){
    
    InDegree <- igraph::degree(c, mode = "in")
    OutDegree <- igraph::degree(c, mode = "out")
    Total.Degree <- igraph::degree(c, mode = "total")
    Btw.Centrality <- igraph::betweenness(c)
    Closeness.Centrality <- igraph::closeness(c)
    Google_Pagerank <- igraph::page.rank(c)$vector
    
    g <- data.frame(
      
      "InDegree"=InDegree,
      "OutDegree"=OutDegree,
      "Total.Degree"=Total.Degree,
      "Btw.Centrality"=Btw.Centrality,
      "Closeness.Centrality"=Closeness.Centrality,
      "Google_Pagerank"=Google_Pagerank
      
    )
    
    return(g)
    
  }
  #create list of df in memory for dynamic network igraph objects
  dynamic_node_stats <- function(c){
    g <- purrr::map(c, get_node_stats)
    return(g)
    
  }
  
  
  
  #get node summary stats in dataframes for each node in igraph objects
  network_summary <- function(c){
    
    node_count <- igraph::vcount(c)
    edge_count <- igraph::ecount(c)
    Density <- igraph::graph.density(c)
    Avg.InDegree <- mean(igraph::degree(c, mode = "in"))
    Sd.InDegree <- sd(igraph::degree(c, mode = "in"))
    Avg.OutDegree <- mean(igraph::degree(c, mode = "out"))
    Sd.OutDegree <- sd(igraph::degree(c, mode = "out"))
    Avg.Btw.Centrality <- mean(igraph::betweenness(c))
    Sd.Btw.Centrality <- sd(igraph::betweenness(c))
    Avg.Closeness.Centrality <- mean(igraph::closeness(c))
    Sd.Closeness.Centrality <- sd(igraph::closeness(c))
    Avg.Google.Pagerank <- mean(igraph::page.rank(c)$vector)
    Sd.Google.Pagerank <- sd(igraph::page.rank(c)$vector)
    Avg.Power.Centrality <- mean(igraph::power_centrality(c))
    Sd.Power.Centrality <- sd(igraph::power_centrality(c))
    
    f <- data.frame(
      "node_count"=node_count,
      "edge_count"=edge_count,
      "Density"=Density,
      "Avg.InDegree"=Avg.InDegree,
      "Sd.InDegree"=Sd.InDegree,
      "Avg.OutDegree"=Avg.OutDegree,
      "Sd.OutDegree"=Sd.OutDegree,
      "Avg.Btw.Centrality"=Avg.Btw.Centrality,
      "Sd.Btw.Centrality"=Sd.Btw.Centrality,
      "Avg.Closeness.Centrality"=Avg.Closeness.Centrality,
      "Sd.Closeness.Centrality"=Sd.Closeness.Centrality,
      "Avg.Google.Pagerank"=Avg.Google.Pagerank,
      "Sd.Google.Pagerank"=Sd.Google.Pagerank,
      "Avg.Power.Centrality"=Avg.Power.Centrality,
      "Sd.Power.Centrality"=Sd.Power.Centrality
    )
    return(f)
  }
  
  #get a list of n df for each dynamic network time periond
  dynamic_network_summary <- function(f){
    f <- purrr::map(c, network_summary)
    return(f)#multiple igraph objects over time assuming c has more than 1 time point.
  } 
  
  
  #create a data table interactive for this information
  network_summary_table <- function(c){
    f <- network_summary(c)
    DT::datatable(f)
  }
  
  #create a data table interactive for this information
  dynamic_summary_table <- function(c){
    f <- purrr::map(c, network_summary)
    DT::datatable(data.table::rbindlist(f))
  }

