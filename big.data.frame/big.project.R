library(foreach)
library(bigmemory)
# library(big.data.frame)

y <- big.data.frame(10, classes=c('integer', 'integer', 'double'), 
                    names=c("elephant", "happy", "turtle"), 
                    init=1:3)
y[, 3] <- rnorm(10)

z <- big.matrix(10, 10, type="double", init=rnorm(100))


s <- big.data.frame(nrow=10, classes=rep(typeof(z), ncol(z)), names=NULL)

s[, 1] <- rnorm(10)
s[, 2] <- 1:10
