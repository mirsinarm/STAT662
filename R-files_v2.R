# to make safer:
#   1.  First check to see if the name of the input file already exists.  If so, kill.
#   2.  Maybe append instead of create a new file???





int2string <- function(i) {  ##converts a number to base-26 starting on a = 1
  e <- floor(log(i, base = 26));
  string <- character(10)
  i <- i %% 26^10            ## loops back to 'a' after 'zzzzzzzzzz'
  for(j in 1:e){
    string[j] <- match(floor(i/26^(e-j+1)), letters);
    i <- i %% 26^(e-j+1)
  }
  return(string)
}



mat[i, 100] <- paste(int2string(i),collapse="")




bigMatrix <- function(rows, outfile) {
  # preferably this will take in a FILE SIZE and calculate the number of rows
  # however, for the moment, I'm just telling it how many rows:
  for(j in 1:(rows/1000)) {
#     print(paste("j = ", j, sep="")) # can use some sort of progress bar???
    smallMatrix(1000)
    system(paste("cat *.vampirerabbit >> ", outfile, ".csv", sep=""))
    system("rm *.vampirerabbit")
  }
  dir()
}



smallMatrix <- function(rows, write.file=TRUE) {
  mat <- matrix(nrow=rows, ncol=100)
  for(i in 1:rows) {
    mat[i, 1:97] <- sample(c(0.1, 0.2, 0.3), size=97, replace = TRUE) # numerics
    mat[i, 98] <- sample(-1:1, size=1) # integer
    mat[i, 99] <- sample(letters, size=1) # factor
    mat[i, 100] <- paste(sample(letters,10,replace=T),collapse="") # characters
  }
  
  if(write.file) {write.table(mat, "f.vampirerabbit", row.names=FALSE, col.names=FALSE)}
}

#####################################################################
###  To generate files, try the following code:
#####################################################################

# setwd("/Users/miranda/Desktop/2014-Fall/STAT662/homeworks/sandbox/")

# create a temporary directory to hold all your files, and move into it
system2("mkdir", args="temp")
setwd("temp")

system.time(bigMatrix(1000, "f0")) # baby matrix
system.time(bigMatrix(200000, "f1")) # 1% size ... 33 seconds
system.time(bigMatrix(2000000, "f2")) # 10% size ... 552 seconds
system.time(bigMatrix(4000000, "f3")) # 20% size ...

# t <- read.table('./f0.csv')

