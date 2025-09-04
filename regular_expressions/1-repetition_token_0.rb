#!/usr/bin/env ruby
# This script takes one argument and checks if it matches the hb[t]+n pattern

input = ARGV[0]

if input =~ /^hb[t]+n$/
  puts input
end
