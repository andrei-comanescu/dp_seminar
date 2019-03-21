#!/usr/bin/env Rscript

# the first numerical argument should be the degree of freedom, the second the sigma value
args <- commandArgs(trailingOnly = TRUE)

nums = as.numeric(args)

S <- diag(nums[2], nums[1], nums[1])
W <- rWishart(1, nums[1] + 1, S)

cat(W)
