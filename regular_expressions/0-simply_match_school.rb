#!/usr/bin/env ruby
# This script takes one argument and checks if it matches "School"

input = ARGV[0]

if input =~ /School/
  puts input
end
