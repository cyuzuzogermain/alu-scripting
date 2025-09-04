#!/usr/bin/env ruby
# This script takes one argument and checks if it matches the hb[t]+n patted


input = ARGV[0]
# Define the regex
regex = /^hb[t]+n$/
# Match the input against the regex
if input.match?(regex)
  puts "Match!"
else
  puts "No match."
end
