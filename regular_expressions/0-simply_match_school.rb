#!/usr/bin/env ruby
# This script takes one argument and checks if it matches exactly "School"

input = ARGV[0]

if input =~ /^School$/
  puts input
end
