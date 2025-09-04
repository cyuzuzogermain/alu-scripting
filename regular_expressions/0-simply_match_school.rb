#!/usr/bin/env ruby
# This script takes one argument and checks if it contains the word "School"

input = ARGV[0]

if input =~ /\bSchool\b/
  puts input
end
